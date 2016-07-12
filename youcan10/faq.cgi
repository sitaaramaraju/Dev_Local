use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();
require "D:/centurylinkyoucan/youcan10/youcan_subs.cgi";
my $cci_id = $cgi->param('cci_id')||0;

#require "D:/centurylinkyoucan/cgi-bin/init.cgi";
my $url = CCICryptography::getUrl();
############## validation ################
my $valid = CCICryptography::validate_CL($cci_id);

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


my  $PAGETITLE = "YOUCAN | Deliver the VIP Experience ";
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;






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
                	<h2>Frequently Asked Questions (FAQ)</h2>
                </div>
                <div class="capsule-content">
                	<img src="assets/img/secondary/faq-qmark.gif" alt="FAQ's" class="right" />
                    <h4>The following questions about the YOUCAN Program are addressed here:</h4>
                    <p>
					<strong>Q:</strong> <a href="#Q1">How do I make a referral through YOUCAN?</a><br />
                    <strong>Q:</strong> <a href="#Q2">How will my rewards be taxed?</a><br />
                    <strong>Q:</strong> <a href="#Q3">When will I receive my rewards?</a><br />
                    <strong>Q:</strong> <a href="#Q4">When will I receive my YOUCAN card?</a><br /> 
					<strong>Q:</strong> <a href="#QN3">How do I update my home address in SAP/ESS?</a><br />
                    <strong>Q:</strong> <a href="#Q5">How can I check my YOUCAN card balance?</a><br /> 
                    <strong>Q:</strong> <a href="#Q6">I lost my YOUCAN card. How do I request a new one?</a><br /> 
                    <strong>Q:</strong> <a href="#Q7">How do I order business cards with YOUCAN information?</a><br /> 

                    <hr class="brk-grey" />
													
					

                    <p id="Q1" class="alt"><strong>Q: How do I make a referral through YOUCAN?</strong><br />
								<strong>A.</strong> There are several ways you can make a referral:
                                <ul>
                                    <li>Create a referral online at centurylinkyoucan.com and YOUCAN will contact your customer.</li>
                                    <li>Provide the customer information to your local Retail Store and a Retail Associate will contact your customer.(Residential/Small Business).</li>
									<li>Provide the customer information to your local Commercial Enterprise Business Seller and Seller will contact your customer (Commercial Enterprise Business) </li>
                                    <li>Other employee groups (Field Technicians, Repair, et cetera) have additional referral tools. See your supervisor for details.</li>
                                </ul></p>
                    
                    <p id="Q2"><strong>Q: How will my rewards be taxed?</strong><br />
                    <strong>A:</strong> Rewards are subject to tax. Withheld amounts will be deducted from award amounts prior to funds being loaded in your account. 
					          <a href="#" onClick="document.lead123.action='tax_info.cgi';document.lead123.submit();">Click here</a> for more information.</p>

                    <p id="Q3" class="alt"><strong>Q: When will I receive my rewards?</strong><br />
					<strong>A:</strong> If your referral was sold and passes our Accuracy Check Review between the first and 15th of a month, referral will generally be awarded around the first of the following month. Referral that was sold and passed our Accuracy Check Review between the 16th and end of the month will generally be awarded around the 15th of the following month. <a href="#" onClick="document.lead123.action='news.cgi';document.lead123.submit();">Click here</a> for the 2016 Award Calendar.<p>

                    <p id="Q4" ><strong>Q: When will I receive my YOUCAN card?</strong><br />
                    <strong>A:</strong> Your YOUCAN card will be sent to you after funds are loaded for your first sold referral. Please allow four to six weeks for delivery. The card is sent in a plain white envelope to your home address as listed in SAP/ESS. </p>

					<p id="QN3" class="alt"><strong>Q: How do I update my home address in SAP/ESS?</strong><br />
                    <strong>A:</strong> Visit the corporate homepage and click ESS/MSS. After logging in navigate to “Employee Self Service”, “Address, Work and Personal Phone Numbers.</p>
					
					<p id="Q5" ><strong>Q: How can I check my YOUCAN card balance?</strong><br />
                    <strong>A:</strong> Visit myprepaidcenter.com and enter the card number or call the number on the back of the card to use the automated system. </p>
                    <p id="Q6" class="alt"><strong>Q: I lost my YOUCAN card. How do I request a new one?</strong><br />
                    <strong>A:</strong> Should the card become lost or stolen, contact Customer Service at 1 877-227-0956 immediately. You may be asked for a Personal Identification Number (PID). This is your full alpha-numeric SAP ID. </p>
                    <p id="Q7"><strong>Q: How do I order business cards with YOUCAN information?</strong><br />
                    <strong>A:</strong> A version of CenturyLink business cards for technicians with YOUCAN toll free numbers is available on CenturyLink&rsquo;s Stationary website at <a href="http://qstat.faconline.com/qstat/default.aspx" target="_balnk"> http://qstat.faconline.com/qstat/default.aspx</a>. Navigate to the site and select Imprinted Stationary > CL Standard > Legacy Qwest YOUCAN or Legacy CTL YOUCAN Technician Business Card. Legacy Qwest (CRIS market) employees may use their CUID or SAPID in the CUID field. Use centurylink.com/refer in the WebRefer field. Please reach out to your supervisor with questions. 
					

                </div>
            </div><!--END CAPSULE-->	
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
EOF
#require "D:/CenturyLink/youcan10/youcan_righttable.cgi";
#require "G:/CenturyLink/xroot/qwest/youcan10/youcan_righttable.cgi";
show_rttbl  ($cci_id);
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

############################################################################
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
