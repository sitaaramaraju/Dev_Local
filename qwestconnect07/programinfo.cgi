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
	$server = "/centurylinkyoucan/";
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
      GET REWARDED IN THE CenturyLink<sup>&reg;</sup> REFERRAL REWARDS PROGRAM</td>
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
      <tr>
     <td>
      Now you can earn rewards for introducing your new movers, and residents to CenturyLink&rsquo;s products and services. </td>
     </tr>
     </table>
       <br />
      <br />
   <table width="423" border="1" align="center" cellpadding="0" cellspacing="0" bordercolor="#000099" bgcolor="#FFFFFF">
     <tr>
       <td>
     <table width="700" border="0" align="center" cellpadding="2" cellspacing="2" bordercolor="#FFFFFF" bgcolor="#FFFFFF">
        <tr>
       <td align="left" valign="top" bgcolor="#FFFFFF">&nbsp;</td>
        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;</td>
         </tr>
        <tr>
       <td align="left" valign="top" bgcolor="#FFFFFF">&nbsp;</td>
     <td align="left" valign="top" bgcolor="#FFFFFF" class="subTitles">
      IT&rsquo;S EASY TO PARTICIPATE </td>
   </tr>
   <tr>
  <td align="left" valign="top" bgcolor="#FFFFFF">&nbsp;</td>
  <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;</td>
   </tr>
   <tr>
  <td width="33" align="left" valign="top" bgcolor="#FFFFFF">
  <img src="images/no1.gif" width="29" height="30" /></td>
  <td align="left" valign="middle" bgcolor="#FFFFFF" class="FAQuestions">
  Enroll in the Program   </td>
   </tr>
   <tr>
  <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;</td>
    <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
   The easiest way to enroll is to call your local CenturyLink Retail Store. You can also enroll at the program Web site at <a href="https://www.centurylinkconnect.com/" class="FAQLink">centurylinkconnect.com</a> just select "Enroll here" on your first visit. Or, enroll by calling the Refer a Friend program headquarters at 1-800-362-1850. </td>
       </tr>
  <tr><td colspan="2"></td></tr>
      <tr>
    <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
  <img src="images/no2.gif" width="29" height="30" /></td>
    <td align="left" valign="middle" bgcolor="#FFFFFF" class="FAQuestions">
   Determine the Referral Opportunity</td>
     </tr>
     <tr>
  <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp; </td>
  <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
Talk to your new movers and residents about how they communicate and what they need to stay connected. Tell them about the products and services CenturyLink offers. Then explain the referral process that with their permission, you will submit their referral information and a CenturyLink representative will contact them within 24-48 hours. </td>
</tr>
<tr><td colspan="2"></td></tr>
<tr>
<td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
  <img src="images/no3.gif" width="29" height="30" /></td>
 <td align="left" valign="middle" bgcolor="#FFFFFF" class="FAQuestions">Submit Your Referrals </td>
</tr>
 <tr>
 <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;  </td>
 <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
When you&rsquo;ve received permission to submit someone as a referral, call your CenturyLink representative or submit a referral online at <a href="https://www.centurylinkconnect.com/" class="FAQLink">centurylinkconnect.com</a>. In addition to providing your name and contact information, you will need the following information about the potential customer to complete a referral:
 <br />
 <ul>
  <li>Customer name</li>
  <li>Complete address</li>
  <li>Home phone number</li>
  <li>Work phone number</li>
  <li>Mobile phone number</li>
  <li>E-mail address</li>
  <li>Products and services of interest<br />
  </li> 
 </ul>
You can track your referral status at <a href="https://www.centurylinkconnect.com/" class="FAQLink">centurylinkconnect.com</a>, by calling your local retail store or program headquarters at 1-800-362-1850. </td>
 </tr>
 <tr>
 <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
 <img src="images/no4.gif" width="29" height="30" /></td>
 <td align="left" valign="middle" bgcolor="#FFFFFF" class="FAQuestions">Receive Your Rewards   </td>
  </tr>
 <tr>
 <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;  </td>
<td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
Each time you make a referral that results in a net increase in sales revenue consistent with the Referral program rules, you&rsquo;ll earn credit toward your reloadable rewards card. Rewards will be added to your card through twice monthly deposits (approximately the 1st and 15th of the month).</td>
 </tr>
 <tr>
 <td align="center" class="subTitles" colspan="3">
   <br /></td>
 </tr>
 <tr>
 <td align="center" class="subTitles" colspan="3">Start making referrals today!    </td>
  </tr>

                                                                    
 <tr>
 <td colspan="2" align="center" valign="top" bgcolor="#FFFFFF">&nbsp;   </td>
 </tr>
                                                              </table>
                                                            </td>
                                                        </tr>
                                                    </table>
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


