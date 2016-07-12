use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use Try::Tiny;
use CGI qw(:standard);
my $cgi = CGI->new();
my $myDB = DBInterface->new();

require "D:/centurylinkyoucan/youcan10/youcan_subs.cgi";

my $emplid = 0;
my $cci_id = $main::session{cci_id}||$cgi->param('cci_id'); 

my ($session_id,$emplid) = CCICryptography::getEmpid($cci_id); 
my $url = CCICryptography::getUrl();

my $chk = CCICryptography::validate_CL($cci_id);

if ($chk <= 0 || length($cci_id) == 0){
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

my $sql;
my $redir = $cgi->param('redir')||0;
my $thisfile="welcome.cgi";

my  $PAGETITLE = "YOUCAN | Deliver the VIP Experience";
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;

my (%qmy_dt, $found);

my $name_sql = "select first_name, rtrim(cuid) as cuid, rtrim(email) as email ,
case when job_title in ('Center Sales and Service Associate','Sales Consultant','Sales and Service Consultant','Credit Consultant')
then 0 else 1 end as show_ctl
from qwesthr with (nolock) where emplid = ?";
#############
my $prog;
try {
	my $sth = $myDB->prepare($name_sql);
	$sth->execute($emplid) or die $sth->errstr;
	$prog = $sth->fetchrow_hashref();
	$sth->finish();
}
catch {
	print "Our apologies. An error occured, please report.";
	DBInterface::writelog('youcan10',"$thisfile", $_ );
	exit;	
};
##############
my $name = $prog->{first_name};
my $cuid = uc($prog->{cuid}); 
my $email = $prog->{email};
my $show_ctl= $prog->{show_ctl};

my $css = "assets/css/style.css";


# LOCKOUT CODE FOR STRIKE.
# Added by bfleming
#


my $lockout_sql = " select 0 as id union
select key_id as id from ctl_lockout with(nolock) where cuid = ?
order by 1 desc";
##############
my $sth = $myDB->prepare($lockout_sql);
$sth->execute($cuid);
my $lockout_prog = $sth->fetchrow_hashref();
$sth->finish();
#$lockout_prog{id};
##############
my $id = 0;

if($id > 0) {
 
print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>YOUCAN | Deliver the VIP Experience</title>

<!--FAVICON-->
<link href="/favicon.ico" rel="shortcut icon" type="image/x-icon" />

<!--CSS-->
<link type="text/css" href="assets/css/style.css" rel="stylesheet" />

<!--JAVASCRIPT-->
<script type="text/javascript" src="assets/js/jquery.js"></script>
<script type="text/javascript" src="assets/js/functions.js"></script>


</head>

<body>
<div id="layout">

	<div id="layout-header">
    	<div id="header-content">
       		<a href="#"><img src="assets/img/header.gif" alt="$PAGETITLE" title="$PAGETITLE" class="youcan-logo" /></a>
        </div><!--END HEADER-CONTENT-->
    </div><!--END LAYOUT-HEADER-->

    <div id="layout-body">
    	<div id="body-left-sec">
        	<div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2>Login</h2>
                </div>
                <div class="capsule-content">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="login-entry">
                      <tr>
                        <td colspan="2"><p><font color="red">The YOUCAN program is temporarily suspended for the duration of the work stoppage in Legacy Qwest markets. For more information about bargaining please visit <a href="http://centurylink.com/bargaining">centurylink.com/bargaining.</a>
</font></p></td>
                      </tr>

                    </table>
                </div>
            </div><!--END CAPSULE-->
        </div><!--END BODY-LEFT-SEC-->
        <div id="body-right-sec">
        	<div class="capsule-230">
            </div><!--END CAPSULE-->
        </div><!--END BODY-RIGHT-SEC-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
    <div id="layout-footer">
    	<div id="footer-content">
				<ul class="footer-legal"><li>&copy; <script type="text/javascript">document.write(new Date().getFullYear());</script> CenturyLink, Inc. All Rights Reserved. The CenturyLink mark, pathways logo, CenturyLink mark,
               Q lightpath logo and certain CenturyLink product names are the property of CenturyLink, Inc.</li>
				</ul>
        </div><!--END FOOTER CONTENT-->
    </div><!--END LAYOUT-FOOTER-->
</div><!--END LAYOUT-->

</body>
</html>
EOF
  
  exit 1;     
}

my $message;

if ($redir==1) {
#-------------------------------------------
$message = submitLead($myDB);

#--------------------------------------------
}


$sql = "select 0 as cnt UNION
select isnull(count(lp_lead.lp_lead_id),0) as cnt
from lp_lead with (Nolock)
inner join lkup_qwest_opts opts with (nolock) on opts.lp_lead_id = lp_lead.lp_lead_id
where program_id = 154 and fund_id = 511 and ISNULL(lp_lead.lp_region_id,0) <> 41
and isnull(lead_status_id,0) > 49
and created_date between convert(varchar, '01/01/'+convert(varchar,DATEPART (yyyy, getdate())))
 and convert(varchar, '12/31/'+convert(varchar,DATEPART (yyyy, getdate()))+' 23:59:59')
and agency_id = ?
order by 1 desc ";

#############
my $prog_total;
try {
my $sth = $myDB->prepare($sql);
$sth->execute($emplid);
$prog_total = $sth->fetchrow_hashref();
$sth->finish();
}
catch {
	print "Our apologies. An error occured, please report.";
	DBInterface::writelog('youcan10',"$thisfile", $_ );
	exit;	
};

#############
my $ref_close = $prog_total->{cnt};

$sql = "select 0 as cnt UNION
select isnull(count(lp_lead.lp_lead_id),0) as cnt
from lp_lead with (Nolock) 
inner join lkup_qwest_opts opts with (nolock) on opts.lp_lead_id = lp_lead.lp_lead_id
where program_id = 154 and fund_id = 511 and ISNULL(lp_lead.lp_region_id,0) <> 41
and isnull(lead_status_id,0) < 50
and created_date between convert(varchar, '01/01/'+convert(varchar,DATEPART (yyyy, getdate())))
 and convert(varchar, '12/31/'+convert(varchar,DATEPART (yyyy, getdate()))+' 23:59:59')
and agency_id = ?
order by 1 desc ";

#############
my $prog_total;
try {
my $sth = $myDB->prepare($sql);
$sth->execute($emplid);
$prog_total = $sth->fetchrow_hashref();
$sth->finish();
}
catch {
	print "Our apologies. An error occured, please report.";
	DBInterface::writelog('youcan10',"$thisfile", $_ );
	exit;	
};
#############
my $ref_pend = $prog_total->{cnt};

my $chk_sql = "select CONVERT(varchar,getdate()-1,101) as ydt";

##################
my $found;
try {
my $sth = $myDB->prepare($chk_sql);
$sth->execute();
$found = $sth->fetchrow_hashref();
}
catch {
	print "Our apologies. An error occured, please report.";
	DBInterface::writelog('youcan10',"$thisfile", $_ );
	exit;	
};
##################
my $ydt = $found->{ydt};


print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta name=robots content=noindex>
<meta name="MSSmartTagsPreventParsing" content="TRUE">
<meta http-equiv="pragma" content="no-cache">
<title>$PAGETITLE</title>
<!--FAVICON-->
<link href="/favicon.ico" rel="shortcut icon" type="image/x-icon" />


<!-- CSS -->
<link type="text/css" rel="stylesheet" href="$css" />
<link href="assets/css/iefix.css" type="text/css" rel="stylesheet" />
<style type="text/css">
        #displayCounter{
        font-size:42px;
        font-family:Georgia;
		align: center;
        }
    </style>
	<style type="text/css">
       div.MyClass p 
			{  
			font-size: 0.7em !important; 
			text-align:center;
			}
    </style>
<!--JAVASCRIPT-->
<script type="text/javascript" src="assets/js/jquery.js"></script>
<script type="text/javascript" src="assets/js/functions.js"></script>


		<script type="text/javascript" src="D:/centurylinkyoucan/jquery/jquery.js"></script>
	<!--	<script type="text/javascript" src="D:/centurylinkyoucan/jquery/javascript/jquery-1.4.1.min.js"></script> -->
		<script  type="text/javascript" src="D:/centurylinkyoucan/jquery/jquery-ui.js"></script>

		<script type="text/javascript" src="D:/centurylinkyoucan/jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="D:/centurylinkyoucan/jquery/simplemodal/simplemodal.css"/>

<script type="text/javascript" src="assets/js/validate.js"></script>
<script type="text/javascript" src="assets/js/youcan_functions.js"></script>
<script type="text/javascript">
	animatedcollapse.addDiv('nav-sec-1', 'fade=0,speed=500,group=nav,hide=1,height=22px,persist=1')
	animatedcollapse.addDiv('nav-sec-5', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-6', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	
	animatedcollapse.init()
</script>

<script type="text/javascript"  src="http://ajax.microsoft.com/ajax/jQuery/jquery-1.4.2.min.js">
    </script>



		<script type="text/javascript">

	   var isNN = (navigator.appName.indexOf("Netscape")!=-1);
function autoTab(input,len, e) {
  var keyCode = (isNN) ? e.which : e.keyCode;
  var filter = (isNN) ? [0,8,9] : [0,8,9,16,17,18,37,38,39,40,46];
  if(input.value.length >= len && !containsElement(filter,keyCode)) {
    input.value = input.value.slice(0, len);
    input.form[(getIndex(input)+1) % input.form.length].focus();
  }

  function containsElement(arr, ele) {
    var found = false, index = 0;
    while(!found && index < arr.length)
    if(arr[index] == ele)
    found = true;
    else
    index++;
    return found;
  }

  function getIndex(input) {
    var index = -1, i = 0, found = false;
    while (i < input.form.length && index == -1)
    if (input.form[i] == input)index = i;
    else i++;
    return index;
  }
  return true;
}

function savvisPrompt (chkbx) {
	    var email = document.getElementById('lead_email').value;
	    if (chkbx.checked){
	      if (email.length < 6){
	    	   window.alert("An email address will help us contact your customer about CenturyLink Technology Solutions - Cloud Products. If available, include the email address for the customer you are referring.");
	      }
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

showhdr ($PAGETITLE, $cci_id);
print<<"EOF";
    </div><!--END LAYOUT-HEADER-->
    
    <div id="layout-body">
    	<div id="body-left">
        	<div class="capsule-470">
            	<div class="capsule-header-green">
                	<h2>Hello <strong>$name ,</strong> <small>welcome back.</small></h2>
                </div>
                <div class="capsule-content">
                	<p>Referrals Closed: <strong>$ref_close</strong> | Referrals Pending: <strong>$ref_pend</strong> </p>	

                </div>
            </div><!--END CAPSULE-->

<!--	start form	-->
            <div class="capsule-470">
            	<div class="capsule-header-green">
				
                	<h2>Submit a New Referral</h2>
                </div>
                <div class="capsule-content">
				<p>$message <br></p>
                    <p class="right"><span class="blue">*</span> Required Fields</p>


<form name="lead" method="post" action="welcome.cgi">
    <input type="hidden" name="usertype" value="">
    <input type="hidden" name="navigation_version" value="">
	<input type="hidden" name="redir" value="">
				<input type="hidden" name="prodvalidate" value="0">
				<input type="hidden" name="cci_id" value="$cci_id">
	
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="referral-entry">
					 <tr>
                        <td><p class="alignright"><span class="blue">*</span>Customer Type: </p></td>
                        <td width="26%"><p><label><input type="radio" name="cust_type" value="56" onclick="showTopic(56, $session_id)"/>Residential</label></p></td>
                        <td width="39%"><p><label><input type="radio" name="cust_type" value="55" onclick="showTopic(55, $session_id)"/>Business</label></p></td>
                      </tr>
					  <tr><td colspan="3"><div class="MyClass"><p>Referral Type must be selected in order for Referral Form to display.</p></div></td></tr>

<tr><td colspan="3">
<div id="themediv" name="themediv" ><!--	--> </div>
</td></tr>
</table>
                  </form>

EOF
print<<"EOF";
                </div>
            </div><!--END CAPSULE-->
<!--	end form	-->

        </div><!--END BODY-LEFT-->
        <div id="body-right">

<div class="capsule-470">
            	<div style="width: 470px; background:#EA0D8C; text-align:center;" ><br><br>
					<h4>New to YOUCAN?</h4>
				 <h2><a href="#" onClick="document.lead123.action='overview.cgi';document.lead123.submit();">Click here</a> to get started</h2> <br>
				 

                    <br />
                </div><!--END PROMO-TOP-->
	</div>
<!-- start	new white box	-->



<!-- end	new white box	-->
<div class="capsule-470">
            	<div style="width: 470px; background:#A5DDEE; text-align:center;" >
					<h4>YOUCAN News</h4><br>
					<h3><a href="#" onClick="document.lead.action='news.cgi';document.lead.submit();">Referral History Function Restored &#40;June 14&#41;</a></h3> <br>
					<h3><a href="pdf/YOUCAN_win_250_June_2016.pdf" target="_blank">Win &#36;250 HSI&#47;prism Promotion &#40;June 6 &ndash;July 2&#41;</a></h3> <br>
					<h3><a href="pdf/Winners_Week1_4_April16.pdf" target="_blank">April Promotion - \$250 HSI or Prism Referrals &ndash; Winners</a></h3> <br>
					<h3><a href="pdf/YCMB_double_awards_March_June_2016.pdf" target="_blank">Double Awards for Commercial Enterprise Referrals through June 2016</a></h3> <br>
					<h3><a href="#" onClick="document.lead.action='maintenance.cgi';document.lead.submit();">Reporting - Where did the function go?</a></h3> <br>
					<h3><a href="pdf/YOUCAN_HSI_Tech_Installs_0216.pdf" target="_balnk">YOUCAN Tech Install Awards</a></h3> <br>
					<h3><a href="#" onClick="document.lead.action='res_biz_awards.cgi';document.lead.submit();">2016 Award Values effective January 1, 2016</a></h3> <br>
				<h3><a href="#" onClick="document.lead.action='news.cgi';document.lead.submit();">2016 YOUCAN Award Calendar</a></h3> <br>
				<h3><a href="#" onClick="document.lead.action='news.cgi';document.lead.submit();">More YOUCAN News</a></h3> <br>
				<h3><a href="#" onClick="document.lead.action='faq.cgi';document.lead.submit();">Frequently Asked Questions</a></h3> <br>
                    <br />
                </div><!--END PROMO-TOP-->
	</div>

<!-- end	new for app	-->
<!-- end old	-->

<!-- start	new V2_orange box	-->
<div class="capsule-470"> <!-- start div1 -->
            	<div style="width: 470px; background:#F8951D; text-align:center;" >
					<h4>YOUCAN Resources</h4> <br />
					<h3><a href="https://www.myprepaidcenter.com" target="_blank">Check my YOUCAN Card Balance</a></h3> <br />
					<h3><a href="#" onClick="document.lead123.action='faq.cgi';document.lead123.submit();">I lost my YOUCAN Card</a></h3> <br />
					<h3><a href="#" onClick="document.lead123.action='mkt_materials.cgi';document.lead123.submit();">Order YOUCAN Collateral and Flyers</a></h3> <br />
                    <h3><a href="http://lqweb.qintra.com/loopqual-webapp/pages/ProductQual/QualCheck/Qualify.faces" target="_blank">Check High Speed Internet Availability</a></h3><br />
                </div><!--END PROMO-TOP-->

			

	</div> <!-- end  div 1-->
<!-- end V2_orange box	-->

  
        </div><!--END BODY-RIGHT-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
EOF

showftr ($cci_id);

print<<"EOF";
</div><!--END LAYOUT-->

</body>
</html>
EOF
undef &CommaFormatted;
undef &get_header;
undef &check_mainbtn;
undef &get_routing_sql;

# -------------------------------------------------------------------

