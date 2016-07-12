use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
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


if ( uc(substr($main::session{logonID},0,4)) eq "CCIS") {
  #  $main::DSN = "DSN=co-opsales;UID=sa;PWD=lotrtt";
  $main::DSN = 'driver={SQL Server};Server=devdb.coopcom.net;database=staging;uid=fm;pwd=sep49sling;';

}else{
 #   $main::DSN = "DSN=co-op;UID=sa;PWD=lotrtt";
   # $main::DSN = 'driver={SQL Server};Server=1.1.1.2;database=coop;uid=fm;pwd=sep49sling;';
  #  $main::DSN = 'driver={SQL Server};Server=galaxy2.cciprod.local;database=coop;uid=fm;pwd=sep49sling;';
#    $main::DSN = 'driver={SQL Server};Server=galaxynew.cciprod.local;database=coop;uid=fm;pwd=sep49sling;';

$main::DSN = 'driver={SQL Server};Server=devdb.coopcom.net;database=staging;uid=fm;pwd=sep49sling;';

   #$main::DSN = 'driver={SQL Server};Server=1.1.1.2;database=staging;uid=fm;pwd=sep49sling;';

}

my $myDB = new Win32::ODBC($main::DSN);


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

my $cgi = CGI->new();
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


    my $DSN2="";
    if ( uc(substr($logon,0,4)) eq "CCIS" ) {
        $DSN2 = "DSN=co-opsales;UID=sa;PWD=lotrtt";
        $main::DSN = "DSN=co-opsales;UID=sa;PWD=lotrtt";
    }else{
        $DSN2 = "DSN=co-op;UID=sa;PWD=lotrtt";
        $DSN2 = 'driver={SQL Server};Server=1.1.1.2;database=coop;uid=fm;pwd=sep49sling;';
	#$DSN2 = 'driver={SQL Server};Server=galaxy2.cciprod.local;database=coop;uid=fm;pwd=sep49sling;';

	$DSN2 = 'driver={SQL Server};Server=galaxynew.cciprod.local;database=coop;uid=fm;pwd=sep49sling;';

        #$DSN2 = 'driver={SQL Server};Server=1.1.1.2;database=staging;uid=fm;pwd=sep49sling;';
    }
#print "Content-type:text/html\n\n";print "here";exit();

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

    my $myDB = new Win32::ODBC($main::DSN);
    my $mySession = new Win32::ODBC($main::DSN);
    my $CustDB = new Win32::ODBC($main::DSN);
    if (! $myDB) {#Verify the connection is valid
		#print "<h3>Failed to Connect $main::DSN</h3>\n";
		Win32::ODBC::DumpError();
		#print "</BODY>\n";   print "</HTML>\n";
                exit;
	}

    my $SQL;
    my $SQL_test;

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
        $SQL = "select left(home_zip,5), rtrim(first_name)+' ' + ltrim(last_name) as name, emplid as staff_id,
                            emplid as contact_info_id, 'qwesthr' as user_type, 2 as source
                        from qwesthr with (nolock) ,qwesthr_password with (nolock)
                        where qwesthr.cuid = qwesthr_password.cuid
                        and qwesthr_password.cuid = '$logon' and password = '$password'
                union
                select left(home_zip,5) as home_zip, rtrim(first_name)+' ' + ltrim(last_name) as name, emplid as staff_id,
                        emplid as contact_info_id, 'qwesthr' as user_type, 2 as source
                        from qwesthr with (nolock)
                        where cuid = '$logon' and left(home_zip,5) = '$short_password'
				 union
                 select left(last_name,5) as home_zip, rtrim(first_name)+' ' + ltrim(last_name) as name, floater_id as staff_id,
                        floater_id as contact_info_id, 'ctl_floater' as user_type, 25 as source
                        from ctl_floaters with (nolock)
                        where cuid = '$logon' and last_name = '$password'   
				union
                select left(home_zip,5) as home_zip, rtrim(first_name)+' ' + ltrim(last_name) as name, emplid as staff_id,
                        emplid as contact_info_id, 'qwesthr' as user_type, 2 as source
                        from qwesthr with (nolock)
                        where SAP_ID = '$logon' and left(home_zip,5) = '$short_password'
                   union
                   select left(home_zip,5), rtrim(first_name)+' ' + ltrim(last_name) as name, emplid as staff_id,
                            emplid as contact_info_id, 'qwesthr' as user_type, 2 as source
                        from qwesthr with (nolock) ,qwesthr_password with (nolock)
                        where qwesthr.cuid = qwesthr_password.cuid
                        and qwesthr.SAP_ID = '$logon' and password = '$password'     
                order by 1 ";
            if ($myDB->Sql($SQL)) {
            print "<h3>Error getting query results</h3>\n";
            $myDB->DumpError();
            print "<br>$SQL";
            }
            $myDB->FetchRow();
            my %user = $myDB->DataHash;
			$source_id = $user{source};
            if ( length($user{staff_id}) > 0 && ( $logon ne $main::INVALIDLOGIN || $short_password ne $main::INVALIDLOGIN ) ) {
                $pass = 2;
            }else{
                #wrong password
                $pass = 0;
            }
    }else{
# ------------------------------------------------------------------------
#
	#Retrieve fields from staff.  For positive validation, LogonID and Password must match and user must be active
    my $SQL = "select staff.staff_id, staff.name, staff.contact_info_id, user_type.description as user_type, 1 as source
               from staff with (nolock), user_type with (nolock), lkup_staff_application with(nolock)
               where staff.staff_id = lkup_staff_application.staff_id and lkup_staff_application.application_id = 3
                    and staff.LogonID = '$logon' and staff.Password = '$password'
                    and staff.user_type_id = user_type.user_type_id and staff.IsActive = 1";

    if ($myDB->Sql($SQL)) {
		die;
	}
    $myDB->FetchRow();
    my %user = $myDB->DataHash;
    if ( length($user{staff_id})> 0 && ($logon ne $main::INVALIDLOGIN || $password ne $main::INVALIDLOGIN)) {
        $pass = 5;
    }
    }
# ------------------------------------------------------------------------
#logon/ user found, setup session vars

    if ( $pass > 0 ) {
        #User was found given userid and password
		$status = $status . "[User is Valid]";
        $myDB->Sql($SQL);
    	my %user = $myDB->DataHash;
    	my $staff_id = $user{'staff_id'};
        my $asp = 3;
        my $logonID = $logon;
        my $asp_system_owner = $user{'asp_system_owner'};
    	my $username = $user{'name'};
		my $contact_info_id = $user{'contact_info_id'};
		my $user_type = $user{'description'};
        my ($client_id, $fgi, $fgo, $fga1, $fga2, $client_name, $program_name, $logo, $home_url);
        my ($cust_id, $user_level, $e_mail, $address1, $address2, $city, $state, $zip, $country, $phone, $fax, $email, $precedence,
              $date_type, $cust_date_type);
        my $group_id = -1;
        if ( $source_id == 1 ) {
            $SQL = "select group_id
					from contact_info with (nolock)
					where contact_info_id = $contact_info_id";
            $myDB->Sql($SQL);
            if ($myDB->FetchRow()) {
              my %group_hash = $myDB->DataHash;
              $group_id = $group_hash{'group_id'};
            }

          #Retrieve staff_client_list record count
          $SQL = "select count(staff_client_list_id) as record_count from staff_client_list  with (nolock) where staff_id = $staff_id";
          $myDB->Sql($SQL);
          $myDB->FetchRow();
          my %count_hash = $myDB->DataHash;
          $client_count = $count_hash{'record_count'};
          $status = $status . "[SCL Ct: $client_count]";
          $date_type = 1;
          $cust_date_type = 1;
        }
        if ( $source_id == 2 ) { #qwesthr
            $client_count = 1;
            $client_count = 1;
            $status = $status . "[SCL Ct: $client_count]";
        }
        # ----------------------------------------------------------------
        #
            $client_count = 1;
        if ( $client_count == 1 ){
            if ( $source_id == 1 ) {
            # One staff_client_list record exists; retrieve that record and populate some variables
			$SQL = "select client_id, staff_client_list.user_level, fgi_permissions, fgo_permissions, fga1_permissions,
                            fga2_permissions, staff_client_list.user_level, precedence, staff_client_list.cu_cust_id
                		from staff_client_list with (nolock), WebAccessLevel with (nolock)
						where staff_id = $staff_id and staff_client_list.user_level = WebAccessLevel.name";
			$myDB->Sql($SQL);
			$myDB->FetchRow();
			my %staff_client_hash = $myDB->DataHash;
              $client_id = $staff_client_hash{'client_id'};
              $user_level = $staff_client_hash{'user_level'};
              $fgi = $staff_client_hash{'fgi_permissions'};
              $fgo = $staff_client_hash{'fgo_permissions'};
              $fga1 = $staff_client_hash{'fga1_permissions'};
              $fga2 = $staff_client_hash{'fga2_permissions'};
              $precedence = $staff_client_hash{'precedence'};
              $cust_id = $staff_client_hash{'cu_cust_id'};
            }else { #($source_id == 2){ to take care of ctl_floaters
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
					where client_id = $client_id";
			$myDB->Sql($SQL);
			if ($myDB->FetchRow()) {
				my %ClientHash = $myDB->DataHash;
				$client_name = $ClientHash{'client_name'};
				$program_name = $ClientHash{'program_name'};
				$logo = $ClientHash{'logo'};
				$navigation_version = $ClientHash{'navigation_version'};
				$home_url = $ClientHash{'home_url'};
				$address1 = $ClientHash{'address1'};
				$address2 = $ClientHash{'address2'};
				$city = $ClientHash{'city'};
				$state = $ClientHash{'state'};
				$zip = $ClientHash{'zip'};
				$country = $ClientHash{'country'};
				$phone = $ClientHash{'phone'};
				$fax = $ClientHash{'fax'};
				$email = $ClientHash{'email'};
				$date_type = $ClientHash{'date_type'};
            }

        } #if ( $client_count == 1 )

        # Create a new session ID

		my $session_id = -1;
		my $session_start = "";

		# Start a new session by calling SP UserSessionStart
		$SQL = "declare \@new_session_id integer declare \@session_start datetime " .
            "execute UserSessionStart2 $staff_id, '$RemoteHost', '$RemoteAddr', 'ProgramsPro', '$main::AppVersion', \@new_session_id output, \@session_start output, " .
            "'$ENV{'HTTP_HOST'}', '$browser_name', '$browser_version', $source_id " .
            "select \@new_session_id as session_id, \@session_start as session_start ";

		if ($myDB->Sql($SQL)) {
			#print "<h3>Error getting query results</h3>\n";
			#$myDB->DumpError();
		}
		else {
			if ($myDB->FetchRow()) {
				my %session = $myDB->DataHash;
				$session_id = $session{'session_id'};
				$session_start = $session{'session_start'};
			}
		}

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
	$Cookie = EscQuote($Cookie);


  my $sql = "insert into cookie_session (cookie_session, staff_id, created_date, last_update_date, session_id)
                values ('$Cookie', $staff_id, getdate(), getdate(), $session_id)";
        if ($myDB->Sql($sql)){
                die $myDB->Error();

        }
        $myDB->FetchRow();
        my %cookie_id = $myDB->DataHash;

       # $SQL = "insert into session(session_id, Logon_Date_Time, staff_id, user_name, name, contact_info_id, user_type, remote_host, remote_addr,
       #         referrer, http_referer, client_count, cust_count, group_id, validation_status, asp, logonid, asp_system_owner, language,
       #         browser_name, browser_version, date_type, cust_id, cust_date_type, client_id, user_level, precedence,
       #         fgi_permissions, fgo_permissions, fga1_permissions, fga2_permissions, client_name, program_name, logo, home_url,
       #         navigation_version, client_address1, client_address2, client_city, client_state, client_zip, client_country,
       #         client_phone, client_fax, client_email, tickle)
       #         values($session_id, getdate(), $staff_id, '$user{name}', '$user{name}', $contact_info_id, '$user{user_type}', '$RemoteHost', '$RemoteAddr',
       #         '$Referer','$Referer', $client_count , $cust_count, $group_id, '$status', '$asp', '$logonID', '$asp_system_owner', 1,
       #         '$browser_name', '$browser_version', '$date_type', '$cust_id', '$date_type', $client_id, '$user_level', $precedence,
       #         '$fgi', '$fgo', '$fga1', '$fga2', '$client_name', '$program_name', '$logo', '$home_url',
       #         '$navigation_version', '$address1', '$address2', '$city', '$state', '$zip', '$country',
       #         '$phone', '$fax', '$email', getdate()) ";
       # if ($myDB->Sql($SQL)) {
       #     print "<h3>Error getting query results</h3>\n";
       #     $myDB->DumpError();
       #     print "<br>$SQL";
       #}

#headernocss();
#print "Content-type:text/html\n\n";
print<<"EOF";
<body>
<form name='direct' method='post' action='/sbgemailbuilder/landing.cgi'>
<input type='hidden' name='session_id' value='$session_id'>
<input type='hidden' name='source_id' value='$source_id'>
<input type='hidden' name='program_id' value='$main::cgi{program_id}'>
<input type='hidden' name='fund_id' value='$main::cgi{fund_id}'>

<script language='javascript'>
    document.direct.submit();
</script>
</body>
</html>
EOF
#print "Content-type:text/html\n\n";print "here";exit();

#die $SQL;

    }else{
            #Insert logon attempt record into user_session_attempt
            my $AttemptSQL = "insert into user_session_attempt
                    (attempt_date, LogonID, Password, machine, IP, app, version, http_host, browser_name, browser_version)
                    values (GetDate(), '$logon', '$password', '$RemoteHost', '$RemoteAddr', 'ProgramsPro', '$main::AppVersion',
                    '$ENV{HTTP_HOST}', '$browser_name', '$browser_version')";
            $myDB->Sql($AttemptSQL);
            $ReturnHash{status} = "Invalid";
            $ReturnHash{navigation_version} = $navigation_version;
headernocss();
print<<"EOF";
<body>
<script language='javascript'>
    location.replace("http://www.smallbizmailtool.com?user_type=Invalid");
</script>
</body>
</html>
EOF
    }

    $myDB->Close();
    $mySession->Close();
    $CustDB->Close();

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
}   ##SubSemicolons($)


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
	my $db = new Win32::ODBC($main::DSN);
	$db->Sql($langSQL);
	if ($db->FetchRow()) {
		my %hLang = $db->DataHash();
		#$charset_tag = "<meta http-equiv=\"charset\" content=\"$hLang{language_charset}\">";
		$charset_tag = "; charset=$hLang{language_charset}";
	}
	$db->Close();

print "$ENV{SERVER_PROTOCOL} 200 OK\n";
#print "Content-type: text/html$charset_tag\n\n";
print "<!--<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">-->\n";
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
}                  ##EscQuote($)

