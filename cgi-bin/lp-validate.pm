use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use CCICryptography;
use DBInterface;
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

my $myDB = DBInterface->new();
my $cgi = CGI->new();

if (! $myDB) {
print<<"EOF";
$ENV{SERVER_PROTOCOL} 200 OK
Content-Type: text/html

<!--<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">-->
<!-- (c) 2001-2005 CCI -->
<html>
<script language='javascript'>
    window.alert('Our apologies.  The application appears to be unavailable at this time.  The Information Systems department has been contacted.  Please attempt to connect again at a later time.  Thank you.');
    document.location='http://www.ccionline.biz';
</script>
EOF
}

my ($name, $value);
%main::cgi;
foreach $name ($cgi->param) {
        foreach $value ($cgi->param($name)) {
              $main::cgi{$name} = $value;
        }
}

my ($logon, $password, $browser_name, $browser_version, $session_id, $source_id);
$logon = $main::cgi{userid};
$password = $main::cgi{password};
$source_id = $main::cgi{source_id};
if ( $source_id eq "" ) {
    $source_id = 1;
}
my $pass = 0;

# ------------------------------------------------------------------------
# General Setup
	#10/26/01 RF: Override $browser_name and $browser_version with correct values
	my $browser = $ENV{'HTTP_USER_AGENT'};
	my ($name, $version, $pos);
	# Search for MSIE first because both IE and Netscape have 'Mozilla' in their
	# browser strings
	if ($ENV{'HTTP_USER_AGENT'} =~ m/MSIE/gi){
		$browser_name = 'MSIE';
		$pos = index ($browser, 'MSIE');
		$browser_version = GetNumber($browser, ($pos + 5));
	}
	elsif ($ENV{'HTTP_USER_AGENT'} =~ m/Mozilla/gi){
		$browser_name = 'Netscape';
		$pos = FindFirstNumberCharPosition($browser);
		$browser_version = GetNumber($browser, $pos);
	}

	
	my $DriverType2 = "SQL Server";
	my $client_count = 0;  #initialize to 0
	my $cust_count = 0;
	my $status = "";
	my $navigation_version;
	my %ReturnHash;

	my $RemoteAddr = $ENV{'REMOTE_ADDR'};
	my $OrigRemoteHost = $ENV{'REMOTE_HOST'};
	my $RemoteHost = $ENV{'REMOTE_HOST'};
	my $Referer = $ENV{'HTTP_REFERER'};

	# Source: AXS Script Set, Logging Module  	<http://www.xav.com/scripts/axs>
	# This code converts un-resolved hostnames to their text versions, then makes
	# the names lowercase.

	my $SQL;

	# 5/22/02 RF: To prevent hackers from possibly executing a malicious delete or update statement,
	#             strip 'delete' and 'update' from $logon and $password
	$logon =~ s/delete//gi;
	$logon =~ s/update//gi;
    $logon =~ s/alter\stable//gi;
    $logon =~ s/drop\stable//gi;
    $logon =~ s/drop\database//gi;
	$password =~ s/delete//gi;
    $password =~ s/update//gi;
    $password =~ s/alter\stable//gi;
    $password =~ s/drop\stable//gi;
    $password =~ s/drop\database//gi;

    if ( length($password) == 0 ) {
        $pass = 0;
    }

# ------------------------------------------------------------------------
    #qwesthr search if source_id = 2
    if ( $source_id == 2 ) {
        my $short_password = substr($password, 0, 5);

		######################
		$SQL = "exec sp_CTL_Employee_Logon ?, ? ";
		my $sth = $myDB->prepare($SQL);
		$sth->execute($logon, $password);
		my $user = $sth->fetchrow_hashref;
		#print "$SQL $logon, $password $user";
		
        if ( length($user->{staff_id}) > 0 && ( $logon ne $main::INVALIDLOGIN || $short_password ne $main::INVALIDLOGIN ) ) {
            $pass = 2;
        }
		else {
            #wrong password
            $pass = 0;
        }
		
		$sth->finish();
    }
	else {
		# ------------------------------------------------------------------------
		#Retrieve fields from staff.  For positive validation, LogonID and Password must match and user must be active
		
=head

		my $SQL = "select staff.staff_id, staff.name, staff.contact_info_id, user_type.description as user_type, 1 as source
               from staff with (nolock), user_type with (nolock), lkup_staff_application with(nolock)
               where staff.staff_id = lkup_staff_application.staff_id and lkup_staff_application.application_id = 3
                    and staff.LogonID = ? and staff.Password = ?
                    and staff.user_type_id = user_type.user_type_id and staff.IsActive = 1";
=cut
		 $SQL = "select staff.staff_id, staff.name, staff.contact_info_id, user_type.description as user_type, 1 as source
               from staff with (nolock)
               inner join  user_type with (nolock) on user_type.user_type_id = staff.user_type_id
               inner join lkup_staff_application with(nolock) on lkup_staff_application.staff_id = staff.staff_id
               where  lkup_staff_application.application_id = 3
               and staff.LogonID = ? and staff.Password = ?
               and staff.IsActive = 1";
		my $sth = $myDB->prepare($SQL);
		$sth->execute($logon, $password); 
		my $user = $sth->fetchrow_hashref();
				
		if (! $user){
		#	die;
		print<<"EOF";
			
			<!--<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">-->
			<!-- (c) 2001-2016 CCI -->
			<html>
			<script language='javascript'>
				window.alert('Your user name or password was incorrect. Please try again. Thank you.');
				document.location="$Referer";
			</script>
EOF
		exit();	
		}

		if ( length($user->{staff_id})> 0 && ($logon ne $main::INVALIDLOGIN || $password ne $main::INVALIDLOGIN)) {
			$pass = 5;
		}
		
		$sth->finish();
    }
# ------------------------------------------------------------------------
#logon/ user found, setup session vars

if ( $pass > 0 ) {

        #User was found given userid and password
		$status = $status . "[User is Valid]";
		#################
		my $sth = $myDB->prepare($SQL);
		$sth->execute($logon, $password);
		my $user = $sth->fetchrow_hashref;		
		$sth->finish();
		################		
    	my $staff_id = $user->{'staff_id'};
        my $asp = 3;
        my $logonID = $logon;
        my $asp_system_owner = $user->{'asp_system_owner'};
    	my $username = $user->{'name'};
		my $contact_info_id = $user->{'contact_info_id'};
		my $user_type = $user->{'description'};
        my ($client_id, $fgi, $fgo, $fga1, $fga2, $client_name, $program_name, $logo, $home_url);
        my ($cust_id, $user_level, $e_mail, $address1, $address2, $city, $state, $zip, $country, $phone, $fax, $email, $precedence,
              $date_type, $cust_date_type, $employee_id, $supervisor_id);
        my $group_id = -1;
        if ( $source_id == 1 ) {
            $SQL = "select group_id, employee_id, supervisor_id
					from contact_info with (nolock)
					where contact_info_id = ?";
			my $sth = $myDB->prepare($SQL);
			$sth->execute($contact_info_id);
			my $group_hash = $sth->fetchrow_hashref();
           
              $group_id = $group_hash->{'group_id'};
			  $employee_id = $group_hash->{'employee_id'};
			  $supervisor_id = $group_hash->{'supervisor_id'}; 
			$sth->finish();	

          #Retrieve staff_client_list record count
          $SQL = "select count(staff_client_list_id) as record_count from staff_client_list  with (nolock) where staff_id = ?";
		  my $sth = $myDB->prepare($SQL);
		  $sth->execute($staff_id);
		  my $count_hash = $sth->fetchrow_hashref();
		  
          $client_count = $count_hash->{'record_count'};
          $status = $status . "[SCL Ct: $client_count]";
          $date_type = 1;
          $cust_date_type = 1;
		  $sth->finish();
        }
		
        if ( $source_id == 2 ) { #qwesthr
            $client_count = 1;
            $client_count = 1;
            $status = $status . "[SCL Ct: $client_count]";
        }
        # ----------------------------------------------------------------
        #

        if ( $client_count == 1 ){
            if ( $source_id == 1 ) {
            # One staff_client_list record exists; retrieve that record and populate some variables
			$SQL = "select client_id, staff_client_list.user_level, fgi_permissions, fgo_permissions, fga1_permissions,
                            fga2_permissions, staff_client_list.user_level, precedence, staff_client_list.cu_cust_id
                		from staff_client_list with (nolock), WebAccessLevel with (nolock)
						where staff_id = ? and staff_client_list.user_level = WebAccessLevel.name";
						
			my $sth = $myDB->prepare($SQL);
			$sth->execute($staff_id);
			my $staff_client_hash = $sth->fetchrow_hashref();
			
	          $client_id = $staff_client_hash->{'client_id'};
              $user_level = $staff_client_hash->{'user_level'};
              $fgi = $staff_client_hash->{'fgi_permissions'};
              $fgo = $staff_client_hash->{'fgo_permissions'};
              $fga1 = $staff_client_hash->{'fga1_permissions'};
              $fga2 = $staff_client_hash->{'fga2_permissions'};
              $precedence = $staff_client_hash->{'precedence'};
              $cust_id = $staff_client_hash->{'cu_cust_id'};
			  
			$sth->finish();  
            }elsif ($source_id == 2){
              $client_id = 50;
              $user_level = 'CU';
              $fgi = '';
              $fgo = '';
              $fga1 = '';
              $fga2 = '';
              $precedence = 20;
              $cust_id = $staff_id;
            }

			#Query for client-related information
			$SQL = "select client_name, program_name, logo, home_url, navigation_version, address1, address2, city, state, zip,
						country, phone, fax, email, date_type from client with (nolock)
					where client_id = ?";

			my $sth =  $myDB->prepare($SQL);	
			$sth->execute($client_id);				
			my $ClientHash = $sth->fetchrow_hashref();
					
			if ($ClientHash) {				 
				$client_name = $ClientHash->{'client_name'};
				$program_name = $ClientHash->{'program_name'};
				$logo = $ClientHash->{'logo'};
				$navigation_version = $ClientHash->{'navigation_version'};
				$home_url = $ClientHash->{'home_url'};
				$address1 = $ClientHash->{'address1'};
				$address2 = $ClientHash->{'address2'};
				$city = $ClientHash->{'city'};
				$state = $ClientHash->{'state'};
				$zip = $ClientHash->{'zip'};
				$country = $ClientHash->{'country'};
				$phone = $ClientHash->{'phone'};
				$fax = $ClientHash->{'fax'};
				$email = $ClientHash->{'email'};
				$date_type = $ClientHash->{'date_type'};
            }

			$sth->finish();		

        } #if ( $client_count == 1 )

        # Create a new session ID

		my $session_id = -1;
		my $session_start = "";

		# Start a new session by calling SP UserSessionStart
	
		my $sql = "declare \@new_session_id integer declare \@session_start datetime " .
            "execute UserSessionStart2 ?, ?, ?, ?, ?, \@new_session_id output, \@session_start output, " .
            "'$ENV{'HTTP_HOST'}', '$browser_name', '$browser_version', $source_id " .
            "select \@new_session_id as session_id, \@session_start as session_start ";
			
		my $sth =  $myDB->prepare($sql);	
		$sth->execute($staff_id,$RemoteHost,$RemoteAddr,'ProgramsPro', $main::AppVersion);				
		my $session = $sth->fetchrow_hashref();

		$session_id = $session->{'session_id'};
		$session_start = $session->{'session_start'};

		$sth->finish();		

		
#############################
my $plaintext = $session_id.'-'.$staff_id;
my $encoded = CCICryptography::encrypt($plaintext);

        $main::session{session_id} = $session_id;

        my $Cookie = ("cookie_name") . "=" . ("X");
        my $CookieHeader = $Cookie;
    	$Cookie = $Cookie . "," . ("staff_id") . "=" . ($staff_id);
    	$Cookie = $Cookie . "," . ("name") . "=" . ($username);
    	$Cookie = $Cookie . "," . ("contact_info_id") . "=" . ($contact_info_id);
        $Cookie = $Cookie . "," . ("user_type") . "=" . ($user_type);
        $Cookie = $Cookie . "," . ("session_id") . "=" . ($session_id);
        $Cookie = $Cookie . "," . ("remote_host") . "=" . ($RemoteHost);
        $Cookie = $Cookie . "," . ("remote_addr") . "=" . ($RemoteAddr);
        $Cookie = $Cookie . "," . ("http_referer") . "=" . ($Referer);
        $Cookie = $Cookie . "," . ("validation_status") . "=" . ($status);
        $Cookie = $Cookie . "," . ("asp_id") . "=" . ($asp);
        $Cookie = $Cookie . "," . ("asp_system_owner") . "=" . ($asp_system_owner);
        $Cookie = $Cookie . "," . ("language") . "=" . ('1') ;
        $Cookie = $Cookie . "," . ("browser_name") . "=" . ($browser_name);
        $Cookie = $Cookie . "," . ("browser_version") . "=" . (SubSemicolons($browser_version));
        $Cookie = $Cookie . "," . ("client_id") . "=" . ($client_id);
        $Cookie = $Cookie . "," . ("user_level") . "=" . ($user_level);
        $Cookie = $Cookie . "," . ("precedence") . "=" . ($precedence);
        $Cookie = $Cookie . "," . ("fgi_permissions") . "=" . ($fgi);
        $Cookie = $Cookie . "," . ("fgo_permissions") . "=" . ($fgo);
        $Cookie = $Cookie . "," . ("fga1_permissions") . "=" . ($fga1);
        $Cookie = $Cookie . "," . ("fga2_permissions") . "=" . ($fga2);
        $Cookie = $Cookie . "," . ("client_name") . "=" . ($client_name);
        $Cookie = $Cookie . "," . ("program_name") . "=" . ($program_name);
        $Cookie = $Cookie . "," . ("home_url") . "=" . ($home_url);
        $Cookie = $Cookie . "," . ("client_address1") . "=" . ($address1);
        $Cookie = $Cookie . "," . ("client_address2") . "=" . ($address2);
        $Cookie = $Cookie . "," . ("client_city") . "=" . ($city);
        $Cookie = $Cookie . "," . ("client_state") . "=" . ($state);
        $Cookie = $Cookie . "," . ("client_zip") . "=" . ($zip);
        $Cookie = $Cookie . "," . ("client_country") . "=" . ($country);
        $Cookie = $Cookie . "," . ("client_phone") . "=" . ($phone);
        $Cookie = $Cookie . "," . ("client_fax") . "=" . ($fax);
        $Cookie = $Cookie . "," . ("client_email") . "=" . ($email);
        $Cookie = $Cookie . "," . ("date_type") . "=" . ($date_type);
        $Cookie = $Cookie . "," . ("cust_id") . "=" . ($cust_id);
        $Cookie = $Cookie . "," . ("cust_date_type") . "=" . ($cust_date_type);
        $Cookie = $Cookie . "," . ("source_id") . "=" . ($source_id);
		$Cookie = $Cookie . "," . ("employee_id") . "=" . ($employee_id);
		$Cookie = $Cookie . "," . ("supervisor_id") . "=" . ($supervisor_id);
		$Cookie = $Cookie . "," . ("cci_id") . "=" . ($encoded); 
		$Cookie = $Cookie . "," ."secure, HttpOnly";
		

		$Cookie = EscQuote($Cookie);
        my $sql = "insert into cookie_session (cookie_session, staff_id, session_id, created_date, last_update_date)
                values (?,?,?, getdate(), getdate())";
				
        my $sth =  $myDB->prepare($sql);	
		$sth->execute($Cookie, $staff_id, $session_id);				
		my $cookie_id = $sth->fetchrow_hashref();
		
		$sth->finish();
		
        
headernocss();
print<<"EOF";
<body>
<form name='direct' method='post' action='lp-directional.cgi'>
<input type='hidden' name='session_id' value='$session_id'>
<input type='hidden' name='cci_id' value='$encoded'>
<input type='hidden' name='source_id' value='$source_id'>
<input type='hidden' name='program_id' value='$main::cgi{program_id}'>
<input type='hidden' name='fund_id' value='$main::cgi{fund_id}'>

<script language='javascript'>
    document.direct.submit();
</script>
</form>
</body>
</html>
EOF
#die $SQL;

}
else {
            #Insert logon attempt record into user_session_attempt
            my $AttemptSQL = "insert into user_session_attempt
                    (LogonID, Password, machine, IP, app, version, http_host, browser_name, browser_version, attempt_date)
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, getdate())";
					
            	
			my $sth =  $myDB->prepare($AttemptSQL);	
			$sth->execute($logon, $password, $RemoteHost, $RemoteAddr, 'ProgramsPro', $main::AppVersion,
                    $main::ServerIP, $browser_name, $browser_version);
			$sth->finish();
			
            $ReturnHash{status} = "Invalid";
            $ReturnHash{navigation_version} = $navigation_version;
			
			
headernocss();

print<<"EOF";
<body>
<script language="JavaScript">
       window.alert('Your user name or password was incorrect. Please try again.')
       location.replace("Javascript:history.back(-1);");
</script>
</body>
</html>
EOF

}

$myDB->disconnect();

############################################################################
sub SubSemicolons($)       #02/28/01 10:38:AM
# Use this sub when passing data between forms using the action and input
# types to pass data.  This will allow the quotes and double quotes to
# display properly and pass cleanly,
############################################################################
 {
    my ($new_delim) = @_;
    if ($new_delim =~ m/[;]/gi) {
        $new_delim =~ s/[;]/-/gi;
    }
    return $new_delim;
}


############################################################################
sub FindFirstNumberCharPosition($)		# 10/26/01 10:53:AM
										# Finds the first position in string $str
										# On failure, it returns the length or $str
############################################################################
{
	my ($str) = @_;
	my $index = 0;
	my $len = length($str);
	my $continue = 1;
	my $char;
	while ($continue == 1) {
		$char = substr($str, $index, 1);
		if ($char =~ m/[0-9.]/gi){
			$continue = 0;
		}
		else {
			$index++;
			if ($index >= $len){
				$continue = 0;
			}
		}
	}
	return $index;
}	##FindFirstNumberChar($)
############################################################################
sub GetNumber($$)		# 10/26/01 10:51:AM
						# Extracts a number in $str starting from position $pos
						# Parameters: $str (string), $pos (integer)
############################################################################
{
	my ($str, $pos) = @_;
	my $index = $pos;
	my $len = length($str);
	my $continue = 1;
	my $char;
	while ($continue == 1) {
		$char = substr($str, $index, 1);
		if ($char =~ m/[0-9.]/gi){
			$index++;
			if ($index >= $len){
				$continue = 0;
			}
		}
		else {
			$continue = 0;
		}
	}
	return substr($str, $pos, ($index - $pos));
}   ##GetNumber($$)

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
	my $myDB = DBInterface->new();
	my $sth =  $myDB->prepare($langSQL);	
	$sth->execute();				
	my $hLang = $sth->fetchrow_hashref();
	$charset_tag = "; charset=$hLang->{language_charset}";
	$sth->finish();
#print "$ENV{SERVER_PROTOCOL} 200 OK\n";
#print "Content-type: text/html$charset_tag\n\n";
#print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">-->\n";
print "<!-- (c) 2001-2004 CCI $charset_tag-->";
print "<!-- $langSQL -->";
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
$myDB->disconnect;
}   ##header

############################################################################
sub EscQuote($)    # 03/30/01 5:40PM  -- RF
                   # Escapes single quotes
                   # Use for preparing strings for SQL statements.
############################################################################
{
    my ($delim_return) = @_;
    $delim_return =~ s/[']/''/gi;
    return $delim_return;
}

1;

