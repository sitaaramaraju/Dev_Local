use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use CCICryptography;
my $cgi = CGI->new();
print $cgi->header('text/html');


my $cci_id = $cgi->param('cci_id');
my ($session_id,$staff_id);
my $PAGETITLE = 'CenturyLink Refer A Friend-Faqs';

if (length($cci_id) == 0) {
	require "graf07/header.cgi";
}
else {
	($session_id,$staff_id) = CCICryptography::getEmpid($cci_id);	
	 
	
	print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>$PAGETITLE</title>
<script language="JavaScript">
function mmLoadMenus() {
  if (window.mm_menu_0221111945_0) return;
            window.mm_menu_0221111945_0 = new Menu("root",250,17,"Arial, Helvetica, sans-serif",11,"#003366","#003366","#FFFFFF","#C1D72E","left","middle",3,0,1000,-5,7,true,true,true,1,true,true);
  mm_menu_0221111945_0.addMenuItem("Program&nbsp;Infomation","location='programinfo.cgi?cci_id=$cci_id'");
  mm_menu_0221111945_0.addMenuItem("PROGRAM TERMS AND CONDITIONS","location='terms.cgi?cci_id=$cci_id'");
  mm_menu_0221111945_0.addMenuItem("VISA&nbsp;Cardholder&nbsp;Agreement", "window.open('images/Universal_VPC_carrier_ATM_2.17.16.pdf', '_blank');");
 // mm_menu_0221111945_0.addMenuItem("Reward&nbsp;Dollar&nbsp;Values","location='awardvalues.cgi'");
   mm_menu_0221111945_0.fontWeight="bold";
   mm_menu_0221111945_0.hideOnMouseOut=true;
   mm_menu_0221111945_0.bgColor='#555555';
   mm_menu_0221111945_0.menuBorder=1;
   mm_menu_0221111945_0.menuLiteBgColor='#FFFFFF';
   mm_menu_0221111945_0.menuBorderBgColor='#003366';

mm_menu_0221111945_0.writeMenus();
} // mmLoadMenus()</script>

<script language="JavaScript" src="mm_menu.js"></script>
<script language="JavaScript" src="validate.js"></script>
<script type="text/javascript" src="/jquery/jquery.js"></script>
<script type="text/javascript" src="../../javascript/jquery-1.4.1.min.js"></script>		
<script  type="text/javascript" src="../../jquery/jquery.js"></script>

<script  type="text/javascript" src="../../jquery/simplemodal/simplemodal.js"></script>
<link rel="stylesheet" type="text/css" href="../../jquery/simplemodal/simplemodal.css"/>


<script language="JavaScript" src="graf07menus.js"></script>

<link href="Style.css" rel="stylesheet" type="text/css" />
<script type="text/JavaScript">
<!--
function MM_openBrWindow(theURL,winName,features) { //v2.0
  window.open(theURL,winName,features);
}

function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}

function MM_goToURL() { //v3.0
  var i, args=MM_goToURL.arguments; document.MM_returnValue = false;
  for (i=0; i<(args.length-1); i+=2) eval(args[i]+".location='"+args[i+1]+"'");
}
//-->
</script>
<script language="JavaScript" src="mm_menu.js"></script>
</head>
<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif')">

    <script language="JavaScript1.2">mmLoadMenus();</script>

    <table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
        <tr>
            <td>
                <table width="954" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                        <td align="center" valign="top">
                            <img src="images/ctl_con_logo4.png" width="954" height="324" /></td>
                    </tr>
                    <tr>
                      <td height="9" align="left" valign="top">
					  <table width="954" border="0" cellspacing="0" cellpadding="0">
                       <tr >
                                   <td width="35" align="left" valign="top"  background="images/nav_blank.gif"><img src="images/nav_blank.gif" width="35" height="31" /></td>
                          <td width="187" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onclick="logoutUser($session_id,$staff_id);" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image58','','images/Logout_white.jpg',1)"><img src="images/Logout_blue.jpg" name="Image58" width="113" height="29" border="0" id="Image58" /></a></td>
                          <td width="311" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','images/Sub_nav_about_on.gif',1)"> <img src="images/Sub_nav_about_off.gif" name="Image29" width="311" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>
						 <td width="177" align="left" valign="top" background="images/nav_blank.gif">
                                        <a href="#" onClick="document.lead_graf.action='faqs.cgi';document.lead_graf.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','images/Sub_nav_faq_on.gif',1)">
                                            <img src="images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a></td>
											
                                   <td width="244" align="left" valign="top" background="images/nav_blank.gif" colspan=2><a href="#" onClick="document.lead_graf.action='contact.cgi';document.lead_graf.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','images/Sub_nav_contact_on.gif',1)"> <img src="images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a></td>
                              </tr>
                            </table>
EOF
	
}

print<<"EOF";
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
		  <form name='lead_graf' action='' method='post'>
		  <input type="hidden" name="cci_id"  value="$cci_id">
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
                    <td align="left" valign="top"><p><a href="#q1" class="FAQLink">Q: Who is eligible to participate in the CenturyLink Partner Referral Program?</a><br />
                        <a href="#q2" class="FAQLink">Q: How do I enroll in the CenturyLink Partner Referral Program?</a><br />
                        <a href="#q3" class="FAQLink">Q: How do I make a referral through the CenturyLink Partner Referral Program?</a><br />
                        <a href="#q4" class="FAQLink">Q: Who am I talking to when I call to make a referral?</a><br />
                        <a href="#q5" class="FAQLink">Q: How long are my referrals valid?</a><br />
                        <a href="#q6" class="FAQLink">Q: How can I track my referrals?</a><br />
                        <a href="#q7" class="FAQLink">Q: When will I receive the VISA&reg; rewards card?</a><br />
                        <a href="#q8" class="FAQLink">Q: Is the VISA&reg;-branded reward card a charge card?</a><br />
                        <a href="#q9" class="FAQLink">Q: How do I use the VISA&reg; reward card?</a><br />
                        <a href="#q10" class="FAQLink">Q: How will VISA&reg; reward card value be taxed?</a><br />
                        <a href="#q11" class="FAQLink">Q: How can I check the VISA&reg; reward card balance?</a><br />
                        <a href="#q12" class="FAQLink">Q: How do I report a lost or stolen card?</a></br>
			<a href="#q13" class="FAQLink">Q: What do I do if there are reward dollars on my VISA&reg; rewards card?</a></br >
			<a href="#q13" class="FAQLink">Q: What if I have additional questions about my VISA&reg; rewards card?</a></ br>
</p>
                      <p></p>
                      <p><br />  
                        <span class="FAQuestions"><a name="q1" id="q1"></a>Q: Who is eligible to participate in the CenturyLink Partner Referral Program?</span><br />
                        <span class="Enrollcopy">A: CenturyLink vendor partners are eligible to participate in this program. Current CenturyLink employees and extended family of Referral Program Headquarters or provisioning centers are not eligible to participate.</span></p>
						
                      <p><span class="FAQuestions"><a name="q2" id="q2"></a>Q:  How do I enroll in the CenturyLink Partner Referral Program?</span><br />
                        <span class="Enrollcopy">A: You can enroll online at</span><span class="FAQLink"><a href="agreement.cgi" class="FAQLink">&nbsp;Enroll</a></span><span class="Enrollcopy"> or by calling 1 866-968-2261. You must agree to program terms and conditions to participate.<br />
                        </span></p>
                      <p><span class="FAQuestions"><a name="q3" id="q3"></a>Q: How do I make a referral through the CenturyLink Partner Referral Program?</span><br />
                        <span class="Enrollcopy">A: Once you have enrolled, submit referrals through the Partner Referral Program website or 1 866-968-2261 and speak to a CenturyLink representative. If you have the party you are referring with you, you can submit their information and have the CenturyLink representative talk to the potential customer right away. Be sure to provide your User ID as the reference code.</span></p>
						
                      <p><span class="FAQuestions"><a name="q4" id="q4"></a>Q: Who am I talking to when I call to make a referral?</span><br />
                        <span class="Enrollcopy">A: Referral calls are answered by CenturyLink employees in the Referral Program sales centers.</span></p>
						
                      <p><span class="FAQuestions"><a name="q5" id="q5"></a>Q: How long are my referrals valid?</span><br />
                        <span class="Enrollcopy">A: Referrals are valid for 30 days. If the customer purchases CenturyLink products or services within 30 days through the Referral Program provisioning center, the program participant who made the referral will receive reward value on a reloadable VISA&reg; reward card.</span></p>
			
                      <p><span class="FAQuestions"><a name="q6" id="q6"></a>Q: How can I track my referrals?</span><br />
                        <span class="Enrollcopy">A: You can track your referrals by login at <a href="../index_raf.cgi" class="FAQLink">Home Page</a> or by calling Program Headquarters at 1 866-968-2261 <br /></span></p>						
                      <p><span class="FAQuestions"><a name="q7" id="q7"></a>Q: When will I receive the reloadable VISA&reg; reward card?</span><br />
					  
	<span class="Enrollcopy">A: The reloadable VISA&reg; reward card will be sent to you approximately four (4) weeks after your first qualified sold referral. You can start making referrals through this program at any time after you enroll.</span></p>
	
                      <p><span class="FAQuestions"><a name="q8" id="q8"></a>Q: Is the VISA&reg; rewards card a credit card?</span><br />
                        <span class="Enrollcopy">A: The VISA&reg; reward card is not a credit card, nor is it an extension of credit from CenturyLink. By using the card, you acknowledge that you agree to the cardholder agreement and program terms and conditions.</span></p>
						
                      <p><span class="FAQuestions"><a name="q9" id="q9"></a>Q: How do I use the VISA&reg; rewards card?</span><br />
                        <span class="Enrollcopy">A: Value is added to the card monthly (approximately the 1st and 15th of every month). Once this occurs, you can use the value virtually anywhere VISA&reg; Cards are welcome in the U.S.</span></p>
						
                      <p><span class="FAQuestions"><a name="q10" id="q10"></a>Q: How will VISA&reg; rewards card value be taxed?</span><br />
                        <span class="Enrollcopy">A: At the end of the year, you will be mailed a 1099-MISC form for earning amounts valued at over \$600.</span></p>
						
                      <p><span class="FAQuestions"><a name="q11" id="q11"></a>Q: How can I check the VISA&reg; rewards card balance?</span><br />
					  
                        <span class="Enrollcopy">A: Visit <a href="https://www.myprepaidcenter.com" class="FAQLink" target="_blank">MyPrepaidCenter.com</a> and enter the card number or call 877-227-0956 to use the automated system.</span></p>
						
                      <p><span class="FAQuestions"><a name="q12" id="q12"></a>Q: How do I report a lost or stolen card?</span><br />
                        <span class="Enrollcopy">A: When you receive the card, you must record the customer service number on the back of the card and the card number itself and keep them in a safe place. Should the Card become lost or stolen, you must contact Customer Service immediately. The Customer Service number is listed on the back of the Card. You will need the Card number when requesting a replacement Card.</span></p>
						
<p><span class="FAQuestions"><a name="q13" id="q13"></a>Q: What do I do if there are reward dollars on my VISA&reg; rewards card?</span><br />
                        <span class="Enrollcopy">A: You must spend the balance of the card prior to the expiration date.</span></p>
<p><span class="FAQuestions"><a name="q14" id="q14"></a>Q: What if I have questions about my CenturyLink REWARDS Visa&reg; debit card?</span><br />
                        <span class="Enrollcopy">A: Please visit <a href="https://www.myprepaidcenter.com" class="FAQLink" target="_blank">MyPrepaidCenter.com</a> or call 877-227-0956 to use the automated system.</span></p>

                      <p><br />
                          <br />
                      </p></td>
                  </tr>
                </table></td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td align="left" valign="top"><img src="images/Sub_bottom.gif" width="913" height="16" /></td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td><img src="images/bottombuffer.gif" width="954" height="15" /></td>
      </tr>
      <tr>
        <td width="954" height="66" align="center" valign="middle" background="images/bottom_amex.gif"><table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
EOF
require "graf07/footer.cgi";
print<<"EOF";
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>


EOF


