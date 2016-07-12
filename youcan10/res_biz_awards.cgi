use strict;       # Require all variables to be scoped explicitly
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
use CCICryptography;
my $cgi = CGI->new();
require "D:/centurylinkyoucan/youcan10/youcan_subs.cgi";
my $cci_id = $cgi->param('cci_id')||'';

my $leadlink=0;


#require "D:/centurylinkyoucan/cgi-bin/init.cgi";

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
                	<h2 id="how-to">Award Values</h2>
                </div>
                <div class="capsule-content">
				<p><strong>Awards Effective January 1, 2016</strong></p>
				<p><em>Program modifications on January 1, 2016 changed product and values on several awards.</em><br><br>To review earlier award values for referrals created:</p>
				<p><em> Before September 1, 2015: Please click here <a href="#" onclick="openModalLarge('old_awards.cgi');return false;">Click here</a></em><br />
				<em> September 1, 2015 through December 31, 2015: Please click here <a href="#" onclick="openModalLarge('old_awards_Sep2015-Dec2015.cgi');return false;">Click here</a></em></p>
                	<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
                      <tr class="green-bg">
                        <td><p><strong>Product Category</strong></p></td>
                        <td><p><strong>Product</strong></p></td>
                        <td><p><strong>Residential Award</strong></p></td>
                        <td><p><strong>Business Award</strong></p></td>
                      </tr>
<!-- HIS	-->				  
						<tr class="alt">
                        <td><p><strong>HSI</strong></p></td>
                        <td><p><strong>New High Speed Internet (Pure/Standalone and Traditional)</strong></p></td>
                        <td><p>\$30.00</p></td>
                        <td><p>\$30.00</p></td>
                      </tr>
					  
					  <tr>
						<td><p>&nbsp;</p></td>
                        <td><p><strong>Upgrade - High Speed Internet</strong></p></td>
                        <td><p>\$10.00</p></td>
                        <td><p>\$10.00</p></td>
                      </tr>
					  
					  <tr  class="alt">
						<td><p>&nbsp;</p></td>
                        <td><p><strong>CenturyLink \@Ease</strong><br><em>Standard, Advanced and Ultra packages</br></em></p></td>
						<td><p>\$3.50</p></td>
                        <td><p>\$3.50</p></td>
                      </tr>


					  <tr>
						<td><p>&nbsp;</p></td>
                        <td><p><strong>High Speed Internet Tech Install (Field Technicians only)</strong>
						<br><em>For more details, <a href="pdf/042816_HSI_Tech_Install_Process.pdf" target="_blank">click here</a></em>

						<br><em>Tech Lite Install, Standard Install or Upgrade from Tech Lite Install to Standard Install</em></p></td>
						<td><p>\$5.00</p></td>
                        <td><p>\$5.00</p></td>
                      </tr>

					  

<!-- Voice	-->									  
                      <tr >
                        <td><p><strong>Voice</strong></p></td>
                        <td><p><strong>New Voice Line and Features</strong><em><strong>(including Digital Home Phone)</strong><em><br /> <em> New line and all voice features and products at point of sale </em></p></td>
                        <td><p>\$20.00</p></td>
                        <td><p>\$20.00</p></td>
                      </tr>
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p><strong>Upgrade - Voice Package/Bundle</strong></p></td>
                        <td><p>\$10.00</p></td>
                        <td><p>\$10.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p><strong>Market Expansion Line</strong></p></td>
                        <td><p>n/a</p></td>
                        <td><p>\$20.00</p></td>
                      </tr>
<!-- Video	-->									
					<tr  class="alt">
                        <td><p><strong>Video</strong></p></td>
                        <td><p><strong>New Prism TV</strong><br /><em>Available in select CenturyLink markets</em> </p></td>
                        <td><p>\$30.00</p>
						</td>
                        <td><p>\$30.00</p>
						</td>
                      </tr>
					   <tr>
                        <td>&nbsp;</td>
                        <td><p><strong>Upgrade - Prism TV</strong><br /><em>Programming tier upgrades, upgrades to High Definition and limited to one upgrade award per customer</em> </p></td>
                        <td><p>\$10.00</p></td>
                        <td><p>\$10.00</p></td>
                      </tr>
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p><strong>New DirecTV</strong></p></td>
                        <td><p>\$15.00</p></td>
                        <td><p>\$15.00</p></td>
                      </tr>
<!--  security -->					  
					
					  <tr>
                        <td><p><strong>Security</strong></p></td>
                        <td><p><strong>Smart Home Security</strong><br /> <em>Available in select CenturyLink markets</em></p></td>
                        <td><p>\$15.00</p></td>
                        <td><p>n/a</p></td>
                      </tr>
					  <tr  class="alt">
                        <td><p>&nbsp;</p></td>
                        <td><p><strong>Smart Home Security - Monitoring</strong></p></td>
                        <td><p>\$3.50</p></td>
                        <td><p>n/a</p></td>
                      </tr>
 
<!--	Cloud	-->
                      <tr>
                        <td><p><strong>Cloud</strong></p></td>
                        <td><p><strong>Small Business a la carte Cloud Services</strong><br><em>McAfee, Backup, Microsoft Office 365.<br /> Per service/license.</em></br></p></td>
                        <td><p>n/a</p></td>
                        <td><p>\$5.00</p></td>
                      </tr>
                     			  
					    <tr  class="alt" >
                        <td><p><strong>Business Monthly Recurring Revenue(MRR)</strong></p></td>
                        <td><p>\$0 &ndash; \$24.99	</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>No Award</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$25 &ndash; \$99.99	</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$50.00</p></td>
                      </tr>
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p>\$100 &ndash; \$249.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$75.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$250 &ndash; \$499.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$100.00</p></td>
                      </tr>
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p>\$500 &ndash; \$999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$150.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$1,000 &ndash; \$1,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$175.00</p></td>
                      </tr>
<!--	-->
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p>\$2,000 &ndash; \$2,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$200.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$3,000 &ndash; \$3,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$300.00</p></td>
                      </tr>
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p>\$4,000+</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$400.00</p></td>
                      </tr>
<!--	-->
					  <tr>
                        <td><p><strong>Business Non Recurring Revenue (NRR)</strong></p></td>
                        <td><p>\$0 &ndash; \$99.99	</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>No Award</p></td>
                      </tr>
					  <tr   class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$100 &ndash; \$249.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$10.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$250 &ndash; \$499.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$25.00</p></td>
                      </tr>
					  <tr   class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$500 &ndash; \$999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$40.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$1,000 &ndash; \$2,499.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$50.00</p></td>
                      </tr>
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p>\$2,500 &ndash; \$4,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$75.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$5,000 &ndash; \$9,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$100.00</p></td>
                      </tr>
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p>\$10,000 &ndash; \$24,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$125.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$25,000 &ndash; \$49,999.99	</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$150.00</p></td>
                      </tr>
					  <tr  class="alt"  >
                        <td>&nbsp;</td>
                        <td><p>\$50,000 &ndash; \$74,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$200.00</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$75,000 &ndash; \$99,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$250.00</p></td>
                      </tr>
					  <tr  class="alt" >
                        <td>&nbsp;</td>
                        <td><p>\$100,000+</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$300.00</p></td>
                      </tr>
					  
                    </table>
         			
                   
				</div>
            </div><!--END CAPSULE-->
            
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
        	<div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Notes</h3>
                </div>
                <div class="capsule-content">
                	<ul>
                    	<li>The award for a new Voice Line includes all voice line add-ons at the point of sale (for example: long distance, a package or calling features).</li>
<li>Self Referrals from CenturyLink employees and any referral where the customer receives an employee discount or retiree concession do not qualify for a YOUCAN award.</li>  
<li>Commercial and Enterprise products listed here (for example: new voice or High Speed internet) will be processed using the standard YOUCAN award for that product. Commercial and Enterprise products not listed here (for example, T1 lines, equipment) will be processed using the net revenue increase and non-recurring charge award tiers. 
</li>
                    </ul>
                </div>

            </div><!--END CAPSULE-->


            
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
