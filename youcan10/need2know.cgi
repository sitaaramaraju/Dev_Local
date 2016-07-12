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
require "D:/xroot/cgi-bin/init.cgi";
}else{
require "D:/xroot/cgi-bin/lp-init.pm";
$leadlink = 1;
}
my $myDB = Win32::ODBC->new($main::DSN);


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
require "D:/xroot/qwest/youcan10/youcan_header.cgi";
showhdr ($PAGETITLE, $session_id, $emplid);
print<<"EOF";
    </div><!--END LAYOUT-HEADER-->
    
    <div id="layout-body">
    	<div id="body-left-sec">
        	<div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2>YOU Need to Know</h2>
                </div>
                <div class="capsule-content">
                	<p>In this section you will find info on how to contact YOUCAN with general program questions, what tax implications come along with the YOUCAN program, Terms and Conditions, and YOUCAN policies and process.</p>
                </div>
            </div><!--END CAPSULE-->
            
            <div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2>YOUCAN General Contact Information</h2>
                </div>
                <div class="capsule-content"> 
                    <p>Please contact us at <a href="mailto:youcan\@centurylink.com?subject=YOUCAN Question">youcan\@centurylink.com</a> with general YOUCAN Program Questions. (To ensure you receive proper credit, do not submit referrals to this e-mail box.)</p>
                    <br class="clear" />
                </div>
            </div><!--END CAPSULE-->
            
            	
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
EOF
require "D:/xroot/qwest/youcan10/youcan_righttable.cgi";
show_rttbl  ($session_id, $emplid);
print<<"EOF";
        </div><!--END BODY-RIGHT-SEC-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
EOF
require "D:/xroot/qwest/youcan10/youcan_footer.cgi";
showftr ($session_id, $emplid);
print<<"EOF";
</div><!--END LAYOUT-->
</body>
</html>
EOF
$myDB ->Close();
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
