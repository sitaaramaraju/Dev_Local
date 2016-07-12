use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||'';

my $server ="";
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
print $header;


#<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />

#<script language="JavaScript" src="qwestconnect07menus.js"></script>


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
        <td width="954" height="9" align="left" valign="top"><img src="images/topBumper.gif" width="954" height="9" /></td>
      </tr>
      <tr>
        <td background="images/background.gif"><table width="913" border="0" align="center" cellpadding="0" cellspacing="0">
          <tr>
            <td align="left" valign="top"><img src="images/Sub_titleTop.gif" width="913" height="16" /></td>
          </tr>
          <tr>
            <td background="images/Subtitle_tile.gif"><table width="900" border="0" cellspacing="1" cellpadding="1">
              <tr>
                <td width="10">&nbsp;</td>
                <td align="left" valign="top" class="BlueTitles">Frequently Asked Questions </td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td align="left" valign="top"><img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
          </tr>
          <tr>
            <td align="left" valign="middle" background="images/Sub_tile.gif"><table width="900" border="0" cellspacing="1" cellpadding="1">
              <tr>
                <td width="10" align="left" valign="top">&nbsp;</td>
                <td><table width="850" border="0" align="center" cellpadding="1" cellspacing="1">
                  <tr>
                    <td align="left" valign="top">&nbsp;</td>
                    <td align="left" valign="top">&nbsp;</td>
                    <td align="left" valign="top"><p>
                        <a href="#q1" class="FAQLink">Q: Who is eligible to participate in the CenturyLink Referral Rewards Program?</a></p>
						<p> <a href="#q2" class="FAQLink">Q: How do I enroll in the CenturyLink Referral Rewards Program?</a></p>
						<p><a href="#q3" class="FAQLink">Q: How do I make a referral through the CenturyLink Referral Rewards Program?</a></p>
						<p><a href="#q4" class="FAQLink">Q: Who am I talking to when I call to make a referral?</a></p>
						<p><a href="#q5" class="FAQLink">Q: How can I track my referrals?</a></p>
						<p><a href="#q6" class="FAQLink">Q: When will I receive the reward?</a></p>
						<p><a href="#q7" class="FAQLink">Q: Is the reward card a credit card?</a></p>
						<p><a href="#q8" class="FAQLink">Q: How do I use the reward card?</a></p>
						<p><a href="#q9" class="FAQLink">Q: How will reward card value be taxed?</a></p>
						<p><a href="#q10" class="FAQLink">Q: How can I check the reward card balance?</a></p>
						<p><a href="#q11" class="FAQLink">Q: How do I report a lost or stolen card?</a></p>
						<p><a href="#q12" class="FAQLink">Q: What do I do if there are reward dollars on my card that is about to expire?</a></p>
			
						<br><br>
						 <p></p>
                        <span class="FAQuestions"><a name="q1" id="q1"></a>Q: Who is eligible to participate in the CenturyLink Referral Rewards Program?</span><br />
                        <span class="Enrollcopy">A: Employee of a multi-dwelling unit community and management company not under marketing agreement with CenturyLink and individuals identified by Retail are eligible to participate. Current CenturyLink employees and extended family members not eligible to participate. </span></p>
                      <p><span class="FAQuestions"><a name="q2" id="q2"></a>Q: How do I enroll in the CenturyLink Referral Rewards Program?</span><br />
                        <span class="Enrollcopy">A: The simplest way to enroll is to call your local CenturyLink representative or local CenturyLink retail store. You can also enroll online at <a href="#" class="FAQLink" onclick="MM_openBrWindow('http://www.centurylinkconnect.com','','')">CenturyLinkconnect.com</a> or by calling 1-800-362-1850. You must agree to program terms and conditions to participate.

						</span></p>
                      <p><span class="FAQuestions"><a name="q3" id="q3"></a>Q: How do I make a referral through the CenturyLink Referral Rewards Program?</span><br />
                        <span class="Enrollcopy">A: Once you have enrolled, submit referrals by calling your CenturyLink representative. You can also submit referrals to your local retail store or online at <a href="#" class="FAQLink" onclick="MM_openBrWindow('http://www.centurylinkconnect.com','','')">CenturyLinkconnect.com</a> or by calling 1-800-362-1850 and speaking to a CenturyLink representative. </span></p>
                      
					  <p><span class="FAQuestions"><a name="q4" id="q4"></a>Q: Who am I talking to when I call to make a referral at 1-800-362-1850?</span><br />
                        <span class="Enrollcopy">A: Referral calls are answered by CenturyLink employees in the Referral program sales centers. </span></p>
                      
					  <p><span class="FAQuestions"><a name="q5" id="q5"></a>Q: How can I track my referrals?</span><br />
                        <span class="Enrollcopy">A: You can track your referrals at <a href="#" class="FAQLink" onclick="MM_openBrWindow('http://www.CenturyLinkconnect.com','','')">CenturyLinkconnect.com</a> or by calling program headquarters at 1-800-362-1850.
						</span></p>
                      
					  <p><span class="FAQuestions"><a name="q6" id="q6"></a>Q: When will I receive the reward?</span><br />
                        <span class="Enrollcopy">A: The reward will be sent to you once you have a qualified sold referral. You can start making referrals through this program at any time after you enroll. If enrolled as an individual you will receive the reward on a reloadable rewards card. If enrolled as a business, you will receive the reward as a check. Award is mailed to the address on file. </span></p>
						
                      <p><span class="FAQuestions"><a name="q7" id="q7"></a>Q: Is the reward card a credit card?</span><br />
                        <span class="Enrollcopy">A: The reward card is not a credit card, nor is it an extension of credit from CenturyLink. By using the card, you acknowledge that you agree to the cardholder <a href="Universal_VPC_carrier_ATM_2_17_16.pdf" target="_blank">agreement and program terms and conditions</a>.</span></p>
                      <p><span class="FAQuestions"><a name="q8" id="q8"></a>Q: How do I use the reward card?</span><br />
                        <span class="Enrollcopy">A: Value is added to the card twice a month (approximately the 1st and 15th of the month). Once this occurs, you can use the value virtually anywhere in the U.S.</span></p>

                      <p><span class="FAQuestions"><a name="q9" id="q9"></a>Q: How will the reward value be taxed?</span><br />
                        <span class="Enrollcopy">A: At the end of the year, you will be mailed a 1099-MISC form for earning amounts valued at over \$600.  </span></p>

                      <p><span class="FAQuestions"><a name="q10" id="q10"></a>Q: How can I check the reward card balance?</span><br />
                        <span class="Enrollcopy">A: Visit <a href="#" class="FAQLink" onclick="MM_openBrWindow('https://www.myprepaidcenter.com/','','')">MyPrepaidCenter.com</a> and enter the card number or call the number on the back of the card to use the automated system.</span></p>

                      <p><span class="FAQuestions"><a name="q11" id="q11"></a>Q: How do I report a lost or stolen card?</span><br />
                        <span class="Enrollcopy">A: When you receive the card, you must record the customer service number on the back of the card and the card number itself and keep them in a safe place. Should the Card become lost or stolen, you must contact Customer Service immediately. The Customer Service number is listed on the back of the Card. You will need the Card number when requesting a replacement Card.</span></p>

<p><span class="FAQuestions"><a name="q12" id="q12"></a>Q: What do I do if there are reward dollars on my card that is about to expire?</span><br />
                        <span class="Enrollcopy">A: You must spend the balance of the card prior to the expiration date.</span></p>
                      <p><br />
                          <br />
                      </p></td>
                  </tr>
                </table></td>
              </tr>
            </table></td>
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

