use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use Try::Tiny;
use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||0;

my $myDB = DBInterface->new();

my $leadlink=0;

require "D:/centurylinkyoucan/cgi-bin/init.cgi";

my $valid = CCICryptography::validate_CL($cci_id);
my ($id,$emplid) = CCICryptography::getEmpid($cci_id); 
my $url = CCICryptography::getUrl();

my $thisfile = 'overview.cgi';

if ($valid <= 0) {
print<<"EOF";
$ENV{SERVER_PROTOCOL} 200 OK
Content-Type: text/html

<!--<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">-->
<!-- (c) 2001-2016 CCI -->
<html>
<script language='javascript'>
    window.alert('Your session has expired. Please login again. Thank You.');
    document.location="$url";
</script>
EOF
exit();

}

my  $PAGETITLE = "YOUCAN | Deliver the VIP Experience";;
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;

my $browse = $ENV{'HTTP_USER_AGENT'};
my $bname = $ENV{'browser_version'};
my $bv = $ENV{'browser_name'};
my $sql= "select dbo.fn_CTL_IsTechEmp(?) as isTechEmp";
#############
my $prog;
try {
my $sth = $myDB->prepare($sql);
$sth->execute($emplid);
$prog = $sth->fetchrow_hashref();
$sth->finish();
}
catch {
	print "Our apologies. An error occured, please report.";
	DBInterface::writelog('youcan10',"$thisfile", $_ );
	exit;	
};
##############
my $isTechEmp = $prog->{isTechEmp};

my $getpage ="";
if ($isTechEmp == 1) {
 $getpage = TechVersion();
}
else {
 $getpage = NonTechVersion();
}
# below to be checked


print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>$PAGETITLE</title>

<!--FAVICON-->
<link href="/favicon.ico" rel="shortcut icon" type="image/x-icon" />

<!--CSS-->
	<link type="text/css" href="assets/css/chevron5.css" rel="stylesheet" />	

<link type="text/css" href="assets/css/style.css" rel="stylesheet" />

<link href="assets/css/iefix.css" type="text/css" rel="stylesheet" />
<!--JAVASCRIPT-->
<script type="text/javascript" src="assets/js/jquery.js"></script>
<script type="text/javascript" src="assets/js/functions.js"></script>
<script type="text/javascript">
	animatedcollapse.addDiv('nav-sec-1', 'fade=0,speed=500,group=nav,hide=1,height=22px,persist=1')
	animatedcollapse.addDiv('nav-sec-2', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-3', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-4', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-5', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-6', 'fade=0,speed=500,group=nav,hide=1,height=22px')

	animatedcollapse.init()
</script>
<!--[if lt IE 8]> <script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE8.js"></script> <![endif]-->
</head>

<body>
<div id="layout">

	<div id="layout-header">
EOF
require "D:/centurylinkyoucan/youcan10/youcan_header.cgi";
showhdr ($PAGETITLE, $cci_id);
print<<"EOF";
    </div><!--END LAYOUT-HEADER-->

    <div id="layout-body">
    	<div id="body-left-sec">
        	<div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2>YOUCAN Overview</h2>
                </div>
                <div class="capsule-content">
<p> <span class="news_header">Welcome to YOUCAN!</span> </p>
 $getpage
                </div>
            </div><!--END CAPSULE-->
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
EOF
show_rttbl ($cci_id);
print<<"EOF";
        </div><!--END BODY-RIGHT-SEC-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
EOF
showftr ($cci_id);
print<<"EOF";
</div><!--END LAYOUT-->
</body>
</html>
EOF
undef &get_header;

# -------------------------------------------------------------------
sub get_header
{

	my %hash  = @_;
	my $title = $hash{title} || '';
	my $css   = $hash{css} || '';
	my $more  = $hash{more} || '';

	$css = "<link rel=\"stylesheet\" href=\"$css\" type=\"text/css\">\n" if $css;

	my $str = "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
	$str .= <<EOF;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>$title</title>
$css$more
<meta name=robots content=noindex>
<meta name="MSSmartTagsPreventParsing" content="TRUE">
<meta http-equiv="pragma" content="no-cache">
<script language="javascript">
  function openwindow(URL) {
    win = window.open(URL, "pop", "width=800, height=550, left=50, top=50, scrollbars=yes, toolbar=yes, menubar=yes, status=yes");
  }
</script>

</head>
EOF
	return $str;
}

############################################################################


sub NonTechVersion {

my $str = qq[

<p> <span class="news_header">How do I participate in YOUCAN?</span> </p>
<ul>
	<li> Familiarize yourself with CenturyLink&rsquo;s products and services. Reviewing centurylink.com is a great way to find out more.</li>
	<li> Talk with your friends, family, neighbors and the businesses in your community you may hear clues about opportunities for CenturyLink. For example:

	<ul style="list-style-type:square;">
		<li> A business you frequent only has one line for the credit card machine and the phone. That&rsquo;s a great opportunity for a High Speed Internet product from CenturyLink.</li>
		<li> A friend or neighbor complains about slow speeds while browsing the Internet or experiences buffering while streaming a TV show. That&rsquo;s an opportunity to explore if faster HSI speeds can be provided by CenturyLink and to speak about available video products.</li>
	</ul>
	<li> Once you&rsquo;ve uncovered an opportunity, gain clear and unambiguous consent for CenturyLink to call the person you are referring.</li>
	<li> On the YOUCAN website create a referral for the business or residential customer you are referring. 
			We&rsquo;ll ask information like the customer&rsquo;s name, Telephone Number and a summary of what product(s) the customer expressed interest in. 
			The more information the better. This helps our salespeople kick off a successful conversation with the person you are referring.</li>
</ul>
<hr>
<p> <span class="news_header">What happens after I submit my lead to YOUCAN?</span> </p>
<p>Once your referral is created, you may follow its progress on the Referral History page. Referrals at all stages in their lifecycle fall into one of these categories</p>
<table width="100%" border="1" cellspacing="0" cellpadding="0" class="reward-values">
	<tr><td colspan="4">


<div id="breadcrumb3">
		<ul class="breadcrumb3" style="margin-left:-20px;padding-left:0;">
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Received&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;In Progress&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;Accuracy Check&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;Awarded &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	</ul>
</div>


<div id="breadcrumb2">
		<ul class="breadcrumb2" style="margin-left:-20px;padding-left:0;">
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Received&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;In Progress&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;Accuracy Check&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;No Award&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
		</ul>
</div>
</td></tr>
<tr><td width="25%">
		<table width="100%">
			<tr><td><p>For Residential and Small Business referrals:</p>
					<ul>
						<li>Once YOUCAN receives your referral we route it to a salesperson to make an initial contact within two business days </li>
						<li>Most of YOUCAN&rsquo;s first calls are made much sooner, many on the same day the referral is received </li>
					</ul>
					<p>For Commercial and Enterprise referrals:</p>
					<ul>
						<li>Once YOUCAN receives your referral we route it to a salesperson in the Commercial and Enterprise teams. </li>
						<li>Your lead will be routed according to the information you provide. To ensure we promptly get the lead to the right salesperson, include as much information as possible including the business location, contact names and the product(s) the business is interested in.  </li>
					</ul>

				</td>
			</tr>
		</table>
	</td>
	<td width="25%">
		<table width="100%">
			<tr><td><p>For Residential and Small Business referrals:</p>
					<ul>
						<li>YOUCAN&rsquo;s sales team makes at least two attempts over multiple days to reach the customer you referred. We leave a voicemail with our number and instructions to call back when possible. </li>
						<li>You may see more detail viewing the Referral History Page. </li>
					</ul>
					<p>For Commercial and Enterprise referrals:</p>
					<ul>
						<li>Some Commercial and Enterprise sales are very complex and may take weeks or months to complete. </li>
						<li>You may see more detail about referrals in progress by viewing your Referral History. </li>
					</ul>
				</td>
			</tr>
		</table>
	</td>
	<td width="25%">
		<table width="100%">
			<tr><td>
					<p>Once a sale is made, we&rsquo;ll review the referral for accuracy.</p>
					<ul>
						<li>We may not complete our review until after the product(s) purchased are installed. This allows us to ensure the YOUCAN award is as accurate as possible. </li>
						<li>Once we complete our review, YOUCAN awards are generally distributed twice each month. The schedule is published on <a href="#" onClick="document.lead123.action='news.cgi';document.lead123.submit();">YOUCAN award calendar</a>.</li>
					</ul>
				
				</td>
			</tr>
		</table>
	</td>
	<td width="25%">
		<table width="100%">
			<tr><td><p>If this is your first sold referral, thank you!</p>
					<ul>
						<li>We&rsquo;ll send a reloadable Visa card to your home address on file with HR.  </li>
						<li>Cards arrive about two weeks after the award distribution date. Your future YOUCAN awards will be loaded to the same card on the distribution date.</li>
						<li>Remember that you will see the net value of the award on the card. Taxes are withheld. <a href="#" onClick="document.lead123.action='tax_info.cgi';document.lead123.submit();">Click here</a> for more information about YOUCAN awards and taxation. </li>
					</ul>
					<p>If you&rsquo;ve referred before and have a YOUCAN Visa card:</p>
					<ul>
						<li>Awards are loaded on or about the distribution date published on the <a href="#" onClick="document.lead123.action='news.cgi';document.lead123.submit();">YOUCAN award calendar</a>.  </li>
					</ul>
					<p>In the event your referral does not generate a qualified sale, we appreciate your perseverance and look forward to your next referral. An email with more information about the no&ndash;sale reason is on the way. </p>
				
				</td>
			</tr>
		</table>
	</td>
</tr>

</table>

<hr>
<p> <span class="news_header">How are Awards determined?</span> </p>
<ul>
	<li>YOUCAN Award values are posted on the Award Value page.</li>
	<li>YOUCAN bases the award for residential and small business referrals on the net new products or upgraded products that are generated by the YOUCAN salesperson from your YOUCAN referral.</li>
	<li>YOUCAN bases the award for Commercial and Enterprise referrals on the net increase in Monthly Recurring or Non - Recurring revenue. The Award Tiers for both MRR and NRR are posted on the Award Value page.</li>
	<li>Several exclusions and limitations apply. Common questions are explained on the <a href="#" onClick="document.lead123.action='res_biz_awards.cgi';document.lead123.submit();">Award Value page</a>.</li>
	<li>Once the Gross award value is determined, we&rsquo;ll calculate the Net and Taxable amounts and distribute the net value to your YOUCAN award card. More information about YOUCAN and Taxation is available <a href="#" onClick="document.lead123.action='tax_info.cgi';document.lead123.submit();">here</a>. 
	Our award calendar is located <a href="#" onClick="document.lead123.action='news.cgi';document.lead123.submit();">here</a>.</li>
</ul>
	
<hr>
<p> <span class="news_header">I still have questions.</span> </p>
<ul>
	<li>Answers to YOUCAN&rsquo;s most frequently asked questions are located <a href="#" onClick="document.lead123.action='faq.cgi';document.lead123.submit();">here</a>.</li>
	<li>Otherwise, please let team YOUCAN know you have a question by sending us an <a href="#" onClick="document.lead123.action='contact.cgi';document.lead123.submit();">email</a>.</li>

</ul>


];

return $str;
}
############################################################################

sub TechVersion {
	my $str = qq[

<p> <span class="news_header">How do I participate in YOUCAN?</span> </p>
<ul>
	<li> Review and follow CenturyLink&rsquo;s Methods and Procedures for your role.</li>
	<li> Familiarize yourself with CenturyLink&rsquo;s products and services. Reviewing centurylink.com is a great way to find out more.</li>
	<li> Once you&rsquo;ve uncovered an opportunity, gain clear and unambiguous consent for CenturyLink to call the person you are referring.</li>
	<li>Enhance your face to face conversation by providing the customer with product information on a YOUCAN authorized flyer (sometimes called collateral or brochures). 
		YOUCAN flyers will direct customers to a YOUCAN toll free number or retail location. Be sure your SAPID or CUID is written in the space provided for it, so the salesperson can create a referral that tracks back to you.
		</li>
	<li>Depending on your location, you may have one or multiple avenues to refer your customer. Consult the chart below to determine the best method choosing just one method per customer:</li>
</ul>
	
<table width="100%" border="1" cellspacing="0" cellpadding="0" class="reward-values">
	<tr>
		<td width="25%"><p><strong>Market</strong></p></td>
		<td width="25%"><p><strong>Customer</strong></p></td>
		<td width="50%"><p><strong>Refer your customer by ..</strong></p></td>
	</tr>
	<tr>
		<td width="25%" rowspan="10"><p>Ensemble</p></td>
		<td width="25%" rowspan="4"><p>Residential</p></td>
		<td width="50%"><p>creating a referral at centurylinkyoucan.com</p></td>
	</tr>
	<tr>
		<td><p>partnering with a retail store, where available</p></td>
	</tr>
	<tr>
		<td><p>providing the customer YOUCAN approved collateral with your SAPID</p></td>
	</tr>
	<tr>
		<td><p>calling the Residential National Order Help Desk YOUCAN number with the customer on the line at 866.228.3731. If the customer isn&rsquo;t available use centurylinkyoucan.com instead.</p></td>
	</tr>
	<tr>
		<td width="25%" rowspan="4"><p>Small Business <br>&lt;\$500 monthly spend.</p></td>
		<td><p>creating a referral at centurylinkyoucan.com</p></td>
	</tr>
	<tr>
		<td><p>partnering with a retail store, where available</p></td>
	</tr>
	<tr>
		<td><p>providing the customer YOUCAN approved collateral with your SAPID</p></td>
	</tr>
	<tr>
		<td><p>calling the Small Business National Order Help Desk YOUCAN number with the customer on the line at 855.296.8703. If the customer isn&rsquo;t available use centurylinkyoucan.com instead.</p></td>
	</tr>
	<tr>
		<td width="25%" rowspan="2"><p>Commercial and Enterprise <br>&gt;\$500 monthly spend.</p></td>
		<td><p>creating a referral at centurylinkyoucan.com</p></td>
	</tr>
	<tr>
		<td><p>partnering with the account&rsquo;s assigned salesperson, if you know who he or she is</p></td>
	</tr>
	<!-- start cris	-->
		<tr>
		<td width="25%" rowspan="10"><p>CRIS</p></td>
		<td width="25%" rowspan="4"><p>Residential</p></td>
		<td width="50%"><p>creating a referral at centurylinkyoucan.com</p></td>
	</tr>
	<tr>
		<td><p>partnering with a retail store, where available</p></td>
	</tr>
	<tr>
		<td><p>providing the customer YOUCAN approved collateral with your SAPID</p></td>
	</tr>
	<tr>
		<td><p>calling the Residential National Order Help Desk YOUCAN number with the customer on the line at 800.850.5252. If the customer isn&rsquo;t available use centurylinkyoucan.com instead.</p></td>
	</tr>
	<tr>
		<td width="25%" rowspan="4"><p>Small Business <br>&lt;\$500 monthly spend.</p></td>
		<td><p>creating a referral at centurylinkyoucan.com</p></td>
	</tr>
	<tr>
		<td><p>partnering with a retail store, where available</p></td>
	</tr>
	<tr>
		<td><p>providing the customer YOUCAN approved collateral with your SAPID</p></td>
	</tr>
	<tr>
		<td><p>calling the Small Business National Order Help Desk YOUCAN number with the customer on the line at 877.529.1558. If the customer isn&rsquo;t available use centurylinkyoucan.com instead.</p></td>
	</tr>
	<tr>
		<td width="25%" rowspan="2"><p>Commercial and Enterprise <br>&gt;\$500 monthly spend.</p></td>
		<td><p>creating a referral at centurylinkyoucan.com</p></td>
	</tr>
	<tr>
		<td><p>partnering with the account&rsquo;s assigned salesperson, if you know who he or she is</p></td>
	</tr>
</table>
<hr>
<p> <span class="news_header">What happens after I submit my lead to YOUCAN?</span> </p>
<p>Once your referral is created, you may follow its progress on the <a href="#" onClick="document.lead123.action='ref_hist.cgi';document.lead123.submit();">Referral History page</a>. Referrals at all stages in their lifecycle fall into one of these categories</p>
<!--	chevron5	-->

<table width="100%" border="1" cellspacing="0" cellpadding="0" class="reward-values" style="float:left" >
	<tr><td colspan="4">


<div id="breadcrumb3">
		<ul class="breadcrumb3" style="margin-left:-20px;padding-left:0;">
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Received&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;In Progress&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;Accuracy Check&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;Awarded &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	</ul>
</div>


<div id="breadcrumb2">
		<ul class="breadcrumb2" style="margin-left:-20px;padding-left:0;">
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Received&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;In Progress&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;Accuracy Check&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#">&nbsp;&nbsp;&nbsp;No Award&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
		</ul>
</div>
</td></tr>
<tr><td width="25%">
		<table width="100%">
			<tr><td><p>For Residential and Small Business referrals:</p>
					<ul>
						<li>Once YOUCAN receives your referral we route it to a salesperson to make an initial contact within two business days </li>
						<li>Most of YOUCAN&rsquo;s first calls are made much sooner, many on the same day the referral is received </li>
					</ul>
					<p>For Commercial and Enterprise referrals:</p>
					<ul>
						<li>Once YOUCAN receives your referral we route it to a salesperson in the Commercial and Enterprise teams. </li>
						<li>Your lead will be routed according to the information you provide. To ensure we promptly get the lead to the right salesperson, include as much information as possible including the business location, contact names and the product(s) the business is interested in.  </li>
					</ul>

				</td>
			</tr>
		</table>
	</td>
	<td width="25%">
		<table width="100%">
			<tr><td><p>For Residential and Small Business referrals:</p>
					<ul>
						<li>YOUCAN&rsquo;s sales team makes at least two attempts over multiple days to reach the customer you referred. We leave a voicemail with our number and instructions to call back when possible. </li>
						<li>You may see more detail viewing the <a href="#" onClick="document.lead123.action='ref_hist.cgi';document.lead123.submit();">Referral History Page</a>. </li>
					</ul>
					<p>For Commercial and Enterprise referrals:</p>
					<ul>
						<li>Some Commercial and Enterprise sales are very complex and may take weeks or months to complete. </li>
						<li>You may see more detail about referrals in progress by viewing your <a href="#" onClick="document.lead123.action='ref_hist.cgi';document.lead123.submit();">Referral History</a>. </li>
					</ul>
				</td>
			</tr>
		</table>
	</td>
	<td width="25%">
		<table width="100%">
			<tr><td>
					<p>Once a sale is made, we&rsquo;ll review the referral for accuracy.</p>
					<ul>
						<li>We may not complete our review until after the product(s) purchased are installed. This allows us to ensure the YOUCAN award is as accurate as possible. </li>
						<li>Once we complete our review, YOUCAN awards are generally distributed twice each month. The schedule is published on <a href="#" onClick="document.lead123.action='news.cgi';document.lead123.submit();">YOUCAN award calendar</a>.</li>
					</ul>
				
				</td>
			</tr>
		</table>
	</td>
	<td width="25%">
		<table width="100%">
			<tr><td><p>If this is your first sold referral, thank you!</p>
					<ul>
						<li>We&rsquo;ll send a reloadable Visa card to your home address on file with HR.  </li>
						<li>Cards arrive about two weeks after the award distribution date. Your future YOUCAN awards will be loaded to the same card on the distribution date.</li>
						<li>Remember that you will see the net value of the award on the card. Taxes are withheld. <a href="#" onClick="document.lead123.action='tax_info.cgi';document.lead123.submit();">Click here</a> for more information about YOUCAN awards and taxation. </li>
					</ul>
					<p>If you&rsquo;ve referred before and have a YOUCAN Visa card:</p>
					<ul>
						<li>Awards are loaded on or about the distribution date published on the <a href="#" onClick="document.lead123.action='news.cgi';document.lead123.submit();">YOUCAN award calendar</a>.  </li>
					</ul>
					<p>In the event your referral does not generate a qualified sale, we appreciate your perseverance and look forward to your next referral. An email with more information about the no&ndash;sale reason is on the way. </p>
				
				</td>
			</tr>
		</table>
	</td>
</tr>

</table>

<hr>

<p> <span class="news_header">How are Awards determined?</span> </p>
<ul>
	<li>YOUCAN Award values are posted on the Award Value page.</li>
	<li>YOUCAN bases the award for residential and small business referrals on the net new products or upgraded products that are generated by the YOUCAN salesperson from your YOUCAN referral.</li>
	<li>YOUCAN bases the award for Commercial and Enterprise referrals on the net increase in Monthly Recurring or Non - Recurring revenue. The Award Tiers for both MRR and NRR are posted on the Award Value page.</li>
	<li>Several exclusions and limitations apply. Common questions are explained on the <a href="#" onClick="document.lead123.action='res_biz_awards.cgi';document.lead123.submit();">Award Value page</a>.</li>
	<li>Once the Gross award value is determined, we&rsquo;ll calculate the Net and Taxable amounts and distribute the net value to your YOUCAN award card. More information about YOUCAN and Taxation is available <a href="#" onClick="document.lead123.action='tax_info.cgi';document.lead123.submit();">here</a>. 
	Our award calendar is located <a href="#" onClick="document.lead123.action='news.cgi';document.lead123.submit();">here</a>.</li>
</ul>
<hr>
<p> <span class="news_header">I still have questions.</span> </p>
<ul>
	<li>Answers to YOUCAN&rsquo;s most frequently asked questions are located <a href="#" onClick="document.lead123.action='faq.cgi';document.lead123.submit();">here</a>.</li>
	<li>Your supervisor may be able to provide you more information about YOUCAN.</li>
	<li>Otherwise, please let team YOUCAN know you have a question by sending us an <a href="#" onClick="document.lead123.action='contact.cgi';document.lead123.submit();">email</a>.</li>

</ul>

];

	return $str;

}

=head
<tr>
<td width="25%" class="leadcreated"><p>Received</p></td>
<td width="25%" class="progressLead"><p>In Progress</p></td>
<td width="25%" class="accuracyLead"><p>Accuracy Check</p></td>
<td width="25%" class="soldLead"><p>Awarded</p></td>
</tr>
<tr>
<td colspan="3" >&nbsp;</td>
<td width="25%" class="noawardLead" style="color:#A9AAA1;"><p>No Award</p></td>
</tr>

=cut