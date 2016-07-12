use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();
require "D:/centurylinkyoucan/youcan10/youcan_subs.cgi";
my $cci_id = $cgi->param('cci_id')||0;

my $url = CCICryptography::getUrl();

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
<script type="text/javascript" src="assets/js/youcan_functions.js"></script>
		<script type="text/javascript" src="../../jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="../../jquery/simplemodal/simplemodal.css"/>
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
<style>
    
    .news_header {
        color:black;
        font-size:125%;  
        font-weight:bold; 
    }
</style>
</head>

<body>
<div id="layout">

	<div id="layout-header">
EOF
require "D:/centurylinkyoucan/youcan10/youcan_header.cgi";
#require "youcan_header.cgi";
showhdr ($PAGETITLE, $cci_id);

print<<"EOF";
    </div><!--END LAYOUT-HEADER-->
    
    <div id="layout-body">
    	<div id="body-left-sec">
            
            <div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2 id="announcements">YOUCAN News</h2>
                </div>
                <div class="capsule-content">
     <p><span class="news_header">Referral History Function Restored &#40;June 14&#41;</span></p>
	 <p>Participants &ndash; the Referral history function has been restored. To check your referral status and history, go to your &ldquo;My YOUCAN&rdquo; page and select link &ldquo;Referral History&rdquo; or <a href="#" onClick="document.lead123.action='ref_hist.cgi';document.lead123.submit();">click here</a>. </p>

<hr>
     <p><span class="news_header"><a href="#" onClick="document.lead123.action='res_biz_awards.cgi';document.lead123.submit();">2016 Award Values effective January 1, 2016</a></span></p>

<hr>
<p><span class="news_header" id="septChanges" > YOUCAN Changes Effective September 1, 2015</span></p>
<p>Please click <a href="pdf/YOUCAN_changes_Sept_2015.pdf" target="_balnk">here</a> to review changes.</p>
<hr>
<p>
<span class="news_header" id="awardCal">2016 YOUCAN Award Calendar </span>
</p>
<p>YOUCAN is modifying some 2016 award payout dates to accommodate holiday schedules of our award processing partners. The calendar below is subject to change. </p>
<p>
<table width="100%" border="1" cellspacing="0" cellpadding="0" class="reward-values">
<tr>
<td width="66%"><p><strong>If your referral was sold and our Accuracy Check review is complete between...</strong></p></td>
<td width="33%"><p><strong>It will be awarded on or about...</strong></p></td>
</tr>

<tr><td width="33%" ><p>March 16 &ndash; March 31</p></td><td width="33%"><p>April 22, 2016</p></td></tr>
<tr><td width="33%" ><p>April 1 &ndash; April 15</p></td><td width="33%"><p>May 6, 2016</p></td></tr>
<tr><td width="33%" ><p>April 16 &ndash; April 30</p></td><td width="33%"><p>May 20, 2016</p></td></tr>
<tr><td width="33%" ><p>May 1 &ndash; May 15</p></td><td width="33%"><p>June 6, 2016</p></td></tr>
<tr><td width="33%" ><p>May 16 &ndash; May 31</p></td><td width="33%"><p>June 17, 2016</p></td></tr>
<tr><td width="33%" ><p>June 1 &ndash; June 15</p></td><td width="33%"><p>July 1, 2016</p></td></tr>

<tr><td width="33%" ><p>July 16 &ndash; July 30</p></td><td width="33%"><p>July 18, 2016</p></td></tr>

</table>
<hr>
<p><span class="news_header" id="mobwebsite">YOUCAN Mobile Website News</span></p>
<p>The YOUCAN Mobile Website has been decommissioned at this time. We will be developing a new mobile website in the future. </p>
<hr>
<p>
<span class="news_header">Get 5% Back With Select Merchants</span>
<p>
Starting September 16th, 2013 you can get 5% back when you use your YOUCAN Visa(R) card at select merchants. Click <a href="pdf/5-back.pdf" target="_balnk"> here </a> for full details.</p> 
<hr>
<p>
<span class="news_header">How to create Referrals</span>
<p>
<p>
<table width="100%" border="1" cellspacing="0" cellpadding="0" class="reward-values">
<tr>
<td width="50%"><p>How do I ...</p></td>
<td width="50%"><p>How</p></td>
</tr>

<tr>
<td width="50%"><p>Create a Small Business Referral?</p></td>
<td width="50%"><p>Create a lead at centurylinkyoucan.com</p></td>
</tr>
<tr>
<td width="50%"><p>Create a Residential Referral?</p></td>
<td width="50%"><p>Create a lead at centurylinkyoucan.com</p></td>
</tr>
<tr>
<td width="50%"><p>Create a Large Business or Mid-Markets Referral?</p></td>
<td width="50%"><p>Create a lead at centurylinkyoucan.com</p></td>
</tr>
<tr>
<td width="50%"><p>Check on the status of my Legacy Qwest / CRIS Market Referral?</p></td>
<td width="50%"><p>Write to youcan\@centurylink.com</p></td>
</tr>
<tr>
<td width="50%"><p>Check on the status of my Legacy CenturyLink Territory/ Ensemble Market Referral?</p></td>
<td width="50%"><p>Write to youcan.ensemble\@centurylink.com</p></td>
</tr>
</table>

<hr>
<p>
<span class="news_header">YOUCAN Team</span>
</p>
<table width="100%" border="1" cellspacing="0" cellpadding="0" class="reward-values">
<tr>
<td width="35%"><p>YOUCAN Program Strategy Manager</p></td>
<td width="25%"><p>Kristie Van Engelen</p></td>
<td width="30%"><p><a href="mailto:KRISTIE.VANENGELEN\@CENTURYLINK.COM">Kristie.Vanengelen\@CenturyLink.com</a></p></td>
<td width="10%"><p>602.716.3685</p></td>
</tr>
<tr>
<td width="35%"><p>YOUCAN Program Manager-Stakeholders</p></td>
<td width="25%"><p>Tami (Cordova) Ward</p></td>
<td width="30%"><p><a href="mailto:TAMI.CORDOVA\@CENTURYLINK.COM">Tami.Cordova\@CenturyLink.com</a></p></td>
<td width="10%"><p>602.630.0023</p></td>
</tr>
<tr>
<td width="35%"><p>YOUCAN Advocate Support &amp; Escalations</p></td>
<td width="25%"><p>Rachel Kirk</p></td>
<td width="30%"><p><a href="mailto:RACHEL.KIRK\@CENTURYLINK.COM">Rachel.Kirk\@CenturyLink.com</a></p></td>
<td width="10%"><p>303.664.7174</p></td>
</tr>
<tr>
<td width="35%"><p>YOUCAN Data and Analytics</p></td>
<td width="25%"><p>Don Swick</p></td>
<td width="30%"><p><a href="mailto:Don.Swick\@CenturyLink.com">Don.Swick\@CenturyLink.com</a></p></td>
<td width="10%"><p>602.716.3663</p></td>
</tr>

</table>

                </div>
            </div><!--END CAPSULE-->
            	
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
EOF

show_rttbl  ($cci_id);

print<<"EOF";        
           &nbsp; 
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
