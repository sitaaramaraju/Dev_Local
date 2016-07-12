# File used to direct traffic.  Each user has a user type..  the user type will
# specify the path/direction that the user will follow
# file name:  /lp_directional.pm
# last modified 7/21/04  DLF
############################################################################
# following lines required on all pages
############################################################################
use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use CCICryptography;
use DBInterface;

require "D:/centurylinkyoucan/cgi-bin/lp-init.pm";

my $db = DBInterface->new();

if ( 1 == 1 ) {

# ###########################################################################
# This first step if for invalid userid/password combinations.
my ($err, $site);
my $UserType = $main::cgi{user_type};
my $server = $main::cgi{server_name};

if ( $UserType eq "Invalid" ) {
header();
print $server;
if ( $main::cgi{server_name} eq 'www.qwestrad.com' || $main::cgi{server_name} eq 'qwestrad.com') {
	$err = "The logon you entered does not exist, please try your logon again.  If you receive this message again, please contact Technical Support at 1-800-325-3066.";
    $site = "http://www.qwestrad.com";
}
elsif ( $main::cgi{server_name} eq 'www.qwestreferral.com' || $main::cgi{server_name} eq 'qwestreferral.com') {
	$err = "The logon you entered does not exist, please try your logon again.  If you receive this message again, please contact Technical Support at 1-888-590-3417.";
    $site = "http://www.qwestreferral.com";
}
elsif ( $main::cgi{server_name} eq 'www.refer2qwest.com' || $main::cgi{server_name} eq 'refer2qwest.com') {
	$err = "The logon you entered does not exist, please try your logon again.  If you receive this message again, please contact Technical Support at 1-888-293-6705.";
    $site = "http://www.refer2qwest.com";
}
elsif ( $main::cgi{server_name} eq 'www.qwest-affinity.com' || $main::cgi{server_name} eq 'qwest-affinity.com') {
	$err = "The logon you entered does not exist, please try your logon again.  If you receive this message again, please contact Technical Support at 1-888-293-6705.";
    $site = "http://www.qwest-affinity.com";
}
elsif ( $main::cgi{server_name} eq '216.31.243.138' || $main::cgi{server_name} eq '216.31.243.138') {#testing
	$err = "The logon you entered does not exist, please try your logon again.  If you receive this message again, please contact Technical Support at 1-888-293-6705.";
    $site = "http://www.qwestyoucan.com";
}
elsif ( $main::cgi{server_name} eq 'www.centurylinkyoucan.com' || $main::cgi{server_name} eq 'centurylinkyoucan.com') {
    $err = "Please try your logon again.  If you receive this message again, please contact Support at 1-866-8YOUCAN.";
    $site = "https://www.centurylinkyoucan.com/";
}
elsif ( $main::cgi{server_name} eq 'www.qwestreferrals.com' || $main::cgi{server_name} eq 'qwestreferrals.com') {
    $err = "Please try your logon again.  If you receive this message again, please contact Support at 1-866-YOUCAN1.";
    $site = "http://www.qwestreferrals.com";
}
elsif ( $main::cgi{server_name} eq 'www.qwestreferafriend.com' || $main::cgi{server_name} eq 'qwestreferafriend.com') {
    $err = "Please try your logon again.  If you receive this message again, please contact Support at 1-866-YOUCAN1.";
    $site = "http://www.qwestreferafriend.com";
}
elsif ( $main::cgi{server_name} eq 'qwestyoucan2.ccionline.biz' || $main::cgi{server_name} eq 'qwestyoucan2.ccionline.biz') {
    $err = "Please try your logon again.  If you receive this message again, please contact Support at 1-866-YOUCAN1.";
    $site = "http://www.qwestyoucan2.ccionline.biz";
}
elsif ( $main::cgi{server_name} eq 'www.qwestbizreferrals.com' || $main::cgi{server_name} eq 'qwestbizreferrals.com') {
    $err = "Please try your logon again.  If you receive this message again, please contact Support at 1-866-YOUCAN1.";
    $site = "http://www.qwestbizreferrals.com";
}
elsif ( $main::cgi{server_name} eq 'cta.ccionline.biz' ) {
    $err = "Please try your logon again.  If you receive this message again, please contact Support at 1-866-YOUCAN1.";
    $site = "http://cta.ccionline.biz";
}
else {
	#Default logon error message  (i.e. ccionline.biz and 209.79.159.157 fall out here)
	$site = "http://cta.ccionline.biz";
	$err = "The logon you entered does not exist, please try your logon again.  If you receive this message again, please contact your Account Supervisor or call our operator for assistance at 415-472-5100x0.";
}

print<<"EOF";
<body>
        <script language="JavaScript">
            <!--
                var msg = "$err";
                if (confirm(msg))
                   location.replace('$site');
                else
                   location.replace('$site');
            //-->
        </script>
</body>
</html>
EOF
exit 0;
}

my $sql = "select * from lkup_staff_application with (nolock), application with (nolock) where application.application_id = lkup_staff_application.application_id and staff_id = -9999";

my $sth = $db->prepare($sql);
$sth->execute();

if (my $result = $sth->fetchrow_hashref()){
    header();
    print "<h3>Error getting query results</h3>\n";
    exit;
}
$sth->finish();

print "<html>";
my $thisfile = "lp_directional.pm";
my $fund_id = $main::cgi{fund_id};
my $program_id = $main::cgi{program_id} || 0;
my ($launch_page, %lnch, $launch_page1, $launch_page2, $launch_page3);

if ( length($fund_id) == 0 ) {
    $fund_id = 0;
}
#get default program for user
if ( $main::session{source_id} == 2 ) {#this is a qwesthr user, precedence will also be 20
    $fund_id = $main::cgi{fund_id};
    $program_id = $main::cgi{program_id};
	
	my $sql = "select * from lp_config_agent with (nolock) where program_id = ? and (fund_id is null or fund_id = ?)";
	my $sth = $db->prepare($sql);
	$sth->execute($program_id, $fund_id);

	my $lnch = $sth->fetchrow_hashref;
	
	$launch_page1 =  $lnch->{culaunch_page};
	$launch_page2 =  $lnch->{cust_console};
}
else {   #admin users should be able to use any cookie-less portal.
	my $sql;
    if ($program_id > 0 ){
        if ( $main::session{precedence} > 20 ) {
              $sql = "splpGet_gtCU_progs $program_id";
        }
		else {#get the cu's landing info
              $sql = "splpGet_CU_progs $program_id, $main::session{staff_id}";
        }
    }
	else {
        $sql = "splp_GetTopProg $main::session{staff_id}";
    }
        
	my $sth = $db->prepare($sql);
	$sth->execute();
		
	my $prgcnt = $sth->fetchrow_hashref;
    $program_id = $prgcnt->{program_id};
    $fund_id = $prgcnt->{fund_id};
        
	$sth->finish();
		
	if ( $prgcnt->{cnt} == 1 ) {
        $launch_page1 =  $prgcnt->{launch_page};
        $launch_page2 =  $prgcnt->{home};
        $launch_page3 =  $prgcnt->{admin_console};
    }
	else {
        #add middle page for list of program options here that should launch
        # before any particular program if the admin user has access to
        # multiple programs.
        $launch_page1 =  $prgcnt->{launch_page};
        $launch_page2 =  $prgcnt->{home};
        $launch_page3 =  $prgcnt->{admin_console};
    }

}

############################################################################

$launch_page = $launch_page1;
if ( length($launch_page) == 0 ) {
    $launch_page = $launch_page2;
}
if ( length($launch_page) == 0 ) {
    $launch_page = $launch_page3;
}

print"<body onload='document.launch.submit();'>";
 
#############################
my $plaintext = $main::session{session_id}."-".$main::session{staff_id};

my $encoded = CCICryptography::encrypt($plaintext);

#launch page for lms is: leadpro/qwest-home.cgi
#			<input type='hidden' name='session_id' value='$main::session{session_id}'>

print<<"EOF";
        <form name='launch' method='post' action='$launch_page'>
            <input type='hidden' name='usertype' value='$UserType'>
            <input type='hidden' name='program_id' value='$program_id'>
            <input type='hidden' name='fund_id' value='$fund_id'>
            <input type='hidden' name='cci_id' value='$encoded'>
         </form>
    </body>
    </html>
EOF

}

1;
