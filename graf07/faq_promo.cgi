
# copied from youcan07/landing.cgi
use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use HTML::Strip;
my $hs = HTML::Strip->new();
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

my $server;

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



my 	$btn = $hs->parse($cgi->param('btn')) ||'';
my  $from_email= $hs->parse($cgi->param('from_email')) ||'';
my $redir = $hs->parse($cgi->param('redir')) ||0;


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

	<link rel="P3Pv1" href="http://www.centurylink.com/w3c/p3p.xml" />

		<link rel="stylesheet" href="http://www.centurylink.com/static/Styles/support.css" type="text/css" media="screen,print">
		<link rel="stylesheet" href="http://www.centurylink.com/static/Styles/main.css" type="text/css" media="screen,print">
		<link rel="stylesheet" href="http://www.centurylink.com/static/Styles/menu.css" type="text/css" media="screen,print">
	<script src="http://www.centurylink.com/static/Common/Includes/Lib/Metrix/Common/TnT/mbox.js" type="text/javascript"></script>
		<script src="http://www.centurylink.com/static/Common/Includes/Lib/global.js" type="text/javascript"></script>


</head>

<body>





<div id="main">

	<div id="masthead">

		<a href="/"><img class="logo" src="images/ctl_con2.jpg" alt="CenturyLink" width="244" height="82"></a><br>

	</div>

		<div id="topbar">

<ul id="topnav">
	<form name="frm" action=""  method="post" >
			<input type="hidden" name="redir" value="$redir">
<input type="hidden" name="btn" value="$btn">
<input type="hidden" name="from_email" value="$from_email">
</form>

	<li>
	<a href="#" onClick="location.href='../index_raf_promo.cgi'"><font size="2">Home</font> </a>
	</li>
	<li class="current"><a href="#" onClick="document.frm.action='faq_promo.cgi';document.frm.submit();this.form.reset()"><font size="2">FAQ&rsquo;s</font> </a>
	</li>
	<li><a href="#" onClick="document.frm.action='tandc_promo.cgi';document.frm.submit();this.form.reset()"><font size="2">Terms & Conditions </font></a>
	</li>
</ul>
		</div>
<!-- Main Content -->

<div id="content">
	<link rel="stylesheet" href="http://www.centurylink.com/static/Styles/support.css" type="text/css" media="screen,print">
	<div class="body">
	<table width="100%" id="myAccount" border="0">
		<tr>
			<td>
			<p><b><u>Referring Customer Questions</u>.</b>

			<p><b> Q:</b> What do I need to do to become a CenturyLink Referring Customer? </p>

<p><b>A:</b> Sign up for CenturyLink service (if you haven&rsquo;t already) and go to the <a href="http://www.centurylinkpassitonrewards.com">www.centurylinkpassitonrewards.com</a>  to send referral e-mails to your friends and family or print off referral coupons to hand out with a unique seven digit referral code. </p>


<p><b> Q:</b> How much money will I receive per referred customer? </p>
<p><b> A:</b> Referring Customers can receive a \$50 bill credit for referring a new customer to CenturyLink High Speed Internet&reg;, or \$100 bill credit for referring a new customer to Prism TV, limit one credit per month. </p>

<p><b> Q:</b> Is there any limit to the amount of rewards credit I can receive? </p>
<p><b> A:</b> Referral credits are limited to one bill credit per referred customer order per month. An overall limit of \$600 is available for each calendar year.</p>

<p><b> Q:</b> Is the customer I refer required to keep service for a specific amount of time before I receive my credit? </p>
<p><b> A:</b> Once your referred customer&rsquo;s order is completed, your account will be credited with the referring customer credit. Please allow 90 days for your credit to apply to your bill, from the time the referred customer activates service.</p>

<p><b> Q:</b> Who should I call if I have not yet received my rewards credit? </p>
<p><b> A:</b> Call the CenturyLink Customer Service Center at 1 866-511-6683. </p>

<p><b> Q:</b> Is there any way I can monitor my rewards credits online? </p>
<p><b> A:</b> Not at this time, but we will have that service available for you in the future.</p>

<p><b> Q:</b> Are CenturyLink employees eligible to become Referring Customers? <br/>
<p><b> A:</b> No, not at this time. </p>

<p><b> Q:</b> Are business customers eligible to become Referring Customers? </p>
<p><b> A:</b> No. At this time the program is limited to residential customers. </p>
<p><b> Q:</b> Can you tell me if one of my referrals has activated service yet? I gave out a coupon but have not received my referral credit yet. </p>
<p><b> A:</b> We cannot provide information regarding another customer&rsquo;s account. You will need to speak to the customer to see if they have activated their service and provided us with your referral number. </p>
<p><b> Q:</b> Can I receive a gift card or check instead of my account being credited? </p>
<p><b> A:</b> No, only credits to your CenturyLink account are available as part of this program.</p>

<br/><br/>
<p>	<b><u>Referred Customer Questions</u></b></p>
<p><b> Q:</b> I received a CenturyLink Pass-It-On coupon from a friend. How can I redeem this coupon? </p>
<p><b> A:</b> You will need to become a new CenturyLink customer or if you already have an account with CenturyLink, you will need to sign up for new CenturyLink High Speed Internet&reg; or Prism by calling 1 866.511.6683. Please provide us with the referral code at the bottom of the coupon.  </p>
<p><b> Q:</b> Where can I find the Referring Customers ID number on this coupon?</p>
<p><b> A:</b> The referral code is the seven digits at the bottom of the coupon. </p>
<p><b> Q:</b> What services am I required to add to receive the \$50 credit?</p>
<p><b> A:</b> You will need to add new CenturyLink High Speed Internet&reg; and/or Prism TV to your new or existing CenturyLink account.  </p>
<p><b> Q:</b> Am I required to keep service for a specific amount of time before I receive my credit? </p>
<p><b> A:</b> You will receive your credit after keeping the product 30 days.</p>
<p><b> Q:</b> Can I also take advantage of your quarterly promotions since I am activating as a referred customer and will receive the referral credit? </p>
<p><b> A:</b> Yes. You are also eligible to receive any current promotion, depending on availability and limitations per promotional offer.</p>


			</td>
		</tr>
	</table>
	</div>
</div>

<!-- End Main Content -->
	<div id="footer">
<div class="about">
            <p class="copyright">Copyright &copy;
<script type="text/javascript">
    var dteNow = new Date();
    var intYear = dteNow.getFullYear();
    document.write(intYear);
</script> CenturyLink, Inc. All Rights Reserved. The CenturyLink mark, pathways logo, Qwest mark, Q lightpath logo and certain CenturyLink product names are the property of 
	CenturyLink, Inc. All other marks are the property of their respective owners.
<br><br>
</p>
</div>
<div class="support">
      	<p class="cta">Call us at 1 866-511-6683</p>
</div> 
	</div>
</div>
<!-- ***************  METRIX RESOURCE SCRIPT CODE BEGIN  ******************** -->
<noscript><img src="http://centelcom.112.2O7.net/b/ss/centelcom/1/H.14--NS/0" height="1" width="1" border="0"/></noscript>
<!-- ***************  METRIX RESOURCE SCRIPT CODE END  ******************** -->
</body></html> 
	
EOF
