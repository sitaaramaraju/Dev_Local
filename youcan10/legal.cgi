use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||0;

my $valid = CCICryptography::validate_CL($cci_id);

my $leadlink=0;


my $myDB = DBInterface->new();

my $valid = CCICryptography::validate_CL($cci_id);
my $url = CCICryptography::getUrl();

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
                	<h2>Legal Notices</h2>
                </div>
                <div class="capsule-content">
					<p><a href="#" onClick="document.lead123.action='tax_info.cgi';document.lead123.submit();">YOUCAN Tax Implications</a></p>
                    <p><a href="pdf/YouCan_Terms_and_Conditions_2016_Final.pdf" target="_blank">Terms and Conditions</a></p>
                </div>
            </div><!--END CAPSULE-->
            
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
EOF

show_rttbl  ($cci_id);
print<<"EOF";
        </div><!--END BODY-RIGHT-SEC-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
EOF
#require "G:/CenturyLink/xroot/qwest/youcan10/youcan_footer.cgi";
showftr ($cci_id);

print<<"EOF";
</div><!--END LAYOUT-->

</body>
</html>
EOF
$myDB->disconnect();
undef &get_header;

# -------------------------------------------------------------------
sub get_header
{

	my %hash  = @_;
	my $title = $hash{title} || '';
	my $css   = $hash{css} || '';
	my $more  = $hash{more} || '';

	$css = "<link rel=\"stylesheet\" href=\"$css\" type=\"text/css\">\n" if $css;

	#my $str = "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
	my $str = <<EOF;
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
