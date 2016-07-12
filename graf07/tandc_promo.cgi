
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
	<li>
	<a href="#" onClick="location.href='../index_raf_promo.cgi'"><font size="2">Home</font> </a>
	</li>
	<li><a href="#" onClick="document.frm.action='faq_promo.cgi';document.frm.submit();this.form.reset()"><font size="2">FAQ&rsquo;s</font> </a>
	</li>
	<li  class="current"><a href="#" onClick="document.frm.action='tandc_promo.cgi';document.frm.submit();this.form.reset()"><font size="2">Terms & Conditions </font></a>
	</li>
</ul>
		</div>
</form>
<!-- Main Content -->

<div id="content">
	<link rel="stylesheet" href="http://www.centurylink.com/static/Styles/support.css" type="text/css" media="screen,print">
	<div class="body">
	<table width="100%" id="myAccount" border="0">
		<tr>
			<td>
			<p><b>CenturyLink Customer Referral Program (&ldquo;Program&rdquo;) </b></p>
<p>Program is subject to change, without notice, and may vary by service area. <b>CenturyLink reserves the right to add, change or remove any restrictions of the Program, discontinue the Program at any time without notice or cancel future eligible redemptions if Program is terminated.</b>  All Program participants must maintain a qualifying CenturyLink account in good credit standing to receive all applicable Program invoice credits, as allocated below.  Customers cannot refer themselves or refer their own accounts.  CenturyLink employees and their immediate family members are not eligible to refer or participate in Program.  Business accounts are not eligible for participation in the Program.  Additional restrictions may apply.</p>
<br>
<p><b>Qualifying Services</b></p>
<p>CenturyLink High-Speed Internet service and/or Prism&trade;  TV Package (each a &ldquo;Service&rdquo;) are eligible for referral within the Program.  Service is not available everywhere. CenturyLink may change, cancel or substitute Service, or vary them by service area, at its sole discretion without notice.  All products and services listed are governed by tariffs, terms of service, or terms and conditions posted at <a href="http://www.centurylink.com" target="_blanl">www.centurylink.com.</a></p> 
<br>
<p><b>Program</b></p>
<p>In order to participate in the Program, the Referring Customer must have an active residential CenturyLink account in one or more CenturyLink local service areas.  Referring Customer and Referred Customer will each receive a one-time \$50 invoice credit when a new CenturyLink Referred Customer subscribes to High Speed Internet service.  When a new CenturyLink Referred Customer subscribes to Prism TV, the Referring Customer will receive a one-time \$100 invoice credit, and the Referred Customer will receive a one-time \$50 invoice credit.Referred customer is required to keep product for a minimum of 30 days.  Credits will appear on Referred and Referring Customer bills within 90 days from the Referred Customer&rsquo;s order date.  The Referred Customer and the Referring Customer are only entitled to one (1) invoice credit per month.  Limit \$600 in Program invoice credits per calendar year for both Referred and Referring Customers.</p>

			</td>
		</tr>
	</table>
	</div>
</div>

<!-- End Main Content -->
	<div id="footer"><!--<a href="http://www.centurylinkreferafriend.com/index_raf.cgi">Click here to go to the CenturyLink legacy Refer-a-Friend site</a>-->
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
