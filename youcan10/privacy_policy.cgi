use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

my $emplid = $cgi->param('emplid')||0;
my $session_id = $cgi->param('session_id')||0;

my $leadlink=0;
if ( $emplid == 0 ) {
require "G:/CenturyLink/xroot/cgi-bin/init.cgi";
}else{
require "G:/CenturyLink/xroot/cgi-bin/lp-init.pm";
$leadlink = 1;
}
require "G:/CenturyLink/xroot/cgi-bin/lp-prog-opts.pm";

if ($emplid==0) {
	$emplid= $main::session{staff_id};
}
my $myDB = Win32::ODBC->new($main::DSN);

my  $PAGETITLE = "YOUCAN | Deliver the VIP Experience";;
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
require "youcan_header.cgi";
showhdr ($PAGETITLE, $session_id, $emplid);
print<<"EOF";
    </div><!--END LAYOUT-HEADER-->  
    <div id="layout-body">
    	<div id="body-left-sec">
        	<div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2>Legal Notices</h2>
                </div>
                <div class="capsule-content">
                	<p><a href="tax-implications.html">YOUCAN Tax Implications</a></p>
                    <p><a href="assets/pdf/YOUCAN_ref_TC_amex.pdf" target="_blank">Terms and Conditions</a></p>
                    <p><a href="assets/pdf/Policy_Process_FINAL_12 12.pdf" target="_blank">Policies and Process</a></p>
                    <p><a href="assets/pdf/YC_Various_Emp_Gr_Guidelines_092008.pdf" target="_blank">Guideline Exceptions</a></p>
                    <p><a href="assets/pdf/TC_amex.pdf" target="_blank">YOUCAN American Express&reg; Branded Reward Card Terms and Conditions</a></p>
                </div>
            </div><!--END CAPSULE-->
            
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
        	<div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Referrals</h3>
                </div>
                <div class="capsule-content">
                	<p><a href="referral-create.html">Start a New Referral.</a></p>
                    <hr class="brk-grey" />
                    <p><a href="referral-history.html">View Referral History.</a></p>
                    <hr class="brk-grey" />
                    <p><a href="referral-report.html">Generate Referral Report.</a></p>
                </div>
            </div><!--END CAPSULE-->
            <div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Contests</h3>
                </div>
                <div class="capsule-content">
                	<p><a href="contest-details.html">Current Contest Details.</a></p>
                    <hr class="brk-grey" />
                    <p><a href="contest-winners.html">Contest Winners.</a></p>
                </div>
            </div><!--END CAPSULE-->
        </div><!--END BODY-RIGHT-SEC-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
    
    <div id="layout-footer">
    	<div id="footer-content">
        	<ul class="footer-links">
            	<li><a href="contact-us.html">Contact Us</a></li>
                <li> | </li>
                <li><a href="faq.html">FAQs</a></li>
                <li> | </li>
                <li><a href="site-map.html">Site Map</a></li>
            </ul>
            <ul class="footer-legal">
            	<li><a href="legal.html">Legal Notices</a></li>
                <li><a href="privacy-policy.html">Privacy Policy</a></li>
                <li>&copy; 2010 Qwest Communications International Inc. All Rights Reserved</li>
            </ul>
        </div><!--END FOOTER CONTENT-->
    </div><!--END LAYOUT-FOOTER-->

</div><!--END LAYOUT-->

</body>
</html>
EOF
$myDB ->Close();
undef &get_header;

# -------------------------------------------------------------------
sub get_header
{

	my %hash  = @_;
	my $title = $hash{title} || '';
	my $css   = $hash{css} || '';
	my $more  = $hash{more} || '';

	$css = "<link rel=\"stylesheet\" href=\"$css\" type=\"text/css\">\n" if $css;

	my $str = "Content-type: text/html\n\n";
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
