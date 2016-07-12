use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
use DBInterface;
use CCICryptography;
use Try::Tiny;

my $myDB= DBInterface->new();

my $server ="";
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
else {
	$server = "D:/centurylinkyoucan";
}

my $thisfile = "graf_submitreferral.cgi";

require "$server/cgi-bin/delimeter.cgi";
require "$server/graf07/graf_subs.cgi";
my $client_id = 50;
my $program_id = 154;
my $fund_id = 649;
my $cci_id = $cgi->param('cci_id');

#my $url = CCICryptography::getUrl_sites('graf03');
my $url = "../index_raf.cgi";

my ($session_id,$staff_id)=(0,0);
my $chk = 0;

if (length($cci_id) > 1) {
	($session_id,$staff_id) = CCICryptography::getEmpid($cci_id);
	$chk = CCICryptography::validate_CL_sites($cci_id,'graf03');
}

############### validation ################
#my $valid  = CCICryptography::validate_CL_sites($cci_id,'graf03');
if ($chk <= 0 || length($cci_id) == 0) {
  print qq[
  <form name="lead" action="$url" method="post">
  <input type="hidden" name="session_id" value="0">
    <script language='javascript'>
      alert("Your session has expired. Please login again.");
      document.lead.action='$url';
      document.lead.submit();
    </script>
  </form>
 </body>
</html>];
exit();
}


my $sql = qq(
	select cust_contact.name as name, cust.cust_id, isnull(cust_type_id,0) as cust_type_id, datepart(year, getdate()) as curryear
	from cust_contact with (nolock), cust with(nolock), staff with(nolock)
	where cust_contact.cust_id = cust.cust_id
	and cust_contact.contact_info_id = staff.contact_info_id
	and staff_id = ?
);

my $prog;
try {
	my $sth = $myDB->prepare($sql);
	$sth->execute($staff_id) or die $sth->errstr;
	$prog = $sth->fetchrow_hashref;
}
catch {
	DBInterface::writelog('graf07',"$thisfile", $_ );
};

my $name = uc($prog->{name});
my $cust_id = $prog->{cust_id};
my $cust_type = $prog->{cust_type_id};
my $year = $prog->{curryear};

my $ref = get_num_referrals($cust_id, $program_id, $fund_id);

# Get Referral Award value
my $ref_award = get_sum_net($cust_id);

my  $PAGETITLE = 'CenturyLink Refer A Friend-Submit Referrals';

print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>GRAF-Submit Referral</title>
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
}  
mmLoadMenus()
</script>
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
 
function openwindow2(URL) {
        win = window.open(URL, "pop", "width=800, height=550, left=50, top=50, scrollbars=yes, toolbar=no, menubar=no, status=yes, resizable=yes");
    }
function openMessage() {
window.open('http://www.qwestreferafriend.com/qwest/visacard_expires.html', "visacard_reminder","width=600, height=100, left=200, top=120, scrollbars=auto, toolbar=no, menubar=no, status=no, resizable=yes");
}
var isNN = (navigator.appName.indexOf("Netscape")!=-1);



    function isNumeric(e) {
		return !String.fromCharCode(window.event ? e.keyCode : e.which).search(/\\d/);
	}
    function enablefields() {
        document.lead_graf.lead_name.disabled = false;
        document.lead_graf.biz_name.disabled = false;
        document.lead_graf.biz_cont_name.disabled = false;
        document.lead_graf.main_btn1.disabled = false;
        document.lead_graf.main_btn2.disabled = false;
        document.lead_graf.main_btn3.disabled = false;
        document.lead_graf.time_to_call.disabled = false;
        document.lead_graf.cust_type.disabled = false;
    }
    function disablefields() {
        document.lead_graf.lead_name.disabled = true;
        document.lead_graf.biz_name.disabled = true;
        document.lead_graf.biz_cont_name.disabled = true;
        document.lead_graf.main_btn1.disabled = true;
        document.lead_graf.main_btn2.disabled = true;
        document.lead_graf.main_btn3.disabled = true;
        document.lead_graf.time_to_call.disabled = true;
        document.lead_graf.cust_type.disabled = true;

    }
    function updateprods(objectname, prod_id){
        if ( objectname.checked == true ) {
            document.lead_graf.prodvalidate.value = (document.lead_graf.prodvalidate.value)*1 + 1;
        }else {
            document.lead_graf.prodvalidate.value = (document.lead_graf.prodvalidate.value)*1 - 1;
        }
    }

    var prevent_double_submits = 0;
    function checkform() {

        document.lead_graf.redir.value = 1;

           if (document.lead_graf.cust_type[0].checked== false && document.lead_graf.cust_type[1].checked== false ) {
                document.lead_graf.redir.value = 0;
                window.alert('Please select the appropriate box indicating the type of customer.');
            }else if (!document.lead_graf.prod_int[0].checked
               && !document.lead_graf.prod_int[1].checked
	       && !document.lead_graf.prod_int[2].checked
	       && !document.lead_graf.prod_int[3].checked
	       && !document.lead_graf.prod_int[4].checked) {
                document.lead_graf.redir.value = 0;
                window.alert('Please check the appropriate box for product of interest.');
            }
            else if (document.getElementById('resCheck').checked && document.lead_graf.lead_name.value == "") { 
              
                document.lead_graf.redir.value = 0;
                window.alert('Please enter customer name.');
                       
            }
            else if (document.getElementById('bizCheck').checked && document.lead_graf.biz_name.value == "") { 
              
                document.lead_graf.redir.value = 0;
                window.alert('Please enter business name.');
                           
            }
            else if (document.getElementById('bizCheck').checked && document.lead_graf.biz_cont_name.value == "") { 
              
                document.lead_graf.redir.value = 0;
                window.alert('Please enter business contact name.');
                           
            }
            else if (document.lead_graf.lead_state.value == "") {
                document.lead_graf.redir.value = 0;
                window.alert('Please enter customer State.');
	    }
	    else if (document.lead_graf.main_btn1.value == "" ){
                    document.lead_graf.redir.value = 0;
                    window.alert('A complete Phone number for the contact or company is required');
                    document.lead_graf.main_btn1.focus();
                }else if (document.lead_graf.main_btn2.value == "" ){
                    document.lead_graf.redir.value = 0;
                    window.alert('A complete Phone number for the contact or company is required');
                    document.lead_graf.main_btn2.focus();
                }else if (document.lead_graf.main_btn3.value == "" ){
                    document.lead_graf.redir.value = 0;
                    window.alert('A complete Phone number for the contact or company is required');
                    document.lead_graf.main_btn3.focus();
                }else if (document.lead_graf.time_to_call.value == "") {
                document.lead_graf.redir.value = 0;
                window.alert('Please select the appropriate time to call.');
            }
			
			
			
        // No errors, and we already submitted once?
        if ( document.lead_graf.redir.value == 1 && prevent_double_submits == 0 ) {
           //alert("hey " + prevent_double_submits );
			   //document.lead_graf.submitbtn.disabled=true;
				document.lead_graf.action = "graf_loggedin.cgi";
				document.lead_graf.submitbtn.value = "Please wait...";

            prevent_double_submits = 1;
            document.lead_graf.submit();
            return true;
        }
        else{
            // Nope, error, or we already submitted once
            //alert("Nope");
	            return false;
        }
    }

//-->
</script>

<script type="text/javascript">
 

function showHide() {     
    if (document.getElementById('resCheck').checked) {      
        document.getElementById('Resdiv1').style.display = 'block';
		document.getElementById('Resdiv2').style.display = 'block';
        document.getElementById('Bizdiv1').style.display = 'none';    
	    document.getElementById('Bizdiv2').style.display = 'none'; 	
		document.getElementById('Bizdiv3').style.display = 'none';    
	    document.getElementById('Bizdiv4').style.display = 'none'; 
		document.getElementById('Resdiv3').style.display = 'none';   
		document.getElementById('Resdiv4').style.display = 'none'; 		
    } 
    else if(document.getElementById('bizCheck').checked) {    
        document.getElementById('Bizdiv1').style.display = 'block';
		document.getElementById('Bizdiv2').style.display = 'block';
		document.getElementById('Bizdiv3').style.display = 'block';
		document.getElementById('Bizdiv4').style.display = 'block';
        document.getElementById('Resdiv1').style.display = 'none';   
		document.getElementById('Resdiv2').style.display = 'none'; 	
		document.getElementById('Resdiv3').style.display = 'none';   
		document.getElementById('Resdiv4').style.display = 'none'; 	
   }
}
</script>


</head>

<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif','images/SubmitNav2_top_on.gif','images/SubmitNav3_top_on.gif','images/checkbalance_on.gif','images/SubmitNav4_top_on.gif','images/transactionsummary_on.gif')">
<script language="JavaScript1.2">mmLoadMenus();</script>
    <table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
        <tr>
            <td>
                <table width="954" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                        <td align="center" valign="top">
                            <img src="images/ctl_con_logo4.png" width="954" height="324"/></td>
                    </tr>
                    <tr>
                        <td>                        </td>
                    </tr>
                    <tr>
                      <td height="9" align="left" valign="top"><table width="954" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td width="35" align="left" valign="top"  background="images/nav_blank.gif"><img src="images/nav_blank.gif" width="35" height="31" /></td>
                          <td width="187" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onclick="logoutUser($session_id,$staff_id);" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image58','','images/Logout_white.jpg',1)"><img src="images/Logout_blue.jpg" name="Image58" width="113" height="29" border="0" id="Image58" /></a></td>
                          <td width="311" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','images/Sub_nav_about_on.gif',1)"> <img src="images/Sub_nav_about_off.gif" name="Image29" width="311" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>
						  <td width="177" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onClick="document.lead_graf.action='faqs.cgi';document.lead_graf.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','images/Sub_nav_faq_on.gif',1)"> <img src="images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a></td>
                          <td width="244" align="left" valign="top" background="images/nav_blank.gif" colspan=2><a href="#" onClick="document.lead_graf.action='contact.cgi';document.lead_graf.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','images/Sub_nav_contact_on.gif',1)"> <img src="images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a></td>                          
                        </tr>
                      </table></td>
                    </tr>
                    <tr>
                        <td width="954" height="9" align="left" valign="top">
                            <img src="images/topBumper.gif" width="954" height="9" /></td>
                    </tr>
                    <tr>
               <td background="images/background.gif">
    <table width="913" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
<td align="left" valign="top"><img src="images/Sub_titleTop.gif" width="913" height="16" /></td>
  </tr>
 <tr>
     <td background="images/Subtitle_tile.gif">
       <table width="900" border="0" cellspacing="1" cellpadding="1">
                                            <tr>
                                                <td width="10">&nbsp;                                                    </td>
                                                <td align="left" valign="top" class="BlueTitles">
                                                    SUBMIT A REFERRAL&nbsp;                                                </td>
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
                                                <td width="10" align="left" valign="top">&nbsp;                                              </td>
                                              <td align="left" valign="top"><table width="881" height="19" border="0" cellpadding="0" cellspacing="0">
                                                <tr>
                                                  <td colspan="2" align="left" valign="top">&nbsp;</td>
                                                </tr>
				<tr><td colspan="2" class="subTitles2">
			Hello $name,<br />
		You have submitted $ref referrals in $year.<br />
		<!--ISSUE CL-982: Remove this line-->
		<!--Your $year awards total is \$$ref_award for sold leads.-->
												</td></tr>
                                                <tr>
                                                  <td colspan="2" align="left" valign="top"><span class="subTitles2">Be sure to review the information under &quot;About the Program&quot; menu above for updates.<br>
												  Questions about your Referral Rewards Card Expiration, <a class="BIG" href="card_expire_raf_mdu_04142016.pdf" target="_blank">click here</a>.</span></td>
                                                </tr>
                                                <tr>
                                                  <td align="left" valign="top">&nbsp;</td>
                                                  <td align="left" valign="top">&nbsp;</td>
                                                </tr>
                                                <tr>
                                                  <td align="left" valign="top">&nbsp;</td>
                                                  <td align="left" valign="top">&nbsp;</td>
                                                </tr>
                                                <tr>
                                                  <td width="225" align="left" valign="top"><table width="195" border="0" cellspacing="0" cellpadding="0">
                                                    <tr>
                                                      <td align="left" valign="top"><img src="images/SubmitNav_top.gif" width="195" height="22" /></td>
                                                    </tr>

                                                    <tr>
 <td align="left" valign="top"> <a href="#" onClick="document.lead_graf.action='graf_leadchk.cgi';document.lead_graf.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image16','','images/SubmitNav2_top_on.gif',1)"><img src="images/SubmitNav2_top_off.gif" name="Image16" width="195" height="33" border="0" id="Image16" /></a></td>
</tr>
<!--
<tr>
<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('https://www.onlinecardaccess.com/main/qwest/Home','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image18','','images/SubmitNav4_top_on.gif',1)"><img src="images/SubmitNav4_top_off.gif" name="Image18" width="195" height="45" border="0" id="Image18" /></a></td>
</tr>

<tr>
<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('http://www.rewardbalance.com','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image17','','images/checkbalance_on.gif',1)"><img src="images/checkbalance_off.gif" name="Image17" width="195" height="41" border="0" id="Image17" /></a></td>
</tr>
<tr>
<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('http://www.rewardbalance.com','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image22','','images/transactionsummary_on.gif',1)"><img src="images/transactionsummary_off.gif" name="Image22" width="195" height="45" border="0" id="Image22" /></a></td>
</tr>
-->
<tr>
<td align="left" valign="top"><a href="#" onClick="document.lead_graf.action='graf_mypref.cgi';document.lead_graf.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image21','','images/SubmitNav6_top_on12.gif',1)"><img src="images/SubmitNav6_top_off3.gif" name="Image21" width="195" height="27" border="0" id="Image21" /></a></td>
</tr>
<tr>
<td align="left" valign="top"><img src="images/SubmitNav_bot.gif" width="195" height="22" /></td>
                                                    </tr>
                                                  </table></td>
                                                  <td width="656" align="left" valign="top"><table width="650" border="0" align="right" cellpadding="1" cellspacing="1" class="Enrollcopy">
<form name='lead_graf' action='' method='post'>
<input type="hidden" name="qwest"  value="1">
<input type="hidden" name="cci_id"  value="$cci_id">
<input type='hidden' name='prodvalidate' value=0>
  <tr>
 <td align="left" class="LEtitle" valign="top" width="204"> Customer Type:<font color="red">*</font> </td>
 <td align="left" class="LEQuiz" valign="top" width="31"><input type="radio" checked onclick="javascript:showHide();" name="cust_type"  value="con" id="resCheck"/></td>
 <td align="left" class="LELeadIn" valign="top" width="147"> Residential</td>
  <td align="left" class="LEQuiz" valign="top" width="42"><input type="radio" onclick="javascript:showHide();" name="cust_type" value="res" id="bizCheck"/></td>
 <td align="left" class="LELeadIn" valign="top" width="210"> Business</td>
   </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top" colspn="5">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Products of Interest:<font color="red">*</font> </td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="BRD" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Broadband <br />
                                                      (High-Speed Internet)  </td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="DTV" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Digital TV </td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="WRL" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Wireless</td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="DIV" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Digital Voice </td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="OTH" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Other</td>
                                                      <td align="left" class="LEQuiz" valign="top">&nbsp;</td>
                                                      <td align="left" class="LEQuiz" valign="top">&nbsp;</td>
                                                    </tr>
                                                    <tr><td align="left" class="LEtitle" valign="top" colspan="5">&nbsp;</td> </tr>
                                                                                                      
													
													<tr>
													<td align="left" class="LEtitle" valign="top" id="Bizdiv1" name="Bizdiv1" style="display: none;">Business Name:<font color="red">*</font></td><td>&nbsp;</td>
                                                    <td  align="left" colspan="4" valign="top" id="Bizdiv2" name="Bizdiv2" style="display: none;"><input class="copytitles" name="biz_name" size="35" type="text" /></td>
													</tr>
													
													<tr>
													<td align="left" class="LEtitle" valign="top" id="Bizdiv3" name="Bizdiv3" style="display: none;">Contact Name:<font color="red">*</font></td><td>&nbsp;</td>
                                                    <td align="left" valign="top" colspan="4" id="Bizdiv4" name="Bizdiv4" style="display: none;"><input class="copytitles" name="biz_cont_name" size="35" type="text" /></td>
													</tr>
													
													<tr>
													<td align="left" class="LEtitle" valign="top" id="Resdiv1" name= "Resdiv1"  style="display: block;">Customer Name:<font color="red">*</font></td><td>&nbsp;</td>
                                                    <td align="left" colspan="4" valign="top" id="Resdiv2" name= "Resdiv2"  style="display: block;"><input class="copytitles" name="lead_name" size="35" type="text" /></td>
													</tr>													
													
                                                    
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">Customer Address 1:</td><td>&nbsp;</td>
                                                      <td align="left" colspan="3" valign="top"><input class="copytitles" name="lead_address" size="35" type="text" /></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">Customer Address 2:</td><td>&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top"><input class="copytitles" name="lead_address2" size="35" type="text" /></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">Customer City:</td><td>&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top"><input class="copytitles" name="lead_city" size="35" type="text" /></td>
                                                    </tr>
                                                   <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Customer State:<font color="red">*</font> </td><td>&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top">
                           <select class="FAQuestions" name='lead_state' >
          <option value="">Select State</option>
EOF
						  my ( %state);
    $sql = "select distinct state, abbreviation from lp_states with (nolock)
where program_id = ?
order by state";
	my $success = eval {
	my $sth = $myDB->prepare($sql) or die $myDB->errstr;
	$sth->{PrintError} = 0;
	$sth->execute($program_id) or die $sth->errstr;

    while ( my $state = $sth->fetchrow_hashref) {
    
        print "<option name='lead_state' value='$state->{abbreviation}' >$state->{state}</option>";
    }
	$sth->finish();
	};
	unless($success) {
		DBInterface::writelog('graf07',"$thisfile", $@ );
	}
    print<<"EOF";
	</select> 
</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Customer Zip:</td><td>&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top"><input class="copytitles" name="lead_zip" size="35" type="text" /></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Primary Phone Number:<font color="red">*</font> </td><td>&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top"><input type="text" name = "main_btn1" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3">-
        <input type="text" name = "main_btn2" onKeyUp="return autoTab(this, 3, event);" size="3" maxlength="3" >-
        <input type="text" name = "main_btn3"  size="4" maxlength="4" ></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Secondary Phone Number: </td><td>&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top"><input type="text" name = "lead_phone1" value=""size="3" maxlength="3"  onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "lead_phone2" value=""size="3" maxlength="3" onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "lead_phone3" value=""size="4" maxlength="4">
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Best Time to Call:<font color="red">*</font> </td><td>&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top"><select class="FAQuestions" name="time_to_call">
                                                          <option value="">-Select One-</option>
                                                          <option value="Anytime">Anytime</option>
                                                          <option value="Morning 8am-noon Mountain Time">Morning 8am-noon Mountain Time</option>
                                                          <option value="Afternoon Noon-5pm Mountain Time">Afternoon Noon-5pm Mountain Time</option>
                                                          <option value="Evening After 5pm Mountain Time">Evening After 5pm Mountain Time</option>
                                                        </select>                                                      </td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">Customer has given permission to call?<font color="red">*</font> </td><td>&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top">
											  <input type="radio" name="contact_permission" value="1" onclick="enablefields();document.lead_graf.permission.value=1;">Yes 
											 &nbsp;&nbsp; <input type="radio" name="contact_permission" value="0" onclick="javascript:window.alert('A referral cannot be entered unless the customer allows CenturyLink to contact them.');">No</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top">&nbsp;</td>
                                                    </tr>

                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" class="littleLinks" colspan="4" valign="top"> Please include additional information that will be helpful for us to reach your customer or better understand her or his needs</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Notes:</td>
                                                      <td align="left" colspan="4" valign="top"><textarea class="littleLinks" cols="30" name="lp_notes"></textarea></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEQuiz" valign="top">&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top">&nbsp;</td>
                                                    </tr>
                                                   
                                                    <tr>
                                                      <td align="center" class="LEQuiz" colspan="5" valign="top">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="center" class="LEQuiz" colspan="5" valign="top">
													  <input type="hidden" name="redir" value="">

						     <input name="submitbtn" id="submitbtn" type="button"  value="Submit to CenturyLink" onClick="checkform();"/>
         
	    
	    
	    </td>
                                                    </tr>
                                                  </table></td>
                                                </tr>
<tr><td colspan="2" class="subTitles2"><span class="subTitles2">
EOF
	# if they haven't filled out a W9 then show this message

	unless (check_status($cust_id)) {
		print qq(
			<br />Once you hit \$500 please click</span> <a class="BIG" href="#" onclick="openModalLarge('w9_qwest.cgi?cci_id=$cci_id&qwest=1&staff_id=$staff_id');return false;">here</a><span class="subTitles2"> to fill out the required W-9.<br />
			If this is not done before you earn \$600, you will not be eligible for referral awards until the form is filled out.</span>
		);
	}
print<<"EOF";

</td></tr>
                                              </table></td>
                                            </tr>
                                        </table>                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/Sub_bottom.gif" width="913" height="16" /></td>
                                </tr>
                            </table>                        </td>
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



 