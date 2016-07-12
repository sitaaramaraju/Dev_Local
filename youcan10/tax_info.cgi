use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();
require "D:/centurylinkyoucan/youcan10/youcan_subs.cgi";
my $cci_id = $cgi->param('cci_id')||0;


############## validation ################
	
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

########################################

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
<link type="text/css" href="assets/css/style_tax.css" rel="stylesheet" />
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
showhdr ($PAGETITLE, $cci_id);

print<<"EOF";
    </div><!--END LAYOUT-HEADER-->
    
    <div id="layout-body">
    	<div id="body-left-sec">
        	<div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2>Tax Implications</h2>
                </div>
                <div class="capsule-content">
                	<h4>YOUCAN Rewards and Tax Implications</h4>
					<p>YOUCAN rewards are paid through a reloadable YOUCAN Rewards card.  YOUCAN rewards are taxable. The net amount (your total YOUCAN earnings minus taxes) is loaded to your Rewards card.  The taxable amount is withheld and remitted to the IRS on your behalf through payroll withholding. </p>
					<p>The withholding rate is calculated according to IRS supplemental tax guidelines. The supplemental federal withholding rate is 25 percent. In addition, FICA, Medicare, state and local taxes will be withheld where applicable. </p>
					<p>Effective with the August 15, 2013 distribution of YOUCAN rewards, a separate payroll statement will be available to YOUCAN participants through the ESS link on CenturyLink&rsquo;s Intranet. In the past, as you earned YOUCAN awards a tax summary posted to future payroll statements. You will now receive a separate statement which will post to your ESS account semi-monthly for  payouts received through YOUCAN. Specifically, referrals that generate a sale from the 1st to the 15th of a month are paid on or about the 1st of the following month. Referrals sold on the 16th to the end of a month are paid on or about the 15th of the following month. The payroll awards statement will include a heading &ldquo;Prizes and Awards&rdquo; and detail the gross amount of the award and the applicable taxes withheld. 
					<u>As an example, and solely for illustration purposes of demonstrating the format of a payroll statement for awards:</u>
					A sample employee that earned \$180 in gross awards on a single YOUCAN award cycle would receive a payroll statement similar to this example. The total award (inclusive of all awards paid out for that &ldquo;period&rdquo;) is listed under Prizes and Awards. The withheld amount is listed under Total Taxes. The net pay does not appear on the statement but is the difference between the total gross and total taxes. Your YOUCAN Rewards card balance and transaction history is available at
					<a href="https://www.myprepaidcenter.com" target="_blank">www.myprepaidcenter.com</a>. Your tax rate will likely be different than what appears in this example. </p><br>

					<table width="100%" border="1" cellspacing="0" cellpadding="0" style="border-color:Black;" >
                      <tr >
                        <td align="center" valign="center"><p>
								<strong>SAMPLE YOUCAN PAYROLL STATEMENT</strong></p></td>
                     </tr>
					 <tr>
					 <td>
						<table width="100%" border="1" cellspacing="0" cellpadding="0" style="border-color:Black;">
						<tr style="border-color:Black;">
							<td width="50%" align="center" valign="center" style="border-color:Black;"><p><strong>EARNINGS AND OTHER PAYMENTS</strong></p>
							</td>
							<td width="50%" align="center" valign="center" style="border-color:Black;"><p><strong>TAXES AND OTHER DEDUCTIONS</strong></p>
							</td>
						</tr>
						<!-- next line	-->
						<tr style="border-color:Black;">
							<td width="50%" align="left" valign="center" style="border-color:Black;">
								<span style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;">
								<strong>&nbsp;<u>EARNINGS</u></strong></span>
							</td>
							<td width="50%" valign="center" style="border-color:Black;">
								<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" ><strong><u>
									TAXES</u></strong></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" ><strong><u>
									CURRENT</u></strong></span>
							</td>
						</tr>
						<!-- next line	-->
						<tr style="border-color:Black;">
							<td width="50%"  valign="center" style="border-color:Black;">
								<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;PRIZES & AWARDS
									</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >
									180.00</span>

							<br> &nbsp;
							<br> &nbsp;
							<br>
								<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >
									<strong>&nbsp; TOTAL GROSS</strong>
									</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" ><strong>
									180.00</strong></span>
							</td>
							<td width="50%" valign="center" style="border-color:Black;">
								<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;FEDERAL WITHHOLDING
									</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >45.00</span>

							<br>
							<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;SOCIAL SECURITY
									</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >11.16</span>
							<br>
							<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;MEDICARE
									</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >2.61</span>
							<br>
							<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;
							<strong>TOTAL TAXES</strong>
									</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >
								<strong>58.77</strong></span>
							</td>
							<!--	next block	-->
							<tr style="border-color:Black;">
								<td width="50%" valign="center" style="border-color:Black;">
								<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;<strong><u>SUMMARY
									</u></strong></span>

							<br>
							<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;TOTAL GROSS
									</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >180.00</span>
							<br>
							<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;TOTAL TAXES
									</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
									&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
								<span align="right" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >58.77</span>
							<br>
							<span align="left" style="font-family:Helvetica, Arial, sans-serif; font-size:14px; line-height:18px;" >&nbsp;
							<strong>NET PAY</strong>
									</span><br>
							</td>
							<!-- right side	-->

								<td width="50%" valign="center" style="border-color:Black;">&nbsp;

							<br> &nbsp;
							<br> &nbsp;
							<br> &nbsp;
							
							</td>

						</tr>
						</table>
					</td>
					</tr>
                      
					  </table>
					  <br>
					<p>If you have any additional questions regarding YOUCAN rewards, talk with your supervisors or contact YOUCAN Program Headquarters at 1 866-896-8226. If you have questions regarding how earnings from YOUCAN will affect your gross income or tax bracket, please consult your tax advisor.</p>
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
#require "D:/CenturyLink/youcan10/youcan_footer.cgi";
#require "G:/CenturyLink/xroot/qwest/youcan10/youcan_footer.cgi";
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
