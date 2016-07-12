
# copied from youcan07/landing.cgi
use strict;       # Require all variables to be scoped explicitly

use CGI::Carp qw/ fatalsToBrowser /;
use HTML::Strip;
my $hs = HTML::Strip->new();
#use cgi::cookie;
use DBInterface;
use CGI qw(:standard);
my $cgi = CGI->new();

my $server;
my $HOST = $ENV{HTTP_HOST};

if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
#else{
#    $server = "d:/xroot";
#}
$server = "D:/centurylinkyoucan";
require "$server/cgi-bin/init.cgi";
require "$server/cgi-bin/delimeter.cgi";



my $myDB = DBInterface->new();
my $btn = $hs->parse($cgi->param('btn')) ;
my $from_email= $hs->parse($cgi->param('from_email')) ;
my $coupon= $hs->parse($cgi->param('coupon')) ||0 ;
my $email= $hs->parse($cgi->param('email')) || 0 ;
my $tomail = $hs->parse($cgi->param('tomail')) || 0 ;
my $action = $hs->parse($cgi->param('action')) || 0 ;
my $to_name = $hs->parse($cgi->param('to_name')) || '' ;
my $from_name = $hs->parse($cgi->param('from_name')) || '' ;

$from_email =~ s/\|~\|/@/g;


#print "from mail".$from_email."btn".$btn;

my $thisfile = "promocode.cgi";

my $ret='under construction';
my $IS_TEST = 1;

my  $PAGETITLE = 'CenturyLink-Pass It On Rewards';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'http://www.centurylink.com/static/Styles/main.css',
    );
#print $header;
#print "Content-type:text/html\n\n";
print<<"EOF";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
	<title>$PAGETITLE</title>
	<meta http-equiv="Content-language" content="en-US">
	<meta http-equiv="Content-type" content="text/html; charset=UTF-8">
	
	<link rel="stylesheet" href="http://www.centurylink.com/static/Styles/support.css" type="text/css" media="screen,print">
	<link rel="stylesheet" href="http://www.centurylink.com/static/Styles/main.css" type="text/css" media="screen,print">
	<link rel="stylesheet" href="http://www.centurylink.com/static/Styles/menu.css" type="text/css" media="screen,print">

		<script  type="text/javascript" src="validate_promo.js"></script>
</head>

<body>

<div id="main">
<!-- Main Content -->

EOF
if ($coupon==1 && $action == 0) {
my $lead = insert_lead ( $from_email, $btn, $email, $coupon, $myDB );
my $coup_html = get_html( $lead);
print<<"EOF";
$coup_html
EOF
}
if ($email==1 && $action == 0)  {
print<<"EOF";
<div id="content">
	<div class="body">
	<table width="100%" id="myAccount" border="0">
		<tr>
			<td>
			<p><b><u>Send Email to Friends and Family</u>.</b>
	<br>
		<form action="$thisfile" method="post" name="frm">
		<input type="hidden" name="action" value="$action">
		<input type="hidden" name="email" value="$email">
		<input type="hidden" name="coupon" value="$coupon">
		<input type="hidden" name="from_email" value="$from_email">
		<input type="hidden" name="btn" value="$btn">

	<p> Your Name <br> <input type="text" name="from_name" maxLength="25"></p>
	<p> Recipients Name <br> <input type="text" name="to_name" maxLength="25"></p>
<p> Recipient&rsquo;s Email <br> <input type="text" name="tomail" maxLength="35"></p>
<br/>
<input type="button" src="http://www.centurylink.com/static/Images/Buttons/btnSubmit.gif" border="0" width="86" height="29" alt="Submit" value="Submit" name="sender" onclick="sendemail()"/>
</form>
		</td>
		</tr>
	</table>
	</div>
</div>

<!-- End Main Content -->
</div>
	

EOF
}
if ($email==1 && $action == 1)  {
	$ret = sendemail ($tomail, $from_email, $btn, $email, $coupon, $to_name, $from_name, $myDB ) ;  
	
	#print  "$tomail, $from_email, $btn, $email, $coupon, $to_name, $from_name, $myDB";
	
print<<"EOF";
<div id="content">
		<div class="body">
	<table width="100%" id="myAccount" border="0">
		<tr>
			<td>

			<p>$ret</p>
		</td>
		</tr>
	</table>
</div>

<!-- End Main Content -->
</div>

EOF
}
print<<"EOF";
<script language="JavaScript">var s_accountOverride ='qwestfull'</script>

<script language="JavaScript" type="text/javascript" src="http://www.qwest.com/global/includes/s_h_code.js"></script>

<!-- SiteCatalyst code version: H.21.
Copyright 1996-2010 Adobe, Inc. All Rights Reserved
More info available at http://www.omniture.com -->
<script language="JavaScript" type="text/javascript"><!--
/* You may give each page an identifying name, server, and channel on
the next lines. */
s.pageName='rsd|shop|referafriend'
/************* DO NOT ALTER ANYTHING BELOW THIS LINE ! **************/
var s_code=s.t();if(s_code)document.write(s_code)//--></script>

<!-- End SiteCatalyst code version: H.21. -->
</body></html> 

EOF
$myDB->disconnect;

sub  sendemail {
	my ($tomail, $from_email, $btn, $email, $coupon, $to_name, $from_name, $myDB ) = @_;
    my $ccimail_id = 0;
	my $lead = 0;#;
	my $ret = 'There was an error sending the mail.';
	my $bcc = '';#'archanak@ccionline.biz';
	my $mail_sql;
#--

my $dnc_email="select 0 as cnt_dnc union select count(dnc_id) as cnt_dnc from do_not_contact with (nolock) where email = '$tomail' order by 1 desc";
	my $sth = $myDB->prepare($dnc_email);
	$sth->execute();
	if($sth->err)
	{	

		DBInterface::writelog("graf07",$thisfile,$sth->errstr);

	}
	my $data = $sth->fetchrow_hashref();
	my $cnt_dnc = $data->{cnt_dnc};



if ($cnt_dnc > 0) {
$ret = 'The Recipient email is on our do not contact list, so your email could not be processed';
}
#--
if ($cnt_dnc == 0 ) {
	if ($ccimail_id ==0 && $lead == 0 ) {
			$lead = insert_lead ( $from_email, $btn, $email, $coupon, $myDB );

	}
		my $body = getbody ($lead, $to_name, $from_name);
		my $subject = "Your friend wanted to share a deal with you.";

	# entry into lp_Lead
	 $mail_sql = "insert into ccimail (client_id, program_id, date_created, lp_lead_id, staff_id, subject, tofield, bccfield, fromfield, longbody, ctype)
values (50, 154, GETDATE(), $lead, 265980, '$subject','$tomail','$bcc','$from_email','$body','text/html'  ) ";

	my $sth = $myDB->prepare($mail_sql);
	$sth->execute();
	if($sth->err)
	{	

		DBInterface::writelog("graf07",$thisfile,$sth->errstr);

	}
	my $data = $sth->fetchrow_hashref();
	$ccimail_id = $data->{ccimail_id};
	#print "here".$ccimail_id;exit();

if ($ccimail_id > 0) {
	$ret = "Thank you! <br>	Your email to $to_name has been sent. <br>Please have your friend call us at 1 866-511-6683. ";
}
}

	return $ret;
	#return $mail_sql;
}
sub insert_lead {
	
	my ( $from_email, $btn, $email, $coupon, $myDB ) = @_;
	# staging cust_id = 245189
	# staging staff_id = 265980
	# coop cust_id = 246946
	# coop staff_id = 268105
	my $hist_note = '';
	my 	$lp_note = '';
	if ($email==1) {
		$hist_note = 'GRAF Generic: Email Code';
	 	$lp_note = 'GRAF Generic (Email): '.$btn.', '.$from_email;
	}
	if ($coupon==1) {
		$hist_note = 'GRAF Generic: Coupon Code';
	 	$lp_note = 'GRAF Generic (Coupon): '.$btn.', '.$from_email;
	}

	my $sql = "insert into lp_lead (created_date, agency_id, client_id,  program_id, fund_id, main_btn_area, 
contact_permission, language_id, source_id, lead_group, original_note, lp_notes, lead_status_change_dt, lp_region_id)
values (GETDATE(),246946, 50, 154, 649, '$btn', 1,1,1,56,convert(varchar,getdate())+'$lp_note',
convert(varchar,getdate())+':$lp_note',
GETDATE(),5 ) ";

	my $sth = $myDB->prepare($sql);
	$sth->execute();
	if($sth->err)
	{	

		DBInterface::writelog("graf07",$thisfile,$sth->errstr);

	}
	my $data = $sth->fetchrow_hashref();
    my $lead_id = $data->{lp_lead_id};


 $sql = " insert into lkup_qwest_opts (lp_lead_id, cust_type, server_name, vccustom1)
 values ($lead_id, 'Residential','centurylinkpassitonrewards.com', '$from_email')";

        	my $sth = $myDB->prepare($sql);
			$sth->execute();
	if($sth->err)
	{	

		DBInterface::writelog("graf07",$thisfile,$sth->errstr);

	}

$sql = "insert into lp_lead_history (lp_lead_id, action, staff_id, history_date, source_id)
            values ($lead_id,'Referral created- $hist_note ', 268105 ,getdate(), 1)";
        
			my $sth = $myDB->prepare($sql);
			$sth->execute();
	if($sth->err)
	{	

		DBInterface::writelog("graf07",$thisfile,$sth->errstr);

	}
			return $lead_id;

}

sub get_html {
	my ( $lead) = @_;
my $str = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Pass-It-On Rewards and Get &#36;50 and great service!</title>
<style type="text/css">
body { font-family: Arial, Helvetica, sans-serif;	font-size: 24px; }
h1 { text-align:center; font-size:36pt; color: #00853F; }
h2 { text-align:center; font-size:24pt; color: #ff6319; margin-top:-30px; }h3 { text-align:center; font-size:24pt; }
.greentitle { 	font-size: 36px; } .subtitle{ font-size: 24px; font-weight:bold; } 
.legal{ font-size:9px; 	color:#999: }
</style> </head> <body>
<div style="text-align:right;width:730px;margin:20px 0 0 50px; padding:0 20px 20px 20px; border-style:dotted"><a href="javascript:window.print()"><img src="images/btnPrint.gif" width="60" height="29" alt="print button"/></a>
<div align="left" > <img src="images/ctl_con2.jpg" alt="CenturyLink "><br/>
<h1>Pass-It-On Rewards</h1><br> <h2>Get &#36;50 and great service!</h2><br>
Use the referral code below to receive a &#36;50 bill credit for purchasing CenturyLink High-Speed Internet&reg; or Prism TV. Offer good for a limited time.
<br><h3>Call 1-866-511-6683 to sign up today!</h3><center>Use Referral Code: ';
$str.=$lead;
$str.='<center><p class="legal" align="center">Terms and Conditions apply.  Call or visit centurylinkpassitonrewards.com  for details. &copy; <script type="text/javascript">document.write(new Date().getFullYear());</script> CenturyLink, Inc. All Rights Reserved.<br/> The CenturyLink mark, pathways logo, Qwest mark, Q lightpath logo and certain CenturyLink product names are the property of CenturyLink, Inc.  </p>
</body>
</html>
';

return $str;
	
}

sub getbody {
	my ($lead, $to_name, $from_name) = @_; 
my $str = qq [<html><body><center><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
	<tr><td align="center"><table width="617" border="0" align="center" cellpadding="0" cellspacing="0">
	<tr><td><table width="617" border="0" cellspacing="0" cellpadding="0">
<tr><td width="9"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="9" height="1"></td>
<td><table width="604" border="0" cellspacing="0" cellpadding="0">
<tr><td style="font-family:Tahoma, Geneva, sans-serif;font-size:14px;line-height:17px;color:#8cc63f">Add CenturyLink and earn a &#36;50 credit! Call today 1-866-511-6683. 
</td></tr>
<tr><td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="3"></td></tr>
<tr><td align="left" style="font-family:Tahoma, Geneva, sans-serif; font-size:10px; line-height:15px; color:#9a9090;">Trouble viewing this message? <a href="#">Click here</a> to view this message as a Web page.</td></tr>
</table></td></tr></table></td></tr>
<tr><td><img src="http://www.centurylinkpassitonrewards.com/graf07/images/ctl_con2.jpg" alt="CenturyLink.&#153;" width="244" height="82" style="display:block"></td></tr>
<tr><td><table width="617" border="0" cellspacing="0" cellpadding="0">
<tr><td width="13"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_05.jpg" width="13" height="117"></td>
<td><table width="604" border="0" cellspacing="0" cellpadding="0">
<tr><td align="left" style="font-family:Arial, Helvetica, sans-serif;color:#8cc63f;font-size:30px;line-height:30px;"><b>Hey ];
$str.=$to_name;
$str.= qq[, want to save on Internet and/or television service?</b></td></tr>
<tr>
	<td align="left" style="font-family:Arial, Helvetica, sans-serif;font-size:16px;line-height:22px;color:#666666">
	I thought you might be interested in a great High-Speed Internet and television promotion CenturyLink is currently offering. 
	Sign up today and you&rsquo;ll receive an additional &#36;50 bill credit. Just call and  <b><span style="color:#8cc63f;">use the referral code below.</span></b>
	</td>
</tr>
</table>
</td>
</tr>
</table>
</td></tr>
<tr><td><table width="617" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="13"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_07.jpg" width="13" height="107"></td>
<td bgcolor="#8cc63f"><table width="595" border="0" cellspacing="0" cellpadding="0"><tr>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_08.jpg" width="595" height="24"></td></tr>
<tr><td><table width="595" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="43"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_10.jpg" width="43" height="83"></td>
<td width="229" valign="top"><table width="229" border="0" cellspacing="0" cellpadding="0">
<tr>
<td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:18px;line-height:24px;"><b>Call. Sign up. Save.</b></td></tr>
<tr><td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:30px;line-height:33px;">1 866-511-6683</td></tr></table></td>
<td width="76"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_12.jpg" width="76" height="83"></td>
<td><table width="247" border="0" cellspacing="0" cellpadding="0"><tr><td>
<table width="247" border="0" cellspacing="0" cellpadding="0"><tr><td valign="top"><table width="193" border="0" cellspacing="0" cellpadding="0">
<tr><td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:12px;line-height:15px;">Use this referral code:</td>
</tr><tr><td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:26px;line-height:29px;"> ];
$str.= $lead;
$str.= qq[ </td></tr><tr><td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:12px;line-height:15px;">Referred by:  ];
$str.=$from_name;
$str.= qq[</td></tr></table></td>
<td width="54"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_14.jpg" width="54" height="63"></td></tr></table></td></tr>
<tr><td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_15.jpg" width="247" height="20"></td></tr></table></td></tr></table></td>
</tr></table></td><td width="9"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_09.jpg" width="9" height="107"></td></tr>
</table></td></tr><tr><td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_16.jpg" width="617" height="26"></td>
</tr><tr><td><table width="617" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="281"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_17.jpg" width="281" height="186"></td>
<td valign="top"><table width="324" border="0" cellspacing="0" cellpadding="0"><tr>

<td>CenturyLink gives you the best in service and products:</td></tr>

<tr><td valign="top"><table width="324" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="4" valign="top" style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">&bull;</td>
<td width="7"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="7" height="26"></td>
<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:13px;color:#666666">
	
High-Speed Internet with a variety of available speeds and offers, including our Price-Lock Guarantee.</td></tr>
<tr><td valign="top"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td></tr>
<tr><td valign="top" style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">&bull;</td>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="7" height="10"></td>
<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">
Internet plans with or without home phone service.</td></tr>


<tr><td valign="top"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td></tr>
<tr><td valign="top" style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">&bull;</td>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="7" height="10"></td>
<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">
Best in class television experiences with CenturyLink&reg; Prism&trade; TV 
	<span style="font-family:Arial, Helvetica, sans-serif;font-size:8px;line-height:8px;color:#666666">- available in select markets</span></td></tr>
<tr><td valign="top"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td></tr>
<tr>
	<td valign="top"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
	<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
	<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="4"></td>
</tr>
<tr>
	<td valign="top" style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">&nbsp;</td>
	<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="7" height="10"></td>
	<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">So don&rsquo;t wait, call and start saving today&#33;</td>
</tr>
</table>
	</td>
	</tr>
	<tr>
		<td><img src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf2_21.jpg" alt="CALL 1 866-511-6683!" width="324" height="28" style="display:block"></td>
	</tr>
	
	</table></td>
						<td width="12"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_19.jpg" width="12" height="186"></td>
					</tr>
				</table></td>
			</tr>
			<tr>
				<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_23.jpg" width="617" height="17"></td>
			</tr>
			<tr>
				<td><table width="617" border="0" cellspacing="0" cellpadding="0">
<tr><td width="13">&nbsp;</td>
<td style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;line-height:13px;">
	You are receiving this email via an associate of yours who is a current CenturyLink subscriber. 
		This one time use of your email information will not be used again unless you have authorized permission to do so otherwise.
Services and offers not available everywhere. CenturyLink may change or cancel services or substitute similar services at its sole discretion without notice. 
		Services require credit approval and deposit may be required. Additional restrictions apply. 
		<span style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;font-weight: bold;height:13px;">Terms and Conditions</span> – All products and services listed are governed by tariffs, terms of service, or terms and conditions posted at <a href="http://www.centurylink.com" target="_blank">www.centurylink.com</a>. 
		<span style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;font-weight: bold;height:13px;">CenturyLink Customer Referral Program (&ldquo;Program&rdquo;)</span> –Program is subject to change, without notice, and may vary by service area. 
		<span style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;font-weight: bold;height:13px;">CenturyLink reserves the right to add, change or remove any restrictions of the Program, discontinue the Program at any time without notice or cancel future
		eligible redemptions if Program is terminated.</span>
All Program participants must maintain a qualifying CenturyLink account in good credit standing to receive all applicable Program invoice credits, as allocated below.
		Customers cannot refer themselves or refer their own accounts.  CenturyLink employees and their immediate family members are not eligible to refer or
		participate in Program.  Business accounts are not eligible for participation in the Program.  Additional restrictions may apply.  
		<span style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;font-weight: bold;height:13px;">Qualifying Services</span> -- CenturyLink&reg; High-Speed Internet service and/or Prism&trade; TV Package (each a &ldquo;Service&rdquo;) are eligible for referral within the Program.
		Service is not available everywhere. CenturyLink may change, cancel or substitute Service, or vary them by service area, at its sole discretion without notice.  All products and services listed are governed by tariffs, terms of service, or terms and conditions posted at <a href="http://www.centurylink.com" target="_blank">www.centurylink.com</a>.<span style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;font-weight: bold;height:13px;">
		Program</span> – In order to participate in the Program, the Referring Customer must have an active residential CenturyLink account in one or more CenturyLink
		local service areas.  Referring Customer and Referred Customer will each receive a one-time &#36;50 invoice credit when a new CenturyLink Referred Customer 
	subscribes to a Service.Referred customer is required to keep product for a minimum of 30 days.  Credits will appear on Referred and Referring Customer bills within 90 days from the Referred Customer&rsquo;s order date.  
		The Referred Customer and the Referring Customer are only entitled only to one (1) invoice credit per month.  Limit &#36;600 in Program invoice credits per
	calendar year for both Referred and Referring Customers. 
		<span style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;font-weight: bold;height:13px;">High-speed Internet</span> – Customers must accept High-Speed Internet Subscriber Agreement prior to using
		service. Download speeds will range from 85&#37; to 100&#37; of the listed download speeds due to conditions outside of network control, including customer
	location, websites accessed, Internet congestion and customer equipment.  
		<span style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;font-weight: bold;height:13px;">Consistent Speed Claim</span> – Claim is based on providing High-Speed Internet customers with 
		a dedicated, virtual-circuit connection between their homes and the CenturyLink central office.  
		<br> &copy; 2016 CenturyLink, Inc.  All Rights Reserved.   
  

</td>
<td width="9">&nbsp;</td></tr></table></td>
</tr></table></td>
</tr></table>
</center></body></html>];

return $str;

}