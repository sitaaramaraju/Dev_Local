# File: /cgi-bin/init.pm
# Perl script that provides common initialization functions required on each page
# This script also automatically configures Co-op DSN
# Global hashes that are created include:
# %main::session -- Session variables maintained in user's cookie
# %main::fp      -- Functional permission constant definitions against which the
#                   user's functional permissions can be compared; for example:
# 					if ( ($main::fp{'FGI_PA_INPUT'} & $main::session{'fgi_permissions'}) > 0 ){
#							$HasPermissions = 1; }
# 					else { $HasPermissions = 0; }
# %main::cookie  -- User's cookie contents; this is provided only for diagnosis purposes and is
#                   defined when ValidateUser() in Validate.cgi is called or
#                   RefreshCookieFromSessionHash() is called.
# %main:SortHash -- Use this hash in the following manner to iterate through your own hash's
#                   values (not keys) in alphabetical order:
#
# %main::SortHash = %YourHashName;  #Copy your hash to be sorted into global hash %main::SortHash
# my @sortedkeys = sort by_names keys(%main::grouping);
# foreach (@sortedkeys) {
# 	print "Key = $_  Value = $main::SortHash{$_}";
# }
##############################################################
use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use DBInterface;
use CGI qw(:standard);


####################################################
#Using ENV var HTTP_HOST works regardless of server
#####################################################
$main::ServerIP = $ENV{'HTTP_HOST'};
$main::AppVersion = "2.1";
%main::session;
%main::cookie;
%main::fp;
%main::SortHash;
$main::INVALIDLOGIN = "<<<INVALID>>>";
$main::DebugHeaderPrinted = 0;
$main::DebugFooterPrinted = 0;
$main::curIncrement = 0;

$main::debug_buffer = "";

my $myDB = DBInterface->new();

if (! $myDB) {
	ErrorToHome('Our apologies.  The application appears to be unavailable at this time.  The Information Systems department has been contacted.  Please attempt to connect again at a later time.  Thank you.');
}

###################################################
#Populate global 'session' hash with cookie crumbs
###################################################
if ( $ENV{'HTTP_COOKIE'}){
    my @cookies = split (/;/, $ENV{'HTTP_COOKIE'});
    my (%crumbs, $cookie, @pairs, $pair, $name, $value);
    foreach $cookie (@cookies) {
		@pairs = split (/,/, $cookie);
		foreach $pair (@pairs) {
			($name, $value) = split (/=/, $pair);
                $name = trim($name);
            if ( $main::session{($name)} eq "" ) {
                $main::session{($name)} = ($value);
            }
		}
	}
}

my $SQL = "select * from cookie_session with (nolock)
           where uniquekey = '" . $main::session{cookie_guid}."'";
my %cookie;

my $sth = $myDB->prepare($SQL);

if ($sth->execute()) {
    my (%crumbs, $cookie, @pairs, $pair, $name, $value);
    my @cookies;
    while (my $cookie = $sth->fetchrow_hashref()) {
        #%cookie = $myDB->DataHash;
        @cookies = split (/;/, $cookie->{cookie_session});

        foreach $cookie (@cookies) {
            @pairs = split (/,/, $cookie);
            foreach $pair (@pairs) {
                ($name, $value) = split (/=/, $pair);
                $main::session{($name)} = ($value);
            }
        }
    }
}

my $SQL = "select name, value
				from [function] with (nolock)
				order by function_group_name, position";
my $sth = $myDB->prepare($SQL);
				
if ($sth->execute()) {
    my $function;
	while ($sth->fetchrow_hashref) {
        $function = $sth->fetchrow_hashref;
		$main::fp{$function->{'name'}} = $function->{'value'};
	}
	$sth->finish();
}
=head
my $SQL = "select name, value
				from [function] with (nolock)
				order by function_group_name, position";
if (! $myDB->Sql($SQL)) {
    my %function;
	while ($myDB->FetchRow()) {
        %function = $myDB->DataHash;
		$main::fp{$function{'name'}} = $function{'value'};
	}
}
=cut
#$myDB->Close();
$myDB->disconnect();


############################################################################
sub readInput()
# Function readInput() returns a hash of input parameters passed from the
# calling page
############################################################################
{
	my (%searchField, $buffer, $pair, @pairs, $name, $value);

	if ($ENV{'REQUEST_METHOD'} eq 'POST') {
		read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
        $main::debug_buffer = $buffer;
		@pairs = split(/&/, $buffer);
	}
	elsif ($ENV{'REQUEST_METHOD'} eq 'GET') {
		@pairs = split(/&/, $ENV{'QUERY_STRING'});
	}
	else {
#        print "<P>Use Post or Get";
	}
foreach $pair (@pairs) {
($name, $value) = split (/=/, $pair);
#print "<P> (Before processing) $name: $value\n";
$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$name =~ tr/+/ /;
$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
### TODO: CHANGE TO DBI PARAM BINDING! ####
$value =~ s/\-\-/-/ig ;# transforms multiple --- in - use to comment in sql scripts
$value =~ s/[*\/]+//ig ; #removes / and * used also to comment in sql scripts
$value =~ s/(;|\s)(exec|execute|select|insert|update|delete|create|alter|drop|rename|truncate|backup|restore)\s//eig ;
#print "<P> (After processing) $name: $value\n"; 
$searchField{$name} = $value;
}
	return (%searchField);
}

############################################################################
sub CCurr
# Function CCurr takes any number as an argument and returns it formatted as
# U.S. currency
############################################################################
{
    my ($cents, $cents_formatted, $dollars, $result, $pos, $sign, $curr_symbol);
    if ( exists $main::session{curr_sym} && length($main::session{curr_sym}) > 0 ) {
        $curr_symbol = $main::session{curr_sym};
    }else{
        $curr_symbol = "\$";
    }

	my $val = $_[0];
	if ($val !~ /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/ && length($val) > 0) {
 		return "NaN";
	}
	$sign = ($val < 0) ? '-':'';
	$dollars = int($val = int((abs($val) * 100.0) + 0.5) / 100.0);
	$sign = '' if ($val == 0.00);
    $cents = $val - $dollars;

    #Format cents
    $cents_formatted = substr((sprintf "%.2f", $cents), -2, 2);
    #Insert commas in dollar value
    $result = "";
    $pos = 0;
    while ($dollars ne "") {
        $pos = $pos + 1;
        if ($pos == 4) {
            $result = chop($dollars) . "," . $result;
            $pos = 1;
            }
        else {
            $result = chop($dollars) . $result;
        }
    }
    return "$curr_symbol".$sign.$result.".".$cents_formatted;
}

############################################################################
sub MCurr
# Function MCurr takes any number as an argument and returns it formatted as
# currency, appending second parameter as currency symbol
############################################################################
{
    my ($cents, $cents_formatted, $dollars, $result, $pos, $sign, $curr_symbol);
    $curr_symbol = $_[1];

	my $val = $_[0];
	if ($val !~ /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/ && length($val) > 0) {
		return "NaN";
	}
	$sign = ($val < 0) ? '-':'';
	$dollars = int($val = int((abs($val) * 100.0) + 0.5) / 100.0);
	$sign = '' if ($val == 0.00);
    $cents = $val - $dollars;

    #Format cents
    $cents_formatted = substr((sprintf "%.2f", $cents), -2, 2);
    #Insert commas in dollar value
    $result = "";
    $pos = 0;
    while ($dollars ne "") {
        $pos = $pos + 1;
        if ($pos == 4) {
            $result = chop($dollars) . "," . $result;
            $pos = 1;
            }
        else {
            $result = chop($dollars) . $result;
        }
    }
    return "$curr_symbol".$sign.$result.".".$cents_formatted;
}

############################################################################
sub Clean($)		#12/12/00; 06/25/04 10:18:AM
# Strips commas, dollar signs, percentage signs and errant K's from input
# Parentheses denotes a negative number
############################################################################
{
	my ($output) = @_;
	my $mult = 1;
	if ( $output =~ m/^\(.+\)$/g ) {
		#Parens found, denoting negative number
		$mult = -1;
		#Strip parens
		$output =~ s/[\(\)\$]//g;
	}
	#Strip non-numeric characters
	$output =~ s/[^0-9.\-]//g;
#	print "mult: $mult<br>";
	$output = $output * $mult;

    if ( $output eq '' ) {
       $output = 0;
    }
    return $output;

}	##Clean($)

############################################################################
sub HasPermission		#10/25/00 4:00:PM
# Takes a function constant (e.g. FGI_PA_INPUT), as defined in Function
# table and returns the function constant's non-zero value (equivalent to
# a logical TRUE) if user has permission to execute function, 0 if not.
############################################################################
{
	my ($function, $tmpDB) = @_;
	my $closeme = 0;
	my $result;
	if ( !ref $tmpDB ) {
		#$tmpDB = new Win32::ODBC($main::DSN);
		$tmpDB = DBInterface->new();
		$closeme = 1;
	}
=head
	my $SQL = "select lkup.lkup_staff_client_list_function_id
				from lkup_staff_client_list_function lkup with (nolock), staff_client_list with (nolock), [function] with (nolock)
				where lkup.staff_client_list_id = staff_client_list.staff_client_list_id
					and staff_client_list.staff_id = $main::session{staff_id}
					and staff_client_list.client_id = $main::session{client_id}
					and lkup.function_id = [function].function_id
					and [function].name = '$function'";
=cut
	my $SQL = "select 0 as funcID union
select lkup.lkup_staff_client_list_function_id as funcID					
				from lkup_staff_client_list_function lkup with (nolock)
				inner join staff_client_list with (nolock) on staff_client_list.staff_client_list_id = lkup.staff_client_list_id
				inner join [function] with (nolock) on [function].function_id = lkup.function_id
				where staff_client_list.staff_id = ?
					and staff_client_list.client_id = ?
					and [function].name = ?
					order by 1 desc	";

		my $sth = $tmpDB->prepare($SQL);
		$sth->execute($main::session{staff_id}, $main::session{client_id}, $function);
		my $user = $sth->fetchrow_hashref();

	if ( $user->{funcID} > 0 ) {
		$result = 1;
	}
	else {
		$result = 0;
	}
	if ( $closeme ) {
	#	$tmpDB->Close();
		$tmpDB->disconnect();
	}
	return ($result);

}	##HasPermission($)

############################################################################
sub HasPermissionForClient		# 06/13/01 9:51:AM
									# Given function name, staff_id and client_id,
									# returns number > 0 if user has specified permission,
									# 0 otherwise.
############################################################################
{
	my ($function, $staff_id, $client_id, $tmpDB) = @_;
	my $closeme = 0;
	my $result;
	if ( !ref $tmpDB ) {
	#	$tmpDB = new Win32::ODBC($main::DSN);
		$tmpDB = DBInterface->new();
		$closeme = 1;
	}
=head
	my $SQL = "select lkup.lkup_staff_client_list_function_id
				from lkup_staff_client_list_function lkup with (nolock), staff_client_list with (nolock), [function] with (nolock)
				where lkup.staff_client_list_id = staff_client_list.staff_client_list_id
					and staff_client_list.staff_id = $staff_id
					and staff_client_list.client_id = $client_id
					and lkup.function_id = [function].function_id
					and [function].name = '$function'";
=cut
	my $SQL = "select 0 as funcID union
				select lkup.lkup_staff_client_list_function_id as funcID 
				from lkup_staff_client_list_function lkup with (nolock)
				inner join staff_client_list with (nolock) on staff_client_list.staff_client_list_id = lkup.staff_client_list_id
				inner join [function] with (nolock) on [function].function_id = lkup.function_id
				where  staff_client_list.staff_id = ?
					and staff_client_list.client_id = ?
					and [function].name = ? 
					order by 1 desc";

		my $sth = $tmpDB->prepare($SQL);
		$sth->execute($staff_id, $client_id, $function);
		my $user = $sth->fetchrow_hashref();

	if ( $user->{funcID} > 0 ) {
		$result = 1;
	}
	else {
		$result = 0;
	}
	if ( $closeme ) {
	#	$tmpDB->Close();
		$tmpDB->disconnect();
	}
	return ($result);

}	##HasPermissionForClient($$$)

############################################################################
sub SetClientPermissions ($$)		#10/24/00 3:00:PM
# Takes staff_id and client_id as arguments and sets the user's 'user_level'
# and functional permissions ('fgi_permissions', 'fgo_permissions',
# 'fga1_permissions', and 'fga2_permissions') in their session hash.
# Clears any customer-related session variables.
# Must be called prior to any HTML header as it refreshes the user's cookie.
# Returns 1 if successful in setting hash values, 0 if unsuccessful.
############################################################################
{
	my ($staff_id, $client_id) = @_;
	my $result;
	my $myDB = DBInterface->new();
=head
	my $SQL = "select client_id, staff_client_list.user_level, fgi_permissions, fgo_permissions, fga1_permissions, " .
		"fga2_permissions, staff_client_list.user_level, precedence " .
        "from staff_client_list with (nolock) , WebAccessLevel  with (nolock) where staff_id = $staff_id and client_id = $client_id and " .
		"staff_client_list.user_level = WebAccessLevel.name";
    my $myDB = new Win32::ODBC($main::DSN);
	$myDB->Sql($SQL);
=cut
	my $SQL = "select client_id, staff_client_list.user_level, fgi_permissions, fgo_permissions, fga1_permissions,  
		fga2_permissions, staff_client_list.user_level, precedence  
        from staff_client_list with (nolock) 
        inner join WebAccessLevel  with (nolock) on WebAccessLevel.name	= staff_client_list.user_level
        where staff_id = ? and client_id = ? ";

		my $sth = $myDB->prepare($SQL);
		$sth->execute($staff_id, $client_id);
	#	$sth->finish();

	if (my $staff_client_hash = $sth->fetchrow_hashref()) {
#		my %staff_client_hash = $myDB->DataHash;
		$main::session{'client_id'} = $client_id;
#        $main::session{'fgi_permissions'} = $staff_client_hash{'fgi_permissions'};
#        $main::session{'fgo_permissions'} = $staff_client_hash{'fgo_permissions'};
#        $main::session{'fga1_permissions'} = $staff_client_hash{'fga1_permissions'};
#        $main::session{'fga2_permissions'} = $staff_client_hash{'fga2_permissions'};
		$main::session{'user_level'} = $staff_client_hash->{'user_level'};
		$main::session{'precedence'} = $staff_client_hash->{'precedence'};
	
		$sth->finish();
	
		#Query for client-related information
		$SQL = "select client_name, program_name, logo, home_url, navigation_version, address1, address2, city, state, zip, country,  
				phone, fax, email from client  with (nolock) where client_id = ?";
		my $sth2 = $myDB->prepare($SQL);
		$sth2->execute( $client_id );
		if (my $ClientHash = $sth2->fetchrow_hashref()) {

			$main::session{'client_name'} = $ClientHash->{'client_name'};
			$main::session{'program_name'} = $ClientHash->{'program_name'};
			$main::session{'logo'} = $ClientHash->{'logo'};
			$main::session{'navigation_version'} = $ClientHash->{'navigation_version'};
			$main::session{'home_url'} = $ClientHash->{'home_url'};
			$main::session{'client_address1'} = $ClientHash->{'address1'};
			$main::session{'client_address2'} = $ClientHash->{'address2'};
			$main::session{'client_city'} = $ClientHash->{'city'};
			$main::session{'client_state'} = $ClientHash->{'state'};
			$main::session{'client_zip'} = $ClientHash->{'zip'};
			$main::session{'client_country'} = $ClientHash->{'country'};
			$main::session{'client_phone'} = $ClientHash->{'phone'};
			$main::session{'client_fax'} = $ClientHash->{'fax'};
			$main::session{'client_email'} = $ClientHash->{'email'};
		}
		$sth2->finish();
		#Clear customer-related variables
    #    $main::session{'cust_id'} = -1;
		$main::session{'client_cust_no'} = "";
		$main::session{'cust_name'} = "";

		#Refresh the user's cookie with the updated session hash information
		RefreshCookieFromSessionHash();

		$result = 1;
	}
	else {
		$result = 0;
	}
	#$myDB->Close();
	$myDB->disconnect();
	return $result;
}	##SetClientPermissions ($$)

############################################################################
sub SetCustomerInfo($)		#10/27/00 5:06:PM
# Takes cust_id as an argument and sets customer-specific session variables
# in the user's session hash.
# Must be called prior to any HTML header as it refreshes the user's cookie.
############################################################################
{
	my ($cust_id) = $_[0];
    my $SQL = "select client_cust_no, name, cust_type_id from cust  with (nolock) where cust_id = ?";
#    my $myDB = new Win32::ODBC($main::DSN);
#	$myDB->Sql($SQL);
	my $myDB = DBInterface->new();
		my $sth = $myDB->prepare($SQL);
		$sth->execute($cust_id);
		

	if (my $cust_hash = $sth->fetchrow_hashref()) {
#		my %cust_hash = $myDB->DataHash;
		$main::session{'cust_id'} = $cust_id;
		$main::session{'client_cust_no'} = $cust_hash->{'client_cust_no'};
		$main::session{'cust_name'} = $cust_hash->{'name'};
        $main::session{'cust_type_id'} = $cust_hash->{'cust_type_id'};

		RefreshCookieFromSessionHash();
	}
	$sth->finish();	
	$myDB->disconnect();
}	##SetCustomerInfo($)

############################################################################
sub SetCustomerInfoFromClientCustNo($)      #10/27/00 5:06:PM
# Takes client_cust_no as an argument and sets customer-specific session variables
# in the user's session hash.
# Must be called prior to any HTML header as it refreshes the user's cookie.
############################################################################
{
    my ($client_cust_no) = $_[0];
	my $result;
#    my $SQL = "select cust_id, name, cust_type_id from cust  with (nolock) where client_cust_no = '$client_cust_no' and client_id = $main::session{client_id}";
#    my $myDB = new Win32::ODBC($main::DSN);
#	$myDB->Sql($SQL);

	my $myDB = DBInterface->new();
    my $SQL = "select cust_id, name, cust_type_id from cust  with (nolock) where client_cust_no = ? and client_id = ?";
		my $sth = $myDB->prepare($SQL);
		$sth->execute($client_cust_no , $main::session{client_id});
	if (my $cust_hash = $sth->fetchrow_hashref()) {
	#	my %cust_hash = $myDB->DataHash;
        $main::session{'cust_id'} = $cust_hash->{'cust_id'};
        $main::session{'client_cust_no'} = $client_cust_no;
		$main::session{'cust_name'} = $cust_hash->{'name'};
        $main::session{'cust_type_id'} = $cust_hash->{'cust_type_id'};


		RefreshCookieFromSessionHash();
		$result = 1;
	}
    else {
		$result = 0;
    }
	$sth->finish();	
	$myDB->disconnect();
	return $result;
}   #SetCustomerInfoFromClientCustNo($)
############################################################################
sub RefreshCookieFromSessionHash()		#10/25/00 4:29:PM
# Refreshes the user's cookie from their currently defined session hash,
# %main::session.  This is useful when you need to define new or modify
# existing session hash variables and need to update the user's cookie to
# reflect the changes.
# NOTE: This must be called before any HTTP page headers as it creates
# a Set-Cookie header.
############################################################################
{
    #my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();

	my $key;
    my $Cookie;
	foreach $key (sort keys (%main::session)) {
		$Cookie = $Cookie . "," . ($key) . "=" . ($main::session{$key});
	}
    my $tmpCookie = $Cookie;
    $tmpCookie =~ s/[']/''/gi;

    if ( $main::session{cookie_guid} ) {
        #update it
=head
        if ( $main::session{thisfile} ) {
            $SQL = "update cookie_session set staff_id = " . $main::session{staff_id} . ",last_update_date = getdate(),cookie_session = '" . $tmpCookie . "' where uniquekey = '" . $main::session{cookie_guid}."'";
        }else{
            $SQL = "update cookie_session set staff_id = " . $main::session{staff_id} . ",last_update_date = getdate(),cookie_session = '" . $tmpCookie . "' where uniquekey = '" . $main::session{cookie_guid}."'";
        }
=cut
            $SQL = "update cookie_session set staff_id = ? ,last_update_date = getdate(),cookie_session = ? where uniquekey = ?";

		my $sth = $myDB->prepare($SQL);
		$sth->execute($main::session{staff_id} , $tmpCookie ,  $main::session{cookie_guid});
		$sth->finish();	

    }else{
        #create it
        $SQL = "insert into cookie_session (cookie_session) values (?)";

		my $sth = $myDB->prepare($SQL);
		$sth->execute($tmpCookie );
		
		my $cookie_id = $sth->fetchrow_hashref();
		$sth->finish();


        my $c = new CGI::Cookie(-name    =>  'CCI',
                                    -value   =>  'cookie_guid=$cookie_id->{guid}'
                                    );
    }
	
	$myDB->disconnect();
}  ##RefreshCookieFromSessionHash()
############################################################################
sub EmptyCookie()      #4/9/01 4:29:PM
# Refreshes the user's cookie from their currently defined session hash,
# %main::session.  This is useful when you need to define new or modify
# existing session hash variables and need to update the user's cookie to
# reflect the changes.
# NOTE: This must be called before any HTTP page headers as it creates
# a Set-Cookie header.
############################################################################
{
	my $Cookie = ("cookie_name") . "=" . ("X");
	my $CookieHeader = $Cookie;
	my $key;
    $Cookie = "";
	#Generate session-wide user cookie; first make sure any existing cookie is deleted and then re-create it
    #print "Set-Cookie:$CookieHeader; expires=Fri, 02-Jan-1970 00:00:00 GMT;domain=$main::ServerIP;path=/\n";
    #print "Set-Cookie:$Cookie; expires=Fri,21-Sep-2040 00:00:00 GMT;domain=$main::ServerIP;path=/\n";
}  ##RefreshCookieFromSessionHash()


############################################################################
sub url_encode		#10/27/00 3:56:PM
############################################################################
{
	my $text = shift;
	$text =~ s/([^a-z0-9_.!~*'() -])/sprintf "%%%02X", ord($1)/ei;
	$text =~ tr/ /+/;
	return $text;

}	##url_encode

############################################################################
sub EntityEquivalent($)		#04/03/01 2:42:PM
# Substitutes tag marker characters with entity equivalents
############################################################################
{
    my ($Equiv) = @_;

	$Equiv =~ s/[&]/&amp;/g;
	$Equiv =~ s/\n/<br>/g;
	$Equiv =~ s/[<]/&lt;/g;
	$Equiv =~ s/[>]/&gt;/g;
	$Equiv =~ s/\"/&quot;/g;

	return $Equiv;
}	##EntityEquivalent

############################################################################
sub EE($)		#07/13/01 2:20:PM
# Alias for EntityEquivalent() for lazy fingers. :)
############################################################################
{
    my ($input) = @_;
	my $output = EntityEquivalent($input);
	return $output;
}	##EE

############################################################################
sub EEHash(%)       #03/02/01 9:20:AM
# Runs EE on a hash
############################################################################
 {
    my (%hashRef) =@_;
    my $key;
    my $value;
    while (($key, $value) = each(%hashRef)) {
        $hashRef{$key} = EntityEquivalent($value);
    }
    return %hashRef;
}   ##EEHash(%)

############################################################################
sub DeEntityEquivalent($)     #04/03/01 2:42:PM
# Substitutes entity equivalents with tag marker characters
############################################################################
{
    my ($Equiv) = @_;

    $Equiv =~ s/&amp;/&/g;
    $Equiv =~ s/<br>/\n/g;
    $Equiv =~ s/&lt;/</g;
    $Equiv =~ s/&gt;/>/g;

	return $Equiv;
}	##EntityEquivalent

############################################################################
sub DE($)       #07/13/01 2:20:PM
# Alias for EntityEquivalent() for lazy fingers. :)
############################################################################
{
    my ($input) = @_;
    my $output = DeEntityEquivalent($input);
	return $output;
}   ##DE


############################################################################
sub by_names       #10/31/00 11:36:AM
############################################################################
{
    (lc($main::SortHash{$a}) cmp lc($main::SortHash{$b})) || (lc($a) cmp lc($b));
}   ##by_names

############################################################################
sub PrintDebugHeader($)		#12/08/00 10:21:AM
############################################################################
{
	if ($main::DebugHeaderPrinted == 0) {
		$main::DebugHeaderPrinted = 1;
		my ($headertext) = @_;
    	#print "HTTP/1.0 200 OK\n";   print "Content-Type: text/html\n\n";
    	print "<HTML>\n";   print "<HEAD>\n";
    	print "<TITLE>$headertext</TITLE>\n";   print "</HEAD>\n";
    	print "<BODY>\n";
    	print "<center>\n";
	}
}	##PrintDebugHeader

############################################################################
sub PrintDebugFooter      #09/21/00 1:42:PM
############################################################################
{
print<<"EOF";
    </center>
    </BODY>
    </HTML>
EOF
}   ##PageFooter

############################################################################

############################################################################
sub header      #01/09/01 1:31:PM
############################################################################
{
	my $clientstring = "";
	if ( exists $main::session{client_name} ) {
		$clientstring = EE(" - $main::session{client_name}");
	}

	my $charset_tag = "";

    my $langSQL = "select language_charset from language  with (nolock) where language_id = $main::session{language}";
	my $myDB = DBInterface->new();
	my $sth =  $myDB->prepare($langSQL);	
	$sth->execute();				
	my $hLang = $sth->fetchrow_hashref();
	$charset_tag = "; charset=$hLang->{language_charset}";
	$sth->finish();

	my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);
	my $CRLF = chr(13) . chr(10);
	#print "$ENV{SERVER_PROTOCOL} 200 OK" ;#. $CRLF . "Content-Type: text/html$charset_tag" . $CRLF . $CRLF;

print<<"EOF";
<!--<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">-->
<!-- (c) 2001-$year CCI -->
<html>
    <head>
        <title>CCI</title>
    </head>
EOF
	#require "G:/CenturyLink/xroot/Universal/styles.cgi";

}   ##header
	#
############################################################################

############################################################################
sub headernocss      #01/09/01 1:31:PM
############################################################################
{
	my $clientstring = "";
	if ( exists $main::session{client_name} ) {
		$clientstring = EE(" - $main::session{client_name}");
	}
	my $charset_tag = "";
	my $charset_tag = "";
    my $langSQL = "select language_charset from language  with (nolock) where language_id = $main::session{language}";
	my $myDB = DBInterface->new();
	my $sth =  $myDB->prepare($langSQL);	
	$sth->execute();				
	my $hLang = $sth->fetchrow_hashref();
	$charset_tag = "; charset=$hLang->{language_charset}";
	$sth->finish();

#print "$ENV{SERVER_PROTOCOL} 200 OK\n";
#print "Content-type: text/html\n\n";
#print "Content-type: text/html$charset_tag\n\n";
print "<!--<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">-->\n";
print "<!-- (c) 2001-2004 CCI $charset_tag-->";
#print "<!-- $langSQL -->";
#print "<http-equiv=\"Cache-Control\" content=\"no-cache\">\n";
#print "<META HTTP-EQUIV=\"Expires\" CONTENT=\"Tue, 01 Jan 1980 1:00:00 GMT\">\n";
print "<html>\n";
print "<head>\n";
print "<title>CCI $clientstring</title>\n";
print<<"EOF";
<meta name=robots content=noindex>
<meta name="MSSmartTagsPreventParsing" content="TRUE">
EOF
print "</head>\n";

}   ##header

# -------------------------------------------------------------------
#   get_header( )
# -------------------------------------------------------------------
#   Yet another header function in init.cgi  Jun 4 2004 prh
#   doctype from Castro http://www.cookwood.com/html/extras/doctypes.html
#
#   Pass optional string params in a hash:
#       key "title"             Default: ""
#       key "css"               Relative css filename like "css/employee.css"
#       key "more"              Strings to insert in <head>
#       (more stuff later)
#
#   Returns:
#       string (this function doesn't print)
#
#   Usage:
#       my $heading = get_header( 'title' => 'My Page', 'css' => 'css/hey.css' );
#
# -------------------------------------------------------------------
sub get_header{

    my %hash = @_;
    my $title = $hash{title} || '';
    my $css   = $hash{css}   || '';
    my $more  = $hash{more}  || '';

    $css = "<link rel=\"stylesheet\" href=\"$css\" type=\"text/css\">\n" if $css;

    #my $str = "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
   my $str = <<EOF;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>$title</title>
$css$more
<meta name=robots content=noindex>
<meta name="MSSmartTagsPreventParsing" content="TRUE">
<meta http-equiv="pragma" content="no-cache">
<script language="javascript">
  function openwindow(URL) {
    win = window.open(URL, "pop", "width=800, height=550, left=50, top=50, scrollbars=yes, toolbar=yes, menubar=yes, status=yes");
  }
</script>

</head>
EOF
    return $str;
}


############################################################################
sub getYear     #09/24/10 1:30:PM
############################################################################
 {
    use Time::localtime;
    my $tm = localtime;
    my ($DAY, $MONTH, $YEAR) = ($tm->mday, $tm->mon, $tm->year);
    return ($YEAR+1900);
}   ##getYear


############################################################################

# Given $batch_type_id, $batch_name, $description, $staff_id, $client_id as parameters and
# returns batch_id for the new batch.
# NOTE: Returns -1 on database connection error.
#
# Example call: my $batch_id = CreateBatch($batch_type_id, $batch_name, $description, $staff_id, $client_id)
#
############################################################################
sub CreateBatch($$$$$)	#12/11/00 9:37:AM
############################################################################
{
		my ($batch_type_id, $batch_name, $description, $staff_id, $client_id) = @_;
		my $batch_id;
		# Start a new batch by calling SP CreateBatch
		#my $myDB = new Win32::ODBC($main::DSN);
		#$SQL = "declare \@batch_id integer " .
		#	"execute UserSessionStart $staff_id, '$RemoteHost', '$RemoteAddr', 'ProgramsPro', '0.1', \@new_session_id output, \@session_start output " .
		#	"select \@new_session_id as session_id, \@session_start as session_start";
		my $myDB = DBInterface->new();
		
		my $SQL = "declare \@batch_id integer " .
			"execute CreateBatch $batch_type_id, '$batch_name', '$description', $staff_id, $client_id, \@batch_id output " .
			"select \@batch_id as batch_id";
		
		my $sth = $myDB->prepare($SQL);
		$sth->execute();
		
		if (my $session = $sth->fetchrow_hashref()) {
			$batch_id = $session->{'batch_id'};
			$sth->finish();
			$myDB->disconnect;
			return $batch_id;
		}
		else {
            $myDB->disconnect;
			return -5;
		}
}	##CreateBatch


############################################################################
# Trims leading and trailing spaces.
# Derived from: http://www.biglist.com/lists/xsl-list/archives/200112/msg01080.html
sub trim($) {
	my ($var) = @_;
	$var =~ s/^\s*//;  #remove leading spaces
	$var =~ s/\s*$//;  #remove trailing spaces
    return $var;
}

#### DBCloseAll func added 8/2/2005
sub DBCloseAll
{
#    my $i;
#    my $cnt = scalar(@main::open_db_connections);
#    for ($i = 0; $i < $cnt; $i++) {
#       if (ref $main::open_db_connections[$cnt - 1]) {
#           $main::open_db_connections[$cnt - 1]->Close();
#       }
#    }
#    if (ref $main::db_xlate) { $main::db_xlate->Close(); }
}

# FILE WILL BE USED AS A VIEW ONLY DIE NICE!!! WILL PASS ERROR INFO INTO A SUB ROUTINE THAT WILL PARSE THROUGH IT AND THEN REDISPLAY NICELY #
#--------------------------------------------------------------------------#
                # create sub routine to handle data #
############################################################################
sub dienicely      #08/06/02 12:59:PM
                    # created by btm
############################################################################
{
	 #($$$$%%%%%)
#--------------------------------------------------------------------------#
            # capture data being passed to use for display
            # and insert to database... generate email
            # to is dept of the error generated. and give
            # user a tracking number.
            # 1. $errortitle = table header - title of error or query
            # 2. $sqlquery = query that errored out
            # 3. $errormsg = sql error message that was generated
            # 4. $filename = name of page error occured
            # 5. %session = main session hash reference
            # 6. %cust = main customer hash (if exists) reference
            # 7. %geo = main group hash (if exists) reference
            # 8. %prefs = main preferences hash reference
            # 9. %post = main postInputs hash reference
    my ($errortitle, $sqlquery, $errormsg, $filename, $mainsessionref, $custref, $georef, $prefsref, $postref) = @_;
    my ($customer, $program, $logon);
    #my $dberror = new Win32::ODBC($main::DSN);
	my $dberror = DBInterface->new();

#--------------------------------------------------------------------------#
            # get text entries ready for entry into database #
    my $sqlqueryinsert = EscQuote2($sqlquery);
    $sqlqueryinsert =~ s/\n\t\r//gi;
    $sqlqueryinsert =~ s/ +/ /gi;
    my $errormsginsert = EscQuote2($errormsg);
    my $filenameinsert = EscQuote2($filename);
    my $logoninsert = EscQuote2($main::session{logonID});
#--------------------------------------------------------------------------#
            # a cust or program may not exist, set value to 0 #
    if ( length($main::cust{cust_id} == 0 )) {
		if ( length($main::session{cust_id}) > 0 ) {
			$customer = $main::session{cust_id};
		}
		else {
	        $customer = 0;
		}
    }else{
        $customer = $main::cust{cust_id};
    }
    if ( length($main::session{program_name} == 0 )) {
        $program = 0;
    }else{
        $program = $main::session{program_name};
    }
#--------------------------------------------------------------------------#
# check to see if session exists , if not , give differnt message and no
                    # insert or email fired off #
    if ( length($main::session{client_id}) > 0 && length($logoninsert) > 0 ) {

#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
                        # main insert into error log #
	my $HTTP = $ENV{'HTTP_HOST'};
    my $insert = "insert into error_log(client_id, cust_id, staff_id, logonid, password, session_id, e_mail, url, query, error, program_id, server)
                  select $main::session{client_id}, $customer, $main::session{staff_id}, '$logoninsert', staff.Password, $main::session{session_id},
                  contact_info.e_mail, '$filenameinsert', '$sqlqueryinsert', '$errormsginsert', $program, '$HTTP'
                  from staff with (nolock) , contact_info with (nolock)
                  where staff.contact_info_id = contact_info.contact_info_id
                  and staff_id = $main::session{staff_id}";

                  if (! $dberror){
						ErrorToHome('Our apologies.  The application appears to be unavailable at this time.  The Information Systems department has been contacted.  Please attempt to connect again at a later time.  Thank you.');
                  }
   my $sth = $dberror->prepare($insert);	
	$sth->execute();
	
	my $hash = $sth->fetchrow_hashref();
    $sth->finish();
	
    my $select = "select e_mail, password from error_log  with (nolock) where error_log_id = $hash->{error_log_id}";
    #$dberror->Sql($select);
    #$dberror->FetchRow();
	my $sth = $dberror->prepare($select);
	$sth->execute();
    #my %data = $dberror->DataHash();
	my $data = $sth->fetchrow_hashref();
#--------------------------------------------------------------------------#
                        # set up subject and body #

my $string0 = "";
if (%$mainsessionref) {
	$string0 = DumpHashHTML(%$mainsessionref);
}
my $string1 = "";
if (%$custref) {
	$string1 = DumpHashHTML(%$custref);
}
my $string2 = "";
if (%$georef ) {
	$string2 = DumpHashHTML(%$georef);
}
my $string3 = "";
if (%$prefsref) {
	$string3 = DumpHashHTML(%$prefsref);
}
my $string4 = "";
if ( %$postref) {
	$string4 = DumpHashHTML(%$postref);
}

#Extract as many CGI environment variables as we can
my $env = "";
$env .= DumpHashHTML(%ENV);  #extracts other env vars not listed above
$env .= "AUTH_TYPE: $ENV{AUTH_TYPE}<br>";
$env .= "CONTENT_TYPE: $ENV{CONTENT_TYPE}<br>";
$env .= "DOCUMENT_ROOT: $ENV{DOCUMENT_ROOT}<br>";
$env .= "HTTP_AGENT: $ENV{HTTP_AGENT}<br>";
$env .= "HTTP_REFERER: $ENV{HTTP_REFERER}<br>";
$env .= "HTTPS: $ENV{HTTPS}<br>";
$env .= "PATH_INFO: $ENV{PATH_INFO}<br>";
$env .= "PATH_TRANSLATED: $ENV{PATH_TRANSLATED}<br>";
$env .= "REMOTE_ADDR: $ENV{REMOTE_ADDR}<br>";
$env .= "REMOTE_HOST: $ENV{REMOTE_HOST}<br>";
$env .= "REMOTE_IDENT: $ENV{REMOTE_IDENT}<br>";
$env .= "SCRIPT_NAME: $ENV{SCRIPT_NAME}<br>";
$env .= "SERVER_NAME: $ENV{SERVER_NAME}<br>";
$env .= "SERVER_PORT: $ENV{SERVER_PORT}<br>";
$env .= "SERVER_PROTOCOL: $ENV{SERVER_PROTOCOL}<br>";

#Extract the DSN from $main::DSN (e.g. DSN=co-op;UID=sa;PWD=lotrtt)
my $DSN = "";
my ($pair, @pairs, $key, $value);
@pairs = split (/;/, $main::DSN);
foreach $pair (@pairs) {
	($key, $value) = split (/=/, $pair);
	if ( $key eq 'DSN' ) {
		$DSN = $value;
	}
}

#Suppress password if the user is an Admin
my $password = "**********";
if ( $main::session{precedence} < 255 ) {
	$password = $data->{'password'};
}

my $email_filename = get_filename2($filename, '/');
my $subject = "Programs Pro Error # $hash->{error_log_id}  $ENV{'HTTP_HOST'} $DSN $email_filename";

my $body = "Server: $ENV{'HTTP_HOST'}<br>";
   $body = $body . "DSN: $DSN<br>";
   $body = $body . "Client Name: $main::session{'client_name'}<br>";
   $body = $body . "Client ID: $main::session{client_id}<br>";
   $body = $body . "Customer ID: $customer<br>";
   $body = $body . "Email: $data->{'e_mail'}<br>";
   $body = $body . "Logon ID: $main::session{logonID}<br>";
   $body = $body . "Password: $password<br>";
   $body = $body . "Page Name (URL): $filename<br>";
   $body = $body . "Browser Name: $main::session{'browser_name'}<br>";
   $body = $body . "Browser Version: $main::session{browser_version}<br>";
   $body = $body . "Error Title: $errortitle<br>";
   $body = $body . "SQL Statement: $sqlquery<br><br>";
   $body = $body . "SQL Error Message: $errormsg<br><br>";
   $body = $body . "Hashes are as follows:<br>";
   $body = $body . "Session:<br>$string0<br><br>";
   $body = $body . "Cust:<br>$string1<br><br>";
   $body = $body . "Geo:<br>$string2<br><br>";
   $body = $body . "Prefs:<br>$string3<br><br>";
   $body = $body . "PostInputs:<br>$string4<br><br>";
   $body = $body . "CGI Environment Variables:<br>$env<br><br>";
#=-------------------------------------------------------------------------#



        my $outputfile="D:/centurylinkyoucan/tmp/error".$hash->{error_log_id}.".htm";
        unless(open(OUTPUT, '>'. $outputfile))
        {
            print "Could not open output file " . $outputfile;
            die;
        }

print OUTPUT <<"EOF";
	<html>
	<head>
<style type="text/css">
/* main style sheet*/
/* forms processing */
        .select1{background-color: FFFFFF; color: #454242; font-family: verdana; font-size: 7.5pt; font-weight: 700;}
        .button1 {color: #5382B2; background-color: #5382B2; font-family: verdana; font-size: 7.5pt; font-weight: 700;}
        .text {background-color: white; color: #454242; font-family: verdana; font-size: 7.5pt; font-weight: 500;}
/* mouseover effects */

.link:link {font-size: 7.5pt; text-decoration: none; color: black; font-family: verdana; font-weight: 600;}
.link:active {font-size: 7.5pt; text-decoration: none; color: black; font-family: verdana; font-weight: 600;}
.link:visited {font-size: 7.5pt; text-decoration: none; color: black; font-family: verdana; font-weight: 600;}
.link:hover {font-size: 7.5pt; text-decoration: none; color: red; font-family: verdana; font-weight: 600; cursor: hand;}

.linkon:link {font-size: 7.5pt; text-decoration: none; color: white; font-family: verdana; font-weight: 700;}
.linkon:active {font-size: 7.5pt; text-decoration: none; color: white; font-family: verdana; font-weight: 700;}
.linkon:visited {font-size: 7.5pt; text-decoration: none; color: white; font-family: verdana; font-weight: 700;}
.linkon:hover {font-size: 7.5pt; text-decoration: none; color: black; font-family: verdana; font-weight: 700; cursor: hand;}


/* border effects for tables */
        .border {border-style: solid; border-color: #69738C; border-width: thin;}
        .border1 {border-style: solid; border-color: black; border-width: thin;}
        .border2 {border-style: solid; border-color: #69738C; background-color: white; border-width: thin;}
        .td_border {border-style: solid; border-color: gray; border-width: thin;}

/*generic body1 class F1F1F0*/
        .body1 {background-color: FFFFFF; margin-top: 0; margin-left: 0;}
        .body2 {background-color: FFFFFF; margin-top: 0; margin-left: 0;}
        BR.pageEnd{page-break-after: always;}
        BR.pageEnd1{page-break-before: always;}

/*body copy*/
        h3 {font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 13pt; color:024D5B }
        .h3a {font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11pt; color:024D5B }


/* font styles */
        .font1 {font-family: Arial, Helvetica, sans-serif; font-weight: 500; font-size: 7pt; color=black}


/* TABLES */
        .th {font-family: Verdana, Arial, Helvetica, sans-serif; color: #ffffff; font-size: 10pt; text-indent: 1px; background-color: #425688; font-weight: 600;}
        .docnav {font-family: Arial, Helvetica, sans-serif; font-size: 9pt; }
        .tbc {font-family: Verdana; font-size: 7.5pt; font-weight: 400; }
        .tbcbold {font-family: Verdana; font-size: 8pt; font-weight: 600; text-indent: 1px; }
        .tbcbigbold {font-family: Verdana; font-size: 9pt; font-weight: 600; text-indent: 1px; }
        .tbcsmallbold {font-family: Verdana; font-size: 7pt; font-weight: 600; text-indent: 1px; }
        .tblfootnote {font-family: Arial, Helvetica, sans-serif; font-style: italic; font-size: 8pt; }
        .tblsmall {font-family: Arial, Helvetica, sans-serif; font-size: 7pt; }
        .tblsubhead {font-family: Arial, Helvetica, sans-serif; font-size: 12pt; font-weight: 700;}
        .tblsubhead1 {font-family: Arial, Helvetica, sans-serif; font-size: 12pt; font-weight: 700; color: 380D56;}
        .hdrbgrnd {background-color:#D4D0C8;}
        .hdrbgrndA {font-family: Verdana, Arial, Helvetica, sans-serif; font-size:9pt; font-weight: 700;background-color:DDDAD6;}
        .hdrP {font-family: Verdana, Arial, Helvetica, sans-serif; color: #380D56; font-size:9pt; font-weight: 700; background-color:6B598F;}
        .hdrG {font-family: Verdana, Arial, Helvetica, sans-serif; color: #380D56; font-size:9pt; font-weight: 700; background-color:7D8394;}
        .hdrB {font-family: Verdana, Arial, Helvetica, sans-serif; color: #ffffff; font-size: 10pt; text-indent: 1px; background-color: #425688; font-weight: 600;}

</style>

	</head>
	<body class='body1'>
	<span class='text'>
	<form name="resolve" action="http://www.ccionline.biz/resolve.cgi" method="post">
	<input type='hidden' name='error_id' value='$hash->{error_log_id}'>
	If you fixed this problem, select your name and press the button<br>
		<select name='resolved_by' class='select1'>
			<option value='Bobby'>Bobby
			<option value='Randy'>Randy
			<option value='Dana'>Dana
			<option value='Don'>Don
			<option value='Kent'>Kent
			<option value='Group'>Group
		</select><br>
		<textarea name='comments' rows=5 cols=40></textarea><br>
		<input type='submit' value='Problem Resolved' class='body1'><br>
	</form>

	$body

	</span></body></html>
EOF
close OUTPUT;

use MIME::Lite;
use MIME::Lite::HTML;


#To       => 'error@ccionline.biz',
        my $mailHTML = new MIME::Lite::HTML
            From     => 'webmaster@ccionline.biz',
            To       => 'error@ccionline.biz',
            Subject => $subject;


        my $url = "http://www.ccionline.biz/tmp/error".$hash->{error_log_id}.".htm";

my        $MIMEmail = $mailHTML->parse($url);

        $MIMEmail->send_by_smtp('mail.ccionline.biz');


#--------------------------------------------------------------------------#
            # display pretty error message and tracking number #
print<<"EOF";
    <style type="text/css">
        /* error display */
            .errtitle {font-family: Verdana, Arial, Helvetica, sans-serif; color: #FFFFFF; font-size: 12pt; font-weight: 700; background-color: #FF0000}
            .errtxt1 {font-family: Verdana, Arial, Helvetica, sans-serif; color: #000000; font-size: 10pt; font-weight: 700; }
            .errtxt2 {font-family: Verdana, Arial, Helvetica, sans-serif; color: #000000; font-size: 9pt; font-weight: 500; }
            .redborder {border-style: solid; border-color: #FF0000; border-width: thin;}
            .bg {background-color: #C0C0C0;}
            .bg2 {background-color: #E0E0E0;}
    </style>
    <table width="60%" align="center" class="redborder" cellpadding="0" cellspacing="0">
        <tr>
            <td width="100%" align="center">
                <table width="100%" align="center" cellpadding="0" cellspacing="0">
                    <tr class="errtitle">
                        <td width="100%" align="center">$errortitle</td>
                    </tr>
                    <tr class="bg2">
                        <td width="100%" align="center"><hr width="80%" align="center" color="darkblue"></td>
                    </tr>
                    <tr class="bg">
                        <td width="100%" align="center">&nbsp;</td>
                    </tr>
                    <tr class="bg">
                        <td width="100%" align="left"><span class="errtxt1">An error has been captured and entered into our problem
                        resolution database.  Your tracking # is $hash->{error_log_id}. An email has been sent to our Problem Response
                        Team. If you have questions or concerns please contact us at
                        <a href="mailto:webmaster\@CCIonline.biz" class="link2">webmaster\@CCIonline.biz</a></span></td>
                    </tr>
                    <tr class="bg">
                        <td width="100%" align="center">&nbsp;</td>
                    </tr>
                    <tr class="bg2">
                        <td width="100%" align="center"><hr width="80%" align="center" color="darkblue"></td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
EOF
    }else{
print<<"EOF";
    <style type="text/css">
        /* error display */
            .errtitle {font-family: Verdana, Arial, Helvetica, sans-serif; color: #FFFFFF; font-size: 12pt; font-weight: 700; background-color: #FF0000}
            .errtxt1 {font-family: Verdana, Arial, Helvetica, sans-serif; color: #000000; font-size: 10pt; font-weight: 700; }
            .errtxt2 {font-family: Verdana, Arial, Helvetica, sans-serif; color: #000000; font-size: 9pt; font-weight: 500; }
            .redborder {border-style: solid; border-color: #FF0000; border-width: thin;}
            .bg {background-color: #C0C0C0;}
            .bg2 {background-color: #E0E0E0;}
    </style>
    <table width="60%" align="center" class="redborder" cellpadding="0" cellspacing="0">
        <tr>
            <td width="100%" align="center">
                <table width="100%" align="center" cellpadding="0" cellspacing="0">
                    <tr class="errtitle">
                        <td width="100%" align="center">Your session has been interrupted.  </td>
                    </tr>
                    <tr class="bg2">
                        <td width="100%" align="center"><hr width="80%" align="center" color="darkblue"></td>
                    </tr>
                    <tr class="bg">
                        <td width="100%" align="center">&nbsp;</td>
                    </tr>
                    <tr class="bg">
                        <td width="100%" align="left"><span class="errtxt1">Your ProgramsPro session has been interrupted.
                        Please close all of your browsers and login again.  If you continue to have problems, close your
                        browser again and before logging back on, delete all cookies from CCIonline.biz.
                        If you have questions or concerns please contact us at
                        <a href="mailto:webmaster\@CCIonline.biz" class="link2">webmaster\@CCIonline.biz</a></span></td>
                    </tr>
                    <tr class="bg">
                        <td width="100%" align="center">&nbsp;</td>
                    </tr>
                    <tr class="bg2">
                        <td width="100%" align="center"><hr width="80%" align="center" color="darkblue"></td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
EOF
    }

	DBCloseAll();
#--------------------------------------------------------------------------#
    # exit 0 kills the page here and does not display default message #
exit 0;

}   ##dienicely($$$$)
#--------------------------------------------------------------------------#

############################################################################
sub EscQuote2($)     # 03/30/01 5:40PM  -- RF
					# Escapes single quotes
					# Use for preparing strings for SQL statements.
############################################################################
{
    my ($delim_return) = @_;
	$delim_return =~ s/[']/''/gi;
    return $delim_return;
}   ##EscQuote($)


############################################################################
sub ErrorToHome($)		#08/05/05 2:35:PM
############################################################################
{
	my ($msg) = @_;
	my $CRLF = chr(13) . chr(10);
	my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);

	#print "$ENV{SERVER_PROTOCOL} 200 OK" . $CRLF . "Content-Type: text/html" . $CRLF . $CRLF;
print<<"EOF";
<!--<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">-->
<!-- (c) 2001-$year CCI -->
<html>
<script language='javascript'>
    window.alert('$msg');
    top.location='http://$ENV{SERVER_NAME}';
</script>
</html>
EOF
}	##ErrorToHome

return 1;
