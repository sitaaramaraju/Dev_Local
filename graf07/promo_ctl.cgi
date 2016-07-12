
use strict;       # Require all variables to be scoped explicitly
#use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use HTML::Strip;
my $hs = HTML::Strip->new();
#use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
use DBInterface;




require "D:/centurylinkyoucan/cgi-bin/init.cgi";
require "D:/centurylinkyoucan/cgi-bin/delimeter.cgi";

my $myDB = DBInterface->new();
my $acct = $hs->parse($cgi->param('acct')) ;
my $from_email= $hs->parse($cgi->param('from_email')) ;
my $coupon= $hs->parse($cgi->param('coupon')) ||0 ;
my $email= $hs->parse($cgi->param('email')) || 0 ;
my $tomail = $hs->parse($cgi->param('tomail')) || 0 ;
my $action = $hs->parse($cgi->param('action')) || 0 ;
my $to_name = $hs->parse($cgi->param('to_name')) || '' ;
my $from_name = $hs->parse($cgi->param('from_name')) || '' ;
my $how_did_you_hear= $hs->parse($cgi->param('how_did_you_hear')) || '' ;

my $thisfile = "promo_ctl.cgi";

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
my $lead = insert_lead ( $from_email, $acct, $email, $coupon,$tomail, $how_did_you_hear, $myDB );

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
		<input type="hidden" name="how_did_you_hear" value="$how_did_you_hear">
		<input type="hidden" name="acct" value="$acct">

	<p> Your Name <br> <input type="text" name="from_name" maxLength="25"></p>
	<p> Your Email <br> <input type="text" name="from_email" maxLength="50"></p>
	<p> Recipients Name <br> <input type="text" name="to_name" maxLength="25"></p>
<p> Recipient&rsquo;s Email <br> <input type="text" name="tomail" maxLength="50"></p>
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
	$ret = sendemail ($tomail, $from_email, $acct, $email, $coupon, $to_name, $from_name, $myDB ) ; 
print<<"EOF";
<div id="content">
    <script type="text/javascript">
		 function loadForm(){
	  	window.location.replace("promo_ctl.cgi?email=1&acct=$acct&how_did_you_hear=$how_did_you_hear");
	   }
	  </script>
		<div class="body">
	<table width="100%" id="myAccount" border="0">
		<tr>
			<td>

			<p>$ret</p>
		</td>
		</tr>
		<tr>
		<td align="left">
		&nbsp; &nbsp; 
		<input type="button" src="http://www.centurylink.com/static/Images/Buttons/btnSubmit.gif" border="0" width="110" height="29" alt="Email Another Friend" value="Email Another Friend" name="loadform" onclick="loadForm();"/>
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
	my ($tomail, $from_email, $acct, $email, $coupon, $to_name, $from_name, $myDB ) = @_;
    my $ccimail_id = 0;
	my $lead = 0;#;
	my $ret = 'There was an error sending the mail.';
	my $bcc = '';#'archanak@ccionline.biz';
	my $mail_sql;
#--

my $dnc_email="select 0 as cnt_dnc union select count(dnc_id) as cnt_dnc from do_not_contact with (nolock) where email = '$tomail' order by 1 desc";
	my $sth = $myDB->prepare($dnc_email);
	$sth->execute() ;

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
			$lead = insert_lead ( $from_email, $acct, $email, $coupon,$tomail, $how_did_you_hear, $myDB )

	}
		my $body = getbody ($lead, $to_name, $from_name);
		my $subject = "Your friend wanted to share a deal with you.";

	# entry into lp_Lead
	 $mail_sql = "insert into ccimail (client_id, date_created, subject, tofield, bccfield, fromfield, longbody, ctype)
values (50, GETDATE(),'$subject','$tomail','$bcc','$from_email','$body','text/html'  ) ";

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
	$ret = "Thank you! <br>	Your email to $to_name has been sent. <br>Please have your friend call us at 1-866-511-6683. ";
}
}

	return $ret;
}
sub insert_lead {
#=x	
	my ( $from_email, $acct, $email, $coupon,$tomail, $how_did_you_hear, $myDB ) = @_;
	my $code_sent = substr($how_did_you_hear, 0, 1).$acct; 
	if ($how_did_you_hear eq "Telephone bill") {
		$code_sent = 'B'.$acct; 
	}

	my $sql = "insert into ctl_pior (cl_account_num, code_sent, email, coupon,to_email, from_email, date_created, how_did_hear)
				values ($acct, '$code_sent', $email,$coupon,'$tomail','$from_email',GETDATE(),'$how_did_you_hear')  ";
	#	print qq[ $sql ];
	
	
	my $sth = $myDB->prepare($sql);
	$sth->execute();
	if($sth->err)
	{

		DBInterface::writelog("graf07",$thisfile,$sth->errstr);

	}
	#my $data = $sth->fetchrow_hashref();
	#$pior_id = $data->{pior_id};
	#print "here".$pior_id;exit();
	


			return $code_sent;
#=cut
}


sub get_html {
	my ( $lead) = @_;
my $str = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Pass-It-On Rewards and Get an extra &#36;10 off for 6 months.</title>
<style type="text/css">
body { font-family: Arial, Helvetica, sans-serif;	font-size: 24px; }
h1 { text-align:center; font-size:36pt; color: #00853F; }
h2 { text-align:center; font-size:24pt; color: #ff6319; margin-top:-30px; }h3 { text-align:center; font-size:24pt; }
.greentitle { 	font-size: 36px; } .subtitle{ font-size: 24px; font-weight:bold; } 
.legal{ font-size:9px; 	color:#999: }
</style> </head> <body>
<div style="text-align:right;width:730px;margin:20px 0 0 50px; padding:0 20px 20px 20px; border-style:dotted"><a href="javascript:window.print()"><img src="images/btnPrint.gif" width="60" height="29" alt="print button"/></a>
<div align="left" > <img src="images/ctl_con2.jpg" alt="CenturyLink "><br/>
<h1>Pass-It-On Rewards</h1> <h2>Get an extra &#36;10 off for 6 months.</h2>
Use the referral code below to save on a CenturyLink product such as 
CenturyLink&#153;  Prism&#153; TV, CenturyLink&#153;  High-Speed Internet or DIRECTV&reg  service from CenturyLink. 
Offer good for a limited time.
<h3>Call 1-866-511-6683 to sign up today!</h3> Referral Code: ';
$str.=$lead;
$str.='<p class="legal" align="center">Terms and Conditions apply.  Call or visit centurylinkpassitonrewards.com for details. &copy; <script type="text/javascript">document.write(new Date().getFullYear());</script> CenturyLink, Inc. All Rights Reserved.<br/> The CenturyLink mark, pathways logo, Qwest mark, Q lightpath logo and certain CenturyLink product names are the property of CenturyLink, Inc.  </p>
</body>
</html>
';

return $str;
	
}

sub getbody {
	my ($lead, $to_name, $from_name) = @_; 
my $str = '<html><body><center><table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
	<tr><td align="center"><table width="617" border="0" align="center" cellpadding="0" cellspacing="0">
	<tr><td><table width="617" border="0" cellspacing="0" cellpadding="0">
<tr><td width="9"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="9" height="1"></td>
<td><table width="604" border="0" cellspacing="0" cellpadding="0">
<tr><td style="font-family:Tahoma, Geneva, sans-serif;font-size:14px;line-height:17px;color:#8cc63f">Add CenturyLink and earn a &#36;60 credit! Call today 1-866-511-6683. 
</td></tr>
<tr><td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="1" height="3"></td></tr>
<tr><td align="left" style="font-family:Tahoma, Geneva, sans-serif; font-size:10px; line-height:15px; color:#9a9090;">Trouble viewing this message? <a href="#">Click here</a> to view this message as a Web page.</td></tr>
</table></td></tr></table></td></tr>
<tr><td><img src="http://www.centurylinkpassitonrewards.com/graf07/images/ctl_con2.jpg" alt="CenturyLink.&#153;" width="244" height="82" style="display:block"></td></tr>
<tr><td><table width="617" border="0" cellspacing="0" cellpadding="0">
<tr><td width="13"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_05.jpg" width="13" height="117"></td>
<td><table width="604" border="0" cellspacing="0" cellpadding="0">
<tr><td align="left" style="font-family:Arial, Helvetica, sans-serif;color:#8cc63f;font-size:30px;line-height:30px;"><b>Hey ';
$str.=$to_name;
$str.=', want to save on Internet and/or television service??</b></td></tr><tr>
<td align="left" style="font-family:Arial, Helvetica, sans-serif;font-size:16px;line-height:22px;color:#666666">
I thought you might be interested in a great High-Speed Internet and television promotion CenturyLink is currently offering. 
Sign up today and you&rsquo;ll receive an additional &#36;10 bill credit for six months. 
Just call and <b><span style="color:#8cc63f;">use the referral code below!</span></b></td>
</tr></table></td></tr></table></td></tr>
<tr><td><table width="617" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="13"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_07.jpg" width="13" height="107"></td>
<td bgcolor="#8cc63f"><table width="595" border="0" cellspacing="0" cellpadding="0"><tr>
<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_08.jpg" width="595" height="24"></td></tr>
<tr><td><table width="595" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="43"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_10.jpg" width="43" height="83"></td>
<td width="229" valign="top"><table width="229" border="0" cellspacing="0" cellpadding="0">
<tr>
<td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:18px;line-height:24px;"><b>Call. Sign up. Save.</b></td></tr>
<tr><td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:30px;line-height:33px;">1 877-516-8478</td></tr></table></td>
<td width="76"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_12.jpg" width="76" height="83"></td>
<td><table width="247" border="0" cellspacing="0" cellpadding="0"><tr><td>
<table width="247" border="0" cellspacing="0" cellpadding="0"><tr><td valign="top"><table width="193" border="0" cellspacing="0" cellpadding="0">
<tr><td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:12px;line-height:15px;">Use this referral code:</td>
</tr><tr><td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:26px;line-height:29px;">';
$str.= $lead;
$str.= '</td></tr><tr><td align="center" style="font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:12px;line-height:15px;">Referred by:  ';
$str.=$from_name;
$str.='</td></tr></table></td>
<td width="54"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_14.jpg" width="54" height="63"></td></tr></table></td></tr>
<tr><td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_15.jpg" width="247" height="20"></td></tr></table></td></tr></table></td>
</tr></table></td><td width="9"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_09.jpg" width="9" height="107"></td></tr>
</table></td></tr><tr><td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_16.jpg" width="617" height="26"></td>
</tr><tr><td><table width="617" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="281"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf_17b.jpg" width="281" height="186"></td>
<td valign="top"><table width="324" border="0" cellspacing="0" cellpadding="0"><tr>
<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:13px;color:#666666">
CenturyLink gives you the best in service and products:</td></tr>
<tr><td valign="top"><table width="324" border="0" cellspacing="0" cellpadding="0"><tr>
<td width="4" valign="top" style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">&bull;</td>
<td width="7"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="7" height="26"></td>
<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:13px;color:#666666">
High-Speed Internet with a variety of available speeds <br> 
and offers, including our Price-Lock Guarantee.
</td>
</tr>
<tr>
<td width="4" style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">&bull;</td>
<td width="7"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="7" height="26"></td>
<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:13px;color:#666666">
Internet plans with or without home phone service.
</td>
</tr>
<tr>
<td width="4" style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666">&bull;</td>
<td width="7"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="7" height="26"></td>
<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:13px;color:#666666">
Best in class television experiences.
</td>
</tr>
<tr>
<td width="4" style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:10px;color:#666666"></td>
<td width="7"><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="7" height="26"></td>
<td style="font-family:Arial, Helvetica, sans-serif;font-size:10px;line-height:13px;color:#666666;">

<span style="font-weight:900;color:black;">So don&rsquo;t wait, call and start saving today!
<br>
<br>
Call 1-866-511-6683
</span>
</td>

</tr>
								</table></td>
								</tr>
							<!--	
							<tr>
								<td><img src="http://www.centurylinkpassitonrewards.com/graf07/images/ftaf2_21.jpg" alt="CALL 1-866-511-6683!" width="324" height="28" style="display:block"></td>
								</tr>
								
							<tr>
								<td><table width="324" border="0" cellspacing="0" cellpadding="0">
									<tr>
										<td><img style="display:block" src="http://www.centurylinkpassitonrewards.com/graf07/images/s.gif" alt="" width="33" height="26"></td>
										<td align="left" style="font-family:Arial, Helvetica, sans-serif;font-size:8px;line-height:11px;color:#666666">*CenturyLink High-Speed Internet network reliability is based on current <br>
											network availability statistics. Individual experiences will vary.</td>
										</tr>
								</table></td>
							</tr>
							-->
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
<td style="font-family:Arial, Helvetica, sans-serif;color:#9a9090;font-size:10px;line-height:13px;">You are receiving this email via an associate of yours who is a current CenturyLink subscriber. This one time use of your email information will not be used again unless you have authorized permission to do so otherwise. <br><br>

Services and offers not available everywhere. 
CenturyLink may change or cancel services or substitute similar services at its sole discretion without notice. 
Services require credit approval and deposit may be required. Additional restrictions apply. 
<span style="font-weight:bold;color:black;">Terms and Conditions &#45;</span> All products and services listed are governed by tariffs, terms of service, 
or terms and conditions posted at www.centurylink.com. 
<span style="font-weight:bold;color:black;">CenturyLink Pass It On Rewards Program ("Program"):  </span>
Program is subject to change, without notice, and may vary by service area. 
<span style="font-weight:bold;color:black;">CenturyLink reserves the right to add, change or remove any restrictions of the Program, 
discontinue the Program at any time without notice or cancel future eligible redemptions if Program is terminated.  </span>
All Program participants must maintain a qualifying CenturyLink account in good credit standing to receive all applicable 
Program invoice credits, as allocated below.  Customers cannot refer themselves or refer their own accounts.  
CenturyLink employees and their immediate family members are not eligible to refer or participate in Program.  
Business accounts are not eligible for participation in the Program.  Additional restrictions may apply.  
<span style="font-weight:bold;color:black;">Qualifying Service(s) --</span> The following Services are eligible for invoice credits, as allocated below, within the Program:  
CenturyLink&reg; Prism&#0153; TV, CenturyLink&reg; High-Speed Internet or DIRECTV&reg; 
service through CenturyLink (each a "Service").  
Services are not available everywhere. CenturyLink may change, cancel or substitute Services, 
or vary them by service area, at its sole discretion without notice.  
All products and services listed are governed by tariffs, terms of service, 
or terms and conditions posted at www.centurylink.com. 
<span style="font-weight:bold;color:black;">Referring Customer &#45;</span> In order to participate in the Program, 
the Referring Customer must have an active residential CenturyLink account in one or more CenturyLink local service areas.  
Referring Customers receive a one-time &#36;100 credit when a new CenturyLink Referred Customer subscribes to 
CenturyLink&reg; PRISM&#0153; TV, or a one-time &#36;50 credit when an existing CenturyLink Referred Customer subscribes to 
CenturyLink&reg; PRISM&#0153; TV.  Referring Customers receive a one-time &#36;50 credit when a new CenturyLink Referred 
Customer subscribes to CenturyLink&reg; High-Speed Internet or DIRECTV&reg; Service through CenturyLink. 
Referring Customers receive a one-time &#36;25 credit when an existing CenturyLink Referred customer adds a 
CenturyLink&reg; High-Speed Internet or DIRECTV&reg; Service through CenturyLink. 
The &#36;100, &#36;50 and &#36;25 will be in the form of credits on the CenturyLink bill. 
Credits will appear on Referred and Referring Customer bills within 30 days from the Referred Customer&rsquo;s order date.  
Referring Customer is entitled only to one (1) invoice credit (highest available) per month, per Referred Customer, 
regardless of number of Services added by Referred Customer.  
Limit &#36;600 in Program invoice credits per calendar year.  
<span style="font-weight:bold;color:black;">Referred Customer &#45;</span> Referred Customer will receive &#36;10 invoice credit each month for one Service for six consecutive months, 
assuming Service eligibility and availability.  
Referred Customer can only receive one &#36;10 monthly invoice credit at a time, 
regardless of number of Services added in that six-month period.  
The Service must be installed within 60 days of the initial referral date by Referring Customer.  
If Service is not so installed, the Referring and Referred Customer will not be eligible for invoice credits.  
Referred Customer must maintain the applicable Service, in good credit standing, for six months to receive full &#36;60 invoice credits.  
<span style="font-weight:bold;color:black;">High-speed Internet &#45;</span> Customers must accept High-Speed Internet Subscriber Agreement prior to using service. 
Download speeds will range from 85% to 100% of the listed download speeds due to conditions outside of network control, 
including customer location, websites accessed, Internet congestion and customer equipment.  
<span style="font-weight:bold;color:black;">Consistent Speed Claim &#45; </span>Claim is based on providing High-Speed Internet customers with a dedicated, 
virtual-circuit connection between their homes and the CenturyLink central office. &#169; 2013 CenturyLink, Inc.  All Rights Reserved.  
All other marks are property of their respective owners.
 
 <br><br>
If you do not wish to receive future marketing emails, please use this unsubscribe link or you can also respond to this email by writing to us:
CenturyLink Customer Response Team P.O. Box 4259 Monroe, LA 71211<br><br>
CenturyLink	<a href="https://www.centurylink.com/Pages/AboutUs/Legal/PrivacyPolicy/">PRIVACY POLICY</a>
</td>
<td width="9">&nbsp;</td></tr></table></td>
</tr></table></td>
</tr></table>
</center></body></html>';

return $str;

}




