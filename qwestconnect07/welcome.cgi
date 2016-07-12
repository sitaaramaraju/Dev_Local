use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||'';

my $server;
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnectuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
	#$server = "/centurylinkyoucan/";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnect.com'){
    $server = "D:/centurylinkyoucan";
}
else {
    $server = "D:/centurylinkyoucan";
	#$server = "/centurylinkyoucan";
}

require "$server/cgi-bin/init.cgi";
require "$server/qwestconnect07/subs.cgi";
#my $url = "centurylinkyoucandev.com/index_lmsii07.cgi";
my $url = CCICryptography::getUrl_sites('lms');

############## validation ################
my $valid = 0;
if ($cci_id ne "") {
	$valid = CCICryptography::validate_CL_sites($cci_id,'lms');
}
else {
	$valid = 1;
}

my $enrollType = $cgi->param('enrollType')||'';
my ($logon, $pwd, $name, $msg)=('','','','');
if ($enrollType eq 'bau') {
	($logon, $pwd, $name, $msg) = enrollBAU();
}
elsif ($enrollType eq 'b2c') {
	($logon, $pwd, $name, $msg) = enrollB2C();
}

if ($valid <= 0) {
  headernocss();
  print qq[
  <form name="lead" action="" method="post">
  <input type="hidden" name="session_id" value="0">
    <script language='javascript'>
      alert("There was an error loading the page.  Please log in and try again.");
      document.lead.action='$url';
      document.lead.submit();
    </script>
  </form>
 </body>
</html>];
exit();

}


my  $PAGETITLE = 'CenturyLink Connect';
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;


#<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />


print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>$PAGETITLE</title>
<script language="JavaScript" src="qwestconnect07menus.js"></script>
<script language="JavaScript" src="validate.js"></script>
<link href="Style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="mm_menu.js"></script>
</head>

<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif')">
<script language="JavaScript1.2">mmLoadMenus();</script>
<table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td>
];
getHeader($cci_id,0,0);

print qq[	
	</td>
      </tr>
                    <tr>
                        <td width="954" height="9" align="left" valign="top">
                            <img src="images/topBumper.gif" width="954" height="9" /></td>
                    </tr>
                    <tr>
                        <td background="images/background.gif">
                            <table width="913" border="0" align="center" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/Sub_titleTop.gif" width="913" height="16" /></td>
                                </tr>
                                <tr>
                                    <td background="images/Subtitle_tile.gif">
                                        <table width="900" border="0" cellspacing="1" cellpadding="1">
                                            <tr>
                                                <td width="10">&nbsp;                                                    </td>
                                                <td align="left" valign="top" class="BlueTitles">
                                                    WELCOME $name <!--	$logon, $pwd	-->                                               </td>
                                            </tr>
                                        </table>                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
                                </tr>
                                <tr>
                                    <td align="left" valign="middle" background="images/Sub_tile.gif">
                                        <table width="900" border="0" cellspacing="1" cellpadding="1">
                                            <tr>
                                                <td width="10" align="left" valign="top">&nbsp;                                                    </td>
                                                <td align="left" valign="top">
                                                    <table width="700" border="0" align="center" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td>
                                                                &nbsp;<table align="center" border="0" cellpadding="1" cellspacing="1" width="650">
                                                                    <tr>
                                                                        <td align="left" valign="top">
                                                                            <table border="0" cellpadding="1" cellspacing="1" class="Enrollcopy" width="650">
                                                                                <tr>
                                                                                    <td align="left" valign="top">&nbsp;</td>
                                                                                </tr>
										$msg                                                                                <tr>
                                                                                  <td align="center">&nbsp;</td>
                                                                                </tr>
                                                                            </table>
                                                                    </tr>
                                                                </table>                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td colspan="2" align="center">                                                            </td>
                                                        </tr>
                                                    </table>                                                </td>
                                            </tr>
                                        </table>                                    </td>
                                </tr>
         ];
getFooter($cci_id);
print qq[
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>
]

#--------------------------------------------------------------------
