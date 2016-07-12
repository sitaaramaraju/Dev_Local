use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

print $cgi->header('text/html');

my $PAGETITLE = 'CenturyLink-Refer A Friend';
my $server;

if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'clpassitonrewardsuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkpassitonrewards.com'){
    $server = "D:/centurylinkyoucan";
}
else {
	$server = "D:/centurylinkyoucan";
}

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
  mm_menu_0221111945_0.addMenuItem("Program&nbsp;Infomation","location='graf07/programinfo.cgi'");
  mm_menu_0221111945_0.addMenuItem("PROGRAM TERMS AND CONDITIONS","location='graf07/terms.cgi'");
  mm_menu_0221111945_0.addMenuItem("VISA&nbsp;Cardholder&nbsp;Agreement","window.open('graf07/images/Universal_VPC_carrier_ATM_2.17.16.pdf', '_blank');");
 // mm_menu_0221111945_0.addMenuItem("Reward&nbsp;Dollar&nbsp;Values","location='graf07/awardvalues.cgi'");
   mm_menu_0221111945_0.fontWeight="bold";
   mm_menu_0221111945_0.hideOnMouseOut=true;
   mm_menu_0221111945_0.bgColor='#555555';
   mm_menu_0221111945_0.menuBorder=1;
   mm_menu_0221111945_0.menuLiteBgColor='#FFFFFF';
   mm_menu_0221111945_0.menuBorderBgColor='#003366';

mm_menu_0221111945_0.writeMenus();
} // mmLoadMenus()</script>

<script language="JavaScript" src="graf07/validate.js"></script>
<script type="text/javascript" src="/jquery/jquery.js"></script>
<script type="text/javascript" src="../javascript/jquery-1.4.1.min.js"></script>		
<script  type="text/javascript" src="../jquery/jquery.js"></script>

<script  type="text/javascript" src="../jquery/simplemodal/simplemodal.js"></script>
<link rel="stylesheet" type="text/css" href="../jquery/simplemodal/simplemodal.css"/>

<link href="graf07/Style.css" rel="stylesheet" type="text/css" />
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
<script language="JavaScript" src="graf07/mm_menu.js"></script>
</head>
<body onload="MM_preloadImages('graf07/images/Sub_nav_home_on.gif','graf07/images/Sub_nav_about_on.gif','graf07/images/Sub_nav_faq_on.gif','graf07/images/Sub_nav_contact_on.gif','graf07/images/Sub_nav_Products_on.gif')">

    <script language="JavaScript1.2">mmLoadMenus();</script>

    <table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
        <tr>
            <td>
                <table width="954" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                        <td align="center" valign="top">
                            <img src="graf07/images/ctl_con_logo4.png" width="954" height="324" /></td>
                    </tr>
                    <tr>
                        <td align="left" valign="top">
                            <table width="954" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td width="35" align="left" valign="top"  background="graf07/images/nav_blank.gif">
                                        <img src="graf07/images/nav_blank.gif" width="35" height="31" /></td>
                                    <td width="187" align="left" valign="top" background="graf07/images/nav_blank.gif">
                                        <a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image28','','graf07/images/Sub_nav_home_on.gif',1)">
                                            <img src="graf07/images/Sub_nav_home_off.gif" name="Image28" width="187" height="31" border="0" id="Image28" /></a></td>
                                    <td width="311" align="left" valign="top" background="graf07/images/nav_blank.gif">
                                        <a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','graf07/images/Sub_nav_about_on.gif',1)">
                                            <img src="graf07/images/Sub_nav_about_off.gif" name="Image29" width="311" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>
                                    <td width="177" align="left" valign="top" background="graf07/images/nav_blank.gif">
                                        <a href="graf07/faqs.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','graf07/images/Sub_nav_faq_on.gif',1)">
                                            <img src="graf07/images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a></td>
                                    <td width="244" align="left" valign="top" background="graf07/images/nav_blank.gif">
                                        <a href="graf07/contact.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','graf07/images/Sub_nav_contact_on.gif',1)">
                                            <img src="graf07/images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a></td>                                 
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td width="954" height="9" align="left" valign="top">
                            <img src="graf07/images/topBumper.gif" width="954" height="9" /></td>
                    </tr>
                    <tr>
                        <td background="graf07/images/background.gif">
                            <table width="924" border="0" align="center" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td width="204" height="13" align="left" valign="top">
                                        <table width="204" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td align="left" valign="top">
                                                    <img src="graf07/images/Landing_L_top.gif" width="204" height="15" /></td>
                                            </tr>
                                            <tr>
                                                <td align="left" valign="bottom" background="graf07/images/Landing_L_tile.gif">
                                                    <table width="190" border="0" align="center" cellpadding="1" cellspacing="1">
                                                        <tr>
                                                            <td class="BIGBoxTitles">
                                                                Interested in earning rewards for your referrals?                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table width="204" border="0" cellspacing="0" cellpadding="0">
                                                        <tr>
                                                            <td align="left" valign="top">
                                                            <table width="97" border="0" cellspacing="1" cellpadding="1">
                                                              <tr>
                                                                <td width="5" align="left" valign="top">&nbsp;</td>
                                                                <td><a href="graf07/agreement.cgi">Enroll Here</a> </td>
                                                              </tr>
                                                              <tr>
                                                                <td colspan="2">&nbsp;</td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td height="20" align="left" valign="top" class="Enrollcopy"> Already Enrolled? </td>
                                                              </tr>
 <form name="logon" action="/cgi-bin/lp-validate.cgi" method="post">
     <input type='hidden' name='program_id' value="154">
     <input type="hidden" name="fund_id" value="649">
     <input type="hidden" name="source_id" value="1">

                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td align="left" valign="top" class="LoginCopy">User ID: </td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td align="left" valign="top" class="LoginCopy"><input name="userid" type="text" id="username" size="8" /></td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td align="left" valign="top" class="LoginCopy">Password:</td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td align="left" valign="top" class="LoginCopy"><input name="password" type="password" id="password" size="8" /></td>
                                                              </tr>
                                                              <tr>
                                                                <td align="left" valign="top">&nbsp;</td>
                                                                <td class="LoginCopy"><input name="Submit" type="submit"  value="Log In" /></td>
                                                              </tr>
</form>

                                                            </table>                                                          </td>
                                                            <td width="103" align="left" valign="bottom">
                                                                <img src="graf07/images/Landing_L_PIC.gif" alt="table" width="103" height="137" /></td>
                                                        </tr>
                                                    </table>                                              </td>
                                            </tr>
                                            <tr>
                                                <td align="left" valign="top">
                                                    <img src="graf07/images/Landing_L_botPic.gif" width="204" height="19" /></td>
                                            </tr>
                                        </table>
                                        <img src="graf07/images/spacer.gif" width="1" height="11" /><br /><br />
                                        <table width="204" height="188" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td>
                                                    <img src="graf07/images/Landing_L_top.gif" width="204" height="15" border="0"/></td>
                                            </tr>
                                            <tr>
                                                <td width="203" align="left" valign="top" background="graf07/images/Landing_L_tile.gif">
                                                    <table width="191" border="0" align="center" cellpadding="1" cellspacing="1">
                                                        <tr>
                                                            <td width="187" height="132" align="center" valign="middle">
                                                                <span class="BlueTitles">Trouble logging in?</span> <span class="Enrollcopy">Questions about the program?</span><br />
                                                                <span class="Earncopy">Give us a call! </span>
                                                                <br />
                                                                <span class="Questionscopy">Referral Program Customer Service</span>
                                                                <br />
                                                                <span class="Earncopy">Call  1 866-968-2261</span><span class="Questionscopy"><br />
                                                                </span><span class="Questionscopy">Mon-Fri 7-7 PST, Sat 7-6 PST<br>Or email <a href="mailto:refer.friend\@centurylink.com">refer.friend\@centurylink.com</a></span><br />
                                                                
        <span class="Questionscopy">Or fill out the <a href="#" onclick="openModalLarge('graf07/quickform.cgi');return false;">Quick Contact Form</a></span>                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>                                                            </td>
                                                        </tr>
                                                    </table>                                                </td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <img src="graf07/images/Landing_L_bot.gif" width="204" height="19" /></td>
                                            </tr>
                                        </table>                                    </td>
                                  <td width="510" align="left" valign="top"><table width="510" height="468" border="0" cellspacing="0" cellpadding="0">
                                    <tr>
                                      <td align="left" valign="top"><img src="graf07/images/Landing_Mtitle_top.gif" width="510" height="13" /></td>
                                    </tr>
                                    <tr>
                                      <td width="510" align="left" valign="top" background="graf07/images/Landing_Mtitle_tile.gif"><table width="500" border="0" cellspacing="0" cellpadding="0">
                                          <tr>
                                            <td width="8" align="left" valign="top">&nbsp;</td>
                                            <td align="left" valign="top" class="BlueTitles"><p><img src="graf07/images/HEADER_TITLE.gif" width="367" height="26" /></p></td>
                                          </tr>
                                      </table></td>
                                    </tr>
                                    <tr>
                                      <td align="left" valign="top"><img src="graf07/images/Landing_Mtitle_bot.gif" width="510" height="8" /></td>
                                    </tr>
                                    <tr>
                                      <td width="510" align="left" valign="top" background="graf07/images/Landing_M_tile.gif" style="height: 470px"><table width="500" border="0" cellspacing="0" cellpadding="0">
                                          <tr>
                                            <td width="10" align="left" valign="top">&nbsp;</td>
                                            <td align="left" valign="top" class="subTitles"><br />
                                                <table>
<tr>
                                                    <td width="364" align="left" valign="top" class="subTitles">Earn rewards for qualified referral orders placed through the CenturyLink Partner Referral Program</td>
                                                    <td width="108"><img src="graf07/images/Land_CashLogo_amex.gif" width="123" height="73" /><br />
                                                        <br /></td>
                                                  </tr>
                                              </table></td>
                                          </tr>
                                          <tr>
                                            <td align="left" valign="top">&nbsp;</td>
                                            <td align="center" valign="top" class="subTitles"><img src="graf07/images/Landing_copy.gif" width="400" height="25" /></td>
                                          </tr>
										  <tr><td align="left" valign="top">&nbsp;</td>
										  <td align="left" valign="top">&nbsp;</td>
										  </tr>
										  <tr><td align="left" valign="top">&nbsp;</td>
										  <td align="left" valign="top" class="subTitles">
										&nbsp</td>
                                          </tr>
<!--	------------------- START	-->

 <tr>
                                                            <td align="left" valign="top">&nbsp;                                                          </td>
                                                          <td height="240" align="left" valign="middle" class="subTitles"> <!--   <table width="457" border="0" align="center" cellpadding="0" cellspacing="0">
                                                            <tr>
                                                              <td width="457" height="233" align="left" valign="top" background="graf07/images/EarnBox.gif"><br />
                                                                  <br />
                                                                <table width="440" border="1" align="center" cellpadding="1" cellspacing="0" bordercolor="#005DAB">
 <tr class="BIGBoxTitles">
 <td colspan="2" align="left" valign="top" bgcolor="#FFFFFF" class="BIGBoxTitles"><div align="center" class="BIGBoxTitles">
 <div align="center">REWARD CARD VALUES</div>
  </div></td>
 </tr>


                                                                <tr class="Enrollcopy">
                                                                  <td  align="center" valign="center" bgcolor="#FFFFFF" class="BlueTitles">
								 </br> Earn \$25 value reward card per residential referral </br></br>
								  for orders placed through the </br></br>
								  <span class="BIGBoxTitles">CenturyLink Refer a Friend Program</span><br> </br></td>
                                                                  </tr>
                                                              </table></td>
                                                            </tr>
                                                          </table>--></td>
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
                                                    <img src="graf07/images/Landing_M_bot.gif" width="510" height="14" /></td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td width="205" align="left" valign="top">
                                        <table width="205" border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td width="205" align="left" valign="top">
                                                    <img src="graf07/images/Land_rbox_top.gif" width="205" height="15" /></td>
<!--	-->
                                            </tr>
                                            <tr>
                                                <td width="205" align="left" valign="top" background="graf07/images/Land_rbox_tile.gif" style="height: 491px">
                                                    <table width="195" border="0" align="center" cellpadding="1" cellspacing="1">
                                                        <tr>
                                                            <td colspan="2" class="BlueTitles">
                                                                Here's How It Works:                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td width="34" align="left" valign="top">
                                                                <img src="graf07/images/no1.gif" width="29" height="30" /></td>
                                                            <td width="154" align="left" valign="top" class="LoginCopy">
                                                                <span class="revLink"><a href="graf07/agreement.cgi">Enroll</a></span> in the CenturyLink Partner Referral Program and obtain your User ID</td>
                                                        </tr>
                                                        <tr>
                                                            <td height="4" colspan="2" align="left" valign="top">
                                                                <img src="graf07/images/spacer.gif" width="1" height="1" /></td>
                                                        </tr>
                                                        <tr>
                                                            <td align="left" valign="top">
                                                                <img src="graf07/images/no2.gif" width="29" height="30" /></td>
                                                            <td width="154" align="left" valign="top" class="LoginCopy" onfocus="MM_openBrWindow('http://qwest.centurylink.com/residential/refer/index.html','','')">
Once you have your User ID, refer potential customers through the CenturyLink Partner Referral Program. You can create a callback referral <a href="graf07/notlogged.cgi" class="revLink">here</a> or call 1-866-968-2261. Be sure to provide your User ID to the Representative.</td>
                                                        </tr>
                                                        <tr>
                                                            <td height="4" colspan="2" align="left" valign="top">
                                                                <img src="graf07/images/spacer.gif" width="1" height="1" /></td>
                                                        </tr>
                                                        <tr>
                                                            <td align="left" valign="top">
                                                                <img src="graf07/images/no3.gif" width="29" height="30" /></td>
                                                            <td align="left" valign="top" class="LoginCopy">
                                                               Earn an award for qualified orders placed through the CenturyLink Partner Referral Program.</td>                                                         </td>
                                                        </tr>
                                                        <tr>
                                                            <td height="4" colspan="2" align="left" valign="top">
                                                                <img src="graf07/images/spacer.gif" width="1" height="1" /></td>
                                                        </tr>
                                                        <tr>
                                                            <td align="left" valign="top">
                                                                <img src="graf07/images/no4.gif" width="29" height="30" /></td>
                                                            <td align="left" valign="top" class="LoginCopy">
                                                                <a href="graf07/notlogged.cgi" class="revLink">
Check</a> your account status at anytime. </td>
                                                        </tr>
                                                        
                                                    </table>
                                              </td>
                                            </tr>
                                            <tr>
                                                <td width="205" align="left" valign="top" style="height: 6px">
                                                    <img src="graf07/images/Land_rbox_bot.gif" width="205" height="13" /></td>
                                            </tr>
                                        </table>                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <img src="graf07/images/bottombuffer.gif" width="954" height="15" /></td>
                    </tr>
                    <tr>
        <td width="954" height="66" align="center" valign="middle" background="graf07/images/bottom_amex.gif"><table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
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


