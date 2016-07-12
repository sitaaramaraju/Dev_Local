use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
my $cgi = CGI->new();
my $redir = 0;
$redir = $cgi->param('redir');

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


require "$server/cgi-bin/delimeter.cgi";
require "$server/graf07/graf_subs.cgi";
my $client_id = 50;
my $program_id = 154;
my $fund_id = 649;

my $cci_id = $cgi->param('cci_id');

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


use DBInterface;
my $myDB3 = DBInterface->new();

my $sql = "select cust.cust_id as cust_id, staff.name
				from cust with(nolock)
				inner join cust_contact cc with(nolock) on cc.cust_id = cust.cust_id
				inner join staff with(nolock)on staff.contact_info_id = cc.contact_info_id
				where  staff.staff_id = ?";
	my $sth = $myDB3->prepare($sql);
			$sth->execute( $staff_id  );
	my  $data = $sth->fetchrow_hashref();
	my	$cust_id = $data->{cust_id};
			$sth->finish();

my $thisfile = "graf_leadchk.cgi";

my ($sql,  %prog );

my $PAGETITLE = 'GRAF-Lead Status';

print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>$PAGETITLE</title>
<script language="JavaScript" src="graf07menus.js"></script>
<link href="Style.css" rel="stylesheet" type="text/css" />
<script type="text/JavaScript">

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
function openwindow2(URL) {
        win = window.open(URL, "pop", "width=800, height=550, left=50, top=50, scrollbars=yes, toolbar=no, menubar=no, status=yes, resizable=yes");
    }



//-->
</script>
<script language="JavaScript" src="mm_menu.js"></script>
<script language="JavaScript" src="validate.js"></script>
<script type="text/javascript" src="/jquery/jquery.js"></script>
<script type="text/javascript" src="../../javascript/jquery-1.4.1.min.js"></script>		
<script  type="text/javascript" src="../../jquery/jquery.js"></script>
</head>

<body onload="MM_preloadImages('images/SubmitNav1_top_on.gif','images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif','images/SubmitNav2_top_on.gif','images/checkbalance_on.gif','images/SubmitNav4_top_on.gif','images/transactionsummary_on.gif')">
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
                        <td>                        </td>
                    </tr>
                    <tr>
                      <td height="9" align="left" valign="top"><table width="954" border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="35" align="left" valign="top"><img src="images/nav_blank.gif" width="35" height="31" /></td>
<!-- <td width="187" align="left" valign="top"><a href="graf_submitreferral.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image28','','images/Sub_nav_home_on.gif',1)"> <img src="images/Sub_nav_home_off.gif" name="Image28" width="187" height="31" border="0" id="Image28" /></a></td> -->
<td width="187" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onclick="logoutUser($session_id,$staff_id);" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image58','','images/Logout_white.jpg',1)"><img src="images/Logout_blue.jpg" name="Image58" width="113" height="29" border="0" id="Image58" /></a></td>
<td width="311" align="left" valign="top"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','images/Sub_nav_about_on.gif',1)"> <img src="images/Sub_nav_about_off.gif" name="Image29" width="311" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>

<!--
<td width="177" align="left" valign="top"><a href="faqs.cgi?session_id=$session_id" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','images/Sub_nav_faq_on.gif',1)"> <img src="images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a></td>
<td width="244" align="left" valign="top"><a href="contact.cgi?session_id=$session_id" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','images/Sub_nav_contact_on.gif',1)"> <img src="images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a></td>
-->
<td width="177" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onClick="document.my_pref.action='faqs.cgi';document.my_pref.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','images/Sub_nav_faq_on.gif',1)"> <img src="images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a></td>
<td width="244" align="left" valign="top" background="images/nav_blank.gif" colspan=2><a href="#" onClick="document.my_pref.action='contact.cgi';document.my_pref.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','images/Sub_nav_contact_on.gif',1)"> <img src="images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a></td>

<!-- <td width="198" align="left" valign="top"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image32','','images/Sub_nav_Products_on.gif',1)"> <img src="images/Sub_nav_Products_off.gif" name="Image32" width="198" height="31" border="0" id="Image32" onclick="MM_openBrWindow('http://www.qwest.com/residential/refer/index.html','','')" /></a></td> --> 
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
<td align="left" valign="top">
<img src="images/Sub_titleTop.gif" width="913" height="16" /></td>
</tr>
<tr>
<td background="images/Subtitle_tile.gif">
<table width="900" border="0" cellspacing="1" cellpadding="1">
<tr>
<td width="10">&nbsp;</td>
<td align="left" valign="top" class="BlueTitles">MY REFERRAL HISTORY&nbsp;</td>
</tr>
</table>
</td>
</tr>
<tr>
<td align="left" valign="top"><img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
</tr>
<tr>
<td align="left" valign="middle" background="images/Sub_tile.gif">
<table width="900" border="0" cellspacing="1" cellpadding="1">
<tr>
<td width="10" align="left" valign="top">&nbsp;</td>
<td align="left" valign="top">
<table width="881" height="19" border="0" cellpadding="0" cellspacing="0">
<tr>
<td colspan="2" align="left" valign="top">&nbsp;</td>
</tr>
<tr>
<td colspan="2" align="left" valign="top"><span class="subTitles2">Be sure to review the information under &quot;About the Program&quot; menu above for updates.</span></td>
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
<td width="225" align="left" valign="top">
<table width="195" border="0" cellspacing="0" cellpadding="0">
<tr>
<td align="left" valign="top"><img src="images/SubmitNav_top.gif" width="195" height="22" /></td>
</tr>

<tr>
<td align="left" valign="top"><a href="#" onClick="document.my_pref.action='graf_submitreferral.cgi';document.my_pref.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image15','','images/SubmitNav1_top_on.gif',1)"><img src="images/SubmitNav1_top_off.gif" name="Image15" width="195" height="28" border="0" id="Image15" /></a></td>
</tr>

<tr>
<td align="left" valign="top"><a href="#" onClick="document.my_pref.action='graf_mypref.cgi';document.my_pref.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image21','','images/SubmitNav6_top_on12.gif',1)"><img src="images/SubmitNav6_top_off3.gif" name="Image21" width="195" height="27" border="0" id="Image21" /></a></td>
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
<td align="left" valign="top"><img src="images/SubmitNav_bot.gif" width="195" height="22" /></td>
</tr>
</table></td>
<td width="656" align="left" valign="top">						  
<table width="650" border="1" align="right" cellpadding="1" cellspacing="1" class="Enrollcopy">
<!-- change content below this -->
<form name='my_pref' action='$thisfile' method='post'>

<input type="hidden" name="cci_id" value="$cci_id">
<input type="hidden" name="client_id"  value="50">
<input type='hidden' name='program_id' value = "$program_id">
<input type="hidden" name="fund_id"    value="$fund_id">
<tr>
<td align="left" class="LEtitle" valign="top" >Referral \#</td>
<td align="left" class="LEtitle" valign="top" >Created Date</td>
<td align="left"  class="LEtitle" valign="top" >Customer name</td>
<td align="left"  class="LEtitle" valign="top" >Phone</td>
<td align="left"  class="LEtitle" valign="top" >Lead Status</td>
</tr>
EOF

my %ldt;
my $lsql = "select lp_lead_id, convert(varchar,created_date,1) as ctdt,lead_name, main_btn, 
case when isnull(lead_status_id ,0) = 0 then 'New'
when isnull(lead_status_id ,0) = 1 then 'Open' else dbo.func_getstatus (lead_status_id, 154) end as ldst
 from lp_lead with (nolock) where program_id = 154 and fund_id = 649 and agency_id = $cust_id
order by lp_lead_id desc";

my $sth = $myDB3->prepare($lsql);
$sth->execute();

while (my $ldt = $sth->fetchrow_hashref) {
print<<"EOF";
<tr>
<td align="left" class="LEtitle" valign="top" >$ldt->{lp_lead_id}</td>
<td align="left" class="LEtitle" valign="top" >$ldt->{ctdt}</td>
<td align="left"  class="LEtitle" valign="top" >$ldt->{lead_name}</td>
<td align="left"  class="LEtitle" valign="top" >$ldt->{main_btn}</td>
<td align="left"  class="LEtitle" valign="top" >$ldt->{ldst}</td>
</tr>
EOF
}

print<<"EOF";
<!-- ------------------------------------------------------------- -->

</table></td>
</tr>
</table></td>
</tr>
</table>   
</td>
</tr>
<tr>
<td align="left" valign="top"><img src="images/Sub_bottom.gif" width="913" height="16" /></td>
</tr>
</table>
</td>
</tr>
<tr>
<td><img src="images/bottombuffer.gif" width="954" height="15" /></td>
</tr>
<tr><td width="954" height="66" align="center" valign="middle" background="images/bottom_amex.gif">
<table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
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

