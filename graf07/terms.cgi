use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use CCICryptography;
my $cgi = CGI->new();
print $cgi->header('text/html');

my  $PAGETITLE = 'CenturyLink Refer A Friend-Terms';

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
                <td align="left" valign="top" class="BlueTitles">CENTURYLINK PARTNER REFERRAL PROGRAM TERMS AND CONDITIONS</td>
              </tr>
            </table></td>
          </tr>
          <tr>
		  <form name='lead_graf' action='' method='post'>
		  <input type="hidden" name="cci_id"  value="$cci_id">
            <td align="left" valign="top"><img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
          </tr>
          <tr>
            <td align="left" valign="middle" background="images/Sub_tile.gif"><table width="900" border="0" cellspacing="1" cellpadding="1">
              <tr>
                <td width="10" align="left" valign="top">&nbsp;</td>
                <td align="left" valign="top" class="subTitles"><br />
                  <table width="700" border="0" align="center" cellpadding="1" cellspacing="1">
                    <tr>
                      <td colspan="3" align="left" valign="top" class="subTitles">Eligible participants who participate in the CenturyLink Refer a Friend Program (the  &quot;Program &quot;) are required to read, understand and follow the Terms and Conditions supporting the program, particularly as they relate to ethical sales practices. CenturyLink reserves the right to revise the program, product eligibility, participant eligibility, rewards or cancel the program at any time, without notice, and without any liability or obligation to any participant.  </td>
                    </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top">&nbsp;</td>
                    </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top" class="Questionscopy">Program Eligibility</td>
                    </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top" class="bodycopy">Participants must meet all the relevant eligibility requirements to participate, and each participant must successfully complete the enrollment process.   </td>
                    </tr>
                    <tr>
                      <td width="60" align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">·	Individuals eligible to participate in the Program upon acceptance of these terms and conditions and completion of enrollment must be:  </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&nbsp;</td>
                      <td width="10" align="right" valign="top" class="bodycopy">&deg;</td>
                      <td width="620" align="left" valign="top" class="bodycopy">Individuals (no corporations or other entities may participant or enroll – if you wish to enroll as a Business, please visit &ldquo;About the Programs&rdquo; at centurylinkpassitonrewards.com for information on our Business to Business Referral Program and the CenturyLink Direct Awards Program)  
 </td>
                    </tr>

                    <tr>
                      <td align="right" valign="top" class="bodycopy">&nbsp;</td>
                      <td align="right" valign="top" class="bodycopy">&deg;</td>
                      <td align="left" valign="top" class="bodycopy">Must be over the age of 18 </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&nbsp;</td>
                      <td align="right" valign="top" class="bodycopy">&deg;</td>
                      <td align="left" valign="top" class="bodycopy">Must provide accurate and complete registration information and complete form W-9 if required  </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&nbsp;</td>
                      <td align="right" valign="top" class="bodycopy">&deg;</td>
                      <td align="left" valign="top" class="bodycopy">Must avoid any conduct or action that conflicts or appears to conflict with honest, ethical conduct and the CenturyLink Code of Conduct. Acts by participants that are inconsistent or in violation of these Terms and Conditions or CenturyLink&rsquo; s policies or rules are prohibited.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">CenturyLink may declare anyone ineligible at any time and terminate their enrollment.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">CenturyLink retirees and certain external groups who are specifically designated and described in writing by the Refer a Friend Program managers are eligible to participate in this program.  </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Current CenturyLink employees and extended family members of Refer a Friend Program Headquarters and provisioning center personnel are not eligible to participate in this program. </td>
                    </tr>

                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Participants who leave the Program must spend the balance on their reward card (as defined below) by the expiration date on the front of their reward card </td>
                    </tr>
                    <tr>
                      <td align="left" valign="top" class="bodycopy">&nbsp;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">&nbsp;</td>
                    </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top" class="Questionscopy">Enrollment</td>
                      </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy"> To participate, individuals must expressly agree to participate and accept and agree to these Terms and Conditions by going online to www.centurylinkpassitonrewards.com or calling 1 866-YOU-CAN1 (1 866-968-2261) to enroll in the program.  </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Enrollment is not complete until the participant completes the registration form including: name, address, phone number, identification number (last four digits of Social Security Number or Individual Taxpayer Identification Number) and date of birth. Social Security Number or Individual Taxpayer Identification Number is required for individual participant identification. </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">·	The full Social Security Number or Individual Taxpayer Identification Number is required when a participant&rsquo;s cumulative reward is over $600.00 for the calendar year. The program will send each participant notification, including a W-9 tax form, when the participant reaches \$500.00 for the calendar year. The participant must complete the W-9 and provide their full Social Security Number or Individual Taxpayer Identification Number, in order to receive rewards greater than \$600.00 for the calendar year. </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">BY CLICKING THE ACCEPTANCE BUTTON OR PARTICIPATING IN THE PROGRAM, YOU EXPRESSLY AGREE TO AND CONSENT TO BE BOUND BY ALL OF THE TERMS OF THIS AGREEMENT. IF YOU DO NOT AGREE TO ALL OF THE TERMS OF THIS AGREEMENT, INCLUDING RECEIVING E-MAIL UPDATES REGARDING THE REFER A FRIEND PROGRAM, THE BUTTON INDICATING NON-ACCEPTANCE MUST BE SELECTED, AND YOU MAY NOT PARTICIPATE IN THE PROGRAM   </td>
                    </tr>
                    <tr>
                      <td align="left" valign="top" class="bodycopy">&nbsp;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">&nbsp;</td>
                    </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top" class="Questionscopy">Referral Process Considerations</td>
                      </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">A prospective customer is defined as: </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&nbsp;</td>
                      <td align="left" valign="top" class="bodycopy">1.</td>
                      <td align="left" valign="top" class="bodycopy">the individual currently responsible for the telephone account,  </td>
                    </tr>

                    <tr>
                      <td align="right" valign="top" class="bodycopy">&nbsp;</td>
                      <td align="left" valign="top" class="bodycopy">2.</td>
                      <td align="left" valign="top" class="bodycopy">the individual who will be responsible for the telephone account, if a new customer, or  </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&nbsp;</td>
                      <td align="left" valign="top" class="bodycopy">3.</td>
                      <td align="left" valign="top" class="bodycopy">an individual clearly authorized to make decisions with respect to the telephone service </td>
                    </tr>
                    
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&nbsp;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy"><table width="631" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td align="left" valign="top">&nbsp;</td>
                          <td align="right" valign="top" class="bodycopy">&bull;</td>
                          <td width="601" align="left" valign="top" class="bodycopy">The prospective customer must expressly consent and agree, and the participant making a referral shall be understood to represent to CenturyLink that the prospective customer has consented and agreed:   </td>
                        </tr>

                        <tr>
                          <td width="10" align="left" valign="top">&nbsp;</td>
                          <td width="10" align="right" valign="top" class="bodycopy">&bull;</td>
                          <td align="left" valign="top" class="bodycopy">To the submission of the referral being made by the Participant; and  </td>
                        </tr>
                        <tr>
                          <td width="10" align="left" valign="top">&nbsp;</td>
                          <td width="10" align="right" valign="top" class="bodycopy">&bull;</td>
                          <td align="left" valign="top" class="bodycopy">To be contacted by telephone by CenturyLink to follow up the referral and conclude the sale of the service/product being referred </td>
                        </tr>

                      </table></td>
                      </tr>                    
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Products and services may NEVER be added to a customer&rsquo;s record without explicit consent of the authorized or responsible party.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Outbound telemarketing, door-to-door sales and promotional advertising are prohibited.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Billing corrections, corrections to service orders, requests for repair, or any other contact or assistance that does not involve the provision and sale of a new or added product or service will not qualify as a referral.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Referrals will not be eligible for program rewards if the product or service is already on the customer service record, or if the contact results in a net revenue decrease.  </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">A participant will not receive rewards if the participant had that specific product on their account and disconnected it within the last 90 days.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Referrals for eligible contract renewals cannot be submitted more than 90 days in advance of the contract expiration date, and a contract renewal referral submitted earlier will be closed with no program reward.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Eligible participants may generally discuss company services and products, but may never make representations, claims, offers or otherwise characterize any company service, product, term, condition, tariff, price list or other matter except as expressly described and stated in company-provided brochures and advertisements.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Prospective customers must always be advised that the actual performance, price or other matter affecting a product or service can only be confirmed by the CenturyLink Provisioning Center (the &quot;QPC&quot;).   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Referrals cannot be made for official company service (OCS) orders for CenturyLink-owned and operated facilities.   </td>
                    </tr>
		   <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Participants may not use non-public company systems, databases or facilities to identify a prospective customer, identify the suitability of a referral or to suggest the availability of a service or product.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Participants may only use information that is publicly available to develop referrals and contacts and identify possible services and products. Participants may never use customer proprietary network information (CPNI) and must follow all relevant corporate guidelines and rules relating to CPNI.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Referrals can be made only for products and services identified in these rules. A referral can include an ineligible product or service as long as the referral includes at least one eligible product or service.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Participants may not share or agree to share anything of value with a potential customer in exchange for the referral or the customer&rsquo;s purchase of a service or product.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Self referrals are not eligible through the Refer a Friend program, except during specified promotional periods.   </td>
                    </tr>

                    <tr>
                      <td align="left" valign="top" class="bodycopy">&nbsp;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">&nbsp;</td>
                    </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top" class="Questionscopy">Program Guidelines and Interpretation</td>
                      </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Questions regarding the Terms and Conditions and their interpretation or any program disputes should be directed to CenturyLink Refer a Friend Program Management.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">The QPC must conclude any and every sale of a product or service, explaining, as appropriate, the functions, features, price, etc., to the prospective customer.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">CenturyLink Refer a Friend Program Management reserves the right to limit the maximum reward issued to any participant in the program.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Two open referrals for the same telephone number, for the same product or service will be considered duplicate referrals.    </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">CenturyLink Refer a Friend Program Management reserves the right to modify the program including structure, reward values, and eligibility.</td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">The actions, resolutions, and determinations of CenturyLink Refer a Friend Program Management are final and cannot be appealed.   </td>
                    </tr>

                    <tr>
                      <td align="left" valign="top" class="bodycopy">&nbsp;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">&nbsp;</td>
                    </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top" class="Questionscopy">Rewards and Redemption</td>
                      </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">Rewards will be provided on a reloadable reward card (&ldquo;reward card&rdquo;). All terms and conditions of the Card Terms and Conditions apply to the reward card. Please see the Card Terms and Conditions for all of the details. </td>
                    </tr>

                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">CenturyLink and its affiliated companies are not liable for products or services acquired using the reward card. Nor are CenturyLink or its affiliated companies responsible, in any way, for the use, misuse, abuse, loss, theft, or otherwise in connection with the reward card. By receipt of any awarded merchandise or travel, the participant shall be deemed to have released and agreed to hold harmless CenturyLink and its affiliated companies from liability and damage resulting from malfunction, injury, death, loss or any other liability that may arise from the participant&rsquo;s use of merchandise or travel awards purchased using the reward card.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">The value of a reward made pursuant to the Refer a Friend Program is subject to federal and state income tax. Participants are responsible for all applicable taxes. Participant&rsquo;s social security numbers are required for tax reporting purposes and a 1099-MISC will be issued to participants earning an annual, cumulative amount of \$600 through this program.   </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">CenturyLink, acting through the Program Headquarters, will make all decisions regarding reward eligibility and issuance. The Program Headquarters is the sole judge in interpreting all provisions, rules, qualifications, rewards and any disputes that may arise in the operation of the Program. All of these decisions are final and cannot be appealed. No contract rights are created by the existence of or participation in the Program.  </td>
                    </tr>
                    <tr>
                      <td align="left" valign="top" class="bodycopy">&nbsp;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">&nbsp;</td>
                    </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top" class="Questionscopy">The American Express&reg;&#45;branded reward card </td>
                      </tr>
                    <tr>
                      <td colspan="3" align="left" valign="top" class="bodycopy">Refer to the Card Terms and Conditions or the Program Web site for complete terms and conditions associated with the reward card.  </td>
                      </tr>

                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">CenturyLink is not responsible for the issuance, terms, conditions and use of the reward card.  </td>
                    </tr>
                    <tr>
                      <td align="right" valign="top" class="bodycopy">&bull;</td>
                      <td colspan="2" align="left" valign="top" class="bodycopy">All terms and conditions of the Card Terms and Conditions apply to the Program. By activating the reward card the participant shall be deemed to have agreed to the Card Terms and Conditions provided with the reward card.   </td>
                    </tr>
                  </table>
                  <br />
                  <br /></td>
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
