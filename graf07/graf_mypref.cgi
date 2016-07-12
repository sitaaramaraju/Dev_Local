use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use CCICryptography;
my $cgi = CGI->new();
my $redir = 0;
$redir = $cgi->param('redir');

use DBInterface;
my $myDB = DBInterface->new();
my $myDB2 = DBInterface->new();

print $cgi->header('text/html');

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
my $thisfile = "graf_mypref.cgi";

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
      alert("Your session has expired. Please login and try again.");
      document.lead.action='$url';
      document.lead.submit();
    </script>
  </form>
 </body>
</html>];
exit();

}


my $sql = "select name as name, cust_id as cust_id , e_mail from cust_contact with (nolock) where contact_info_id in
(select contact_info_id from staff with (nolock)
where staff_id = ? ) ";

my $sth = $myDB->prepare($sql);
$sth->execute($staff_id);
my $prog = $sth->fetchrow_hashref();
$sth->finish();

my $name = uc($prog->{name});
my $cust_id = $prog->{cust_id};
my $curr_email =  $prog->{e_mail};

$sql = " select contact_main_id, isnull(icust1, 0) as yes_offer, isnull(icust2, 0) as yes_ref_email
from contact_main with (nolock) where cust_id = ? ";

my $sth = $myDB->prepare($sql);
$sth->execute($cust_id);
my $prefs = $sth->fetchrow_hashref();
$sth->finish();

my $yes_offer = $prefs->{yes_offer};
my $yes_ref_email =  $prefs->{yes_ref_email};
my $contact_main_id =  $prefs->{contact_main_id};
my ( $chk_yes_offer, $chk_no_offer, $chk_yes_ref_email, $chk_no_ref_email);
if ($yes_offer == 1) {
	$chk_yes_offer = "checked";
	$chk_no_offer = "";
} else {
	$chk_yes_offer = "";
	$chk_no_offer = "checked";
}

if ($yes_ref_email == 1) {
	$chk_yes_ref_email = "checked";
	$chk_no_ref_email = "";
}
else {
	$chk_yes_ref_email = "";
	$chk_no_ref_email = "checked";
}

#=head
#my $emplid = $prog{emplid};
# <input type='hidden' name='p' value = '$main::cgi{p}'>
my $TABLE_NAME;
my $table_sql = "select 0 as cnt UNION
           select isnull(count(cust_id),0) as cnt
           from  youcan.dbo.patriot with (Nolock)
           where cust_id = ?
           order by 1 desc ";

my $sth = $myDB->prepare($table_sql);
$sth->execute($cust_id);
my $found_patriot = $sth->fetchrow_hashref();
$sth->finish();


my $patriot = $found_patriot->{cnt};
my $patriot2 ;
if ($patriot == 0) {
my $table_sql2 = "select 0 as cnt UNION
           select isnull(count(cust_id),0) as cnt
           from  youcan.dbo.patriot_consumer_sep19 with (Nolock)
           where cust_id = ?
           order by 1 desc";

my $sth = $myDB->prepare($table_sql2);
$sth->execute($cust_id);
my $found_old = $sth->fetchrow_hashref();
$sth->finish();

 $patriot2 = $found_old->{cnt};

}
if ($patriot == 1) {
	$TABLE_NAME = ' youcan.dbo.patriot';
}
elsif ($patriot2 == 1) {
	$TABLE_NAME = 'youcan.dbo.patriot_consumer_sep19';
}

my $email_sql2 = "select get_paper from youcan.dbo.patriot with (nolock) where cust_id = ? ";
#$myDB->Sql($email_sql2);
#$myDB->FetchRow();
#my %paper_st = $myDB->DataHash();

my $sth = $myDB->prepare($email_sql2);
$sth->execute($cust_id);
my $paper_st = $sth->fetchrow_hashref();
$sth->finish();


my $get_paper = $paper_st->{get_paper};
my ( $yes_paper, $no_paper);
if ($get_paper == 1) {$yes_paper = "checked"; $no_paper = ""; }
else {$yes_paper = ""; $no_paper = "checked"; }
#=cut

my $PAGETITLE = 'GRAF-MY Preferences';


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


    var prevent_double_submits = 0;
    function checkform() {
        document.my_pref.redir.value = 1;

        if(document.my_pref.redir.value == 1){
           if (!document.my_pref.paper[0].checked && !document.my_pref.paper[1].checked ) {
                document.my_pref.redir.value = 0;
                window.alert('Please select the appropriate choice for receiving VISA Statements.');
		   } 
		   else if (!document.my_pref.offers[0].checked && !document.my_pref.offers[1].checked ) {
                document.my_pref.redir.value = 0;
                window.alert('Please select the appropriate choice for receiving E-mail Offers.');
            }
	
        }
                if ( document.my_pref.redir.value == 0 ) {
                    return false;
                }
                else  {
                    document.my_pref.submit();
                    return true;
                }

        // No errors, and we already submitted once?
    }

</script>
<script language="JavaScript" src="mm_menu.js"></script>
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
<td width="187" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onclick="logoutUser($session_id,$staff_id);" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image58','','images/Logout_white.jpg',1)"><img src="images/Logout_blue.jpg" name="Image58" width="113" height="29" border="0" id="Image58" /></a></td>
                          <td width="311" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','images/Sub_nav_about_on.gif',1)"> <img src="images/Sub_nav_about_off.gif" name="Image29" width="311" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>
						  <td width="177" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onClick="document.my_pref.action='faqs.cgi';document.my_pref.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','images/Sub_nav_faq_on.gif',1)"> <img src="images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a></td>
                          <td width="244" align="left" valign="top" background="images/nav_blank.gif" colspan=2><a href="#" onClick="document.my_pref.action='contact.cgi';document.my_pref.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','images/Sub_nav_contact_on.gif',1)"> <img src="images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a></td>  
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
<td align="left" valign="top" class="BlueTitles">MY PREFERENCES&nbsp;</td>
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
  <td align="left" valign="top"> <a href="#" onClick="document.my_pref.action='graf_leadchk.cgi';document.my_pref.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image16','','images/SubmitNav2_top_on.gif',1)"><img src="images/SubmitNav2_top_off.gif" name="Image16" width="195" height="33" border="0" id="Image16" /></a></td>
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
<table width="650" border="0" align="right" cellpadding="1" cellspacing="1" class="Enrollcopy">
<!-- change content below this -->
<form name='my_pref' action='' method='post'>
<input type="hidden" name="client_id"  value="50">
<input type='hidden' name='program_id' value = "$program_id">
<input type="hidden" name="fund_id"    value="$fund_id">
<input type="hidden" name="cci_id" value="$cci_id">
<tr>
EOF

my $msg = '';
my ($e_mail, $paper, $offers, $ref_email);
#my $e_mail = EscQuote($cgi->param('e_mail'));
#my $paper = EscQuote($cgi->param('paper'));
#my $offers = EscQuote($cgi->param('offers'));
#my $ref_email =  EscQuote($cgi->param('ref_email'));
my ($patriot_sql, $cm_sql, $email_sql, $email_sql_2, $email_sql_3, $email_sql_4);
if($redir == 1){
my ($e_mail_msg, $offer_msg, $ref_msg);
if (($e_mail ne '') and (length($e_mail) != 0) ) {
 $email_sql = "update cust_contact set e_mail = ? where cust_id = ? ";
 my $sth = $myDB->prepare($email_sql);
 $sth->execute($e_mail, $cust_id) or die $sth->errstr;
 $sth->finish();
 #$myDB2->Sql($email_sql);
 $email_sql_2 = "update cust set Email = '$e_mail' where cust_id = $cust_id ";
 #$myDB2->Sql($email_sql_2);
 #$email_sql_3 = "update contact_info set e_mail = '$e_mail' where contact_info_id = $contact_info_id";
 #$myDB2->Sql($email_sql_3);
 #$email_sql_4 = "update contact_personnel set personnel_email = '$e_mail' where contact_main_id = $contact_main_id";
 #$myDB2->Sql($email_sql_4);
}
my $paper_msg = 'Your Qwest Rewards VISA&reg; Stetements are available online ';
if ($paper == 0) {
$paper_msg .= '.'
}
else {
$paper_msg .= 'and will be mailed to you.'
}
#$patriot_sql = "update $TABLE_NAME set get_paper = $paper where cust_id = $cust_id  ";
#$myDB->Sql($patriot_sql);

if ($offers == 1) {
$offer_msg = 'We will ';
}
else {
$offer_msg = 'We will not '; 
}
$offer_msg .= 'email you our promotion offers.';
if ($ref_email == 1) {
$ref_msg = 'We will ';
}
else {
$ref_msg = 'We will not '; 
}
$ref_msg .= 'send you updates on your referrals.';
$cm_sql = "update contact_main set icust1 = $offers , icust2 = $ref_email where cust_id = $cust_id  ";
#$myDB->Sql($cm_sql);
print<<"EOF";
<tr>
<td align="left" class="LEtitle" valign="top" nowrap>Thank You for letting us know about your preferences. $e_mail </td></tr>
<td align="left" class="LEtitle" valign="top" nowrap>&nbsp;</td></tr>
<td align="left" class="LEtitle" valign="top" nowrap>&nbsp;$paper_msg</td></tr>
<td align="left" class="LEtitle" valign="top" nowrap>&nbsp;</td></tr>
<td align="left" class="LEtitle" valign="top" nowrap>&nbsp;$offer_msg</td></tr>
<td align="left" class="LEtitle" valign="top" nowrap>&nbsp;</td></tr>
<td align="left" class="LEtitle" valign="top" nowrap>&nbsp;$ref_msg </td></tr>
EOF
#';
}
elsif ($redir == 0) {

print<<"EOF";

<!-- ------------------------------------------------------------- -->
<td align="left" class="LEtitle" valign="top" nowrap> MY e-mail address: </td>
<td align="left" class="LEtitle" valign="top" >&nbsp;</td>
<td align="left" colspan="2" class="LEtitle" valign="top" >
<input class="LEtitle"  name="e_mail" size="50" type="text" value="$curr_email"/></td>
<td align="left" class="LEtitle" valign="top" >&nbsp;</td>
<td align="left" class="LEtitle" valign="top" >&nbsp;</td>
</tr>
<tr>
<td align="left" class="LEtitle" valign="top">&nbsp; </td>
<td align="left" class="LEtitle" valign="top" >&nbsp; </td>
EOF
if ($curr_email eq '') {
print<<"EOF";
       <td align="left" colspan="2" class="FAQuestions" valign="top">&nbsp;</td>
EOF

}
else {
print<<"EOF";
     <td align="left" colspan="2" class="FAQuestions" valign="top">(Please edit e-mail address if required)</td>
EOF
}
 
print<<"EOF";
<td align="left" class="subTitles" valign="top">&nbsp;</td>
<td align="left" class="subTitles" valign="top">&nbsp;</td>
</tr>
<tr>
<td align="left" class="subTitles" colspan="6" valign="top">&nbsp;</td>
</tr>
<tr>
<td align="left" colspan="6" class="LEtitle" valign="top"> I would like to receive the American Express&reg;&#45;branded reward card transaction summary <br> </td>
</tr>
<tr>
<td align="left" class="LEtitle" valign="top">&nbsp;</td> 
<td align="left" colspan="2" valign="top" class="LEtitle" nowrap><input name="paper" type="radio" value="0" $no_paper/> Online Only </td>
<td align="left" colspan="2" class="LEtitle" valign="top" nowrap><input name="paper" type="radio" value="1" $yes_paper/> Online and Paper </td>
</tr>
<tr>
<td align="left" class="subTitles" colspan="6" valign="top">&nbsp;</td>
</tr>
<tr>
<td align="left" colspan="6" class="LEtitle" valign="top"> I would like to receive Program Updates and Special Offers via e-mail:</td>
</tr>
<tr>
<td align="left" class="LEtitle" valign="top">&nbsp;</td>
<td align="left" colspan="2" valign="top" class="LEtitle" nowrap><input name="offers" type="radio" value="1" $chk_yes_offer/> Yes </td>
<td align="left" colspan="2" class="LEtitle" valign="top" nowrap><input name="offers" type="radio" value="0" $chk_no_offer/> No</td>
</tr>
<tr>
<td align="left" class="subTitles" colspan="6" valign="top">&nbsp;</td>
</tr>
<tr>
<td align="left" colspan="6" class="LEtitle" valign="top"> I would like to receive e-mail updates on every referral I place</td>
</tr>
<tr>
<td align="left" class="LEtitle" valign="top">&nbsp;</td>
<td align="left" colspan="2" valign="top" class="LEtitle" nowrap><input name="ref_email" type="radio" value="1" $chk_yes_ref_email/> Yes </td>
<td align="left" colspan="2" class="LEtitle" valign="top" nowrap><input name="ref_email" type="radio" value="0" $chk_no_ref_email/> No</td>
</tr>
<tr>
<td align="left" class="subTitles" colspan="6" valign="top">&nbsp;</td>
</tr>
<tr>
<td align="center" class="LEQuiz" colspan="5" valign="top">
<input type="hidden" name="redir" value="">
<input type="button" name="go" value="Update MY Preferences" class="btnon"
   onMouseOver="this.className='btnoff';"
   onMouseOut="this.className='btnon';" onclick="checkform();"></form></td>
</tr>

EOF

}

print<<"EOF";
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
require "D:/centurylinkyoucan/graf07/footer.cgi";
print<<"EOF";
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>


EOF


$myDB->disconnect();
$myDB2->disconnect();
