
# copied from youcan07/landing.cgi
use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use HTML::Strip;
my $hs = HTML::Strip->new();
#use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

require "D:/centurylinkyoucan/cgi-bin/init.cgi";
require "D:/centurylinkyoucan/cgi-bin/delimeter.cgi";


#<!--	Webpage error details	-->
#Message: 'document.body' is null or not an object
#Line: 5
#Char: 23004
#Code: 0
#URI: http://www.centurylink.com/static/Common/Includes/Lib/Metrix/Common/TnT/mbox.js

my $thisfile = "index_raf_promo.cgi";
my $btn =  $hs->parse($cgi->param('btn')) ||0;
my $from_email= $hs->parse($cgi->param('from_email')) || '';
my $redir =  $hs->parse($cgi->param('redir')) ||0;
             

	 
if ($redir == 0) {
	if ($btn eq "" && $from_email eq "") {
		$redir = 1;
	}
}
             
my  $PAGETITLE = 'CenturyLink-Pass It On Rewards';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'http://www.centurylink.com/static/Styles/main.css',
    );
#print $header;
	#print "Content-type:text/html\n\n";
#print "here $redir";exit();
	
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

		<script type="text/javascript" src="/jquery/jquery.js"></script>
		<script type="text/javascript" src="/jquery/javascript/jquery-1.4.1.min.js"></script>
		<script  type="text/javascript" src="/jquery/jquery-ui.js"></script>

		<script type="text/javascript" src="/jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="/jquery/simplemodal/simplemodal.css"/>
		<script  type="text/javascript" src="graf07/validate_promo.js"></script>

		<script type="text/javascript">


			function acceptDigits(objtextbox){
				var exp = /[^\\d]/g;
				objtextbox.value = objtextbox.value.replace(exp,'');
			}

		</script>
</head>

<body>



<!-- ***************  METRIX CONFIGURATION CODE BEGIN  ******************** -->




<div id="GlobalProvisioner" class="mboxDefault"><!--DefaultContent--></div>


<!-- ***************  METRIX CONFIGURATION CODE END  ******************** -->


<div id="main">

	<div id="masthead">

		<a href="/"><img class="logo" src="graf07/images/ctl_con2.jpg" alt="CenturyLink" width="244" height="82"></a><br>

	</div>

		<div id="topbar">
		<form action="$thisfile" method="post" name="frm">
		<input type="hidden" name="redir" value="$redir">
		<ul id="topnav">

			<li class="current"><a href="#" onClick="location.href='index_raf_promo.cgi'"><font size="2">Home</font> </a>
EOF
		if ($redir == 1) {
		$from_email =~ s/@/\|~\|/g;
print<<"EOF";
		<input type="hidden" name="btn" value="$btn">
		<input type="hidden" name="from_email" value="$from_email">

				<ul>
				<li class="first"><a href="#"onclick="openModalLarge('graf07/promocode.cgi?email=1&btn=$btn&from_email=$from_email');return false;">Email</a></li>
				<li><a href="#"onclick="openModalLarge('graf07/promocode.cgi?coupon=1&btn=$btn&from_email=$from_email');return false;">Coupon </a></li>
				</ul>
EOF

		}

print<<"EOF";
			</li>
			<li><a href="#" onClick="document.frm.action='graf07/faq_promo.cgi';document.frm.submit();this.form.reset()" ><font size="2">FAQ&rsquo;s</font> </a>
			</li>
			<li><a href="#" onClick="document.frm.action='graf07/tandc_promo.cgi';document.frm.submit();this.form.reset()"><font size="2">Terms & Conditions</font> </a>
			</li>
		</ul>
		</div>


<!-- Main Content -->

<div id="content">

<div class="flashheader">
		<img src="http://www.centurylink.com/static/Images/Support/headerSupportRewards.jpg" width="746" height="230" alt="Rewards">
	</div>
	<div class="body">
	<table width="100%" id="myAccount">
		<col><col width="190">
		<tr>
			<td>
				<table cellpadding="5" class="myafeatures">
					<tr> 
						<td>
			<p><b>It&rsquo;s easy. Tell more friends. Get more rewards.</b>
			<p>You deserve more than our thanks for referring your friends and family to CenturyLink. Pass it on and get up to \$600 a year in bill credits.
	<ul>
	<li>You&rsquo;ll receive a \$50 bill credit for each new customer that signs up for CenturyLink High-Speed Internet&reg;.</li>
	<li>Or, you can receive a \$100 bill credit for each new customer who signs up for Prism TV from CenturyLink! </li>
	<li><b>Plus, let your friends and family know they will get a one-time \$50 bill credit on top of the current promotional price for qualifying services.</b> </li>
	</ul>

<p>More info? <a class="targetlink" href="graf07/faq_promo.cgi" >Read Frequently Asked Questions</a></p>
<p>&nbsp;</p>
<p>*Certain conditions may apply. <a href="graf07/tandc_promo.cgi">Click here for details.</a></p>
			</p>
			</td>
			</tr>
			</table>
			</td>
			<td class="callout">
			<h2 style="color: #666; font-weight: bold;">Two ways to pass it on:</h2>
<p>&nbsp;</p>
EOF
if ($redir==0) {
	print<<"EOF";
<h3 style="color:#666; font-weight: bold;">Email</h3>

EOF
}

if ($redir==1) {
	print<<"EOF";
<div class="menuitem"><h2><font size="5"><a href="#" onclick="openModalLarge('graf07/promocode.cgi?email=1&btn=$btn&from_email=$from_email');return false;">Email</a></font></h2></div>

EOF
}

print<<"EOF";
<p>Send a Pass-It-On email to friends and family. It&rsquo;s the fastest way to earn more rewards.</p>


EOF
if ($redir==0) {
	print<<"EOF";
<h3 style="color:#666; font-weight: bold;">Print</h3>

EOF
}

if ($redir==1) {
	print<<"EOF";
<div class="menuitem"><h2><font size="5"><a href="#" onclick="openModalLarge('graf07/promocode.cgi?coupon=1&btn=$btn&from_email=$from_email');return false;">Print</a></font></h2></div>

EOF
}

print<<"EOF";
<p>Print your own Pass-It-On Coupons.<br>
It&rsquo;s as simple as that.</p>
<hr>
EOF

if ($redir == 0) {
	print<<"EOF";
<p style="color: #666; font-weight: bold;">Your Phone Number<br/>
<input type="text" name="btn" maxLength="10" onkeyup="acceptDigits(this);"> </p>
<p style="color:#666; font-weight: bold;">Confirm Your Phone Number<br/>
<input type="text" name="btn2" maxLength="10" onkeyup="acceptDigits(this);"></p>
<br/>
<p style="color:#666; font-weight: bold;">Your Email Address<br/>
<input type="text" name="from_email" maxLength="35"></p>
<br/>
<input type="image" src="http://www.centurylink.com/static/Images/Buttons/btnSubmit.gif" border="0" target="_blank" width="86" height="29" alt="Submit" onclick="acceptDigits(btn);acceptDigits(btn2);checkform()"/>
EOF

}

print<<"EOF";
			</td>
		</tr>
	</table>
	</div>
</div>

<!-- End Main Content -->
	<div id="footer"><a href="http://www.centurylinkpassitonrewards.com/index_raf.cgi">Click here to go to the CenturyLink legacy Refer-a-Friend site</a>
<div class="about">
            <p class="copyright">Copyright &copy;
<script type="text/javascript">document.write(new Date().getFullYear());</script>CenturyLink, Inc. All Rights Reserved. The CenturyLink mark, pathways logo, Qwest mark, Q lightpath logo and certain CenturyLink product names are the property of 
	CenturyLink, Inc. All other marks are the property of their respective owners.
<br><br>
</p>
</div>
<div class="support">
      	<p class="cta">Call us at 1 866-511-6683 </p>
</div> 
	</div>
</div>
<!-- ***************  METRIX RESOURCE SCRIPT CODE BEGIN  ******************** -->
<noscript><img src="http://centelcom.112.2O7.net/b/ss/centelcom/1/H.14--NS/0" height="1" width="1" border="0"/></noscript>
<!-- ***************  METRIX RESOURCE SCRIPT CODE END  ******************** -->
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
</form></body></html> 
	
EOF
