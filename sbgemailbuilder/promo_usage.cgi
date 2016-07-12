use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

require "G:/CenturyLink/xroot/cgi-bin/init.cgi";
require "G:/CenturyLink/xroot/cgi-bin/delimeter.cgi";
my $db = Win32::ODBC->new($main::DSN);
my $myDB = Win32::ODBC->new($main::DSN);

my  $PAGETITLE = 'CenturyLink Business - Tech Service Tool';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;

my $session_id=$main::cgi{session_id};
my $source=$main::cgi{source};
my $emplid = $cgi->param('staff_id');

my ($ss, $s, $e, $staff) = 	(	$cgi->param('session_id') , $cgi->param('source'), $cgi->param('emplid'), $cgi->param('staff_id'));

my $thisfile = "promo_usage.cgi";

my $sql = "";
if ($s == 2) {
	$sql = "select RTRIM(first_name)+' '+RTRIM(last_name) as ename , rtrim(cuid) as ecuid from qwesthr with (nolock) where emplid = $staff";
}
else {
	$sql = "select RTRIM(first_name)+' '+RTRIM(last_name) as ename , rtrim(cuid) as ecuid from ctl_floaters with (nolock) where floater_id = $staff";
}

$myDB->Sql($sql);
$myDB->FetchRow();
my %show_data = $myDB->DataHash();
my $ename=$show_data{ename};
my $ecuid = $show_data{ecuid};


print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" itemscope itemtype="http://schema.org/Event">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<title>$PAGETITLE</title>

<!--FAVICON-->
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<!--CSS-->
<link type="text/css" href="assets/css/style.css" rel="stylesheet" title="print" media="screen" />
<link type="text/css" href="assets/css/chevron6.css" rel="stylesheet" />
<!--JAVASCRIPT-->
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="/assets/js/functions.js"></script>
<script type="text/javascript" src="sbgvalidate.js"></script>
		<script type="text/javascript" src="http://centurylinkyoucan.com//jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="http://centurylinkyoucan.com//jquery/simplemodal/simplemodal.css"/>

<!--[if lte IE 7]>
	<script type="text/javascript" src="/assets/js/ie-fix.js"></script>
<![endif]-->
</head>
<body>
<center>
<table width="600" border="0" cellspacing="0" cellpadding="0">
<tr align="right">
<td><img src="http://www.smallbizmailtool.com/emails/logo-centurylink.gif" alt="CenturyLink Business" border="0" style="margin-top:6px;" /></td></tr>
<tr><td><div style="padding:0 12px;"><font size="+3" face="Arial, Helvetica, sans-serif" color="#00853F">
<strong>Promo Offer Usage<br> Data for $ename</strong> </font></div>
</td></tr>
</table>
<table width="600" cellspacing="0" cellpadding="0" class="email-content-title">

<tr> <td width="50%" align="center"><p><strong> Promotion </p></strong></td><td width="25%" align="center"><p><strong> Current Month To Date</p></strong></td><td width="25%" align="center"><p><strong> Previous Month</p></strong></td></tr>
</table>
<table width="600" border="0" class="email-content">
EOF

my $row_class = "class=\"alt\"";
=head
$sql = "select distinct PU.promo_name, 
(select ISNULL(sum(qty_used),0) from ctl_sbg_PromoUsage p1 with (nolock) where p1.promo_name = PU.promo_name
and date_used between dbo.fnFirstDayofMonth (getdate()) and CONVERT(varchar, dbo.fnLastDayofMonth (getdate()), 110)+' 23:59:59' and p1.CUID = PU.cuid) as thismonth,
 (select ISNULL(sum(qty_used),0) from ctl_sbg_PromoUsage p1 with (nolock) where p1.promo_name = PU.promo_name
and date_used between dateadd(mm, datediff(mm, 0, dateadd(MM, -1, getdate())), 0)
           and dateadd(ms, -3, dateadd(mm, datediff(mm, 0, dateadd(MM, -1, getdate())) + 1, 0)) and p1.CUID = PU.cuid) as lastmonth
 from ctl_sbg_PromoUsage  PU with (nolock)
where PU.cuid ='$ecuid'";

#print qq[<tr><td colspan="3">$sql</td></tr>];
$myDB->Sql($sql);
while ($myDB->FetchRow()) {
	%show_data = $myDB->DataHash();

	if ($row_class eq "") { $row_class = "class=\"alt\""; }
		else {$row_class = ""; }
		
			print qq[
			<tr $row_class><td width="50%" align="center" ><p>$show_data{promo_name} </p></td>
				<td width="25%" align="center"><p>$show_data{thismonth}</p></td>
				<td width="25%" align="center"><p>$show_data{lastmonth}</p></td>
			</tr>
				];

}

=cut
#get dates
$sql = "select dbo.fnFirstDayofMonth (getdate()) as thismnthbegin,
 CONVERT(varchar, dbo.fnLastDayofMonth (getdate()), 110)+' 23:59:59' as thismnthend,
 dateadd(mm, datediff(mm, 0, dateadd(MM, -1, getdate())), 0) as lastmnthbegin,
 dateadd(ms, -3, dateadd(mm, datediff(mm, 0, dateadd(MM, -1, getdate())) + 1, 0)) as lastmnthend";
$myDB->Sql($sql);
$myDB->FetchRow();
%show_data = $myDB->DataHash();

my $thismnthbegin = $show_data{thismnthbegin};
my $thismnthend = $show_data{thismnthend};
my $lastmnthbegin = $show_data{lastmnthbegin};
my $lastmnthend = $show_data{lastmnthend};

my ($pmname, $sql1, %dt, $lastqu, $thisqu);
#get promos
$sql = "select distinct rtrim(promo_name) as pmname from  ctl_sbg_PromoUsage with (nolock)
where cuid = '$ecuid' and date_used between '$lastmnthbegin' and '$thismnthend'";
$myDB->Sql($sql);
while ($myDB->FetchRow()) {
	%show_data = $myDB->DataHash();
	$pmname = $show_data{pmname};

	#lastmnth
	$sql1 = "select isnull(SUM(qty_used),0) as lastqu from ctl_sbg_PromoUsage with (nolock)
			where CUID = '$ecuid' and promo_name = '$pmname' and date_used between '$lastmnthbegin' and '$lastmnthend'";
	$db->Sql($sql1);
	$db->FetchRow();
	%dt = $db->DataHash();
	$lastqu = $dt{lastqu};

	
	$sql1="select isnull(SUM(qty_used),0) as thisqu from ctl_sbg_PromoUsage with (nolock)
			where CUID = '$ecuid' and promo_name = '$pmname' and date_used between '$thismnthbegin' and '$thismnthend'";
	$db->Sql($sql1);
	$db->FetchRow();
	%dt = $db->DataHash();
	$thisqu = $dt{thisqu};
	
	if ($row_class eq "") { $row_class = "class=\"alt\""; }
		else {$row_class = ""; }
		
			print qq[
			<tr $row_class><td width="50%" align="center" ><p>$pmname </p></td>
				<td width="25%" align="center"><p>$thisqu</p></td>
				<td width="25%" align="center"><p>$lastqu</p></td>
			</tr>
				];




}
print<<"EOF";
</td></tr></table>
</body>
</html>
EOF
$db ->Close();
$myDB->Close();
