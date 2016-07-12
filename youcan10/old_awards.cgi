use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');
my $emplid = 0;
my $cci_id = $cgi->param('cci_id')||0;


my  $PAGETITLE = "YOUCAN | Deliver the VIP Experience";;
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
#print $header;



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

<!--[if lt IE 8]> <script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE8.js"></script> <![endif]-->

</head>

<body>

		<div id="body-left-sec">
        	<div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2 id="how-to">Old Award Values</h2>
                </div>
                <div class="capsule-content">
                	<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
                      <tr class="green-bg">
                        <td><p><strong>Product Category</strong></p></td>
                        <td><p><strong>Product</strong></p></td>
                        <td><p><strong>Residential Award</strong></p></td>
                        <td><p><strong>Business Award</strong></p></td>
                      </tr>
                      <tr>
                        <td><p><strong>New Voice</strong></p></td>
                        <td><p>New Line<br /> <em>Includes new line and all voice features and products at point of sale</em></p></td>
                        <td><p>\$20</p></td>
                        <td><p>\$20</p></td>
                      </tr>
					  <tr class="alt">
                        <td>&nbsp;</td>
                        <td><p>New Core Connect<br /><em>Core Connect is a small business package that includes voice and HSI products</em> </p></td>
                        <td><p>NA</p></td>
                        <td><p>\$50</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>Market Expansion Line</p></td>
                        <td><p>NA</p></td>
                        <td><p>\$20</p></td>
                      </tr>
					  <tr class="alt">
                        <td>&nbsp;</td>
                        <td><p>Temporary Service<br />
						<em>Temporary Service is awarded for any service installed fewer than 90 days (including festivals, concerts and similar customers) and is awarded one payout per customer</em></p></td>
                        <td><p>NA</p></td>
                        <td><p>\$25</p></td>
                      </tr>
                      <tr>
                        <td><p><strong>Voice Feature</strong></p></td>
                        <td><p>Voice Features</p></td>
                        <td><p>\$3.50</p></td>
                        <td><p>\$3.50</p></td>
                      </tr>
                      <tr class="alt">
                        <td>&nbsp;</td>
                        <td><p>CenturyLink Long Distance</p></td>
                        <td><p>\$3.50</p></td>
                        <td><p>\$3.50</p></td>
                      </tr>
                      <tr >
                        <td>&nbsp;</td>
                        <td><p>Package/Bundle Upgrade</p></td>
                        <td><p>\$10</p></td>
                        <td><p>\$10</p></td>
                      </tr>
                      <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>Inside Wire Maintenance Plans</p></td>
                        <td><p>\$3.50</p></td>
                        <td><p>\$3.50</p></td>
                      </tr>

                      <tr>
                        <td><p><strong>Security</strong></p></td>
                        <td><p>Smart Home Security<br /> <em>Smart Home Security is available in select CenturyLink markets.</em></p></td>
                        <td><p>\$15</p></td>
                        <td><p>NA</p></td>
                      </tr>
<!--	security	-->
                      <tr class="alt">
                        <td><p>&nbsp;</p></td>
						<td><p>Security Monitoring <br /> <em>Security Monitoring is available in select CenturyLink markets </em></p></td>
                        <td><p>\$3.50</p></td>
                        <td><p>\$3.50</p></td>
                      </tr>

<!--	HSI	-->

                      <tr >
                        <td><p><strong>High Speed Internet</strong></p></td>
                        <td><p>New High Speed Internet<br /> <em>Smart Home Security is available in select CenturyLink markets</em></p></td>
                        <td><p>\$30</p></td>
                        <td><p>\$30</p></td>
                      </tr>
                      <tr class="alt">
                        <td>&nbsp;</td>
                        <td><p>HSI Speed Upgrade</p></td>
                        <td><p>\$10</p></td>
                        <td><p>\$10</p></td>
                      </tr>
					<tr>
                        <td>&nbsp;</td>
                        <td><p>CenturyLink \@Ease<br/><em>Standard, Advanced and Ultra packages</em></p></td>
                        <td><p>\$3.50</p></td>
                        <td><p>NA</p></td>
                      </tr>

                      <tr class="alt">
                        <td><p><strong>Video</strong></p></td>
                        <td><p>New DirecTV</p></td>
                        <td><p>\$15</p>
						</td>
                        <td><p>\$15</p>
						</td>
                      </tr>
					   <tr >
                        <td>&nbsp;</td>
                        <td><p>New Prism TV<br /><em>Prism TV is available in select CenturyLink markets</em> </p></td>
                        <td><p>\$30</p></td>
                        <td><p>\$30</p></td>
                      </tr>
					   <tr class="alt">
                        <td>&nbsp;</td>
                        <td><p>Prism Upgrade<br />
						<em>Prism TV Upgrade awards are limited to programming tier upgrades, upgrades to High Definition and limited to one upgrade award per customer</em></p></td>
                        <td><p>\$10</p></td>
                        <td><p>\$10</p></td>
                      </tr>
                      <tr>
                        <td><p><strong>Verizon Wireless</strong></p></td>
                        <td><p>Verizon Wireless Plan <br /><em>Includes all lines at the point of sale</em></p></td>
                        <td><p>\$10</p></td>
                        <td><p>\$10</p></td>
                      </tr>
                      <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>Verizon Wireless Mobile Broadband</p></td>
                        <td><p>\$10</p></td>
                        <td><p>\$10</p></td>
                      </tr>
<!--	-->
                      <tr>
                        <td><p><strong>Small Business Cloud and Managed Services</strong></p></td>
                        <td><p>Small Business Cloud - Grow</p></td>
                        <td><p>NA</p></td>
                        <td><p>\$20</p></td>
                      </tr>
                      <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>Small Business Cloud - Protect</p></td>
                        <td><p>NA</p></td>
                        <td><p>\$20</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>Small Business Cloud - Support</p></td>
                        <td><p>NA</p></td>
                        <td><p>\$20</p></td>
                      </tr>
<!--	-->

					  <tr   class="alt">
                        <td><p><strong>Business Monthly Recurring Revenue</strong></p></td>
                        <td><p>\$0 &ndash; \$24.99	</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>No Award</p></td>
                      </tr>
					  <tr   >
                        <td>&nbsp;</td>
                        <td><p>\$25 &ndash; \$99.99	</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$50</p></td>
                      </tr>
					  <tr class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$100 &ndash; \$249.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$75</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$250 &ndash; \$499.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$100</p></td>
                      </tr>
					  <tr   class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$500 &ndash; \$999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$150</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$1,000 &ndash; \$1,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$175</p></td>
                      </tr>
<!--	-->
					  <tr   class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$2,000 &ndash; \$2,499.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$200</p></td>
                      </tr>
					  <tr >
                        <td>&nbsp;</td>
                        <td><p>\$2,500 &ndash; \$2,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$300</p></td>
                      </tr>
					  <tr class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$3,000 and up</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$400</p></td>
                      </tr>
<!--	-->
					  <tr>
                        <td><p><strong>Business Non Recurring Revenue</strong></p></td>
                        <td><p>\$0 &ndash; \$99.99	</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>No Award</p></td>
                      </tr>
					  <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$100 &ndash; \$249.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$10</p></td>
                      </tr>
					  <tr >
                        <td>&nbsp;</td>
                        <td><p>\$250 &ndash; \$499.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$25</p></td>
                      </tr>
					  <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$500 &ndash; \$999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$40</p></td>
                      </tr>
					  <tr >
                        <td>&nbsp;</td>
                        <td><p>\$1,000 &ndash; \$2,499.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$50</p></td>
                      </tr>
					  <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$2,500 &ndash; \$4,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$75</p></td>
                      </tr>
					  <tr >
                        <td>&nbsp;</td>
                        <td><p>\$5,000 &ndash; \$9,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$100</p></td>
                      </tr>
					  <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$10,000 &ndash; \$24,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$125</p></td>
                      </tr>
					  <tr >
                        <td>&nbsp;</td>
                        <td><p>\$25,000 &ndash; \$49,999.99	</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$150</p></td>
                      </tr>
					  <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$50,000 &ndash; \$74,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$200</p></td>
                      </tr>
					  <tr>
                        <td>&nbsp;</td>
                        <td><p>\$75,000 &ndash; \$99,999.99</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$250</p></td>
                      </tr>
					  <tr  class="alt">
                        <td>&nbsp;</td>
                        <td><p>\$100,000 and up</p></td>
                        <td><p>&nbsp;</p></td>
                        <td><p>\$300</p></td>
                      </tr>
                    </table>
         			
                   
				</div>
            </div><!--END CAPSULE-->
            
        </div><!--END BODY-LEFT-SEC-->
        <br class="clear" />
EOF
#    </div><!--END LAYOUT-BODY-->

#require "G:/CenturyLink/xroot/qwest/youcan10/youcan_footer.cgi";
#showftr ($session_id, $emplid);
#</div><!--END LAYOUT-->

print<<"EOF";
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
