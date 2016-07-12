use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use Try::Tiny;
use CGI qw(:standard);
my $cgi = CGI->new();
require "D:/centurylinkyoucan/youcan10/youcan_subs.cgi";
my $myDB = DBInterface->new();
$myDB->{LongReadLen} = 512 * 1024;
my $cci_id = $cgi->param('cci_id'); 
my ($id,$emplid ) = CCICryptography::getEmpid($cci_id);
my $url  = CCICryptography::getUrl();


my $thisfile = 'ref_hist.cgi';

my $valid = CCICryptography::validate_CL($cci_id);

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

# get numbers for chevrons
my($new, $open,$purch,$closePaid,$noSold) = (0,0,0,0,0);
my $ast_isr = 407328; # staging = 404503, coop = 407328 407328
my $program_id = 154;
my $fund_id = 511;
my $region_id = 41;


my ($sth,$show_data); 
my $show_sql = " select 0 as cnt UNION select count(lp_Lead.lp_lead_id) from lp_lead with (nolock) 
				inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id 
				where agency_id = ?
                and program_id = ? and fund_id = ? and isnull(lead_status_id,0)=0 and created_date > '01/01/2014'
				and ISNULL(lp_lead.lp_region_id,0) <> ?
                order by 1 desc";
#############
try {
 $sth = $myDB->prepare($show_sql);
$sth->execute($emplid, $program_id, $fund_id, $region_id) or die $sth->errstr;
 $show_data = $sth->fetchrow_hashref();
$sth->finish();
$new=$show_data->{cnt};
}
catch {
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############

$show_sql = " select 0 as cnt UNION select count(lp_Lead.lp_lead_id) from lp_lead with (nolock) 
				inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
				where agency_id = ?
                and program_id = ? and fund_id = ? and isnull(lead_status_id,0) between 1 and 49 and created_date > '01/01/2014'
				and ISNULL(lp_lead.lp_region_id,0) <> ?
                order by 1 desc";
#############
try {
 $sth = $myDB->prepare($show_sql);
$sth->execute($emplid, $program_id, $fund_id, $region_id) or die $sth->errstr;
 $show_data = $sth->fetchrow_hashref();
$sth->finish();
$open=$show_data->{cnt};
}
catch {
		DBInterface::writelog('youcan10',"$thisfile", $_ );
};

##############

$show_sql = " select 0 as cnt UNION select count(lp_Lead.lp_lead_id) from lp_lead with (nolock) 
				inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
				where agency_id = ?
                and program_id = ? and fund_id = ? and isnull(lead_status_id,0) in (50,51) and created_date > '01/01/2014'
				and ISNULL(lp_lead.lp_region_id,0) <> ?
                order by 1 desc";
#############
try {
my $sth = $myDB->prepare($show_sql);
$sth->execute($emplid, $program_id, $fund_id, $region_id) or die $sth->errstr;
my $show_data = $sth->fetchrow_hashref();
$sth->finish();
$purch=$show_data->{cnt};
}
catch {
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############

$show_sql = " select 0 as cnt UNION select count(lp_Lead.lp_lead_id) from lp_lead with (nolock) 
				inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
				where agency_id = ?
                and program_id = ? and fund_id = ? and isnull(lead_status_id,0) = 52 and created_date > '01/01/2014'
				and ISNULL(lp_lead.lp_region_id,0) <> ?
                order by 1 desc";
#############
try {
my $sth = $myDB->prepare($show_sql);
$sth->execute($emplid, $program_id, $fund_id, $region_id) or die $sth->errstr;
my $show_data = $sth->fetchrow_hashref();
$sth->finish();
$closePaid=$show_data->{cnt};
}
catch {	
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############

$show_sql = " select 0 as cnt UNION select count(lp_Lead.lp_lead_id) from lp_lead with (nolock) 
				inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
				where agency_id = ?
                and program_id = ? and fund_id = ? and isnull(lead_status_id,0) > 52 and created_date > '01/01/2014'
				and ISNULL(lp_lead.lp_region_id,0) <> ?
                order by 1 desc";
#############
try {
my $sth = $myDB->prepare($show_sql);
$sth->execute($emplid, $program_id, $fund_id, $region_id) or die $sth->errstr;
my $show_data = $sth->fetchrow_hashref();
$sth->finish();
$noSold=$show_data->{cnt};
}
catch {	
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############

#my $divClass = 'class="hideable" style="display: none;"';
my $divClass = ' style="display: none;"';
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
	<link type="text/css" href="assets/css/chevron6.css" rel="stylesheet" />	
<link type="text/css" href="assets/css/style.css" rel="stylesheet" />
<link href="assets/css/iefix.css" type="text/css" rel="stylesheet" />
<!--JAVASCRIPT-->

<script type="text/javascript" src="assets/js/jquery.js"></script>
<script type="text/javascript" src="assets/js/functions.js"></script>
		<script type="text/javascript" src="http://www.centurylinkyoucan.com/jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="http://www.centurylinkyoucan.com/jquery/simplemodal/simplemodal.css"/>




<script type="text/javascript">
<!--
function toggleDiv(item, a){

	if (document.getElementById(item).style.display=='none'){
        document.getElementById(item).style.display='';
		a.innerHTML='Hide Lead List';
		
    }
    else{
         document.getElementById(item).style.display='none';
		a.innerHTML='Show Lead List';
    }


    }


 function showRefDiv (ele) {
         var srcElement = document.getElementById(ele);

		document.getElementById('hide_show_new').style.display = 'none';

		document.getElementById('hide_show_open').style.display = 'none';
		document.getElementById('hide_show_purch').style.display = 'none';
		document.getElementById('hide_show_close_purch').style.display = 'none';
		document.getElementById('hide_show_nosale').style.display = 'none';

		document.getElementById(ele).style.display = 'block';
  }

  function showRefDiv3 (id){
        if (document.getElementById) {
          var divid = document.getElementById(id);
          var divs = document.getElementsByClassName("hideable");
          for(var div in divs) {
             div.style.display = "none";
          }
          divid.style.display = "block";
        } 
        return false;
 }

function openModalmedium(src) {
        jQuery.modal('<iframe src="' + src + '" height="250" width="740" style="border:0">');
                jQuery.modal({
                        autoResize: true
                });
 }
//-->
</script>
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

  <style type="text/css">
        #ht {
        position: absolute;
        top: 950px;
        left: 100px;
        visibility: hidden;}
        </style>
    <span id='ht' class='details'>not yet populated </span>

</head>

<body>
<div id="layout">

	<div id="layout-header">
EOF

require "D:/centurylinkyoucan/youcan10/youcan_header.cgi";
showhdr ($PAGETITLE, $cci_id);

$show_sql = "select 0 as cnt union 
select count(lp_Lead.lp_lead_id) from lp_lead with (nolock) 
inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
where program_id = ? and fund_id = ?
and agency_id = ? and created_date > '01/01/2014'
and ISNULL(lp_lead.lp_region_id,0) <> ?
 order by 1 desc ";

#############
my $ld_cnt;
try {
my $sth = $myDB->prepare($show_sql);
$sth->execute($program_id, $fund_id, $emplid, $region_id) or die $sth->strerr;
my $show_data = $sth->fetchrow_hashref();
$sth->finish();
$ld_cnt=$show_data->{cnt};
}
catch {	
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############

my $note;
my $excelfile ;
my $lead_note="";
if ($ld_cnt > 0 ) {
$excelfile	= '/tmp/' . $id ."_" . time() . ".xls";
unless(open(CSVDATA, '>D:/centurylinkyoucan' . $excelfile)) {
    $note ="Could not generate Report";
}
	$show_sql = "select convert(varchar,getdate(),1) as rund , 
				RTRIM(first_name)+' '+RTRIM(last_name) as emp_name 
				from qwesthr with (nolock) where emplid = ?";

#############
my $show_data;
try {
my $sth = $myDB->prepare($show_sql);
$sth->execute($emplid) or die $sth->errstr;
$show_data = $sth->fetchrow_hashref();
$sth->finish();
}
catch {
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############
print CSVDATA "Referral Report for $show_data->{emp_name} \n";
print CSVDATA "Rundate $show_data->{rundt} \n";

$lead_note = "<p>Here are your last 10 Referrals.</p><br>";

}# if leads to show



print<<"EOF";
    </div><!--END LAYOUT-HEADER-->

    <div id="layout-body">
    	<div id="body-center">
        	<div class="capsule-960">
            	<div class="capsule-960-header">
                	<h2>My Referral History</h2><br>
                </div>

<!--	START CHEVRON	-->


				<div class="capsule-content">
				
				     <p>We&rsquo;ve updated how your Referral History appears. <a href="#" onClick="document.lead123.action='overview.cgi';document.lead123.submit();">Click here</a> for more information.</p>
				<p><a href="$excelfile" target="_blank">Download Report</a></p>

<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values" style="float:left" >
	<tr><td colspan="4">



<div id="breadcrumb6">
		<ul class="breadcrumb6" style="margin-left:-20px;padding-left:0;">
	<li style="list-style-type: none;"><a href="#" onclick="showRefDiv('hide_show_new')">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Received <small>($new)</small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#" onclick="showRefDiv('hide_show_open')">&nbsp;&nbsp;&nbsp;In Progress <small>($open)</small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#" onclick="showRefDiv('hide_show_purch')">&nbsp;&nbsp;&nbsp;Accuracy Check <small>($purch)</small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#" onclick="showRefDiv('hide_show_close_purch')">&nbsp;&nbsp;&nbsp;Awarded <small>($closePaid)</small>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	</ul>
</div>



<div id="breadcrumb">
		<ul class="breadcrumb" style="margin-left:-20px;padding-left:0;">
	<li style="list-style-type: none;"><a href="#" onclick="showRefDiv('hide_show_new')">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Received <small>($new)</small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#" onclick="showRefDiv('hide_show_open')">&nbsp;&nbsp;&nbsp;In Progress <small>($open)</small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#" onclick="showRefDiv('hide_show_purch')">&nbsp;&nbsp;&nbsp;Accuracy Check <small>($purch)</small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
	<li style="list-style-type: none;"><a href="#" onclick="showRefDiv('hide_show_nosale')">&nbsp;&nbsp;&nbsp;No Award <small>($noSold)</small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>
		</ul>
</div>
</td></tr>
</table>
<!--	END CHEVRON	-->

<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
<tr><td> 

EOF
my(  $new_sql, $curr_status, $stat_cnt, $open_cnt, $close_cnt, %data);
my $isopen = -1;
## for lead_status_id = 0

print qq[<div id="hide_show_new" $divClass >
			<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
			<tr class="leadcreated">
          <td colspan="6"><p><strong>Received ($new)</strong></p></td>
                      </tr>
					  ];
print CSVDATA "Received ($new)\n";
if ($new > 0) {
$new_sql="  select lp_lead.lp_lead_id , convert(varchar,created_date,1) as fmt_created_date, main_btn, 
			isnull(rtrim(lead_company_name), '') as lead_company_name, rtrim(lead_name) as lead_name,
			isnull(lead_status_id,0) as lead_status_id, dbo.func_getstatus(lp_lead.lead_status_id, 154)as status_name,
			isnull(( select RTRIM(description) from lp_status_description lsd with (nolock) 
where lsd.program_id = lp_lead.program_id and lsd.lead_status_id = isnull(lp_lead.lead_status_id,0)
and isActive = 1
),'') as st_ex
        from lp_lead with (nolock)
		inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
        where lp_lead.agency_id = ?
        and lp_lead.program_id = ?
        and lp_lead.fund_id = ?
		and ISNULL(lp_lead.lp_region_id,0) <> ?
                and isnull(lp_lead.lead_status_id,0) =0 and created_date > '01/01/2014'
                order by lead_status_id, lp_lead.lp_lead_id desc";
print qq[
 <tr><td width="14.25%"><p><strong>Referral \#</strong></p></td>
	 <td width="14.25%"><p><strong>Created Date</strong></p></td>
	 <td width="14.25%"><p><strong>Business Name</strong></p></td>
 <td width="14.25%"><p><strong>Customer name</strong></p></td>
	 <td width="14.25%"><p><strong>Telephone Number</strong></p></td>
<td colspan="2"><p><strong>Status Explanation</strong></p></td>
</tr>
];
print CSVDATA "Referral \# \tCreated Date \tBusiness Name \tCustomer Name \tTelephone Number\t Status Explanation\n";
# ?session_id=$main::session{session_id}&lead_id=$show_data{lp_lead_id}&emplid=$emplid

my $success = eval {
my $sth = $myDB->prepare($new_sql) or die $myDB->errstr;
$sth->{PrintError} = 0;
$sth->execute($emplid, $program_id, $fund_id, $region_id)  or die $sth->errstr;

while(my $show_data = $sth->fetchrow_hashref){

	print qq[
			<tr><td><p>$show_data->{lp_lead_id} </p></td>
				<td><p>$show_data->{fmt_created_date}</p></td>
				<td><p>$show_data->{lead_company_name}</p></td>
				<td><p>$show_data->{lead_name}</p></td>
				<td><p>$show_data->{main_btn}</p></td>
				<td colspan="4"><p>$show_data->{st_ex}</p></td>
			</tr>
];
	  print CSVDATA $show_data->{lp_lead_id}."\t".$show_data->{fmt_created_date}."\t".$show_data->{lead_company_name}."\t".$show_data->{lead_name}."\t". $show_data->{main_btn}."\t".$show_data->{st_ex}."\n";
	}
$sth->finish();	

};
unless($success) {
	DBInterface::writelog('youcan10',"$thisfile", $@ );
}

}
print qq [</table></div>];

## show open

print qq[<div id="hide_show_open" $divClass >
			<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
			<tr class="progressLead">
          <td colspan="8"><p><strong>In Progress ($open)</strong></p></td>
                      </tr>
					  ];
print CSVDATA "In Progress ($open)\n";

if ($open > 0) {
print qq[
	 <tr><td width="14.25%"><p><strong>Referral \#</strong></p></td>
	 <td width="14.25%"><p><strong>Created Date</strong></p></td>
	 <td width="14.25%"><p><strong>Business Name</strong></p></td>
 <td width="14.25%"><p><strong>Customer name</strong></p></td>
	 <td width="14.25%"><p><strong>Telephone Number</strong></p></td>
<td colspan="2"><p><strong>Status Explanation</strong></p></td>
</tr>
];
print CSVDATA "Referral \# \tCreated Date \tBusiness Name \tCustomer Name \tTelephone Number \tStatus Explanation\n";

$new_sql=" select lp_lead.lp_lead_id , convert(varchar,created_date,1) as fmt_created_date,main_btn,
isnull(rtrim(lead_company_name), '') as lead_company_name, rtrim(lead_name) as lead_name, lead_status_id,
	dbo.func_getstatus(lp_lead.lead_status_id, 154)as status_name,
isnull(( select RTRIM(description) from lp_status_description lsd with (nolock) 
where lsd.program_id = lp_lead.program_id and lsd.lead_status_id = isnull(lp_lead.lead_status_id,0)
and isActive = 1
),'') as st_ex
        from lp_lead with (nolock)
	inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
        where lp_lead.agency_id = ?
        and lp_lead.program_id = ?
        and lp_lead.fund_id = ? and created_date > '01/01/2014'
		and ISNULL(lp_lead.lp_region_id,0) <> ?
                and isnull(lp_lead.lead_status_id,0) between 1 and 49
                order by lead_status_id, lp_lead.lp_lead_id desc";
my $success = eval {				
my $sth = $myDB->prepare($new_sql);
$sth->execute($emplid, $program_id, $fund_id, $region_id) or die $sth->errstr;

while(my $show_data = $sth->fetchrow_hashref){

print<<"EOF";
 <tr><td><p>$show_data->{lp_lead_id} </p></td>
	 <td><p>$show_data->{fmt_created_date}</p></td>
	 <td><p>$show_data->{lead_company_name}</p></td>
	<td><p>$show_data->{lead_name}</p></td>
	 <td><p>$show_data->{main_btn}</p></td>
<td colspan="4"><p>$show_data->{st_ex}</p></td>
</tr>
EOF
	  print CSVDATA $show_data->{lp_lead_id}."\t".$show_data->{fmt_created_date}."\t".$show_data->{lead_company_name}."\t".$show_data->{lead_name}."\t". $show_data->{main_btn}."\t".$show_data->{st_ex}."\n";
}
$sth->finish();
};
unless($success) {
	DBInterface::writelog('youcan10',"$thisfile", $@ );
}

}
print qq [</table></div>];
#--
# show purchased 
print qq[<div id="hide_show_purch" $divClass >
			<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
			<tr class="accuracyLead">
          <td colspan="7"><p><strong>Accuracy Check ($purch)</strong></p></td>
                      </tr>
					  ];
print CSVDATA "Accuracy Check ($purch)\n";
if ($purch > 0) {
$new_sql=" select lp_lead.lp_lead_id , convert(varchar,created_date,1) as fmt_created_date,main_btn,
isnull(rtrim(lead_company_name), '') as lead_company_name,rtrim(lead_name) as lead_name, lead_status_id,
'' as prodsold --dbo.fnGetLeadProductsSold (lp_lead.lp_Lead_id) as prodsold
        from lp_lead with (nolock)
	inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
        where lp_lead.agency_id = ?
        and lp_lead.program_id = ?
        and lp_lead.fund_id = ? and created_date > '01/01/2014'
		and ISNULL(lp_lead.lp_region_id,0) <> ?
			 and isnull(lp_lead.lead_status_id,0) > 0
                and isnull(lp_lead.lead_status_id,0) in (50,51)
                order by lead_status_id, lp_lead.lp_lead_id desc";

print qq[ <tr><td width="14.25%"><p><strong>Referral \#</strong></p></td>
	 <td width="14.25%"><p><strong>Created Date</strong></p></td>
	 <td width="14.25%"><p><strong>Business Name</strong></p></td>
 <td width="14.25%"><p><strong>Customer name</strong></p></td>
	 <td width="14.25%"><p><strong>Telephone Number</strong></p></td>
	 <td width="14.25%"><p><strong>Products Sold</strong></p></td>
<td colspan="1"><p><strong>&nbsp;</strong></p></td>
</tr>
];
print CSVDATA "Referral \# \tCreated Date \tBusiness Name \tCustomer Name \tTelephone Number \tProducts Sold\n";

my $success = eval {
my $sth = $myDB->prepare($new_sql);
$sth->execute($emplid, $program_id, $fund_id, $region_id) or die $sth->errstr;

while(my $show_data = $sth->fetchrow_hashref){

print<<"EOF";
 <tr><td><p>$show_data->{lp_lead_id}</p></td>
	 <td><p>$show_data->{fmt_created_date}</p></td>
	 <td><p>$show_data->{lead_company_name}</p></td>
	<td><p>$show_data->{lead_name}</p></td>
	 <td><p>$show_data->{main_btn}</p></td>
	 <td><p>$show_data->{prodsold}</p></td>
<td><p>&nbsp;</p></td>
</tr>
EOF
	  print CSVDATA $show_data->{lp_lead_id}."\t".$show_data->{fmt_created_date}."\t".$show_data->{lead_company_name}."\t".$show_data->{lead_name}."\t". $show_data->{main_btn}."\t".$show_data->{prodsold}."\n";
}
$sth->finish();
};
unless($success) {
	DBInterface::writelog('youcan10',"$thisfile", $@ );
}

}
print qq [</table></div>];
# TO ADD CLOSED PAID
my ($curr_batch_id, $inBatch_id, $batch_date, $dt_sql, %dt_dt, $print_dt, $print_gross, $print_net);
print qq[<div id="hide_show_close_purch" $divClass >
			<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
			<tr class="accuracyLead">
          <td colspan="7"><p><strong>Awarded ($closePaid)</strong></p></td>
                      </tr>
					  ];
print CSVDATA "Awarded ($closePaid)\n";
if ($closePaid > 0) {
$new_sql="select lp_lead.lp_lead_id , convert(varchar,created_date,1) as fmt_created_date,main_btn, 
isnull(rtrim(lead_company_name), '') as lead_company_name,rtrim(lead_name) as lead_name, lead_status_id,
lead_gross_amount,batch_id , '' as prodsold, --, dbo.fnGetLeadProductsSold (lp_lead.lp_Lead_id) as prodsold,
case when (select payroll_batch_id  from ctl_payroll_batches with (nolock) where process_batch_id = lp_lead.batch_id) > 0  
then 1 else 0 end as pay_processed, datename (month, lead_check_date) as mname, DATEPART(dd, lead_check_date) as dname,DATEPART(yyyy, lead_check_date) as yyyy,
--(select date_created from batch with (nolock) where batch_id = lp_Lead.batch_id) as batch_date,
(select bs.description from batch_status bs with (nolock) 
	inner join batch with (nolock) on batch.batch_status_id = bs.batch_status_id and batch.batch_id = lp_lead.batch_id) as batch_status,
(select SUM(lead_gross_amount) from lp_lead b with (nolock) where b.batch_id = lp_lead.batch_id and b.agency_id = lp_lead.agency_id
and b.program_id = 154 and b.fund_id = 511) as total_gross,	
case when (select payroll_batch_id  from ctl_payroll_batches with (nolock) where process_batch_id = lp_lead.batch_id) > 0 
then (select approved_net from ctl_payroll_visa cpv with (nolock) where cpv.batch_id = lp_lead.batch_id and cpv.emplid = lp_lead.agency_id)
else (select sum(a.lead_check_amount) from lp_lead a with (nolock) where a.batch_id = lp_lead.batch_id 
and a.agency_id = lp_lead.agency_id and a.program_id = 154 and a.fund_id = 511)
end as net
        from lp_lead with (nolock)
	inner join lkup_qwest_opts opts with (nolock) on opts.lp_lead_id = lp_lead.lp_lead_id
        where lp_lead.agency_id = ?
        and lp_lead.program_id = ?
        and lp_lead.fund_id = ? and created_date > '01/01/2014'
		and ISNULL(lp_lead.lp_region_id,0) <> ?
			 and isnull(lp_lead.lead_status_id,0) > 0
                and isnull(lp_lead.lead_status_id,0) = 52
                order by batch_id desc
";
#$new_sql = "exec sp_CTL_getPayrollAwarded ?,?,?";
 ($curr_batch_id, $print_gross, $print_net)=(-1,0,0);
			
print qq[
 <tr><td width="14.25%"><p><strong>Referral \#</strong></p></td>
	 <td width="14.25%"><p><strong>Created Date</strong></p></td>
	 <td width="14.25%"><p><strong>Business Name</strong></p></td>
 <td width="14.25%"><p><strong>Customer name</strong></p></td>
	 <td width="14.25%"><p><strong>Telephone Number</strong></p></td>
	 <td width="14.25%"><p><strong>Products Sold</strong></p></td>
<td><p><strong>Gross Amount</strong></p></td>
</tr>
];
print CSVDATA "Referral \# \tCreated Date \tBusiness Name \tCustomer Name \tTelephone Number \tProducts Sold \tGross Amount\n";
 
my $success = eval {
my $sth = $myDB->prepare($new_sql) or die $myDB->errstr;
$sth->{PrintError} = 0;
$sth->execute($emplid, $program_id, $fund_id, $region_id)  or die $sth->errstr;

while(my $show_data = $sth->fetchrow_hashref){
	#$batch_date = $show_data->{batch_date};
	$print_dt = $show_data->{mname}.' '.$show_data->{dname}.', '.$show_data->{yyyy};
	if ($curr_batch_id==$show_data->{batch_id}) {
		print qq[
 <tr><td><p>$show_data->{lp_lead_id}</p></td>
	 <td><p>$show_data->{fmt_created_date}</p></td>
	<td><p>$show_data->{lead_name}</p></td>
	 <td><p>$show_data->{main_btn}</p></td>
	 <td><p>$show_data->{prodsold}</p></td>
<td><p>$show_data->{lead_gross_amount}</p></td>
</tr>
];
	  print CSVDATA $show_data->{lp_lead_id}."\t".$show_data->{fmt_created_date}."\t".$show_data->{lead_company_name}."\t".$show_data->{lead_name}."\t". $show_data->{main_btn}."\t".$show_data->{prodsold}."\t".$show_data->{lead_gross_amount}."\n";
	}
	else {
		#finish previous net, gross - if any leads displayed so not for 1
		if ($curr_batch_id > 0) {
		print qq[ <tr class="alt"><td colspan="2"><p><strong>Gross Total Award : $print_gross</strong></p></td>
					<td><p>&nbsp;</p></td>
					<td colspan="2"><p><strong>Net to Award Card : $print_net</p></td>
					<td colspan="2">&nbsp;</td>
				</tr> ];
	  print CSVDATA "Gross Total Award \t".$print_gross."\t \tNet to Award Card". $print_net."\n";
		}
		print qq[ <tr><td colspan="7"><p><strong>Referrals Awarded $print_dt </strong></p></td></tr> ];
		print CSVDATA "Closed Sales \t".$print_dt."\n";

		# print lead one
		print qq[  <tr><td><p>$show_data->{lp_lead_id}</p></td>
						<td><p>$show_data->{fmt_created_date}</p></td>
						<td><p>$show_data->{lead_company_name}</p></td>
						<td><p>$show_data->{lead_name}</p></td>
						<td><p>$show_data->{main_btn}</p></td>
						<td><p>$show_data->{prodsold}</p></td>
						<td><p>$show_data->{lead_gross_amount}</p></td>
					</tr> ];
	  print CSVDATA $show_data->{lp_lead_id}."\t".$show_data->{fmt_created_date}."\t".$show_data->{lead_company_name}."\t".$show_data->{lead_name}."\t". $show_data->{main_btn}."\t".$show_data->{prodsold}."\t".$show_data->{lead_gross_amount}."\n";
		# set $curr_batch_id = new batch id
		$curr_batch_id=$show_data->{batch_id};
		$print_gross =  $show_data->{total_gross};
		$print_net = $show_data->{net};
	}
}
$sth->finish();	

};
unless($success) {
	DBInterface::writelog('youcan10',"$thisfile", $@ );
}



		print qq[ <tr class="alt"><td colspan="2"><p><strong>Gross Total Award : $print_gross</strong></p></td>
					<td><p>&nbsp;</p></td>
					<td colspan="2"><p><strong>Net to Award Card : $print_net</p></td>
					<td colspan="2">&nbsp;</td>
				</tr> ];
	  print CSVDATA "Gross Total Award \t".$print_gross."\t \tNet to Award Card". $print_net."\n";

#close div
}

print qq[</table></div>];
# SHOW NO SOLD

print qq[<div id="hide_show_nosale" $divClass >
			<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
			<tr class="noawardLead" style="color:#A9AAA1;">
          <td colspan="7"><p><strong>No Award ($noSold)</strong></p></td>
                      </tr>
					  ];
print CSVDATA "No Award ($noSold)\n";

if ($noSold > 0) {
$new_sql="select lp_lead.lp_lead_id , convert(varchar,created_date,1) as fmt_created_date,main_btn,
isnull(rtrim(lead_company_name), '') as lead_company_name,rtrim(lead_name) as lead_name, lead_status_id,
dbo.func_getstatus(lp_lead.lead_status_id, 154)as status_name,isnull((
select RTRIM(description) from lp_status_description lsd with (nolock) 
where lsd.program_id = lp_lead.program_id and lsd.lead_status_id = lp_lead.lead_status_id
and isActive = 1
),'') as st_ex
        from lp_lead with (nolock)
	inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
        where lp_lead.agency_id = ?
        and lp_lead.program_id = ?
        and lp_lead.fund_id = ? and created_date > '01/01/2014'
		and ISNULL(lp_lead.lp_region_id,0) <> ?
			 and isnull(lp_lead.lead_status_id,0) > 0
                and isnull(lp_lead.lead_status_id,0) > 52
                order by lp_lead.lp_lead_id desc";
print qq[<tr><td width="14.25%"><p><strong>Referral \#</strong></p></td>
	 <td width="14.25%"><p><strong>Created Date</strong></p></td>
		 <td width="14.25%"><p><strong>Business Name</strong></p></td>
 <td width="14.25%"><p><strong>Customer name</strong></p></td>
	 <td width="14.25%"><p><strong>Telephone Number</strong></p></td>
	 <td width="14.25%"><p><strong>Closed Reason</strong></p></td>
<td ><p><strong>Status Explanation</strong></p></td>
</tr>
];
print CSVDATA "Referral \# \tCreated Date \tBusiness Name \tCustomer Name \tTelephone Number \tClosed Reason \tStatus Explanation\n";

my $sth = $myDB->prepare($new_sql);
$sth->execute($emplid, $program_id, $fund_id, $region_id);

while(my $show_data = $sth->fetchrow_hashref){

print<<"EOF";
 <tr><td><p>$show_data->{lp_lead_id} </p></td>
	 <td><p>$show_data->{fmt_created_date}</p></td>
	 <td><p>$show_data->{lead_company_name}</p></td>
	<td><p>$show_data->{lead_name}</p></td>
	 <td><p>$show_data->{main_btn}</p></td>
	 <td><p>$show_data->{status_name}</p></td>
<td><p>$show_data->{st_ex}</p></td>
</tr>
EOF
	  print CSVDATA $show_data->{lp_lead_id}."\t".$show_data->{fmt_created_date}."\t".$show_data->{lead_company_name}."\t".$show_data->{lead_name}."\t". $show_data->{main_btn}."\t".$show_data->{status_name}."\t".$show_data->{st_ex}."\n";
}

}
print qq[</table></div>];

# grand table
print qq[ </td></tr></table>];

#-------------------------OKAY ABOVE THIS	--------------------------------------------------------------------------------

#--
=head
#===show closed/paid
my ($curr_batch_id, $inBatch_id, $batch_date, $dt_sql, %dt_dt, $print_dt, $print_gross, $print_net);
$show_sql = " select 0 as cnt UNION select count(lp_lead_id) from lp_lead with (nolock) where agency_id = ?
                and program_id = ? and fund_id = ? and isnull(lead_status_id,0) = ? and created_date > '01/01/2009'
                order by 1 desc";
				
my $sth = $myDB->prepare($show_sql);
$sth->execute($emplid, $program_id, $fund_id, 52);

my $show_data = $sth->fetchrow_hashref();				
				
$open_cnt=$show_data->{cnt};
print qq[ <table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
			<tr class="soldLead">
          <td colspan="6"><p><strong>Awarded ($open_cnt)</strong> ];
if ($open_cnt > 0) {
	print qq[ <small><a href="javascript:void(0)" onclick="toggleDiv('hide_show_close_purch',this);">Show Lead List</a></small> ];
}

print qq [  </p></td>
                      </tr>
					 </table><hr />  ];
					
print CSVDATA "Awarded ($open_cnt)\n";
	
if ($open_cnt > 0) {
$new_sql="select lp_lead_id , convert(varchar,created_date,1) as fmt_created_date,main_btn, 
isnull(rtrim(lead_company_name), '') as lead_company_name,rtrim(lead_name) as lead_name, lead_status_id,
lead_gross_amount,batch_id, dbo.fnGetLeadProductsSold (lp_lead.lp_Lead_id) as prodsold,
case when (select payroll_batch_id  from ctl_payroll_batches with (nolock) where process_batch_id = lp_lead.batch_id) > 0  
then 1 else 0 end as pay_processed, datename (month, lead_check_date) as mname, DATEPART(dd, lead_check_date) as dname,DATEPART(yyyy, lead_check_date) as yyyy,
(select date_created from batch with (nolock) where batch_id = lp_Lead.batch_id) as batch_date,
(select bs.description from batch_status bs with (nolock) 
	inner join batch with (nolock) on batch.batch_status_id = bs.batch_status_id and batch.batch_id = lp_lead.batch_id) as batch_status,
(select SUM(lead_gross_amount) from lp_lead b with (nolock) where b.batch_id = lp_lead.batch_id and b.agency_id = lp_lead.agency_id
and b.program_id = 154 and b.fund_id = 511) as total_gross,	
case when (select payroll_batch_id  from ctl_payroll_batches with (nolock) where process_batch_id = lp_lead.batch_id) > 0 
then (select approved_net from ctl_payroll_visa cpv with (nolock) where cpv.batch_id = lp_lead.batch_id and cpv.emplid = lp_lead.agency_id)
else (select sum(a.lead_check_amount) from lp_lead a with (nolock) where a.batch_id = lp_lead.batch_id 
and a.agency_id = lp_lead.agency_id and a.program_id = 154 and a.fund_id = 511)
end as net
        from lp_lead with (nolock)
        where lp_lead.agency_id = ?
        and lp_lead.program_id = ?
        and lp_lead.fund_id = ? and created_date > '01/01/2009'
			 and isnull(lp_lead.lead_status_id,0) > 0
                and isnull(lp_lead.lead_status_id,0) = ?
                order by batch_id desc
";
			 #<!--	387 $new_sql	-->
print qq[
<div id="hide_show_close_purch"  $divClass >  <!--	408	<pre>$new_sql</pre>	-->
				<table width="100%" border="0" cellspacing="0" cellpadding="0" class="reward-values">
 <tr><td width="14.25%"><p><strong>Referral \#</strong></p></td>
	 <td width="14.25%"><p><strong>Created Date</strong></p></td>
	 <td width="14.25%"><p><strong>Business Name</strong></p></td>
 <td width="14.25%"><p><strong>Customer name</strong></p></td>
	 <td width="14.25%"><p><strong>Telephone Number</strong></p></td>
	 <td width="14.25%"><p><strong>Products Sold</strong></p></td>
<td><p><strong>Gross Amount</strong></p></td>
</tr>
];
print CSVDATA "Referral \# \tCreated Date \tBusiness Name \tCustomer Name \tTelephone Number \tProducts Sold \tGross Amount\n";

my $sth = $myDB->prepare($new_sql);
$sth->execute($emplid, $program_id, $fund_id, 52);

($curr_batch_id, $print_gross, $print_net)=(-1,0,0);

while(my $show_data = $sth->fetchrow_hashref){

	$batch_date = $show_data->{batch_date};
	$print_dt = $show_data->{mname}.' '.$show_data->{dname}.', '.$show_data->{yyyy};
	if ($curr_batch_id==$show_data->{batch_id}) {
		print qq[
 <tr><td><p>$show_data->{lp_lead_id}</p></td>
	 <td><p>$show_data->{fmt_created_date}</p></td>
	<td><p>$show_data->{lead_name}</p></td>
	 <td><p>$show_data->{main_btn}</p></td>
	 <td><p>$show_data->{prodsold}</p></td>
<td><p>$show_data->{lead_gross_amount}</p></td>
</tr>
];
	  print CSVDATA $show_data->{lp_lead_id}."\t".$show_data->{fmt_created_date}."\t".$show_data->{lead_company_name}."\t".$show_data->{lead_name}."\t". $show_data->{main_btn}."\t".$show_data->{prodsold}."\t".$show_data->{lead_gross_amount}."\n";
	}
	else {
		#finish previous net, gross - if any leads displayed so not for 1
		if ($curr_batch_id > 0) {
		print qq[ <tr class="alt"><td colspan="2"><p><strong>Gross Total Award : $print_gross</strong></p></td>
					<td><p>&nbsp;</p></td>
					<td colspan="2"><p><strong>Net to Award Card : $print_net</p></td>
					<td>&nbsp;</td>
				</tr> ];
	  print CSVDATA "Gross Total Award \t".$print_gross."\t \tNet to Award Card". $print_net."\n";
		}

		# print new heading
		$dt_sql = "select case when DATEPART(dd, '$batch_date') between 1 and 15 then 1 else 2 end as mp,
					DATENAME(MONTH, '$batch_date') as mname, DATEPART(yyyy, '$batch_date') as yy,
					datepart(dd,dbo.fnLastDayofMonth ('$batch_date')) as last_day";
		$myDB4->Sql($dt_sql);
		$myDB4->FetchRow();
		%dt_dt=  $myDB4->DataHash();
	#	$print_dt = $dt_dt{mname}.' ';
	#	if ($dt_dt{mp} == 1) { $print_dt .= '1-15, ';}
	#	else {$print_dt .='15-'.$dt_dt{last_day}.', ';}
	#	$print_dt .= $dt_dt{yy};

		print qq[ <tr><td colspan="6"><p><strong>Referrals Awarded $print_dt </strong></p></td></tr> ];
		print CSVDATA "Closed Sales \t".$print_dt."\n";

		# print lead one
		print qq[  <tr><td><p>$show_data->{lp_lead_id}</p></td>
						<td><p>$show_data->{fmt_created_date}</p></td>
						<td><p>$show_data->{lead_company_name}</p></td>
						<td><p>$show_data->{lead_name}</p></td>
						<td><p>$show_data->{main_btn}</p></td>
						<td><p>$show_data->{prodsold}</p></td>
						<td><p>$show_data->{lead_gross_amount}</p></td>
					</tr> ];
	  print CSVDATA $show_data->{lp_lead_id}."\t".$show_data->{fmt_created_date}."\t".$show_data->{lead_company_name}."\t".$show_data->{lead_name}."\t". $show_data->{main_btn}."\t".$show_data->{prodsold}."\t".$show_data->{lead_gross_amount}."\n";
		# set $curr_batch_id = new batch id
		$curr_batch_id=$show_data->{batch_id};
		$print_gross =  $show_data->{total_gross};
		$print_net = $show_data->{net};

	}
}
		print qq[ <tr class="alt"><td colspan="2"><p><strong>Gross Total Award : $print_gross</strong></p></td>
					<td><p>&nbsp;</p></td>
					<td colspan="2"><p><strong>Net to Award Card : $print_net</p></td>
					<td>&nbsp;</td>
				</tr> ];
	  print CSVDATA "Gross Total Award \t".$print_gross."\t \tNet to Award Card". $print_net."\n";

#close div
print qq[ </table> </div> ];
}
# show Closed/No Sale

	

}
=cut
print<<"EOF";
					  </div>
                
			</div><!--END CAPSULE-->	
        </div><!--END BODY-LEFT-SEC-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
EOF
close CSVDATA;
showftr ( $cci_id);
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

