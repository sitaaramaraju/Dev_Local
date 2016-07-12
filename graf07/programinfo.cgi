use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use CCICryptography;
my $cgi = CGI->new();
print $cgi->header('text/html');

my  $PAGETITLE = 'CenturyLink Refer A Friend-Program Info';

my $cci_id = $cgi->param('cci_id');
my ($session_id,$staff_id);
my $PAGETITLE = 'CenturyLink Refer A Friend-Contact';

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
                                                 
                                                    CenturyLink Partner Referral Program
                                                 
                                               </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
                                </tr>
								<form name='lead_graf' action='' method='post'>
								<input type="hidden" name="cci_id"  value="$cci_id">
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
                                                            <td class="subTitles">
                                                            Now you can earn reward dollars for introducing new customers to CenturyLink&rsquo;s products and services. The more you refer, the more you can earn! It&rsquo;s our way of thanking you for being a great referral partner.															
															</td>
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
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF">&nbsp;                                                                      </td>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="subTitles">
                                                                            IT&rsquo;S EASY TO PARTICIPATE! HERE&rsquo;S HOW IT WORKS:</td>
                                                                    </tr>
                                                                    <tr>
                                                                      <td align="left" valign="top" bgcolor="#FFFFFF">&nbsp;</td>
                                                                      <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;</td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td width="33" align="left" valign="top" bgcolor="#FFFFFF">
                                                                            <img src="images/no1.gif" width="29" height="30" /></td>
                                                                        <td align="left" valign="middle" bgcolor="#FFFFFF" class="FAQuestions">
                                                                            Enroll in the Program                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;                                                                            </td>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
                                                                            You can enroll using the Partner Referral program website by selecting "Click to Enroll" on the home page, clicking <a href = "agreement.cgi" class="FAQLink">here</a> or by calling Referral Program Headquarters at 1-866-968-2261. </td>
                                                                    </tr>
                                                                    <tr><td colspan="2"></td></tr>
                                                                    <tr>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
                                                                            <img src="images/no2.gif" width="29" height="30" /></td>
                                                                        <td align="left" valign="middle" bgcolor="#FFFFFF" class="FAQuestions">
                                                                            Submit Your Referrals </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;                                                                            </td>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">Once you have your User ID, talk to potential customers about how they communicate and what they need to stay connected and how CenturyLink can meet their needs. Then explain the referral process—that with their permission, you will submit their referral information and a CenturyLink representative will contact them within 24-48 hours.<br />
                                                                        When you've received permission from someone to submit a referral, you can enter their information <a href = "../index_raf.cgi" class="FAQLink">online</a> or by calling Referral Program Headquarters at 866-968-2261. Have your User ID as the reference code. </td>
                                                                    </tr>
                                                                    <tr><td colspan="2"></td></tr>
                                                                    <tr>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
                                                                            <img src="images/no3.gif" width="29" height="30" /></td>
                                                                        <td align="left" valign="middle" bgcolor="#FFFFFF" class="FAQuestions">Receive Your Rewards </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;                                                                            </td>
                                                                      <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
                                                                          Earn rewards for qualified orders placed through the CenturyLink Partner Referral Program. Eligible referral rewards will be loaded onto the reward card twice a month.</td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
                                                                            <img src="images/no4.gif" width="29" height="30" /></td>
                                                                        <td align="left" valign="middle" bgcolor="#FFFFFF" class="FAQuestions">Check Your Account</td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">&nbsp;                                                                            </td>
                                                                        <td align="left" valign="top" bgcolor="#FFFFFF" class="FAQuestions">
                                                                            Check your account status anytime. Simply log in using your User ID and password on the home page.</td>
                                                                    </tr>
                                                                    <tr>
                                                                      <td align="center" class="subTitles" colspan="3">
                                                                            <br />
                                                                          Earn rewards for qualified orders placed through the CenturyLink Partner Referral Program. </td>
                                                                    </tr>
                                                                    <tr>
                                                                      <td align="center" class="subTitles" colspan="3">
                                                                            <br />
                                                                            <p>Help your friends stay connected and get rewarded. </p>
                                                                            <p>Start making referrals today! </p></td>
                                                                    </tr>
                                                                    
                                                                   
                                                                    <tr>
                                                                        <td colspan="2" align="center" valign="top" bgcolor="#FFFFFF">&nbsp;                                                                      </td>
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
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/Sub_bottom.gif" width="913" height="16" /></td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <img src="images/bottombuffer.gif" width="954" height="15" /></td>
                    </tr>
                    <tr>
        <td width="954" height="66" align="center" valign="middle" background="images/bottom_amex.gif"><table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
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


