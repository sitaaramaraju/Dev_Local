use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||'';
my $redir = $cgi->param('redir')||0;
my $server ="";
my $msg ="";
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnectuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
	$server = "/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnect.com'){
    $server = "D:/centurylinkyoucan";
}
else {
    $server = "D:/centurylinkyoucan";
	#$server = "/centurylinkyoucan";
}

#require "$server/cgi-bin/init.cgi";
require "$server/qwestconnect07/subs.cgi";
my $thisfile = "contact.cgi";
my $url = CCICryptography::getUrl_sites('lms');

############## validation ################
my $valid = 0;
my ($s, $e) = (0,0);
if ($cci_id ne "") {
	$valid =  CCICryptography::validate_CL_sites($cci_id,'lms');
	($s, $e) = CCICryptography::getEmpid($cci_id); 
}
else {
	$valid = 1;
}

if ($valid <= 0) {
  #my $url = "https://www.centurylinkconnect.com/";
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
#print $header;

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
		<script type="text/javascript" src="/jquery/jquery.js"></script>
		<script type="text/javascript" src="/jquery/javascript/jquery-1.4.1.min.js"></script>
		<script  type="text/javascript" src="/jquery/jquery-ui.js"></script>

		<script type="text/javascript" src="/jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="/jquery/simplemodal/simplemodal.css"/>
</head>
<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif')">

    <script language="JavaScript1.2">mmLoadMenus();</script>

    <table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
        <tr>
            <td>
];
getHeader($cci_id, $s, $e);

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
     <td width="10">&nbsp;
     </td>
     <td align="left" valign="top" class="BlueTitles">
      How to Contact Us</td>
      </tr>
       </table>
       </td>
        </tr>
    <tr>
     <td align="left" valign="top">
     <img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
       </tr>
      <tr>
     <td align="left" valign="middle" background="images/Sub_tile.gif">
       <table width="900" border="0" cellspacing="1" cellpadding="1">
        <tr>
    <td width="10" align="left" valign="top">&nbsp;
         </td>
     <td align="left" valign="top" class="subTitles">
      <br />
     <table width="700" border="0" align="center" cellpadding="0" cellspacing="0">
      <tr class="subTitles">
     <td>
      If you have reviewed the Frequently Asked Questions (FAQs) and you still have questions about the CenturyLink Referral Rewards Program, there are several ways to contact us:</td>
     </tr>

	 	<tr><td>
	 <ul>
			<li> <span class="Enrollcopy">Call your local CenturyLink representative at your local CenturyLink Retail Store</span> </li>
                          <br />
                          <li><span class="Enrollcopy">Call Program Headquarters at 1 800-362-1850</span></li>
                          <br />
                          </li>
                          <li><span class="Enrollcopy">Fill out the</span> <a href="#" onclick="openModalLarge('quickform.cgi');return false;">Quick Contact Form</a> </li>

                        </ul>

						</td></tr>
		</tr>
				<td align="center">&nbsp;
										</td>
                      </tr>



     </table>
       <br />
      <br />

                                                </td>
                                            </tr>

                                        </table>
                                    </td>
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
];
