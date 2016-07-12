
# copied from youcan07/landing.cgi
use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use HTML::Strip;
my $hs = HTML::Strip->new();
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

require "D:/centurylinkyoucan/cgi-bin/init.cgi";
require "D:/centurylinkyoucan/cgi-bin/delimeter.cgi";



my 	$btn = $hs->parse($cgi->param('btn')) ||'';
my  $from_email= $hs->parse($cgi->param('from_email')) ||'';
my $redir = $hs->parse($cgi->param('redir')) ||0;


my  $PAGETITLE = 'CenturyLink Pass it on Rewards';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'http://www.centurylink.com/static/Styles/main.css',
    );
#print $header;
#	print "Content-type:text/html\n\n";
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

		<a href="/"><img class="logo" src="images/ctl_con2.jpg" alt="CenturyLink" width="244" height="82"></a>

	</div>

		<div id="topbar">

<ul id="topnav">
	<form name="frm" action=""  method="post" >
			<input type="hidden" name="redir" value="$redir">
<input type="hidden" name="btn" value="$btn">
<input type="hidden" name="from_email" value="$from_email">
	<li>
	<a href="#" onClick="location.href='../index_pior.cgi'"><font size="2">Home</font> </a>
	</li>
	<li><a href="#" onClick="document.frm.action='faq_pior.cgi';document.frm.submit();this.form.reset()"><font size="2">FAQ&rsquo;s </font></a>
	</li>
	<li class="current"><a href="#"><font size="2">Terms & Conditions</font> </a>
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
			<b>General</b>
			<p><p>
			Program is subject to change, without notice, and may vary by service area. 
			<b>CenturyLink reserves the right to add, change or remove any restrictions of the Program, 
			discontinue the Program at any time without notice or cancel future eligible redemptions if Program is terminated.  </b>
			All Program participants must maintain a qualifying CenturyLink account in good credit standing to receive all applicable 
			Program invoice credits, as allocated below.  Customers cannot refer themselves or refer their own accounts.  
			CenturyLink employees and their immediate family members are not eligible to refer or participate in Program.  
			Business accounts are not eligible for participation in the Program.  Additional restrictions may apply.  
            <p><p>
            <b>Qualifying Service(s)</b>
            <p><p>
            The following Services are eligible for invoice credits, as allocated below, within the Program:  
            CenturyLink Prism TV, CenturyLink&#174; High-Speed Internet or DIRECTV service through CenturyLink (each a "Service").  
            Services are not available everywhere. CenturyLink may change, cancel or substitute Services, or vary them by service area, 
            at its sole discretion without notice.  All products and services listed are governed by tariffs, terms of service, or terms and 
            conditions posted at <a href="http://www.centurylink.com" target="_blank">www.centurylink.com</a>
            <p><p>
            <b>Referring Customer</b>
            <p><p>
            In order to participate in the Program, the Referring Customer must have an active residential CenturyLink account 
            in one or more CenturyLink local service areas.  Referring Customers receive a one-time \$100 credit when a new 
            CenturyLink Referred Customer subscribes to CenturyLink PRISM TV, or a one-time \$50 credit when an existing 
            CenturyLink Referred Customer subscribes to CenturyLink PRISM TV.  Referring Customers receive a one-time \$50 credit when a new 
            CenturyLink Referred Customer subscribes to CenturyLink High-Speed Internet or DIRECTV&#174; Service through CenturyLink. 
            Referring Customers receive a one-time \$25 credit when an existing CenturyLink Referred customer adds a CenturyLink 
            High-Speed Internet or DIRECTV Service through CenturyLink. The \$100, \$50 and \$25 will be in the form of credits on the 
            CenturyLink bill. Credits will appear on Referred and Referring Customer bills within 30 days from the Referred Customer’s order date.  
            Referring Customer is entitled only to one (1) invoice credit (highest available) per month, per Referred Customer, 
            regardless of number of Services added by Referred Customer.  Limit \$600 in Program invoice credits per calendar year.  
            <p><p>
            <b>Referred Customer</b>
            <p><p>
            Referred Customer will receive \$10 invoice credit each month for one Service for six consecutive months, 
            assuming Service eligibility and availability.  Referred Customer can only receive one \$10 monthly invoice credit 
            at a time, regardless of number of Services added in that six-month period.  The Service must be installed within 
            60 days of the initial referral date by Referring Customer.  If Service is not so installed, the Referring 
            and Referred Customer will not be eligible for invoice credits.  Referred Customer must maintain the 
            applicable Service, in good credit standing, for six months to receive full \$60 invoice credits.

			 </p>


			</td>
		</tr>
	</table>
	</div>
</div>

<!-- End Main Content -->
	<div id="footer"><a href="https://www.centurylinkpassitonrewards.com/index_raf.cgi">Click here to go to the CenturyLink legacy Refer-a-Friend site</a>
<div class="about">
            <p class="copyright">Copyright &copy;
<script type="text/javascript">
    var dteNow = new Date();
    var intYear = dteNow.getFullYear();
    document.write(intYear);
</script> Qwest&reg;
<br>
All Rights Reserved.<br> The name Qwest and the Qwest logo are trademarks of CenturyLink, Inc.<br> All other marks are the property of their respective owners.
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

