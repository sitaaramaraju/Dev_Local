use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use DBInterface;
my $cgi = CGI->new();
my ($name, $value);
%main::cgi;

foreach $name ($cgi->param) {
        foreach $value ($cgi->param($name)) {
              $value =~ s/delete//gi;
              $value =~ s/update//gi;
              $value =~ s/alter\stable//gi;
              $value =~ s/drop\sdatabase//gi;
              $value =~ s/drop\stable//gi;
              $main::cgi{$name} = $value;
        }
}

$main::DriverType = "SQL Server";
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

my $db = DBInterface->new();

my $session_id = $main::cgi{session_id};
my $session_close;
my ($sql, $error, %st);
if ( length($session_id) == 0 ) {
    $error = 1;
    $session_close = "There is no session available for your request to proces.  Please logon from your program portal to use LeadPro";  #no session available

}elsif ($session_id <= 0){
    $error = 1;
    $session_close = "A problem has been detected with your session.  Please logon again to continue.";  #session corrupted


}else{
    $sql = "select DATEDIFF(hour, last_update_date, getdate())as dif, isnull(client.session_limit, 1)as limit
        from cookie_session, client where cookie_session.client_id = client.client_id and cookie_session.session_id = $session_id";
	my $sth = $db->prepare($sql);
    $sth->execute();
	my $st = $sth->fetchrow_hashref();
	$sth->finish();
    if ( $st->{dif} > $st->{limit} ) { #session timing out, update session table with logoff.
        $error = 1;
        $session_close = "Your session has remained inactive beyond the $st->{limit} limit.  Please logon again to continue.";
    }else{                         #active session, keep tickle up to date
        $error = 0;
        $sql = "update cookie_session set last_update_date = getdate() where session_id = $session_id";
		my $sth = $db->prepare($sql);
		$sth->execute();
		$sth->finish();
    }
}

if ( $main::cgi{server_name} eq 'cta.ccionline.biz' ) {
    $main::session{home_url} = "http://cta.ccionline.biz";
}

if ( $error > 0 ) {
#headernocss();
print $sql;
print<<"EOF";
<script language='javascript'>
    window.alert("$session_close");
    location.replace("$main::session{home_url}");
</script>
EOF
exit;
}


#---------------------------------------------------------------------------
#Populate global session hash from session record
#---------------------------------------------------------------------------

	# Extract session_id from the CGI input params
    $sql = "select cookie_session from cookie_session with(nolock) where session_id = ?";
	my $sth = $db->prepare($sql);
	$sth->execute($session_id);
	
    while (my $cookie = $sth->fetchrow_hashref) {
        my @cookies = split (/;/, $cookie->{cookie_session});
        my (%crumbs, $cookie, @pairs, $pair, $name, $value);

        foreach $cookie (@cookies) {
            @pairs = split (/,/, $cookie);
            foreach $pair (@pairs) {
                ($name, $value) = split (/=/, $pair);
                $main::session{($name)} = ($value);
            }
        }
    }

$main::cgi{cookie} = "$sql";
$sth->finish();

=head
if ( $myDB ){
    my $SQL = "select name, value from [function]  with (nolock) order by function_group_name, position";
	if (! $myDB->Sql($SQL)) {
		while ($myDB->FetchRow()) {
			my %function = $myDB->DataHash;
			$main::fp{$function{'name'}} = $function{'value'};
		}
	}
}


$myDB->Close();
=cut


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

    if ($_[0] < 0) { $sign = "-"; } else { $sign = ""; }
    $dollars = abs(int($_[0]));
    #Round to nearest cent
    #$cents = int((($_[0]-$dollars)*100)+0.5)/100;
    $cents = $_[0] - $dollars;
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

    if ($_[0] < 0) { $sign = "-"; } else { $sign = ""; }
    $dollars = abs(int($_[0]));
    #Round to nearest cent
    #$cents = int((($_[0]-$dollars)*100)+0.5)/100;
    $cents = $_[0] - $dollars;
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
sub Clean($)                 #12/12/00 11:30am
# Strips commas, dollar signs, percentage signs and errant K's from input
############################################################################
{
	my ($output) = @_;
    #$output =~ s/[,\$\%Kk]//g;
    $output =~ s/[^0-9.\-]//g;

    if ( $output eq '' ) {
       $output = 0;
    }
    return $output;
}

############################################################################
sub HasPermission($)		#10/25/00 4:00:PM
# Takes a function constant (e.g. FGI_PA_INPUT), as defined in Function
# table and returns the function constant's non-zero value (equivalent to
# a logical TRUE) if user has permission to execute function, 0 if not.
############################################################################
{
	my $function = @_[0];
	my ($prefix, $fpkey);
	$prefix = substr($function, 0, 4);
	#Determine which of the four session variables to perform bitwise AND with
	if ($prefix eq "FGI_"){
			$fpkey = "fgi_permissions";
		}
		elsif ($prefix eq "FGO_"){
			$fpkey = "fgo_permissions";
		}
		elsif ($prefix eq "FGA1"){
			$fpkey = "fga1_permissions";
		}
		elsif ($prefix eq "FGA2"){
			$fpkey = "fga2_permissions";
		}
		else {
			$fpkey = "";
		}
	#Check if we have a valid session variable to compare to
	if ( $fpkey ne "" ){
		#Return the function constant's value, which will be greater than 0
		#and is considered TRUE
		#Needed to add 0 to &'s arguments to ensure they're treated as
		#numbers, not strings
		return (($main::fp{$function}+0) & ($main::session{$fpkey}+0));
	}
	else {
		#We don't, so just return 0, which is considered FALSE
		return 0;
	}
}	##HasPermission($)

############################################################################
sub HasPermissionForClient($$$)		# 06/13/01 9:51:AM
									# Given function name, staff_id and client_id,
									# returns number > 0 if user has specified permission,
									# 0 otherwise.
############################################################################
{
	my ($function, $staff_id, $client_id) = @_;
	my $result;
	my $db = DBInterface->new();

	my $SQL = "select staff_client_list_id, fgi_permissions, fgo_permissions, fga1_permissions, fga2_permissions ".
        "From staff_client_list  with (nolock) where staff_id = ? and client_id = ?";
	my $sth = $db->prepare($SQL);	
	$sth->execute($staff_id, $client_id);
	
	if (my $hPerm = $sth->fetchrow_hashref()){
	
		my $fgi = $hPerm->{'fgi_permissions'};
		my $fgo = $hPerm->{'fgo_permissions'};
		my $fga1 = $hPerm->{'fga1_permissions'};
		my $fga2 = $hPerm->{'fga2_permissions'};

		my $fnSQL = "select value, function_group_name from [function]  with (nolock) where name = ?";
		my $sth = $db->prepare($fnSQL);
		$sth->execute($function);
		
		if (my $hFn = $sth->fetchrow_hashref()){
			
			my $fngroup = $hFn->{'function_group_name'};
			my $fnvalue = $hFn->{'value'};
			if ($fngroup eq "FGI"){
				$result = ($fgi + 0) & ($fnvalue + 0);
			}
			elsif ($fngroup eq "FGO"){
				$result = ($fgo + 0) & ($fnvalue + 0);
			}
			elsif ($fngroup eq "FGA1"){
				$result = ($fga1 + 0) & ($fnvalue + 0);
			}
			elsif ($fngroup eq "FGA2"){
				$result = ($fga2 + 0) & ($fnvalue + 0);
			}
		} # if ($db2->FetchRow())
		$sth->finish();
	} # if ($db->FetchRow())
	$sth->finish();

	return $result;
}	##HasPermissionForClient($$$)

############################################################################
sub DumpHash(\%)        #10/17/00 4:45:PM
############################################################################
{
    my (%hashRef) = @_;
    my (@keys, $counter);
    $counter = 1;
	@keys = sort keys(%hashRef);
	foreach (@keys) {
        print "<p>$counter:  $_ = $hashRef{$_}</p>";
        $counter++;
    }
}   ##DumpHash(\%)

############################################################################
sub DumpHashTable(\%)	#10/17/00 4:47:PM
# Table version of DumpHash
############################################################################
{
	my (%hashRef) = @_;
    my ($counter, $key);
    $counter = 1;

print<<"EOF";  #Start table code
<table border=1 cellpadding=5>
	<tr>
		<th Align=left width=5%>#
		<th Align=left width=30%>Key
		<th Align=left >Value
	</tr>
EOF
	foreach $key (sort keys (%hashRef)) {
print<<"EOF"; #Generate a table data row
	<tr><td Align=left width="5%">$counter
		<td Align=left width="30%">$key
		<td Align=left width="30%">$hashRef{$key}
	</tr>
EOF
        $counter++;
    }
print "</table>\n";
}	##DumpHashTable
############################################################################
sub DumpFunctionalPermissions		#10/25/00 4:05:PM
# Diagnostic function that creates a table displaying the user's
# functional permissions.
############################################################################
{
	my ($key, $counter, $flag);
	$counter = 1;

print<<"EOF";  #Start table code
<table border=1 cellpadding=5>
	<tr>
		<th Align=left width=5%>#
		<th Align=left width=30%>Function
		<th Align=left >Permission
	</tr>
EOF
	foreach $key (sort keys (%main::fp)) {
		$flag = HasPermission($key);

print<<"EOF"; #Generate a table data row
	<tr><td Align=left width=5%>$counter
		<td Align=left width=30%>$key
		<td Align=left width=30%>$flag
	</tr>
EOF
        $counter++;
    }
print "</table>\n";

}   ##Dump FunctionalPermissions

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
    ($main::SortHash{$a} cmp $main::SortHash{$b}) || ($a cmp $b);
}   ##by_names

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
	#my $db = new Win32::ODBC($main::DSN);
	my $db = DBInterface->new();
	my $sth = $db->prepare($langSQL);
	$sth->execute();
	if (my $hLang = $sth->fetchrow_hashref()) {
		#$charset_tag = "<meta http-equiv=\"charset\" content=\"$hLang{language_charset}\">";
		$charset_tag = "; charset=$hLang->{language_charset}";
	}
	$sth->finish();
	$db->disconnect();
#$ENV{SERVER_PROTOCOL} 200 OK
#Content-Type: text/html$charset_tag

print<<"EOF";


<!--<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">-->
<!-- (c) 2001-2004 CCI -->
<html>
    <head>

    </head>
EOF
require "D:/centurylinkyoucan/Universal/styles.cgi";

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
    my $langSQL = "select language_charset from language  with (nolock) where language_id = $main::session{language}";
	#my $db = new Win32::ODBC($main::DSN);
	my $db = DBInterface();
	my $sth = $db->prepare($langSQL);
	
	if (my $hLang = $sth->fetchrow_hashref()) {
		
		#$charset_tag = "<meta http-equiv=\"charset\" content=\"$hLang{language_charset}\">";
		$charset_tag = "; charset=$hLang->{language_charset}";
	}
	$sth->finish();
	$db->disconnect();

#print "$ENV{SERVER_PROTOCOL} 200 OK\n";
#print "Content-type: text/html$charset_tag\n\n";
print "<!--<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">-->\n";
print "<!-- (c) 2001-2009 CCI $charset_tag-->";
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
		my $myDB = new Win32::ODBC($main::DSN);
		#$SQL = "declare \@batch_id integer " .
		#	"execute UserSessionStart $staff_id, '$RemoteHost', '$RemoteAddr', 'ProgramsPro', '0.1', \@new_session_id output, \@session_start output " .
		#	"select \@new_session_id as session_id, \@session_start as session_start";
		my $SQL = "declare \@batch_id integer " .
			"execute CreateBatch $batch_type_id, '$batch_name', '$description', $staff_id, $client_id, \@batch_id output " .
			"select \@batch_id as batch_id";

		$myDB->Sql($SQL);
		if ($myDB->FetchRow()) {
			my %session = $myDB->DataHash;
			$myDB->Close();
			$batch_id = $session{'batch_id'};
			return $batch_id;
		}
		else {
			return -5;
		}
}	##CreateBatch

############################################################################
sub GetNextFieldInteger($$)	#03/27/01 3:39:PM
# Returns next highest integer given $table and $field.  $field must be an
# integer field.  Does not find "gaps" in integer sequence but just
# takes the "max plus 1".
#
# Parameters:
# 1. table (varchar)
# 2. field (varchar)
############################################################################
{
	my ($table, $field) = @_;
	my $NewID;
	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();
    my $SQL = "select IsNull(max($field), 1) + 1 as NewID from $table with (nolock) ";
	my $sth = $myDB->prepare($SQL);
	$sth->execute();
	
    if (my $IDHash = $sth->fetchrow_hashref()) {
		$NewID = $IDHash->{'NewID'};
		$sth->finish();
		$myDB->disconnect;
		return $NewID;
	}
	else {
		$myDB->disconnect;
		return -1;
	}
}	##GetNextFieldInteger

############################################################################
sub GetLookupValue($$$$)		#03/27/01 3:57:PM
# Returns a lookup table value given:
# 1. table (varchar)
# 2. lookupfield (varchar)
# 3. indexfield (varchar)
# 4. indexvalue (int)
# Returns empty string if query returns no results.
############################################################################
{
	my ($table, $lookupfield, $indexfield, $indexvalue) = @_;
	my $value;
	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();
    my $SQL = "select $lookupfield as value from $table  with (nolock) where $indexfield = $indexvalue";
	my $sth = $myDB->prepare($SQL);
	$sth->execute();
	
    if (my $ValueHash = $sth->fetchrow_hashref()) {
		$value = $ValueHash->{value};
		$sth->finish();
		$myDB->disconnect();
		return $value;
	}
	else {
		$myDB->disconnect();
		return "";
	}

}	##GetLookupValue

############################################################################
# Trims leading and trailing spaces.
# Derived from: http://www.biglist.com/lists/xsl-list/archives/200112/msg01080.html
sub trim($) {
	my ($var) = @_;
	$var =~ s/^\s*//;  #remove leading spaces
	$var =~ s/\s*$//;  #remove trailing spaces
    return $var;
}

############################################################################
sub EscQuote($)    # 03/30/01 5:40PM  -- RF
                   # Escapes single quotes
                   # Use for preparing strings for SQL statements.
############################################################################
{
    my ($delim_return) = @_;
    $delim_return =~ s/[']/''/gi;
    return $delim_return;
}                  ##EscQuote($)

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
sub get_filename2($$)   # 05/21/02 12:49:PM RF
					    # Given path + filename and delimiter character (usually / or \),
						# returns the filename
					    # e.g. "/dir1/dir2/myfile.txt" returns "myfile.txt"
############################################################################
 {
	my ($fullpathname, $delimiter) = @_;
	if ( $delimiter eq '' ) {
		$delimiter = '/';
	}
	my $pos = length($fullpathname)-1;
	my $result = -1;
	my $filename = $fullpathname;  #If slash isn't found, default to $fullpathname
	while ( $pos >= 0 && $result == -1) {
		$result = index($fullpathname, $delimiter, $pos);
		$pos--;
	}
	if ( $result > -1 ) {
		$filename = substr($fullpathname, $result + 1, (length($fullpathname) - $result));
	}
	return $filename;
}	##get_filename($)

############################################################################
sub getDateType ()          # gets the correct date format (american or
                            # european) based on session variables
############################################################################
{

    my $date_type;

    if ($main::session{'precedence'} <= 20 ) {
        $date_type = $main::session{'cust_date_type'};
    }
    elsif ($main::session{'precedence'} < 100) {
        $date_type = $main::session{'date_type'};
    }
    else {
        $date_type = 1;
    }

    return $date_type;

}

############################################################################
sub getYear     #09/24/10 1:30:PM
############################################################################
 {
    my ($second, $minute, $hour, $dayOfMonth, $month, $yearOffset, $dayOfWeek, $dayOfYear, $daylightSavings) = localtime();
    my $year = 1900 + $yearOffset;
    return $year;
}   ##getYear


return 1;
