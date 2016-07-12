#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw/ fatalsToBrowser /;
use CCICryptography;
use DBInterface;
use CGI qw(:standard);
use Date::Calc qw(Today Add_Delta_Days);

my $cgi = CGI->new();
#print $cgi->header('text/html');

my $db = DBInterface->new();

my $thisfile = "sbgOrderConfirmReview.cgi";


my $server;
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}

require "$server/cgi-bin/delimeter.cgi";
require "$server/cgi-bin/inccalendar.cgi";
require "$server/sbgemailbuilder/sbgemail_subs.cgi";



my $cci_id = $cgi->param('cci_id') ;
my $source_id = $cgi->param('source_id') ;

my $emp_email = $cgi->param('emp_email')||'';
my $SAP_ID =  $cgi->param('SAP_ID')||'';
my $emp_first_name =  $cgi->param('emp_first_name')||'';
my $redir = $cgi->param('redir') || 0;
my $pre_oc_id =  $cgi->param('pre_oc_id') ||0;




my  $PAGETITLE = 'CenturyLink Business - Tech Service Tool';
#my $header = get_header(  # init.cgi new improved header
#        'title' => $PAGETITLE,
#        'css'   => 'style.css',
#    );
#print $header;
my $str = "";
my $str2;

#$str .= $str2;
#$str = '';
#	 <tr>
#        <td align="center" colspan="3">$str</td>
#	 </tr>

my $msg = '';
my $onload = "";
if ($pre_oc_id == 0 && $redir == 0) {
	#print qq [calling coe in cgi<br> ];
 ($str, $pre_oc_id) = createOCemail ();
	#print qq [finished coe<br> ];
}
elsif ($pre_oc_id > 0 && $redir == 1) {
	#$str .="to Update";
 $str .= UpdateOCemail ($pre_oc_id);
}

if ($pre_oc_id > 0) {
	$onload = '';#"onLoad=\"EditOCemail(2, $pre_oc_id )\"";
} 
print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<title>$PAGETITLE</title>
];

print qq [
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
		
<script type='text/javascript' src='/javascriptspellcheck/include.js' ></script>
		<script type="text/javascript" src="../jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="../jquery/simplemodal/simplemodal.css"/>


<!--	cci complete	-->
<script type="text/javascript" src="/assets/js/functions.js"></script>
<script type="text/javascript" src="sbgvalidate.js"></script>
<script type="text/javascript" src="sbgvalidate_ajax.js"></script>

<script type='text/javascript'>
		  \$Spelling.ServerModel = "asp";
          \$Spelling.DefaultDictionary = "English (USA),Espanol";
          \$Spelling.UserInterfaceTranslation = "en";
          \$Spelling.SpellCheckAsYouType('edit_personal_note')
</script>


<script type="text/javascript">
	\$(document).ready(function(){
		\$(".inline").colorbox({inline:true, width:"90%"});
	});


</script>

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
<body $onload>
<div id="layout">
<script type="text/javascript">
	\$(window).load(function() {
   EditOCemail(2, $pre_oc_id );
});
</script>

	<div id="layout-header">
    	<img src="assets/img/logo-centurylink.png" width="242px"/>
    </div><!--END LAYOUT-HEADER-->
    <div id="layout-body">
<form name="frm" action="" method="post">
<input type="hidden" name="cci_id" value="$cci_id">
<input type="hidden" name="source_id" value="$source_id">

<input type="hidden" name="redir" value="">
<input type="hidden" name="pre_oc_id" value="$pre_oc_id">
<table width="100%" border="0" class="form-table"> 
	 <tr>
        <td align="center" colspan="4">$str </td>
	 </tr>
	 <tr>
        <td colspan="4" align="center" ><h4> <i>DRAFT ORDER CONFIRMATION EMAIL </i></h4><br>
		<small> Please click on "Edit" , "Cancel" or "Send" buttons below to complete the process</small></td>
	 </tr><tr><td colspan="4"><hr/></td></tr>

	 <tr>
        <td align="center" width="25%" > <input name="" type="" value="" class="button-edit" onclick="EditOCemail(1, $pre_oc_id);"/> </td>
        <td align="center" width="25%"> <input name="" type="" value="" class="button-review" onclick="EditOCemail(2, $pre_oc_id);"/> </td>
        <td align="center" width="25%"> <input name="send" type="" value="" class="button-send2" onclick="sendOCemail();"/> </td>
        <td align="center" width="25%"> <input name="cancel" type="" value="" class="button-cancel" onclick="cancelOCemail();"/> </td>
	 </tr>

	 </table>
			<div style="height:0;overflow:hidden;visibility:hidden;">&nbsp;</div>
			<div id="editOCemaildiv" name="editOCemaildiv" class="body-biggest"><!-- here	--> </div>

	
  </form>

        </div>
<!--			<div style="clear: both;"></div>	-->

        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
			<div style="clear: both;"></div>

    <div id="layout-footer">
    	<p>&copy;<script language="javascript">var year=getFullYear();document.write(year);</script> CenturyLink, Inc. All Rights Reserved.</p>
    </div><!--END LAYOUT-FOOTER-->
</div><!--END LAYOUOT-->

<!--POPUP CONTENT MAP moved -->

</body>
</html>
];

$db->disconnect();

=head
$dt{personal_note}<br>
		
		$emp_first_name,<br>
		Small Business Sales & Care Representative<br>
		1-800-672-6242 <br>
		$emp_email
=cut
#-------------------------------------------------------------------------------------------------------


