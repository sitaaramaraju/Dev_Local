use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');

my $cci_id = $main::session{cci_id}||$cgi->param('cci_id') ||""; 
my  $PAGETITLE = 'CenturyLink Connect';

my $server;

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


#and when it goes like it'll be centurylinkconnect.com


#else{
#    $server = "d:/xroot";
#}

#require "$server/cgi-bin/init.cgi";
#require "$server/qwestconnect07/subs.cgi";
#<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />


print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>$PAGETITLE</title>
<script language="JavaScript" src="/qwestconnect07/validate.js"></script>

<script type="text/javascript" src="/jquery/jquery.js"></script>
		<script type="text/javascript" src="/jquery/javascript/jquery-1.4.1.min.js"></script>
		<script  type="text/javascript" src="/jquery/jquery-ui.js"></script>

		<script type="text/javascript" src="/jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="/jquery/simplemodal/simplemodal.css"/>

<script language="JavaScript">function mmLoadMenus() {
  if (window.mm_menu_0221111945_0) return;
        window.mm_menu_0221111945_0 = new Menu("root",200,17,"Arial, Helvetica, sans-serif",11,"#003366","#003366","#FFFFFF","#C1D72E","left","middle",3,0,1000,-5,7,true,true,true,1,true,true);
  mm_menu_0221111945_0.addMenuItem("Program Infomation","location='/qwestconnect07/programinfo.cgi'");
  mm_menu_0221111945_0.addMenuItem("Terms & Conditions","location='/qwestconnect07/terms.cgi'");
  
  
   mm_menu_0221111945_0.fontWeight="bold";
   mm_menu_0221111945_0.hideOnMouseOut=true;
   mm_menu_0221111945_0.bgColor='#555555';
   mm_menu_0221111945_0.menuBorder=1;
   mm_menu_0221111945_0.menuLiteBgColor='#FFFFFF';
   mm_menu_0221111945_0.menuBorderBgColor='#003366';

mm_menu_0221111945_0.writeMenus();
} // mmLoadMenus()</script>
<link href="/qwestconnect07/Style.css" rel="stylesheet" type="text/css" />

<script language="JavaScript" src="/qwestconnect07/mm_menu.js"></script>
</head>

<body onload="MM_preloadImages('/qwestconnect07/images/Sub_nav_home_on.gif','/qwestconnect07/images/Sub_nav_about_on.gif','/qwestconnect07/images/Sub_nav_faq_on.gif','/qwestconnect07/images/Sub_nav_contact_on.gif','/qwestconnect07/images/Sub_nav_Products_on.gif')">
<script language="JavaScript1.2">mmLoadMenus();</script>
    <table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
        <tr>
            <td>
                <table width="954" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                        <td align="center" valign="top">
                            <img src="/qwestconnect07/images/ctl_con_logo4.png" width="954" height="324" /></td>
                    </tr>
                    <tr>
                        <td><table width="954" border="0" cellspacing="0" cellpadding="0">
                          <tr>
                            <td width="45" align="left" valign="top"><img src="/qwestconnect07/images/nav_blank.gif" width="45" height="31" /></td>
                            <td width="179" align="left" valign="top"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image28','','/qwestconnect07/images/Sub_nav_home_on.gif',1)"><img src="/qwestconnect07/images/Sub_nav_home_off.gif" name="Image28" width="179" height="31" border="0" id="Image28" /></a></td>
                            <td width="309" align="left" valign="top"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','/qwestconnect07/images/Sub_nav_about_on.gif',1)"><img src="/qwestconnect07/images/Sub_nav_about_off.gif" name="Image29" width="309" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>
                            <td width="177" align="left" valign="top"><a href="/qwestconnect07/faqs.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','/qwestconnect07/images/Sub_nav_faq_on.gif',1)"><img src="/qwestconnect07/images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a></td>
                            <td width="244" align="left" valign="top"><a href="/qwestconnect07/contact.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','/qwestconnect07/images/Sub_nav_contact_on.gif',1)"><img src="/qwestconnect07/images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a></td>
                            
                          </tr>
                        </table></td>
                    </tr>
                    <tr>
                        <td width="954" height="9" align="left" valign="top">
                            <img src="/qwestconnect07/images/topBumper.gif" width="954" height="9" /></td>
                    </tr>
                    <tr>
                        <td background="/qwestconnect07/images/background.gif">
                            <table width="924" border="0" align="center" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td width="204" height="13" align="left" valign="top">
                                        <table width="204" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td align="left" valign="top">
                                                    <img src="/qwestconnect07/images/Landing_L_top.gif" width="204" height="20" /></td>
                                            </tr>
                                            <tr>
                                                <td align="left" valign="top" background="/qwestconnect07/images/Landing_L_tile.gif">
                                                    <table width="190" border="0" align="center" cellpadding="1" cellspacing="1">
                                                        <tr>
                                                            <td class="BIGBoxTitles">
                                                                Interested in earning rewards for your referrals?
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table width="204" border="0" cellspacing="0" cellpadding="0">
                                                        <tr>
                                                            <td align="left" valign="top"><table width="97" border="0" cellspacing="1" cellpadding="1">
                                                              <tr>
                                                                <td width="5" align="left" valign="top">&nbsp;</td>
                                                                <td><a href="/qwestconnect07/b2c_bau.cgi" class="BIG">Enroll Here </a> </td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td height="20" align="left" valign="top" class="Enrollcopy">&nbsp;</td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td height="20" align="left" valign="top" class="Enrollcopy"> Already Enrolled? </td>
                                                              </tr>
<form name="logon" action="/cgi-bin/lp-validate.cgi" method="post">
<input type="hidden" name="program_id" value="269">
<input type="hidden" name="fund_id" value="1036">
<input type="hidden" name="source_id" value="1"><!-- force staff not qwesthr login messed up-->
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td class="LoginCopy">User ID: </td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td class="LoginCopy"><input name="userid" type="text" id="username" size="10" /></td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td class="LoginCopy">Password:</td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td class="LoginCopy"><input name="password" type="password" id="password" size="10" /></td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td class="LoginCopy"><input name="Submit" type="submit" value="Log In" /></td>
                                                              </tr>
                                                            </table>
                                                             
                                                          </td>
                                                            
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                
                                            </tr>
                                        </table>
                                        <img src="/qwestconnect07/images/spacer.gif" width="1" height="11" /><br />
                                        <table width="204" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td>
                                                    <img src="/qwestconnect07/images/Landing_L_top.gif" width="204" height="20" /></td>
                                            </tr>
                                            <tr>
                                                <td width="204" align="left" valign="top" background="/qwestconnect07/images/Landing_L_tile.gif">
                                                    <table width="195" border="0" align="center" cellpadding="1" cellspacing="1">
                                                        <tr>
                                                          <td height="132" align="center" valign="middle">
                                                              <span class="BlueTitles">Trouble logging in?</span> <span class="Enrollcopy">Questions about the program?</span><br />
                                                            <span class="Earncopy">Give us a call!</span><br />
                                                                <span class="Questionscopy">Refer a Friend Customer Service</span>
                                                                <br />
                                                                <span class="Earncopy">Call 1 800-362-1850 </span><span class="Questionscopy">
                                                                    <br />
                                                                </span><span class="Questionscopy">Monday-Friday
                                                                    <br />
    7:30 a.m. - 6:30 p.m. MT </span>
                                                                <br />
                                                                <span class="FAQuestions">Or fill out the</span><span class="bodycopy">                                                                <br />
                                                                <a href="#" onclick="openModalLarge('qwestconnect07/quickform.cgi');return false;">Quick Contact Form</a></span> </td>
                                                        </tr>
                                                        <tr>
                                                            <td>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <img src="/qwestconnect07/images/Landing_L_bot.gif" width="204" height="19" /></td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td width="510" align="left" valign="top">
                                        <table width="510" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td align="left" valign="top">
                                                    <img src="/qwestconnect07/images/Landing_Mtitle_top.gif" width="510" height="13" /></td>
                                            </tr>
                                            <tr>
                                                <td width="510" align="left" valign="top" background="/qwestconnect07/images/Landing_Mtitle_tile.gif">
                                                    <table width="500" border="0" cellspacing="0" cellpadding="0">
                                                        <tr>
                                                            <td width="10" align="left" valign="top">&nbsp;
                                                          </td>
                                                            <td class="BlueTitles"><img src="/qwestconnect07/images/HEADER_TITLE.gif" width="367" height="26" /></td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left" valign="top">
                                                    <img src="/qwestconnect07/images/Landing_Mtitle_bot.gif" width="510" height="8" /></td>
                                            </tr>
                                            <tr>
                                                <td width="510" align="left" valign="top" background="/qwestconnect07/images/Landing_M_tile.gif" style="height: 488px">
                                                    <table width="500" height="460" border="0" cellspacing="0" cellpadding="0">
                                                        <tr>
                                                            <td width="10" align="left" valign="top">&nbsp;                                                          </td>
                                                            <td height="103" align="left" valign="top" class="subTitles">
                                                                <br />
                                                                <table>
                                                                    <tr>
                                                                        <td width="352" align="left" valign="top">With the CenturyLink Referral Rewards Program, you can earn rewards for introducing movers and residents to CenturyLink’s products and services. </td>
           <td width="126" align="left" valign="top"><img src="/qwestconnect07/images/Land_CashLogo_amex.gif" width="123" height="73" /></td>
                                                                    </tr>
                                                                </table>                                                            </td>
                                                        </tr>
                                                        <tr>
                                                          <td align="left" valign="top">&nbsp;</td>
                                                          <td align="left" valign="top" class="subTitles">&nbsp;</td>
                                                        </tr>
                                                        <tr>
                                                            <td align="left" valign="top">&nbsp;                                                          </td>
                                                            <td align="left" valign="top" class="subTitles"><div align="center"><img src="/qwestconnect07/images/Landing_copy.gif" width="400" height="25" /> </div></td>
                                                        </tr>
<tr><td>&nbsp</td> <td class="BIGBoxTitles" align="centre">
	&nbsp;</br>
</td></tr>
                  <tr>
    <td align="left" valign="top">&nbsp;                                                          </td>
          <td height="240" align="left" valign="middle" class="subTitles"><table width="457" border="0" align="center" cellpadding="0" cellspacing="0">
 <tr>
 <td width="457" height="233" align="left" valign="top" background="/qwestconnect07/images/EarnBox.gif"><br />
        <br />
      <table width="440" border="1" align="center" cellpadding="1" cellspacing="0" bordercolor="#005DAB">
<!------------	--> 
<tr bgcolor="#FFFFFF"><td colspan="2"><div align="center"><img src="/qwestconnect07/images/CashAwardHeader.gif" width="196" height="25" /></div></td></tr>
 <tr class="BIGBoxTitles">
 <td colspan="2" align="left" valign="top" bgcolor="#FFFFFF" class="BIGBoxTitles"><div align="center" class="BIGBoxTitles">
 <div align="center">YOU can earn awards for your sold referrals!</div>
  </div></td>
 </tr>
<!------------	-->
                                                                <tr class="Enrollcopy">
                                                            <td  align="center" valign="center" bgcolor="#FFFFFF" class="BlueTitles"></br>
                                   <span class="BIGBoxTitles">YOU</span> can earn a <br /><!--	283	yup	-->
                                   <span class="BIGBoxTitles">\$25 Value Reward Card</span> <br />
                                    for your closed referral. <p />
                                   </td>
                                                                  </tr>
                                                              </table></td>
                                                            </tr><tr><td>&nbsp;</td></tr><tr><td class="LoginCopy" align="center">Multi-dwelling unit property (MDU) must not be an existing participant in marketing or promotional agreements with CenturyLink.</td></tr>
                                                          </table></td>
                                                        </tr>
                                                        <tr>
                                                            <td align="left" valign="top">&nbsp;                                                          </td>
                                                            <td align="left" valign="top" class="subTitles">&nbsp;                                                          </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left" valign="top">
                                                    <img src="/qwestconnect07/images/Landing_M_bot.gif" width="510" height="14" /></td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td width="205" align="left" valign="top">
                                        <table width="205" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td width="205" align="left" valign="top">
                                                    <img src="/qwestconnect07/images/Land_rbox_top.gif" width="205" height="15" /></td>
                                            </tr>
                                            <tr>
                                                <td width="205" align="left" valign="top" background="/qwestconnect07/images/Land_rbox_tile.gif" style="height: 520px">
                                                    <table width="195" border="0" align="center" cellpadding="1" cellspacing="1">
                                                        <tr>
                                                            <td colspan="2" class="BlueTitles">
                                                                Here's How It Works:
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td width="26" align="left" valign="top">
                                                                <img src="/qwestconnect07/images/smno1.gif" width="26" height="26" /></td>
                                                            <td width="154" align="left" valign="top" class="LoginCopy">
                                                                <a href="/qwestconnect07/b2c_bau.cgi">Enroll</a> in CenturyLink&rsquo;s Referral Rewards Program and obtain your User ID.</td>
                                                        </tr>
                                                        <tr>
                                                            <td height="4" colspan="2" align="left" valign="top">
                                                                <img src="//qwestconnect07/images/spacer.gif" width="1" height="1" /></td>
                                                        </tr>
                                                        <tr>
                                                            <td align="left" valign="top">
                                                                <img src="/qwestconnect07/images/smno2.gif" width="26" height="26" /></td>
                                                            <td align="left" valign="top" class="LoginCopy">
                                                                Once you have your User ID, Login from this page to enter a Referral or contact your local retail store.</td>
                                                        </tr>
                                                        <tr>
                                                            <td height="4" colspan="2" align="left" valign="top">
                                                                <img src="/qwestconnect07/images/spacer.gif" width="1" height="1" /></td>
                                                        </tr>
                                                        <tr>
                                                            <td align="left" valign="top">
                                                                <img src="/qwestconnect07/images/smno3.gif" width="26" height="26" /></td>
                                                            <td align="left" valign="top" class="LoginCopy">
                                                               Earn an award per residential referral for orders placed through the CenturyLink Referral Rewards Program.</td>
                                                        </tr>
                                                        <tr>
                                                            <td height="4" colspan="2" align="left" valign="top">
                                                                <img src="/qwestconnect07/images/spacer.gif" width="1" height="1" /></td>
                                                        </tr>
                                                        

                                                    </table>
                                                    <img src="/qwestconnect07/images/spacer.gif" width="1" height="1" /></td>
                                            </tr>
                                            <tr>
                                                <td width="205" align="left" valign="top">
                                                    <img src="/qwestconnect07/images/Land_rbox_bot.gif" width="205" height="13" /></td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <img src="/qwestconnect07/images/bottombuffer.gif" width="954" height="15" /></td>
                    </tr>
                    <tr>
					        <td width="954" height="75" align="center" valign="middle" background="/graf07/images/bottom_amex.gif"><table width="954" border="0" align="center" cellpadding="0" cellspacing="0">

<tr>
<td align="center" valign="top" class="Legalcopy" nowrap>&copy;<script type="text/javascript">
    var dteNow = new Date();
    var intYear = dteNow.getFullYear();
    document.write(intYear);
</script> CenturyLink, Inc. All Rights Reserved. The CenturyLink mark, pathways logo, CenturyLink mark,
               Q lightpath logo and certain CenturyLink product names are the property of CenturyLink, Inc.</td>
</tr>
<tr>
<td align="center" valign="top" class="Legalcopy">
<a href="#" class="revLink" onclick="MM_openBrWindow('http://www.qwest.com/legal/','','')">Legal Notices</a>
| <a href="#" class="revLink" onclick="MM_openBrWindow('http://www.qwest.com/privacy/','','')">Privacy Policy</a>
| <a href="SiteMap.cgi" class="revLink">Site Map </a></td>
</tr>
</table>
</td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>

];
