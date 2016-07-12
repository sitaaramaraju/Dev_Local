use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CCICryptography;
use CGI qw(:standard);
use Try::Tiny;
use HTML::Strip;
my $cgi = CGI->new();

use DBInterface;
my $myDB = DBInterface->new();

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


require "$server/cgi-bin/init.cgi";
require "$server/cgi-bin/delimeter.cgi";
my $thisfile = "graf_loggedin.cgi";

my $cci_id= $cgi->param('cci_id'); 
my $url = "../index_raf.cgi";

my ($session_id,$staff_id); 
my $chk = 0;

if (length($cci_id) != 0) {
	($session_id,$staff_id) = CCICryptography::getEmpid($cci_id);
	$chk = CCICryptography::validate_CL_sites($cci_id,'graf03');
}

if ($chk <= 0 || length($cci_id) == 0){
print<<"EOF";
<!--<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">-->
<!-- (c) 2001-2016 CCI -->
<script language='javascript'>
    window.alert('Your session has expired. Please login again. Thank You.');
    document.location="$url";
</script>
EOF
exit();
}



my $client_id = 50;
my $program_id = 154;
my $fund_id = 649;

my $sql = "select name from cust_contact with (nolock) where contact_info_id in
(select contact_info_id from staff with (nolock)
where staff_id = ? ) ";

my $name;
try {
	my $sth = $myDB->prepare($sql);
	$sth->execute($staff_id) or die $sth->errstr;
	my $prog = $sth->fetchrow_hashref();
	$name = uc($prog->{name});
	$sth->finish();
}
catch {
	DBInterface::writelog('graf07',"$thisfile", $_ );
};


$sql = "select personnel_first_name as fname
from contact_personnel with (nolock)
where contact_main_id in
( select contact_main_id from contact_main where cust_id in
( select cust_id from cust_contact where contact_info_id in
(select contact_info_id from staff with (nolock)
where staff_id = ?)))
and isnull(personnel_first_name, '') <> '' ";

my $fname;
try {
	my $sth = $myDB->prepare($sql);
	$sth->execute($staff_id) or die $sth->errstr;
	my $name_data = $sth->fetchrow_hashref();
	$fname = uc($name_data->{fname});
	$sth->finish();
}
catch {
	DBInterface::writelog('graf07',"$thisfile", $_ );
};

$sql = "select cust_id as cust_id from cust_contact where contact_info_id in
(select contact_info_id from staff with (nolock)
where staff_id = ?) ";

my $agency_id;
try {
	my $sth = $myDB->prepare($sql);
	$sth->execute($staff_id) or die $sth->errstr;
	my $cust_data = $sth->fetchrow_hashref();
	$agency_id = uc($cust_data->{cust_id});
	$sth->finish();
}
catch {
	DBInterface::writelog('graf07',"$thisfile", $_ );
};


my $msg = do_submit();

# for old browsers
my  $PAGETITLE = 'CenturyLink Refer A Friend-Logged';


print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>GRAF-Logged In</title>
<script language="JavaScript" src="graf07menus.js"></script>
<script language="JavaScript" src="mm_menu.js"></script>
<script language="JavaScript" src="validate.js"></script>
<script type="text/javascript" src="/jquery/jquery.js"></script>
<script type="text/javascript" src="../../javascript/jquery-1.4.1.min.js"></script>		
<script  type="text/javascript" src="../../jquery/jquery.js"></script>

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
//-->
</script>
<script language="JavaScript" src="mm_menu.js"></script>
</head>

<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif','images/SubmitNav1_top_on.gif','images/SubmitNav2_top_on.gif','images/SubmitNav3_top_on.gif','images/SubmitNav4_top_on.gif','images/SubmitNav5_top_on.gif')">
<!-- pass to leadpro_frame -->
<form name="lead" action="" method="post">
    
    <input type="hidden" name="client_id"  value="50">
    <input type="hidden" name="program_id" value="$program_id">
    <input type="hidden" name="fund_id"    value="$fund_id">
    <input type="hidden" name="cci_id" value="$cci_id">
    
</form>
<script language="JavaScript1.2">mmLoadMenus();</script>
<table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><table width="954" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td align="center" valign="top"><img src="images/ctl_con_logo4.png" width="954" height="324" /></td>
      </tr>
      <tr>
        <td align="left" valign="top"><table width="954" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="35" align="left" valign="top"><img src="images/nav_blank.gif" width="35" height="31" /></td>
            <td width="187" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onclick="logoutUser($session_id,$staff_id);" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image58','','images/Logout_white.jpg',1)"><img src="images/Logout_blue.jpg" name="Image58" width="113" height="29" border="0" id="Image58" /></a></td>
            <td width="311" align="left" valign="top"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','images/Sub_nav_about_on.gif',1)"> <img src="images/Sub_nav_about_off.gif" name="Image29" width="311" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>            		
			<td width="177" align="left" valign="top" background="images/nav_blank.gif"><a href="#" onClick="document.lead.action='faqs.cgi';document.lead.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','images/Sub_nav_faq_on.gif',1)"> <img src="images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a></td>
            <td width="244" align="left" valign="top" background="images/nav_blank.gif" colspan=2><a href="#" onClick="document.lead.action='contact.cgi';document.lead.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','images/Sub_nav_contact_on.gif',1)"> <img src="images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a></td>           
          </tr>
        </table></td>
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
                <td align="left" valign="top" class="BlueTitles">WELCOME, $name </td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td width="913" height="376" align="left" valign="top" background="images/LoggedInback.gif">
              <table width="900" border="0" cellspacing="1" cellpadding="1">
                <tr>
                  <td width="10" align="left" valign="top">&nbsp;</td>
                  <td align="left" valign="top"><table width="790" border="0" cellspacing="0" cellpadding="0">

                    <tr>
                      <td>&nbsp;</td>
                      <td>&nbsp;</td>
                    </tr>
													<! -- Side Table View --> 
                    <tr>
                      <td width="203" align="left" valign="top"><table width="195" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td align="left" valign="top"><img src="images/SubmitNav_top.gif" width="195" height="22" /></td>
                        </tr>
                        <tr>                          
						  <td align="left" valign="top"><a href="#" onclick="document.lead.action='graf_submitreferral.cgi';document.lead.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image15','','images/SubmitNav1_top_on.gif',1)"><img src="images/SubmitNav1_top_off.gif" name="Image15" width="195" height="28" border="0" id="Image15" /></a></td>
                        </tr>
						
						
                        <tr>
                          <td align="left" valign="top"><a href="#" onclick="document.lead.action='graf_leadchk.cgi';document.lead.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image16','','images/SubmitNav2_top_on.gif',1)"><img src="images/SubmitNav2_top_off.gif" name="Image16" width="195" height="33" border="0" id="Image16" /></a></td>
                        </tr>
						<!--
                        <tr>
                          <td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('http://www.qwestreward.com','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image17','','images/SubmitNav3_top_on.gif',1)"><img src="images/SubmitNav3_top_off.gif" name="Image17" width="195" height="41" border="0" id="Image17" /></a></td>
                        </tr>
                        <tr>
                          <td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('http://www.qwestreward.com','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image18','','images/SubmitNav4_top_on.gif',1)"><img src="images/SubmitNav4_top_off.gif" name="Image18" width="195" height="45" border="0" id="Image18" /></a></td>
                        </tr>
						-->
<tr>
<td align="left" valign="top"><a href="#" onClick="document.lead.action='graf_visastatement.cgi';document.lead.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image22','','images/SubmitNav7_top_on2.gif',1)"><img src="images/SubmitNav7_top_off2.gif" name="Image22" width="195" height="27" border="0" id="Image22" /></a></td>
</tr>
<tr>
<td align="left" valign="top"><a href="#" onClick="document.lead.action='graf_mypref.cgi';document.lead.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image21','','images/SubmitNav6_top_on12.gif',1)"><img src="images/SubmitNav6_top_off3.gif" name="Image21" width="195" height="27" border="0" id="Image21" /></a></td>
</tr>

<!--                        <tr>
			<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('http://qwest.groupo.com/include/processlogin.asp?btn=$agency_id&type=cust1   ','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image19','','images/SubmitNav5_top_on.gif',1)"><img src="images/SubmitNav5_top_off.gif" name="Image19" width="195" height="27" border="0" id="Image19" /></a></td>
                        </tr> -->
                        <tr>
                          <td align="left" valign="top"><img src="images/SubmitNav_bot.gif" width="195" height="22" /></td>
                        </tr>
                      </table></td>
                      <td width="587" align="left" valign="top"><span class="BIGBoxTitles">Thank you, $fname for submitting a referral!<br>
							</span>
							<br>
							<span class="subTitles"> $msg </span></td>
                    </tr>
                  </table>
                  </td>
                </tr>
              </table></td>
          </tr>
          <tr>
            <td align="left" valign="middle">&nbsp;</td>
          </tr>
          <tr>
            <td align="left" valign="top">&nbsp;</td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td><img src="images/bottombuffer.gif" width="954" height="15" /></td>
      </tr>
      <tr>
        <td width="954" height="35" align="center" valign="middle" background="images/bottom_green.gif"><table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
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
$myDB->disconnect();
undef &getrouting_sql;
undef &getproductlist;
###########################################################################################################
sub do_submit {

	my $hs = HTML::Strip->new();
	
	my $cust_type = EscQuote( $hs->parse($cgi->param('cust_type')) );
	my $prod_int  = EscQuote( $hs->parse($cgi->param('prod_int')) );
	my $lead_name = EscQuote( $hs->parse($cgi->param('biz_cont_name')) );
	my $phone1 = EscQuote( $hs->parse($cgi->param('main_btn1')) ).EscQuote( $hs->parse($cgi->param('main_btn2')) ).EscQuote( $hs->parse($cgi->param('main_btn3')) );

	my $phone2 = EscQuote( $hs->parse($cgi->param('lead_phone1')) ).EscQuote( $hs->parse($cgi->param('lead_phone2')) ).EscQuote( $hs->parse($cgi->param('lead_phone3')) );
	my $time_to_call = EscQuote( $hs->parse($cgi->param('time_to_call')) );
	my $lp_notes = EscQuote( $hs->parse($cgi->param('lp_notes')) );
	my $lead_state =  EscQuote( $hs->parse($cgi->param('lead_state')) );
    my $contact_permission = $cgi->param('contact_permission');

	my $lead_address = EscQuote( $hs->parse($cgi->param('lead_address')) )||'';
	my $lead_address2 = EscQuote( $hs->parse($cgi->param('lead_address2')) )||'';
	my $lead_city = EscQuote( $hs->parse($cgi->param('lead_city')) )||'';
	my $lead_zip = EscQuote( $hs->parse($cgi->param('lead_zip')) )||'';
    # following is copy over from b2b
	my $source=1;
    my $mainbtn = $phone1;
       my ($validated, $mainbtn, $duplicate_lead, $sql) = check_mainbtn($mainbtn, 154, 649, $myDB );
	   #print "check_mainbtn : $validated, $mainbtn, $duplicate_lead, $sql";
        if ( $validated == 0 ) {
print<<"EOF";
<script language='javascript'>
    window.alert('A referral $duplicate_lead on this Billing Telephone Number $mainbtn has already been placed and is still in an open status. Duplicate referral can not be placed until all open referrals for this number are closed. If you have any questions please call 1 866-968-2261');
        window.location("graf_submitreferral.cgi");
</script>
EOF

$msg = "  A referral $duplicate_lead on this Billing Telephone Number $mainbtn has already been placed and is still in an open status. Duplicate referral can not be placed until all open referrals for this number are closed. If you have any questions please call 1 866-968-2261
        <br><br>";

        }else{




# figure out values based on info that came in
	my $lead_group = 55 ;
	if ($cust_type eq 'con') {
		$lead_group = 56 ;
	}

	my $class1;
	my $class2;
	my $prod_interest;
	my $have_interest = 1;
	if ($prod_int eq 'BRD' ) {
		if ( $cust_type eq 'con'){
			$class1 = " and class1 = 'Residential' ";
			$class2 = " and class2 = 'High-Speed Internet Service' ";
			$prod_interest =  'High-Speed Internet Service' ;
		}
		else {
			$class1 = " and class1 = 'Business' ";
			$class2 = " and class2 = 'High-Speed Internet Service' ";
			$prod_interest = 'High-Speed Internet Service' ;
		}
	}
	elsif ($prod_int eq 'DTV') {
		if ($cust_type eq 'con'){
			$class1 = " and class1 = 'Residential' ";
			$class2 = " and class2 = 'Digital TV Service' ";
			$prod_interest = 'Digital TV Service' ;
		}
		else {
			$class1 = " and class1 = 'Business' ";
			$class2 = " and class2 = 'Digital TV Service' ";
			$prod_interest = 'Digital TV Service' ;
		}
	}
	elsif ($prod_int eq 'WRL') {
		if ($cust_type eq 'con'){
			$class1 = " and class1 = 'Residential' ";
			$class2 = " and class2 = 'Wireless Service' ";
			$prod_interest =  'Wireless Service';
		}
		else {
			$class1 = " and class1 = 'Business' ";
			$class2 = " and class2 = 'Wireless Service' ";
			$prod_interest = 'Wireless Service' ;
		}
	}
	elsif ($prod_int eq 'DIV') {
		if ($cust_type eq 'con'){
			$class1 = " and class1 = 'Residential' ";
			$class2 = " and class2 = 'Digital Voice: Local & Long Distance Service' ";
			$prod_interest = 'Digital Voice: Local & Long Distance Service' ;
		}
		else {
			$class1 = " and class1 = 'Business' ";
			$class2 = " and class2 = 'Digital Voice: Local & Long Distance Service' ";
			$prod_interest =  'Digital Voice: Local & Long Distance Service' ;
		}
	}
	else {
		$have_interest = 0;
	}

	my @product;
	if ( $have_interest == 1) {
		my $prod_sql = " select prod.prod_id from prod with (nolock)
			where prod_id in
			(select prod_id from fund_prod with (nolock) where fund_id = ?)
			and ProdIsActive = 1
			$class1
			$class2 ";
			
			
			my $success = eval {
				my $sth = $myDB->prepare($prod_sql) or die $myDB->errstr;
				$sth->{PrintError} = 0;
				$sth->execute($fund_id) or die $sth->errstr;
				
				while (my $prod_data = $sth->fetchrow_hashref()){
					push @product, $prod_data->{prod_id};
				}
				$sth->finish();
			};
			unless($success) {
				DBInterface::writelog('graf07',"$thisfile", $@ );
			}
	}

#post submission, insert records, route and print confirmation

            $sql = "insert into lp_lead (created_date, created_by, agency_id, lead_name, lead_company_name,
	    lead_phone, lead_email, lead_address,lead_address2,lead_city, lead_state, lead_zip, btn_id, main_btn,
        client_id,lp_changed_by, program_id,  fund_id, warm_xfer, lead_group, source_id, lp_region_id, contact_permission)
        values (getdate(), $staff_id, $agency_id , ltrim('$lead_name'), '',
          '$phone1','', rtrim('$lead_address'), rtrim('$lead_address2'), rtrim('$lead_city'),'$lead_state',  rtrim('$lead_zip'), '$phone1',  '$phone1',
       50, $staff_id,154, 649, 0, $lead_group, $source, 5, $contact_permission)";

			my $lead_id;
			try {
					my $sth = $myDB->prepare($sql);
					$sth->execute() or die $sth->errstr;
					my $data = $sth->fetchrow_hashref();
					$lead_id = $data->{lp_lead_id};
					$sth->finish();
				}
			catch {
				DBInterface::writelog('graf07',"$thisfile", $_ );
			};	
				
            ###################################################
            # extra optional fields
           # my $phone2 =         EscQuote($cgi->param('mobile_no'));
            my $best_contact_time = ''; #EscQuote($cgi->param('best_contact_time'));
            my $best_contact_date = ''; #EscQuote($cgi->param('best_contact_date'));
            my $lead_source =       EscQuote( $hs->parse($cgi->param('lead_source')) );
            #3my $local_service =     EscQuote($cgi->param('local_service'));
            my $sales_center =     '' ;# EscQuote($cgi->param('sales_center'));
            my $cust_type = $lead_group == 55? "Business" : "Consumer/Residential";
            my $referral_source = 'other'; # Dont leave it blank
            my $event_id = $cgi->param('event_id')||0;
			
			$hs->eof;

            (my $server_name = lc($cgi->server_name()) || 'unknown_154isr_154_649_'.$agency_id.'_'.$lead_id) =~ s/^www\.// ;

            $sql = "insert into lkup_qwest_opts (lp_lead_id, campaign_id, mobile_no, cust_type, best_contact_time,
                    lead_source,  vccustom1, server_name, sales_center, vccustom2,
                    referral_source)
                    values($lead_id, $event_id, '$phone2', '$cust_type', '$time_to_call',
                    '$lead_source',  '', '$server_name','$sales_center','',
                    '$referral_source' )";

			#if ($myDB->Sql($sql)) {
			# $myDB->DumpError();
            # print "<br>$sql<br>";
            ##################################################
			#}
			
			my $sth = $myDB->prepare($sql);
            if (! $sth->execute()){
				DBInterface::writelog('graf07',"$thisfile", $sth->errstr );
            }
			
			
			$sql = "insert into lp_lead_history (lp_lead_id, action, staff_id, history_date, source_id, user_ip)
                    values ( $lead_id, 'Referral created', $staff_id, getdate(), 1 , '$ENV{REMOTE_HOST}')";
            
			try {
				my $sth = $myDB->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('graf07',"$thisfile", $_ );
			};
			
#print<<"EOF";
#hist insert <pre>$sql</pre><br>
#EOF
#     new           convert(varchar,getdate())+': $main::session{name}'+char(13)+char(10)+'$comment'+char(13)+char(10)+'----------'+char(13)+char(10)+'$notes',
# old 				convert(varchar,getdate())+': ".$main::session{name} . "'+char(13)+char(10)+'" .$class2."'+char(13)+char(10)+'" . delim_return($cgi->param('lp_notes')) . "'+char(13)+char(10)+'----------'+char(13)+char(10)+isnull(lp_notes,''), lead_status_change_dt = getdate() where lp_lead_id = " . $lead_id;

$class2 = "Product types interested: $prod_interest";
          #  if ( length($cgi->param('lp_notes')) > 0 ) {
             my   $lp_note_sql = " update lp_lead set original_note =
				 convert(varchar,getdate())+': $name'+char(13)+char(10)+'$lp_notes'+char(13)+char(10)+'----------'+char(13)+char(10)+'$class2',
				lead_status_change_dt = getdate() where lp_lead_id = " . $lead_id;
				
				               
				try {
					my $sth = $myDB->prepare($lp_note_sql);
					$sth->execute() or die $sth->errstr;
					$sth->finish();
				}
				catch {
					DBInterface::writelog('graf07',"$thisfile", $_ );
				};
				

                $lp_note_sql = " update lp_lead set lp_notes =
				 convert(varchar,getdate())+': $main::session{name}'+char(13)+char(10)+'$lp_notes'+char(13)+char(10)+'----------'+char(13)+char(10)+'$class2',
				lead_status_change_dt = getdate() where lp_lead_id = " . $lead_id;
               
			   try {
				   my $sth = $myDB->prepare($lp_note_sql);
				   $sth->execute() or die $sth->errstr;
				   $sth->finish();
			   }
			   catch {
					DBInterface::writelog('graf07',"$thisfile", $_ );
				};
          #  }
# prod interest set at the begining
#            my %product = $cgi->param('product');
 #           foreach my $prod (@product){
 #               $sql = "insert into lkup_lead_product_interest (prod_id, lp_lead_id)
 #                       values ($prod, $lead_id)";
 #               $myDB->Sql($sql);
#
#            }
            my $prod_group = $lead_group;
                ###############################
	  my $language_id = 1 ; # $cgi->param('language_id') new form does not have an option
                # get isr id
                my $isrsql = get_routing_sql( $lead_id, $prod_group, $language_id, $myDB);

				my ($new_isr_id, $region);
				try {
					my $sth = $myDB->prepare($isrsql);
					$sth->execute() or die $sth->errstr;
					my $data = $sth->fetchrow_hashref();
					
					$new_isr_id = $data->{isr_id};
					$region = $data->{lp_region_id} || 5;
					$sth->finish();
				}
				catch {
					DBInterface::writelog('graf07',"$thisfile", $_ );
				};

                $sql = "update lp_lead set lp_isr_id = $new_isr_id, lp_region_id = $region
                        where lp_lead_id = $lead_id";
                
				try {
					my $sth = $myDB->prepare($sql);
					$sth->execute();
					$sth->finish();
				}
				catch {
					DBInterface::writelog('graf07',"$thisfile", $_ );
				};

$msg .= "  Thank you for submitting your referral. <br>  The information you provided has been routed to the
            appropriate CenturyLink service rep and your customer will be contacted within 2 business days.
		<br><br>
            Your reference number for this submission is $lead_id ";

        }#end validate
return $msg;
}
############################################################################
#   get_routing_sql
############################################################################
sub get_routing_sql{
    my ( $lead_id, $prod_group_id, $language_id, $myDB) = @_;

    my $sql;
    my $sql_1 = "select dbo.func_GetCust_custtype(agency_id)as vendor_type from lp_lead with(nolock) where lp_lead_id = ?";
    
	my $data;
	try {
		my $sth = $myDB->prepare($sql_1);
		$sth->execute($lead_id) or die $sth->errstr;
		$data = $sth->fetchrow_hashref();
		$sth->finish();
	}
	catch {
		DBInterface::writelog('graf07',"$thisfile", $_ );
	};
	   
    my $region = ($data->{vendor_type} == 241 || $data->{vendor_type} == 364) ? 35 : 5;  #vendor by-pass to tcim reps
    
    if ( $prod_group_id == 56 ) {
        if ( $region == 35 ) {
            $sql = "select 171968 as isr_id, 0, 35 as lp_region_id";
        }else{
            $sql = "select 318050 as isr_id, 0, 5 as lp_region_id";
        }
    }elsif ($prod_group_id == 55) {

            $sql = "exec splp_yc_bizroute $lead_id";
			$sql = "select 411887 as isr_id, 0, 5 as lp_region_id";
    }
	
    return $sql;
}

############################################################################
sub check_mainbtn      #08/01/08 9:04:AM
############################################################################
 {

    my $mainbtn = shift;
    my $program_id = shift;
    my $fund_id = shift;
    my $myDB = shift;           # passed around
    my $sql;
    my $validated = 0;
    my $duplicate_lead = 0;

    # Save original BTN to return
    my $origbtn = $mainbtn;

    # Forget trim, eat everything except digits
    $mainbtn =~ s/\D+//g;  # Then 'unknown' or 'new service' passes as '' case

    # Return a cleaned up BTN if numbers in it, else original
    my $clean_btn = $origbtn =~ /\d/ ? $mainbtn : $origbtn;

    if ( $mainbtn eq ''                ||   # text was stripped
        $mainbtn =~ /^999+$/          ||   # all nines (at least 3)
        $mainbtn =~ /^\d\d\d999+$/    ){   # areacode then all nines

        $validated = 1;
    }
    else{


        # The BTN has numbers in it    Check it out
        $sql = "select lp_lead.lp_lead_id
                from lp_lead with(nolock)
                where dbo.fnCleanPhone10(main_btn) = '$mainbtn'
                    and isnull(lead_status_id,0) < 50 and program_id = $program_id
                    and fund_id = $fund_id
                    and lead_name <> 'test'
                   and client_id = 50";
		
		my $data;
		try {
			my $sth = $myDB->prepare($sql);
			$sth->execute() or die $sth->errstr;
			$data = $sth->fetchrow_hashref();
			$sth->finish();
		}
		catch {
			DBInterface::writelog('graf07',"$thisfile", $_ );
		};
        
        if ( $data->{'lp_lead_id'} ) {
            $duplicate_lead = $data->{'lp_lead_id'};
        }

        if ( $duplicate_lead ) {
            $validated = 0;
        }
        else{
            # Not a duplicate
            $validated = 1;
        }
		
    }
    return ($validated, $clean_btn, $duplicate_lead, $sql);
}


=head
            my $contact_name = EscQuote($main::cgi{contact_name});
            my $lead_phone = EscQuote($main::cgi{contact_phone});
            my $lead_email = EscQuote($main::cgi{lead_email});
            my $company_name = EscQuote($main::cgi{company_name});
            my $lead_state = $main::cgi{company_state};
            my $lead_address1 = EscQuote($main::cgi{company_address1});
            my $lead_address2 = EscQuote($main::cgi{company_address2});
            my $lead_city = EscQuote($main::cgi{company_city});
            my $main_btn  = EscQuote($main::cgi{main_btn});
            my $btn_id = EscQuote($main::cgi{btn_id}); #employee phone number
            my $language_id = $main::cgi{language_id};
            my $source=1;
            my $i_am_referring = $main::cgi{i_am_referring} || ''; # vccustom2

=cut
