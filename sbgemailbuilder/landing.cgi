use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use CGI qw(:standard);
my $cgi = CGI->new();
my $myDB = DBInterface->new();
my $myDB2 = DBInterface->new();
my $thisfile = "landing.cgi";
my $redir = $cgi->param('redir')||0;
my $cci_id = $main::session{cci_id}||$cgi->param('cci_id'); 
my $source_id = $main::session{source_id}||$cgi->param('source_id'); 
#print "Content-type:text/html\n\n";
print $cgi->header('text/html');

my $chk = CCICryptography::validate_CL($cci_id);


print qq[<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" >
];




my $server;
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}


require "$server/sbgemailbuilder/sbgemail_subs.cgi";

my  $PAGETITLE = 'CenturyLink Business - Tech Service Tool';

my $preProposal_id = $cgi->param('preProposal_id')||0;
my $pre_oc_id = $cgi->param('pre_oc_id')||0;

my $onload = '';
my $msg = 'Hello '; #.$main::session{name}
my ( $emplid, $staff_id);
 # $msg .= '<br>redir = '.$redir.'<br>';
my ($str, $str2);
my $show_ast_button = "";


if ($redir == 1) {
	($str, $str2) = process_email ();
	$msg.= $str;
}
elsif ($redir == 2) {
	$msg .= sendFinalProposal ($preProposal_id);
}
elsif ($redir == 3) {
	$msg .= dropProposal ($preProposal_id);
}
elsif ($redir == 4) {
	$msg .= sendOrderConfirmation ($pre_oc_id);
}
elsif ($redir == 5) {
	$msg .= dropOrderConfirmation ($pre_oc_id);
}

	$msg .= '<br> Please Fill out Form';
my ($sql);
# Promo usage off for now
#if ($source_id == 2) {
#$show_ast_button = qq[
#	<a class="right button-promo-usage" href="#"  onclick="openModalmedium('promo_usage.cgi?cci_id=$cci_id&source=$source_id');return false;">Promo Usage</a>];
#}

# took off AST Lead List
#<a class="right button-leadlist" href="#"  onclick="openModalAST('ast_leadlist.cgi?cci_id=$cci_id&source=$source_id');return false;">Lead List</a>

#<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
#<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

#<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
#	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
#<html xmlns="http://www.w3.org/1999/xhtml">

print qq[
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<title>$PAGETITLE</title>

<!--FAVICON-->
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<!--CSS-->
<link type="text/css" href="assets/css/style.css" rel="stylesheet" title="print" media="screen" />
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<!--JAVASCRIPT-->

<!--	cci	--><!--	http://www.centurylinkyoucan.com/jquery/jquery.js	-->
		<script  type="text/javascript" src="../jquery/jquery.js"></script>
		<script  type="text/javascript" src="../jquery/jquery-ui.js"></script>
		<script  type="text/javascript" src="../jquery/jmenu/js/jmenu.js"></script>
		
<script type='text/javascript' src='javascriptspellcheck/include.js' ></script>
		<script type="text/javascript" src="../jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="../jquery/simplemodal/simplemodal.css"/>

<!-- datepicker	-->

<script language="JavaScript" src="Datepicker/date-picker.js"></script>


<!-- end datepicker	-->

<!--	cci complete	-->
<script type="text/javascript" language="JavaScript" src="/assets/js/functions.js"></script>
<script type="text/javascript" language="JavaScript" src="sbgvalidate.js"></script>
<script type="text/javascript" language="JavaScript" src="sbgvalidate_ajax.js"></script>

<script type='text/javascript'>
		  \$Spelling.ServerModel = "asp";
          \$Spelling.DefaultDictionary = "English (USA),Espanol";
          \$Spelling.UserInterfaceTranslation = "en";
          \$Spelling.SpellCheckAsYouType('note')
</script>

  <script type='text/javascript'>
		  \$Spelling.ServerModel = "asp";
          \$Spelling.DefaultDictionary = "English (USA),Espanol";
          \$Spelling.UserInterfaceTranslation = "en";
          \$Spelling.SpellCheckAsYouType('personal_note')
</script>

<script type="text/javascript">
	\$(document).ready(function(){
		\$(".inline").colorbox({inline:true, width:"90%"});
	});


</script>




$onload

<!--[if lte IE 7]>
	<script type="text/javascript" src="assets/js/ie-fix.js"></script>
<![endif]-->
<!--[if lte IE 7]>  
<style type="text/css">
#body-left {min-height:2500px !important;}
#right-sidebar {min-height:650px !important;}

</style> 

<![endif]-->


</head>
];

print qq[
<body>
<div id="layout">
		 <form name="frm" action="" method="post">
<input type="hidden" name="cci_id" value="$cci_id">
<input type="hidden" name="source_id" value="$source_id">

	<div id="layout-header">
<script type="text/javascript">
	\$(window).load(function() {
   showTrack($source_id);
});
</script>
    	
$show_ast_button

<img src="assets/img/logo-centurylink.png" width="242px"/>
    	<a class="right button-contentmap" href="#" onclick="openWin('content_map.cgi')">Content Map</a>



    </div><!--END LAYOUT-HEADER-->
    <div id="layout-body">
    	<div id="body-left">


<input type="hidden" name="redir" value="">

		<p> $msg <!-- $preProposal_id $pre_oc_id--></p>
            <h3>Business Offer Optimization Sales Tool</h3> 
            <p class="orange"><em>*required field</em></p>
            <h3>Step 1. Recipient Information</h3>
                <table width="100%" border="0" class="form-table">
                  <tr>
                    <td width="38%" align="right"><p>
                      <label for="company-name"><span class="orange">*</span>Company Name</label></p></td>
                    <td width="62%"><input name="company_name" id="company_name" type="text" tabindex="1" class="text-field"/>
					<label><span id='req_company_name'></label></td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="first-name"><span class="orange">*</span>Recipient First Name</label></p></td>
                    <td><input name="first_name" id="first_name" type="text" tabindex="2" class="text-field"/>
					<label><span id='req_first_name'></label></td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="last-name"><span class="orange">*</span>Recipient Last Name</label></p></td>
                    <td><input name="last_name" id="last_name" type="text" tabindex="3" class="text-field"/>
					<label><span id='req_last_name'></label></td>
                  </tr>
                  <tr>
                    <td align="right"><p>
                      <label for="email"><span class="orange">*</span>Recipient Email Address</label></p></td>
                    <td><input name="email" id="email" type="text" tabindex="4" class="text-field"/>
					<label><span id='req_email'></label></td>
                  </tr>
    
                  <tr>
                    <td width="38%" align="right"><p>
                      <label for="bau"><span class="orange">*</span>I want to </label></p></td>
					  <td width="62%">&nbsp;<small class="orange"><em>Email, Proposal or Confirmation must be selected in order for Form to display.</em></td>
				</tr>
				<tr>
				<td width="38%" align="right"><p>&nbsp;</p></td>

                    <td width="62%"><label><input type="radio" name="bau" value="1" id="l3" onClick="showFlow(1)" class="radio-button" />&nbsp;Send an Email</label>&nbsp;<br>
					<label><input type="radio" name="bau" value="2" id="l4" onClick="showFlow(2)" class="radio-button" />&nbsp;Create a Proposal</label><br>
					<label><input type="radio" name="bau" value="3" id="l5" onClick="showFlow(3)" class="radio-button" />&nbsp;Send a Confirmation</label>
					
					</td>
                  </tr>
				  <tr>
                    <td width="38%" align="right"><p>
                      <label for="language"><span class="orange">*</span>Language</label></p></td>
                    <td width="62%"><label><input type="radio" name="language_id" value="1"  onClick="checkFlow_lang(1)" class="radio-button" checked />&nbsp;English</label>&nbsp;
					<label><input type="radio" name="language_id" value="2"  class="radio-button" onClick="checkFlow_lang(2)"/>&nbsp;Spanish</label><br>
					<small class="orange"><em>Language selection is for product sheets only.</em>
					</td>
                  </tr>
                  <tr>
                    <td width="38%" align="right"><p>
                      <label for="language"><span class="orange">*</span>Legacy options</label></p></td>
                    <td width="62%"><label><input type="radio" name="legacy" value="1"  class="radio-button" onClick="checkFlow_legacy(1)" checked/>&nbsp;CRIS (West)</label>&nbsp;
					<br>
					<label><input type="radio" name="legacy" value="2"  class="radio-button" onClick="checkFlow_legacy(2)" />&nbsp;ENS (East) </label><br>
					<small class="orange"><em>If Legacy Option is not selected Email is sent out for Legacy Qwest by default</em>
					</td>
                  </tr>

                </table>
                <hr />
			<div id="body-biggest">

			<div id="flowdiv" name="flowdiv" class="body-biggest"><!--	--> </div>
			</div> <!--	 close big body	-->
<!--	TAKE OFF EVERYTHING UNDER THIS	-->
];

print qq[				
          </form>
        </div>

	<script type="text/javascript" language="javascript1.2" src="/leadpro/udm4/udm-resources/udm-dom.js"></script>	
        <div id="body-right">
        	<div id="right-sidebar" >

            	<h5>New Connect Sold Account Tracker</h5>
              <p>Mark <strong>SOLD</strong> accounts by clicking on the box to the left of your customer&rsquo;s name below.</p>
				<p>Accounts will appear in this list for <br /><strong>15 days</strong> after sending an email.<br />
			    After 15 days they will be removed.</p>
				<div id="trackdiv" name="trackdiv"></div>
				<!-- table comes in from sub	-->
		  </div><!--END RIGHT-SIDEBAR-->
        </div><!--END BODY-RIGHT-->
			<div style="clear: both;"></div>

        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
<div style="clear:both;"></div>
    <div id="layout-footer">
    	
    </div><!--END LAYOUT-FOOTER-->
</div><!--END LAYOUOT-->

<!--POPUP CONTENT MAP moved -->

</body>
</html>
];

   $myDB->disconnect();
   $myDB2->disconnect();




