use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
my $emplid = $cgi->param('eid')||0;
my $session_id = $cgi->param('session_id')||0;

require "G:/CenturyLink/xroot/cgi-bin/init.cgi";
my $myDB = Win32::ODBC->new($main::DSN);
my $myDB2 =  Win32::ODBC->new($main::DSN);

my  $PAGETITLE = 'CenturyLink Business - Tech Service Tool';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;




print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<title>$PAGETITLE</title>

<!--FAVICON-->
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<!--CSS-->
<link type="text/css" href="assets/css/style.css" rel="stylesheet" title="print" media="screen" />
<!--JAVASCRIPT-->
<!--	cci	-->
		<script  type="text/javascript" src="/jquery/jquery.js"></script>
		<script  type="text/javascript" src="/jquery/jquery-ui.js"></script>
		<script  type="text/javascript" src="/jquery/jmenu/js/jmenu.js"></script>
		<script  type="text/javascript" src="/jquery/simplemodal/simplemodal.js"></script>
<!--	cci complete	-->
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="assets/js/functions.js"></script>
<script type="text/javascript" src="assets/js/sbgvalidate.js"></script>
<script type="text/javascript">
	\$(document).ready(function(){
		\$(".inline").colorbox({inline:true, width:"90%"});
	});
</script>
<!--[if lte IE 7]>
	<script type="text/javascript" src="assets/js/ie-fix.js"></script>
<![endif]-->
</head>
<body>
<div id="layout">
	<div id="layout-header">
    	<a class="inline right button-contentmap" href="#popup">Content Map</a>
    	<h1>CenturyLink Business</h1>
    </div><!--END LAYOUT-HEADER-->
    <div id="layout-body">
    	<div id="body-left">
            <h2>Send a Follow Up</h2>
            <p class="orange"><em>*required field</em></p>
            <h3>Step 1. Recipient Information</h3>
            <form action="" method="get">
                <table width="100%" border="0" class="form-table">
                  <tr>
                    <td width="38%" align="right"><p>
                      <label for="company-name"><span class="orange">*</span>Company Name</label></p></td>
                    <td width="62%"><input name="company-name" id="company-name" type="text" tabindex="1" class="text-field"/></td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="first-name"><span class="orange">*</span>Recipient First Name</label></p></td>
                    <td><input name="first-name" id="first-name" type="text" tabindex="2" class="text-field"/></td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="last-name"><span class="orange">*</span>Recipient Last Name</label></p></td>
                    <td><input name="last-name" id="last-name" type="text" tabindex="3" class="text-field"/></td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="email"><span class="orange">*</span>Recipient Email Address</label></p></td>
                    <td><input name="email" id="email" type="text" tabindex="4" class="text-field"/></td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="address">Recipient Address</label></p></td>
                    <td><input name="address" id="address" type="text" tabindex="5" class="text-field"/></td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="city">Recipient City</label></p></td>
                    <td><input name="city" id="city" type="text" tabindex="6" class="text-field"/></td>
                  </tr>
                  <tr>
                    <td align="right"><p>Recipient State</p></td>
                    <td><select name="state" tabindex="7" class="drop-down">
					<option value="" selected="selected">Select...</option>

];

my $sql = "select  state, abbreviation from lp_states with (nolock) where program_id = 154 order by state ";
my %data;
$myDB->Sql($sql);
while ($myDB->FetchRow()) {
	%data = $myDB->DataHash();

	print qq[  <option value=\"$data{abbreviation}\">$data{state}</option> ];

}

print qq[
                    </select>
                    </td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="zipcode">Recipient Zipcode</label></p></td>
                    <td><input name="zipcode" id="zipcode" type="text" tabindex="8" class="text-field"/></td>
                  </tr>
                  <tr>
                    <td align="right"><p>Opportunity Type</p></td>
                    <td><p><label><input type="radio" name="opportunitytype" value="new connect" id="RadioGroup1_0" class="radio-button"/> New Connect</label><br />
                      	   <label><input type="radio" name="opportunitytype" value="upsell" id="RadioGroup1_1" class="radio-button"/> Upsell</label><br />
                      	   <label><input type="radio" name="opportunitytype" value="technology discussion" id="RadioGroup1_2" class="radio-button"/> Technology Discussion</label><br />
                    	</p>
                    </td>
                  </tr>
                </table>
                <hr />
                <h3>Step 2. Theme Selection <small class="orange"><em>must select one</em></small></h3>
                <table width="100%" border="0" class="form-table">
                  <tr>
                  	<td><a class="inline button-contentmap" href="#popup">Content Map</a></td>
                  </tr>
];
my ($sql2, %data2);
$sql2="select theme_id, RTRIM(description) as description from ctl_sbgEmail_theme with (nolock) where is_active = 1 order by theme_id";
my $id = '';
my $description = '';
print qq[<!--	$sql2	-->];
$myDB2->Sql($sql2);
while ($myDB2->FetchRow()) {
	%data2 = $myDB2->DataHash();
	$id= 'RadioGroup2_'.$data2{theme_id};
	$description = $data2{description};

 print qq[ <tr><td><p><label><input type="radio" name="theme" value="$description" id="$id" class="radio-button"/>$description</label></p></td></tr>];
}
#print qq[<!--	$id	-->];

print qq[

                </table>
                <hr />
                <h3>Step 3. Topic Selection <small class="orange"><em>must select one or more</em></small></h3>
            <!--GENERAL PRODUCT INFORMATION-->
				<table width="100%" border="0" id="topic-1" class="form-table">
                  <tr>
                    <td width="50%"><p style="margin-bottom:2px;"><label for="t1-core-connect"><input name="t1-core-connect" id="t1-core-connect" type="checkbox" value="" /> Core Connect</label></p>
                    				<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td width="50%"><p style="margin-bottom:2px;"><label for="t1-high-speed-internet"><input name="t1-high-speed-internet" id="t1-high-speed-internet" type="checkbox" value="" /> High-Speed Internet</label></p>
                    				<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                  </tr>
                  <tr>
                    <td><p style="margin-bottom:2px;"><label for="t1-voice-packages"><input name="t1-voice-packages" id="t1-voice-packages" type="checkbox" value="" /> Voice Packages</label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td><p style="margin-bottom:2px;"><label for="t1-voice-packages-az"><input name="t1-voice-packages-az" id="t1-voice-packages-az" type="checkbox" value="" /> Voice Packages - AZ</label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                  </tr>
                  <tr>
                    <td><p style="margin-bottom:2px;"><label for="t1-grow-packs"><input name="t1-grow-packs" id="t1-grow-packs" type="checkbox" value="" /> Grow Packs</label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td>&nbsp;</td>
                  </tr>
                </table>
            <!--MARKETING YOUR BUSINESS OPTIONS-->
				<table width="100%" border="0" id="topic-2" class="form-table">
                  <tr>
                    <td width="50%"><p style="margin-bottom:2px;"><label for="t2-marketing-online"><input name="t2-marketing-online" id="t2-marketing-online" type="checkbox" value="" /> Marketing Online</label></p>
                    				<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td width="50%"><p style="margin-bottom:2px;"><label for="t2-crm"><input name="t2-crm" id="t2-crm" type="checkbox" value="" /> CRM</label></p>
                    				<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                  </tr>
                  <tr>
                    <td><p style="margin-bottom:2px;"><label for="t2-social-media"><input name="t2-social-media" id="t2-social-media" type="checkbox" value="" /> Social Media</label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td><p style="margin-bottom:2px;"><label for="t2-measuring-marketing"><input name="t2-measuring-marketing" id="t2-measuring-marketing" type="checkbox" value="" /> Measuring Marketing</label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                  </tr>
                </table>
            <!--IMPROVE BUSINESS OPERATIONS OPTIONS-->
				<table width="100%" border="0" id="topic-3" class="form-table">
                  <tr>
                    <td width="50%"><p style="margin-bottom:2px;"><label for="t3-internet-based-computing"><input name="t3-internet-based-computing" id="t3-internet-based-computing" type="checkbox" value="" /> Internet Based Computing</label></p>
                    				<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td width="50%"><p style="margin-bottom:2px;"><label for="t3-high-speed-internet"><input name="t3-high-speed-internet" id="t3-high-speed-internet" type="checkbox" value="" /> High Speed Internet</label></p>
                    				<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                  </tr>
                  <tr>
                    <td><p style="margin-bottom:2px;"><label for="t3-connecting-inside-business"><input name="t3-connecting-inside-business" id="t3-connecting-inside-business" type="checkbox" value="" /> Connecting Inside the Business</label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td><p style="margin-bottom:2px;"><label for="t3-connecting-outside-business"><input name="t3-connecting-outside-business" id="t3-connecting-outside-business" type="checkbox" value="" /> Connecting Outside<br /> <span style="padding-left:32px;">the Business</span></label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                  </tr>
                  <tr>
                    <td><p style="margin-bottom:2px;"><label for="t3-email"><input name="t3-email" id="t3-email" type="checkbox" value="" /> Email</label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td>&nbsp;</td>
                  </tr>
                </table>
            <!--PROTECTING YOUR BUSINESS OPTIONS-->
            	<table width="100%" border="0" id="topic-4" class="form-table">
                  <tr>
                    <td width="50%"><p style="margin-bottom:2px;"><label for="t4-protecting-your-data"><input name="t4-protecting-your-data" id="t4-protecting-your-data" type="checkbox" value="" /> Protecting Your Data</label></p>
                    				<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td width="50%"><p style="margin-bottom:2px;"><label for="t4-security-threats"><input name="t4-security-threats" id="t4-security-threats" type="checkbox" value="" /> Security Threats</label></p>
                    				<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                  </tr>
                  <tr>
                    <td><p style="margin-bottom:2px;"><label for="t4-compliance"><input name="t4-compliance" id="t4-compliance" type="checkbox" value="" /> Compliance</label></p>
                    	<p class="included"><a class="inline" href="#popup">View included pieces</a></p>
                    </td>
                    <td>&nbsp;</td>
                  </tr>
                </table>
                <hr />
              <h3>Step 4. Add Sell Sheets and/or a Personalized Note</h3>
                <small style="margin-top:12px;"><em>attach product sell sheets</em></small>
                <table width="100%" border="0" class="form-table">
                  <tr>
                    <td colspan="3"><h4>Core Connect</h4></td>
                  </tr>
                  <tr>
                    <td><p><label for="cc-zone-1"><input name="cc-zone-1" id="cc-zone-1" type="checkbox" value="" /> Zone 1</label></p></td>
                    <td><p><label for="cc-zone-2"><input name="cc-zone-2" id="cc-zone-2" type="checkbox" value="" /> Zone 2</label></p></td>
                    <td><p><label for="cc-zone-3"><input name="cc-zone-3" id="cc-zone-3" type="checkbox" value="" /> Zone 3</label></p></td>
                  </tr>
                  <tr>
                    <td colspan="3"><h4>High-Speed Internet</h4></td>
                  </tr>
                  <tr>
                    <td><p><label for="hsi-zone-1"><input name="hsi-zone-1" id="hsi-zone-1" type="checkbox" value="" /> Zone 1</label></p></td>
                    <td><p><label for="hsi-zone-2"><input name="hsi-zone-2" id="hsi-zone-2" type="checkbox" value="" /> Zone 2</label></p></td>
                    <td><p><label for="hsi-zone-3"><input name="hsi-zone-3" id="hsi-zone-3" type="checkbox" value="" /> Zone 3</label></p></td>
                  </tr>
                  <tr>
                    <td colspan="3"><h4>Other Sell Sheets</h4></td>
                  </tr>
                  <tr>
                    <td><p><label for="oss-voice"><input name="oss-voice" id="oss-voice" type="checkbox" value="" /> Voice Packages</label></p></td>
                    <td><p><label for="oss-grow-packs"><input name="oss-grow-packs" id="oss-grow-packs" type="checkbox" value="" /> Grow Packs</label></p></td>
                    <td><p><label for="oss-tst"><input name="oss-tst" id="oss-tst" type="checkbox" value="" /> Technology Support Team</label></p></td>
                  </tr>
                  <tr>
                    <td colspan="3"><small><em>personal note - up to 300 characters max.</em></small><br /></td>
                  </tr>
                  <tr>
                    <td colspan="3"><textarea name="" cols="" rows="6" class="text-box"></textarea></td>
                  </tr>
                  <tr>
                  	<td colspan="3" align="center"><h4>Be sure to review your input and selections. If everything is complete and correct click "Send" below.</h4></td>
                  </tr>
                  <tr>
                	<td align="center" colspan="3"><input name="send" type="button" value="" class="button-send" /></td>
              	  </tr>
                </table>
          </form>
        </div>
        <div id="body-right">
        	<div id="right-sidebar">
            	<h5>New Connect Sold Account Tracker</h5>
              <p>Mark <strong>SOLD</strong> accounts by clicking on the box to the left of your customer's name below.</p>
				<p>Accounts will appear in this list for <br /><strong>15 days</strong> after sending an email.<br />
			    After 15 days they will be removed.</p>
                <table width="100%" border="0" class="tracker">
                  <tr>
                    <td width="10%"><p>X</p></td>
                    <td width="63%"><p>Name</p></td>
                    <td width="27%" align="right"><p>Date Sent</p></td>
                  </tr>
                  <tr>
                    <td><!--<input name="" type="checkbox" value="" />--></td>
                    <td><p>Customer Name <span class="sold">SOLD</span><br /><small>Company Name</small></p></td>
                    <td align="right"><p>05/26/11</p></td>
                  </tr>
                  <tr>
                    <td><input name="" type="checkbox" value="" /></td>
                    <td><p>Customer Name <br /><small>Company Name</small></p></td>
                    <td align="right"><p>05/27/11</p></td>
                  </tr>
                  <tr>
                    <td><input name="" type="checkbox" value="" /></td>
                    <td><p>Customer Name <br /><small>Company Name</small></p></td>
                    <td align="right"><p>05/28/11</p></td>
                  </tr>
                </table>
          </div><!--END RIGHT-SIDEBAR-->
        </div><!--END BODY-RIGHT-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
    <div id="layout-footer">
    	<p>&copy;2011 CenturyLink, Inc. All Rights Reserved.</p>
    </div><!--END LAYOUT-FOOTER-->
</div><!--END LAYOUOT-->

<!--POPUP CONTENT MAP-->
<div style="display:none;">
    <div id="popup" style="padding:10px; background:#FFFFFF;">
    	<h2>Email Content</h2>
    	<table width="100%" cellpadding="6" border="0" class="email-content-title">
          <tr>
            <td width="32%">Theme Selection</td>
            <td width="32%">Topic Selection</td>
            <td width="36%">Linked Content</td>
          </tr>
        </table>
        
        <h5>General Product Information</h5>
        <table width="100%" border="0" class="email-content">
          <tr>
            <td width="32%">&nbsp;</td>
            <td width="32%"><p class="greendk"><strong>Core Connect</strong></p></td>
            <td width="36%"><p><a href="assets/pdf/01_Core_Connect.pdf">Core Connect Sell Sheet</a></p></td>
          </tr>
          <tr class="alt">
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>High-Speed Internet</strong></p></td>
            <td><p><a href="#">High-Speed Internet Sell Sheet</a></p></td>
          </tr>
          <tr>
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Voice Packages</strong></p></td>
            <td><p><a href="assets/pdf/01_Voice.pdf">Voice Packages Sell Sheet</a><br /><a href="assets/pdf/01_Voice_AZ.pdf">Voice Packages Sell Sheet - AZ</a></p></td>
          </tr>
          <tr class="alt">
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Grow Packs</strong></p></td>
            <td><p><a href="#">Grow Packs Sell Sheet</a></p></td>
          </tr>
        </table>
        
        <h5>Marketing Your Busniness</h5>
        <table width="100%" border="0" class="email-content">
          <tr>
            <td width="32%">&nbsp;</td>
            <td width="32%"><p class="greendk"><strong>Marketing Online</strong></p></td>
            <td width="36%"><p><a href="assets/pdf/02_Marketing_Online_Brochure.pdf" target="_blank">Marketing Online Brochure</a><br />
            				   <a href="assets/pdf/02_Marketing_Online_Tips_Sheet.pdf" target="_blank">Top 10 Tips - Marketing Online</a></p></td>
          </tr>
          <tr class="alt">
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>CRM</strong></p></td>
            <td><p><a href="assets/pdf/02_CRM_Brochure.pdf" target="_blank">CRM Brochure</a><br />
				   <a href="assets/pdf/02_CRM_White_Paper.pdf" target="_blank">CRM Whitepaper</a><br />
                   <a href="assets/pdf/02_CRM_Tips_Sheet.pdf" target="_blank">Top 10 Tips - CRM</a></p></td>
          </tr>
          <tr>
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Social Media</strong></p></td>
            <td><p><a href="assets/pdf/02_Social_Media_Tips_Sheet.pdf" target="_blank">Top 10 Tips - Social Media</a></p></td>
          </tr>
          <tr class="alt">
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Measuring Marketing</strong></p></td>
            <td><p><a href="assets/pdf/02_Marketing_Performance_Brochure.pdf" target="_blank">Marketing Performance Brochure</a><br />
				   <a href="assets/pdf/02_Marketing_Performance_White_Paper.pdf" target="_blank">Marketing Performance Whitepaper</a><br />
                   <a href="assets/pdf/02_Marketing_Performance_Tips_Sheet.pdf" target="_blank">Top 10 Tips - Marketing Performance</a></p></td>
          </tr>
        </table>
        
        <h5>Improve Business Operations</h5>
        <table width="100%" border="0" class="email-content">
          <tr>
            <td width="32%">&nbsp;</td>
            <td width="32%"><p class="greendk"><strong>Internet Based Computing</strong></p></td>
            <td width="36%"><p><a href="assets/pdf/03_Internet_Based_Computing_Tips.pdf" target="_blank">Top 10 Tips - Internet Based Computing</a></p></td>
          </tr>
          <tr class="alt">
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>High-Speed Internet</strong></p></td>
            <td><p><a href="assets/pdf/03_Internet_Connections_Brochure.pdf" target="_blank">Internet Connections Brochure</a><br />
				   <a href="assets/pdf/03_Internet_Connections_Tips_Sheet.pdf" target="_blank">Top 10 Tips - Maximizing Connections</a></p></td>
          </tr>
          <tr>
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Connecting Inside the Business</strong></p></td>
            <td><p><a href="assets/pdf/03_Connecting_Inside_Brochure.pdf" target="_blank">Connecting Inside Brochure</a><br />
				   <a href="assets/pdf/03_Connecting_Inside_Tips_Sheet.pdf" target="_blank">Top 10 Tips - Connecting Inside</a></p></td>
          </tr>
          <tr class="alt">
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Connecting Outside the Business</strong></p></td>
            <td><p><a href="assets/pdf/03_Connecting_Outside_Brochure.pdf" target="_blank">Connecting Outside Brochure</a><br />
				   <a href="assets/pdf/03_Connecting_Outside_White_Paper.pdf" target="_blank">Connecting Outside Whitepaper</a><br />
				   <a href="assets/pdf/03_Connecting_Outside_Tips.pdf" target="_blank">Top 10 Tips - Connecting Outside</a></p></td>
          </tr>
          <tr>
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Email</strong></p></td>
            <td><p><a href="assets/pdf/03_Email_Brochure.pdf" target="_blank">Email Brochure</a><br />
				   <a href="assets/pdf/03_Email_White_Paper.pdf" target="_blank">Email Whitepaper</a><br />
                   <a href="assets/pdf/03_Email_Tips.pdf" target="_blank">Top 10 Tips - Email</a></p></td>
          </tr>
        </table>
        
        <h5>Protecting Your Business</h5>
        <table width="100%" border="0" class="email-content">
          <tr>
            <td width="32%">&nbsp;</td>
            <td width="32%"><p class="greendk"><strong>Protecting Your Data</strong></p></td>
            <td width="36%"><p><a href="assets/pdf/04_Data_Protection_Brochure.pdf" target="_blank">Data Protection Brochure</a><br />
							   <a href="assets/pdf/04_Data_Protection_White_Paper.pdf" target="_blank">Data Protection Whitepaper</a><br />
							   <a href="assets/pdf/04_Data_Protection_Tips.pdf" target="_blank">Top 10 Tips - Protecting Your Data</a></p></td>
          </tr>
          <tr class="alt">
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Security Threats</strong></p></td>
            <td><p><a href="assets/pdf/04_Security_Threats_Brochure.pdf" target="_blank">Security Threats Brochure</a><br />
				   <a href="assets/pdf/04_Security_Threats_White_Paper.pdf" target="_blank">Security Threats Whitepaper</a><br />
				   <a href="assets/pdf/04_Security_Threats_Tips.pdf" target="_blank">Top 10 Tips - Security Threats</a></p></td>
          </tr>
          <tr>
            <td>&nbsp;</td>
            <td><p class="greendk"><strong>Compliance</strong></p></td>
            <td><p><a href="assets/pdf/04_Compliance_Brochure.pdf" target="_blank">Compliance Brochure</a><br />
				   <a href="assets/pdf/04_Compliance_White_Paper.pdf" target="_blank">Compliance Whitepaper</a></p></td>
          </tr>
        </table>
        
    </div>
</div>
</body>
</html>
];
$myDB ->Close();
$myDB2 ->Close();
