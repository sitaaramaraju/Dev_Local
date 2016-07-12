use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use Try::Tiny;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||0;

my $valid = CCICryptography::validate_CL($cci_id);
my $url = CCICryptography::getUrl();

my $myDB = DBInterface->new();

my ($id,$emplid) = CCICryptography::getEmpid($cci_id); 

if ($valid <= 0) {
print<<"EOF";
$ENV{SERVER_PROTOCOL} 200 OK
Content-Type: text/html

<!--<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">-->
<!-- (c) 2001-2016 CCI -->
<script language='javascript'>
    window.alert('Your session has expired. Please login again. Thank You.');
    document.location="$url";
</script>
EOF
exit();

}
my $thisfile = "my_youcan.cgi";
my  $PAGETITLE = "YOUCAN | Deliver the VIP Experience";;
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;
# below to be checked
my ($sql, $data, $bare, $bare_msg, $sth);
my ($id,$emplid ) = CCICryptography::getEmpid($cci_id);
if ($emplid > 0) {
$sql = "select  sales_indicator from qwesthr with (nolock) where emplid = ? ";
#############
try {
$sth = $myDB->prepare($sql);
$sth->execute($emplid) or die $sth->errstr;
$data = $sth->fetchrow_hashref();
$sth->finish();
}
catch {
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############
$bare = uc($data->{sales_indicator});
############
$bare_msg = "<p><strong>Your Eligibility code is &ldquo;$bare&rdquo;</strong></p> ";
if ($bare eq 'A') {
 $bare_msg .="<p>You are eligible to receive credit for business and residential referrals.";
}elsif ($bare eq 'B'){
 $bare_msg .="<p>You are eligible to receive credit for business referrals.";
}elsif($bare eq 'E'){
 $bare_msg ="<p>You are not eligible to participate in the YOUCAN program because you sell on behalf of the YOUCAN program, are a business and residential salesperson or a program administrator.";
}elsif($bare eq 'R'){
 $bare_msg .="<p>You are eligible to receive credit for residential referrals."
	}
$bare_msg .="<br>For more information about eligibility, refer to the information on the right.</p>"
}
else {
$bare_msg = "<p>Due to being compensated for referrals and to ensure it does not affect your normal job functions, we have some eligibilty codes attached to every employee name. Below is the code and their definitions. 
	If you are unsure what code you have or need further explanation, please contact the YOUCAN program HQ at 1 866-896-8226, option 3.</p>";
}

=head
my $sql = "select youcanyear, soldreferrals, revenue, participation, convert(varchar,updatedate,1) as updatedate from qwest_youcan_stats with (nolock)";

$myDB->Sql($sql);
$myDB->FetchRow();
my %prog = $myDB->DataHash();
############
my $sth = $myDB->prepare($sql);
$sth->execute();
my $prog = $sth->fetchrow_hashref();
############
my $cnt_stat = $prog->{'cnt'};
my $year = $prog->{youcanyear};
my $soldref = CommaFormatted($prog->{soldreferrals});
my $revenue = CCurr($prog->{revenue});
my $participation = $prog->{participation};
my $updatedate = $prog->{updatedate};
=cut
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
showhdr ($PAGETITLE,$cci_id);
print<<"EOF";
    </div><!--END LAYOUT-HEADER-->
    
    <div id="layout-body">
    	<div id="body-left-sec">
        	<div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2>My YOUCAN</h2>
                </div>
                <div class="capsule-content">
                	<h4>Program Eligibility</h4>
                    $bare_msg
                    <br />

                        
				</div>
            </div><!--END CAPSULE-->
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
        	<div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Program Eligibility</h3>
                </div>
                <div class="capsule-content">
                	<p><strong>B.</strong></p>
                    <small>Consumer Representatives who identify referral needs from a business in the community may submit referrals to YOUCAN through the YOUCAN website at centurylinkyoucan.com</small>
                    <p><strong>E.</strong></p>
                    <small>Designates that the employee is excluded from submitting referrals. Employees who are on sales compensation for selling residential AND business products are in this category, as well as YOUCAN and Retail staff.</small>
                    <p><strong>A.</strong></p>
                    <small>Designates that the employee can refer customers for ALL eligible YOUCAN products. Employees who are not on any type of sales compensation for selling CenturyLink products are in this category.</small>
                    <p><strong>R.</strong></p>
                    <small>Business Representatives who identify referral needs from a friend, neighbor or family member may submit referrals to YOUCAN through the YOUCAN website at centurylinkyoucan.com.</small>
                </div>
            </div><!--END CAPSULE-->

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
$myDB->disconnect();
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
sub CommaFormatted        #06/27/07 9:28:AM
 {
	my $delimiter = ','; # replace comma if desired
	my($n,$d) = split /\./,shift,2;
	my @a = ();
	while($n =~ /\d\d\d\d/)
	{
		$n =~ s/(\d\d\d)$//;
		unshift @a,$1;
	}
	unshift @a,$n;
	$n = join $delimiter,@a;
	$n = "$n\.$d" if $d =~ /\d/;
	return $n;
}   ##hold

############################################################################
sub CCurr
# Function CCurr takes any number as an argument and returns it formatted as
# U.S. currency
############################################################################
{
    my ($cents, $cents_formatted, $dollars, $result, $pos, $sign, $curr_symbol);
    if ( exists $main::session{curr_sym} && length($main::session{curr_sym}) > 0 ) {
        $curr_symbol = $main::session{curr_sym};
    }else{
        $curr_symbol = "\$";
    }

	my $val = $_[0];
	if ($val !~ /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/ && length($val) > 0) {
 		return "NaN";
	}
	$sign = ($val < 0) ? '-':'';
	$dollars = int($val = int((abs($val) * 100.0) + 0.5) / 100.0);
	$sign = '' if ($val == 0.00);
    $cents = $val - $dollars;

    #Format cents
    $cents_formatted = substr((sprintf "%.2f", $cents), -2, 2);
    #Insert commas in dollar value
    $result = "";
    $pos = 0;
    while ($dollars ne "") {
        $pos = $pos + 1;
        if ($pos == 4) {
            $result = chop($dollars) . "," . $result;
            $pos = 1;
            }
        else {
            $result = chop($dollars) . $result;
        }
    }
    return "$curr_symbol".$sign.$result.".".$cents_formatted;
}
############################################################################
