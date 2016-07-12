use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use HTML::Strip;
use CCICryptography;
use DBInterface;
use Try::Tiny;
use CGI qw(:standard);
$CGI::Application::LIST_CONTEXT_WARN = 0;
my $cgi = CGI->new();



print $cgi->header('text/html');


my $cci_id = $cgi->param('cci_id')||'';
  #require "G:/CenturyLinkTest/xroot/cgi-bin/init.cgi";
  #require "D:/centurylinkyoucan/cgi-bin/init.cgi";
my $chk = CCICryptography::validate_CL($cci_id);
my $url = CCICryptography::getUrl();

#require "D:/CenturyLink/cgi-bin/email.cgi";
#require "G:/CenturyLinkTest/xroot/cgi-bin/email.cgi";
#require "D:/centurylinkyoucan/cgi-bin/email.cgi";

my $leadlink=0;
if ( $chk <= 0) {
 
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

}else{
 #require "D:/CenturyLink/cgi-bin/lp-init.pm";

  $leadlink = 1;
}
#require "d:/CenturyLink/cgi-bin/delimeter.cgi";
#require "G:/CenturyLinkTest/xroot/cgi-bin/delimeter.cgi";
#require "D:/centurylinkyoucan/cgi-bin/delimeter.cgi";

#my $myDB = Win32::ODBC->new($main::DSN);

my $myDB = DBInterface->new();
my $thisfile = "mkt_materials.cgi";
#my (%prog );
my ($sth, $prog);

my ($id,$emplid ) = CCICryptography::getEmpid($cci_id);

my $s2 = "select rtrim(cuid) as cuid, rtrim(first_name)+' '+rtrim(last_name) as emp_name ,rtrim(job_title) as job_title,
RTRIM(work_addr1)+' '+rtrim(ISNULL(office_number,''))+' '+RTRIM(work_addr2)+', '+rtrim(work_city)+', '+work_state+' '+work_zip as wk_addr,
RTRIM(work_addr1)+' '+RTRIM(ISNULL(office_number, '')) as wk_addr1, RTRIM(work_addr2) as wk_addr2, rtrim(work_city) as wk_city, rtrim(ltrim(work_state)) as work_state, work_zip
from qwesthr with (nolock) where emplid = ?"; 

#############
try {
$sth = $myDB->prepare($s2);
$sth->execute($emplid) or die $sth->errstr;
$prog = $sth->fetchrow_hashref();
$sth->finish();
}
catch {
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############

my $cuid = uc($prog->{cuid});
my $name =" ". $prog->{emp_name};
my $wk_addr = $prog->{wk_addr};
my $job_title = $prog->{job_title};
my $wk_addr1 = $prog->{wk_addr1};
my $wk_addr2 = $prog->{wk_addr2};
my $wk_city = $prog->{wk_city};
my $work_state = $prog->{work_state};
my $work_zip = $prog->{work_zip};

my $redir = $cgi->param('redir');
my $comment_str ='Please let us know your comments!';


#print qq[$cuid ,$name,$wk_addr ,$job_title, $emplid , $session_id, $work_state <br>];
#print qq[$state_list];


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
<script type="text/javascript">
	animatedcollapse.addDiv('nav-sec-1', 'fade=0,speed=500,group=nav,hide=1,height=22px,persist=1')
	animatedcollapse.addDiv('nav-sec-2', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-3', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-4', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-5', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-6', 'fade=0,speed=500,group=nav,hide=1,height=22px')

	animatedcollapse.init()
</script>
<script language="javascript">
    var prevent_double_submits = 0;

    function checkformMktMat(){
    document.frm.redir.value = 1;
    document.frm.savebutton.disabled = true;
    document.frm.savebutton.value = "Please wait...";
    
        if (    document.frm.yc_sb_tf.checked==false && document.frm.hsi_cris.checked==false && document.frm.hsi_ensemble.checked==false 
			&& document.frm.prism_flyer_cris.checked==false && document.frm.prism_flyer_ens.checked==false ) {
                    document.frm.redir.value = 0;
                    window.alert('At least one collateral type is required.');
                    document.frm.savebutton.disabled=false;
                }
	
				if ( document.frm.yc_sb_tf.checked==true ) {
					if (document.frm.yc_sb_tf_qty.value=="") {
                    document.frm.redir.value = 0;
                    window.alert('Please indicate quantity for Small Business Tri-Fold - All Markets.');
                    document.frm.savebutton.disabled=false;
					}
				}
			
				if ( !document.frm.yc_sb_tf_qty.value== "") {
						if ( document.frm.yc_sb_tf.checked==false ) {
                    document.frm.redir.value = 0;
                    window.alert('If you would like to order Small Business Tri-Fold - All Markets, please click the checkbox');
                    document.frm.savebutton.disabled=false;
					}
				}

		if ( document.frm.hsi_cris.checked==true ) {
					if (document.frm.hsi_cris_qty.value=="") {
                    document.frm.redir.value = 0;
                    window.alert('Please indicate quantity for Residential HSI Price Lock pamphlet All Speeds - CRIS Markets Only.');
                    document.frm.savebutton.disabled=false;
					}
				}
			
				if ( !document.frm.hsi_cris_qty.value== "") {
						if ( document.frm.hsi_cris.checked==false ) {
                    document.frm.redir.value = 0;
                    window.alert('If you would like to order Residential HSI Price Lock pamphlet All Speeds - CRIS Markets Only, please click the checkbox');
                    document.frm.savebutton.disabled=false;
					}
				}

       if ( document.frm.hsi_ensemble.checked==true ) {
					if (document.frm.hsi_ensemble_qty.value=="") {
                    document.frm.redir.value = 0;
                    window.alert('Please indicate quantity for Residential HSI Price Lock pamphlet All Speeds - Ensemble Markets Only.');
                    document.frm.savebutton.disabled=false;
					}
				}
			
				if ( !document.frm.hsi_ensemble_qty.value== "") {
						if ( document.frm.hsi_ensemble.checked==false ) {
                    document.frm.redir.value = 0;
                    window.alert('If you would like to order Residential HSI Price Lock pamphlet All Speeds - Ensemble Markets Only, please click the checkbox');
                    document.frm.savebutton.disabled=false;
					}
				}
	       if ( document.frm.prism_flyer_ens.checked==true ) {
					if (document.frm.prism_flyer_ens_qty.value=="") {
                    document.frm.redir.value = 0;
                    window.alert('Please indicate quantity for Generic Prism Flyer - Ensemble Markets Only.');
                    document.frm.savebutton.disabled=false;
					}
				}
			
				if ( !document.frm.prism_flyer_ens_qty.value== "") {
						if ( document.frm.prism_flyer_ens.checked==false ) {
                    document.frm.redir.value = 0;
                    window.alert('If you would like to order Generic Prism Flyer - Ensemble Markets Only, please click the checkbox');
                    document.frm.savebutton.disabled=false;
					}
				}
	       if ( document.frm.prism_flyer_cris.checked==true ) {
					if (document.frm.prism_flyer_cris_qty.value=="") {
                    document.frm.redir.value = 0;
                    window.alert('Please indicate quantity for Generic Prism Flyer - Consumer CRIS Markets Only.');
                    document.frm.savebutton.disabled=false;
					}
				}
			
				if ( !document.frm.prism_flyer_cris_qty.value== "") {
						if ( document.frm.prism_flyer_cris.checked==false ) {
                    document.frm.redir.value = 0;
                    window.alert('If you would like to order Generic Prism Flyer - Ensemble Markets Only, please click the checkbox');
                    document.frm.savebutton.disabled=false;
					}
				}
				if (document.frm.ship_addr1.value =="" || document.frm.ship_city.value =="" || document.frm.ship_st.value =="" || document.frm.ship_zip.value =="") {
				    document.frm.redir.value = 0;
                    window.alert('Please fill out complete shipping address');
                    document.frm.savebutton.disabled=false;

				}

				if (document.frm.redir.value == 1  && prevent_double_submits==0 ) {
					prevent_double_submits=1;
                    document.frm.submit();
                    return true;

                }
                else  {
                    return false;
                }
    }
</script>
<!--[if lt IE 8]> <script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE8.js"></script> <![endif]-->
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
                	<h2>Customer Marketing Materials</h2>
                </div>
                <div class="capsule-content">
EOF
if ($redir==1) {
my $hs = HTML::Strip->new();
my ( $prism_flyer_cris, $prism_flyer_ens,  $hsi_cris, $hsi_ensemble, $yc_sb_tf);
my(  $prism_flyer_cris_qty,$prism_flyer_ens_qty,  $hsi_cris_qty, $hsi_ensemble_qty, $yc_sb_tf_qty);
my ($ship_addr1 , $ship_addr2 , $ship_city , $ship_st , $ship_zip, $text_comment, $str, $adr_str, $ret);

	$yc_sb_tf =  $cgi->param('yc_sb_tf') || 'no';
	$prism_flyer_cris =  $cgi->param('prism_flyer_cris') || 'no';
	$prism_flyer_ens =  $cgi->param('prism_flyer_ens') || 'no';
  $hsi_cris =  $cgi->param('hsi_cris') || 'no';
  $hsi_ensemble =  $cgi->param('hsi_ensemble') || 'no';
    
	$yc_sb_tf_qty = $cgi->param('yc_sb_tf_qty') || '0';
	$prism_flyer_cris_qty =  $cgi->param('prism_flyer_cris_qty') || '0';
	$prism_flyer_ens_qty =  $cgi->param('prism_flyer_ens_qty') || 'no';
	$hsi_cris_qty =  $cgi->param('hsi_cris_qty') || 0;
  $hsi_ensemble_qty =  $cgi->param('hsi_ensemble_qty') || 0;


	$ship_addr1 = EscQuote($hs->parse( $cgi->param('ship_addr1') ));
		$hs->eof;
 	$ship_addr2 = EscQuote($hs->parse( $cgi->param('ship_addr2') ));
		$hs->eof;
 	$ship_city = EscQuote($hs->parse( $cgi->param('ship_city') ));
 	$ship_st = EscQuote($hs->parse( $cgi->param('ship_st') ));
	$ship_zip = EscQuote($hs->parse( $cgi->param('ship_zip') ));
 	$text_comment = EscQuote($hs->parse( $cgi->param('text_comment') ));
 	$hs->eof;
 	my($to, $cc, $bcc, $from, $subject, $body, $client_id);
	$client_id = 50;
$to = "Don.Swick\@CenturyLink.com, Tami.Cordova\@CenturyLink.com";
#$to = "archanak\@channelmanagement.com";

#$to = 'scotts@channelmanagement.com,archanak@channelmanagement.com';

#$bcc= ' archanak@channelmanagement.com';
#$bcc = 'scotts@channelmanagement.com,archanak@channelmanagement.com';
#$cc = "scotts\@channelmanagement.com, kayla.jones\@channelmanagement.com";
$cc = '';#"Don.Swick\@CenturyLink.com, Tami.Cordova\@CenturyLink.com";
$bcc='';#'archanak@channelmanagement.com';
$from = 'do_not_reply@ccionline.biz';
$subject = 'YOUCAN Collateral Request';
$body = "Request by $name [$cuid] \n Job Title : $job_title \n";

$str = '<br>';
if ( $yc_sb_tf eq 'yes') { 
	$str.= $yc_sb_tf_qty.'  Small Business Tri-Fold - All Markets <br>'; 
	$body .= 'Small Business Tri-Fold - All Markets: '.$yc_sb_tf_qty."\n";
	}
if ($hsi_cris eq 'yes') {
	$str.= $hsi_cris_qty.'  Residential HSI Price Lock Pamphlet All Speeds - CRIS Markets Only. <br>'; 
	$body .= 'Residential HSI Price Lock Pamphlet All Speeds - CRIS Markets Only. : '.$hsi_cris_qty."\n";
}
if ($hsi_ensemble eq 'yes') {
	$str.= $hsi_ensemble_qty.'  Residential HSI Price Lock Pamphlet All Speeds - Ensemble Markets Only. <br>'; 
	$body .= 'Residential HSI Price Lock Pamphlet All Speeds - Ensemble Markets Only. : '.$hsi_ensemble_qty."\n";
}
if ($prism_flyer_cris eq 'yes') {
	$str.= $prism_flyer_cris_qty.'  Generic Prism flyer - Consumer CRIS Markets only. <br>'; 
	$body .= 'Generic Prism flyer - Consumer CRIS Markets only. : '.$prism_flyer_cris_qty."\n";
}
if ($prism_flyer_ens eq 'yes') {
	$str.= $prism_flyer_ens_qty.'  Generic Prism flyer - Consumer Ensemble Markets only. <br>'; 
	$body .= 'Generic Prism flyer - Consumer Ensemble Markets only. : '.$prism_flyer_ens_qty."\n";
}

$adr_str='<br>';
$adr_str.=$name.', ';
$adr_str.=$ship_addr1.', ';
if ($ship_addr2 ne "") { $adr_str.=$ship_addr2.', ';}
$adr_str.=$ship_city.', ';
$adr_str.=$ship_st.' ';
$adr_str.=$ship_zip;
$adr_str.='<br><br>Please allow two weeks for delivery.';

$body .='Shipping Address: '.$ship_addr1.' '.$ship_addr2.' '.$ship_city.' '.$ship_st.' '.$ship_zip;
if ($text_comment ne $comment_str) {
	if ($text_comment ne "") {
			$body.=" \n Comments: $text_comment ";
	}
}
my  $prevent_double=0;
my $sql = '';
my $ret = 0;
if ($prevent_double==0) {
=head
$sql = "insert into ccimail (client_id, program_id,tofield, ccfield, bccfield, fromfield, subject, longbody) values
        (50,154,'" . EscQuote($to) . "','" . EscQuote($cc) . "','" . EscQuote($bcc) . "','" . EscQuote($from). "','" .EscQuote($subject). "','" . EscQuote($body). "' )";
$myDB->Sql($sql) ;		
=cut
$sql = "insert into ccimail (client_id, program_id,tofield, ccfield, bccfield, fromfield, subject, longbody) 
							values (50,154, ?, ? , ? , ? , ? ,? )";

$prevent_double++;
#############
try {
$sth = $myDB->prepare($sql);
$sth->bind_param(1, EscQuote($to));
$sth->bind_param(2, EscQuote($cc));
$sth->bind_param(3, EscQuote($bcc));
$sth->bind_param(4, EscQuote($from));
$sth->bind_param(5, EscQuote($subject));
$sth->bind_param(6, EscQuote($body));

$sth->execute() or die $sth->errstr;
$sth->finish();
}
catch {
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############

}

	print<<"EOF";
	                    <h4>Thank you </h4>
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="marketing-materials">
					<tr><td><p>	Thank you for requesting: $str</p><br>
						<p>	The collateral will be shipped to: $adr_str </p></td></tr>
				</table>
						
EOF

}
else {
print<<"EOF";
<form name="frm" action="$thisfile" method="post" >
<input type="hidden" name="cci_id" value="$cci_id">
<input type="hidden" name="redir" value="">
                    <br />
<!--	-->
                    <!-- <h4>Small Business</h4> -->
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="marketing-materials">
                      <tr>
                        <th width="11%" valign="bottom"><p>Select</p></th>
                        <th width="34%" valign="bottom"><p>Material</p></td>
                        <th width="14%" valign="bottom"><p>Quantity</p></th>
                        <th width="41%" valign="bottom"><p>Description</p></th>
                      </tr>
<!--	-->
                      <tr>
                        <td align="right" valign="top"><input name="yc_sb_tf" type="checkbox" value="yes" /></td>
                        <td><p><a href="pdf/2014_SB.pdf" target="_blank">Small Business Tri-Fold - All Markets</a><p></td>
                        <td valign="top"><select name="yc_sb_tf_qty" size="1">
                          <option value="" selected="selected">Select...</option>
                          <option value="100">100</option>
                          <option value="200">200</option>
                          <option value="300">300</option>
                        </select></td>
                        <td valign="top"><p>Small Business Tri-Fold - All Markets</p></td>
                      </tr>
<!--	-->
		                      <tr>
                        <td align="right" valign="top"><input name="hsi_cris" type="checkbox" value="yes" /></td>
                        <td><p><a href="pdf/HSI_price_lock.png" target="_blank">Residential HSI Price Lock pamphlet All Speeds - CRIS Markets Only</a><p></td>
                        <td valign="top"><select name="hsi_cris_qty" size="1">
                          <option value="" selected="selected">Select...</option>
                          <option value="100">100</option>
                          <option value="200">200</option>
                          <option value="300">300</option>
                        </select></td>
                        <td valign="top"><p>Residential HSI Price Lock pamphlet All Speeds - CRIS Markets Only</p></td>
                      </tr>
<!--	-->
		                      <tr>
                        <td align="right" valign="top"><input name="hsi_ensemble" type="checkbox" value="yes" /></td>
                        <td><p><a href="pdf/HSI_price_lock.png" target="_blank">Residential HSI Price Lock pamphlet All Speeds - Ensemble Markets Only</a><p></td>
                        <td valign="top"><select name="hsi_ensemble_qty" size="1">
                          <option value="" selected="selected">Select...</option>
                          <option value="100">100</option>
                          <option value="200">200</option>
                          <option value="300">300</option>
                        </select></td>
                        <td valign="top"><p>Residential HSI Price Lock pamphlet All Speeds - Ensemble Markets Only</p></td>
                      </tr>
<!--	-->
		                      <tr>
                        <td align="right" valign="top"><input name="prism_flyer_ens" type="checkbox" value="yes" /></td>
                        <td><p><a href="pdf/Prism_flyer_04082016.pdf" target="_blank">Generic Prism Flyer - Consumer Ensemble Markets Only</a><p></td>
                        <td valign="top"><select name="prism_flyer_ens_qty" size="1">
                          <option value="" selected="selected">Select...</option>
                          <option value="100">100</option>
                          <option value="200">200</option>
                          <option value="300">300</option>
                        </select></td>
                        <td valign="top"><p>Generic Prism Flyer - Consumer Ensemble Markets Only</p></td>
                      </tr>
<!--	-->
		                      <tr>
                        <td align="right" valign="top"><input name="prism_flyer_cris" type="checkbox" value="yes" /></td>
                        <td><p><a href="pdf/Prism_flyer_04082016.pdf" target="_blank">Generic Prism Flyer - Consumer CRIS Markets Only</a><p></td>
                        <td valign="top"><select name="prism_flyer_cris_qty" size="1">
                          <option value="" selected="selected">Select...</option>
                          <option value="100">100</option>
                          <option value="200">200</option>
                          <option value="300">300</option>
                        </select></td>
                        <td valign="top"><p>Generic Prism Flyer - Consumer CRIS Markets Only</p></td>
                      </tr>
<!-- here	-->

                    </table>
                    <br />
                     <table width="100%" border="0" cellspacing="0" cellpadding="0">
                       <tr>
                        <td width="30%">
                         <h4>Shipping Address</h4>
                        </td>
                        <td>
                          <font color="red">NOTE:  We use USPS as our default shipping method. If your location does not accept  deliveries from the postal service, 
                                            please enter the correct  shipping address in the boxes below and let us know in the comments section.   
                          </font>
                        </td>
                       </tr>
                      </table>
                      <br />
                     <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td colspan="2"><p>Address 1: <input name="ship_addr1" type="text" value="$wk_addr1"/></p></td>
                        <td width="60%"><p>Address 2: <input name="ship_addr2" type="text" value="$wk_addr2" /></p></td>
                      </tr>
                    </table>
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                      <tr>
                        <td width="31%"><p>City: <input name="ship_city" type="text" size="16" value="$wk_city"/></p></td>
                        <td width="34%"><p>State: $work_state<select name="ship_st">
                          <option value="">Select</option>
EOF

	my $st_sql = "select  state as state1, rtrim(ltrim(abbreviation)) as abbreviation from lp_states with (nolock) where program_id = 154 order by state1";

#----------------
my ($checked, $abb); 
my $success = eval {
my $sth = $myDB->prepare($st_sql) or die $myDB->errstr;
$sth->{PrintError} = 0;
$sth->execute()  or die $sth->errstr;

while(my $state = $sth->fetchrow_hashref){
	$abb = $state->{abbreviation};
	if ( $work_state eq $abb ) {
                    $checked = qq[selected="selected"];
                }else{
                    $checked = "";
                }
	print qq[  <option  value="$abb" $checked >$state->{state1}</option> ];

	}
$sth->finish();	

};
unless($success) {
	DBInterface::writelog('youcan10',"$thisfile", $@ );
}
#------------------

print qq[

         </select>
                        </p></td>
                        <td width="35%"><p>Zip: <input name="ship_zip" type="text" size="10" value="$work_zip"/></p></td>
                      </tr>
                      <tr>
                        <td colspan="3"><p>Comments:<textarea name="text_comment" rows="6" onclick="document.frm.text_comment.value='';">$comment_str</textarea></p></td>
                      </tr>
                      <tr>
                        <td colspan="3"><small>All fields are required. Please allow up to two weeks for delivery.</small></td>
                      </tr>
                      <tr>
                        <td colspan="3" class="aligncenter"><input name="savebutton" type="submit" class="but-request" value="" onClick="checkformMktMat();"/></td>
                      </tr>
                    </table>
                    </form>
	];
}
print qq[
                </div>
            </div><!--END CAPSULE-->
            	
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
];
if ( $cci_id>0 ) {
print qq[
        	<div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Make a Referral</h3>
                </div>
                <div class="capsule-content">
					<p><a href="#" onClick="document.lead123.action='welcome.cgi';document.lead123.submit();">click here</a> to make a referral.</p>
                </div>
            </div><!--END CAPSULE-->
            <div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Before Ordering</h3>
                </div>
                <div class="capsule-content">
                	<p>Collateral may be appropriate for specific markets only. Collateral will be marked CRIS, Ensemble or All Markets.
                     <br><br>CRIS markets are legacy Qwest territory. Ensemble markets are legacy CenturyLink territory. Collateral for All markets may be used in both.
                     <br><br>If you are uncertain about which piece to order please contact your supervisor or <a href="mailto:youcan.support\@centurylink.com">youcan.support\@centurylink.com</a>
                     <br><br>No Access door hangers for CRIS and Ensemble technicians are ordered in <a href="http://qstat.faconline.com/qstat/default.aspx" target="_blank">here</a>. Please see your supervisor to request No Access door hangers</p>
                </div>
            </div><!--END CAPSULE-->
];

}

print qq[
        </div><!--END BODY-RIGHT-SEC-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
];
#require "D:/CenturyLink/youcan10/youcan_footer.cgi";
#require "G:/CenturyLink/xroot/qwest/youcan10/youcan_footer.cgi";
showftr ($cci_id);
print qq[
</div><!--END LAYOUT-->
</body>
</html>
];
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
sub EscQuote($)     # 03/30/01 5:40PM  -- RF
					# Escapes single quotes
					# Use for preparing strings for SQL statements.
############################################################################
{
    my ($delim_return) = @_;
	$delim_return =~ s/[']/''/gi;
	return $delim_return;
}