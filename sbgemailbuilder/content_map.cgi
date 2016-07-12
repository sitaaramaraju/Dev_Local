use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $server;
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}

$main::DSN = 'driver={SQL Server};Server=qadb.coopcom.net;database=staging;uid=fm;pwd=sep49sling;';
    
require "$server/cgi-bin/delimeter.cgi";
require "$server/cgi-bin/init.cgi";

	my $db          = Win32::ODBC->new($main::DSN);
	my $db2         = Win32::ODBC->new($main::DSN);
	my $db3         = Win32::ODBC->new($main::DSN);
my (%data, $description,$sql, $sql2, %data2, $theme_id);
my ($row_class, $cnt, $desc2);


print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<title>CenturyLink Business - Tech Service Tool</title>

<!--FAVICON-->
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<!--CSS-->
<link type="text/css" href="assets/css/style.css" rel="stylesheet" title="print" media="screen" />
<!--JAVASCRIPT-->
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="assets/js/functions.js"></script>
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
<!--POPUP CONTENT MAP--> 
    <div id="popup" style="padding:10px; background:#FFFFFF;">
    	<h2>Email Content Links</h2>
    	<table width="100%" cellpadding="6" border="0" class="email-content-title">
          <tr>
            <td width="16%" rowspan="2">Theme Selection </td>
            <td width="16%" rowspan="2">Topic Selection</td>
            <td width="17%" colspan="2" float="50%">Legacy Qwest/CRIS</td>
		<!--	<td width="17%">Linked Content Legacy Qwest/CRIS (Spanish)</td>	-->
            <td width="17%" colspan="2" float="50%">Legacy CenturyLink/Ensemble </td>
         <!--   <td width="17%">Linked Content Legacy CenturyLink/Ensemble (Spanish)</td>	-->
          </tr>
		  <tr>
		 <!--   <td width="16%">Theme Selection </td>	-->
          <!--    <td width="16%">Topic Selection</td>	-->
            <td width="17%">&nbsp;English</td>
			<td width="17%">&nbsp;Spanish</td>
            <td width="17%">&nbsp;English</td>
            <td width="17%">&nbsp;Spanish</td>
          </tr>

        </table>
];
my ($pdf_url_spanish, $pdf_LCL,$pdf_LCL_spanish ,$ns, $n_LCL, $n_LCLS , $pdf_url);

# for sell_sheets
$sql = "select theme.theme_id, theme.description 
			from ctl_sbgEmail_theme theme with (nolock)
			where theme.is_active = 1 and theme_id = 1 ";
$db->Sql($sql);
#	print qq[ $sql <br>	];
while ($db->FetchRow()) {
	%data = $db->DataHash();
	$description = $data{description};
	$theme_id = $data{theme_id};
	$cnt = 0;
	$row_class = "";
	print qq[ <h5>$description </h5> 
				<table width="100%" border="0" class="email-content">];
		$sql2 = "select  heading as desc2, description as pdf_name, pdf_url
				from  ctl_sbgEmail_sellsheets with (nolock) where is_active = 1
				order by heading_order, item_order ";
		$sql2 = "select  heading as desc2, description as pdf_name, isnull(LQ_english,0) as LQ_english, pdf_url,isnull( LQ_spanish,0) as LQ_spanish,
 pdf_url_spanish,ISNULL( LCTL_english,0) as LCTL_english , pdf_LCL,isnull(LCTL_spanish,0) as LCTL_spanish, pdf_LCL_spanish
				from  ctl_sbgEmail_sellsheets with (nolock) where is_active = 1
				order by heading_order, item_order";
$db2->Sql($sql2);
	print qq[<!-- $sql2 <br> -->	];
while ($db2->FetchRow()) {
	%data2 = $db2->DataHash();
	$pdf_url		= $data2{pdf_url};	
	$pdf_url_spanish = $data2{pdf_url_spanish};
	$pdf_LCL		= $data2{pdf_LCL};
	$pdf_LCL_spanish = $data2{pdf_LCL_spanish};

#--
	#--
	if ($desc2 ne  $data2{desc2}) {
		if ($cnt > 0) { print qq [</p> </td></tr>]; }
		if ($row_class eq "") { $row_class = "class=\"alt\""; }
		else {$row_class = ""; }

		print qq[  <tr $row_class>
				<td width="16%">&nbsp;</td>
				<td width="16%"><p class="greendk"><strong>$data2{topic_head} $data2{desc2}</strong></p></td>
				
			];
		$cnt++;
	}
	else {
		print qq[  <tr $row_class>
				<td width="16%">&nbsp;</td>
				<td width="16%"><p class="greendk">&nbsp;</p></td>
			];

	}

	# if's here for LQ English
	if ($data2{LQ_english} == 1 && $pdf_url eq "" ) {
		print qq[ <td width="17%"><p>LQ $data2{pdf_name} <font color="red">(need pdf)</font></p></td> ];
	}
	elsif ($data2{LQ_english} == 0) {
		print qq[ <td width="17%"><p><font color="red">&ndash;</font></p></td> ];
	}
	else {
		print qq[ <td width="17%"><p><a href="$pdf_url">LQ $data2{pdf_name}</a></p></td> ];
	}
	# if's here for LQ Spanish
	if ($data2{LQ_spanish} == 1 && $pdf_url_spanish eq "" ) {
		print qq[ <td width="17%"><p>LQ-S $data2{pdf_name} <font color="red">(need pdf)</font></p></td> ];
	}
	elsif ($data2{LQ_spanish} == 0) {
		print qq[ <td width="17%"><p><font color="red">&ndash;</font></p></td> ];
	}
	else {
		print qq[ <td width="17%"><p><a href="$pdf_url_spanish">LQ-S $data2{pdf_name}</a></p></td> ];
	}
	# if's here for LCTL English
	if ($data2{LCTL_english} == 1 && $pdf_LCL eq "" ) {
		print qq[ <td width="17%"><p>LCTL $data2{pdf_name} <font color="red">(need pdf)</font></p></td> ];
	}
	elsif ($data2{LCTL_english} == 0) {
		print qq[ <td width="17%"><p><font color="red">&ndash;</font></p></td> ];
	}
	else {
		print qq[ <td width="17%"><p><a href="$pdf_LCL">LCTL $data2{pdf_name}</a></p></td> ];
	}
	# if's here for LCTL Spanish
	if ($data2{LCTL_spanish} == 1 && $pdf_LCL_spanish eq "" ) {
		print qq[ <td width="17%"><p>LCTL-S $data2{pdf_name} <font color="red">(need pdf)</font></p></td> ];
	}
	elsif ($data2{LCTL_spanish} == 0) {
		print qq[ <td width="17%"><p><font color="red">&ndash;</font></p></td> ];
	}
	else {
		print qq[ <td width="17%"><p><a href="$pdf_LCL_spanish">LCTL-S $data2{pdf_name}</a></p></td> ];
	}
	$desc2 = $data2{desc2};

}
print qq[ </table> ];

}
# for all others
print qq [
    	<table width="100%" cellpadding="6" border="0" class="email-content-title">
          <tr>
            <td width="16%">Theme Selection </td>
            <td width="16%">Topic Selection</td>
            <td width="68%">Linked Content </td>
          </tr>
        </table>
];
$sql = "select theme.theme_id, theme.description 
			from ctl_sbgEmail_theme theme with (nolock)
			where theme.is_active = 1 and theme_id > 1
order by theme_id ";
$db->Sql($sql);
#	print qq[ $sql <br>	];
while ($db->FetchRow()) {
	%data = $db->DataHash();
	$description = $data{description};
	$theme_id = $data{theme_id};
	$cnt = 0;
	$row_class = "";
	print qq[ <h5>$description </h5> 
				<table width="100%" border="0" class="email-content">];
		$sql2 = "select topic_head, description as desc2, pdf_url, pdf_name
		from ctl_sbgEmail_topic with (nolock)
		where is_active = 1 and theme_id = $theme_id";
$db2->Sql($sql2);
#	print qq[ $sql2 <br>	];
while ($db2->FetchRow()) {
	%data2 = $db2->DataHash();
	$pdf_LCL		= $data2{pdf_LCL};

	#--
		if ($cnt % 2 == 0) {
		$row_class = "class=\"alt\"";
	}
	else {
		$row_class = "";
	}

	#--
	if ($desc2 ne  $data2{desc2}) {
		if ($cnt > 0) { print qq [</p> </td></tr>]; }
		print qq[  <tr $row_class>
				<td width="16%">&nbsp;</td>
				<td width="16%"><p class="greendk"><strong>$data2{topic_head} $data2{desc2}</strong></p></td>
				<td width="68%"><p><a href="$data2{pdf_url}">$data2{pdf_name}</a></p>
			];
		$cnt++;
	}
	else {
		print qq[  <br><p><a href="$data2{pdf_url}">$data2{pdf_name}</a></p>];

	}

	$desc2 = $data2{desc2};

}
print qq[ </table> ];

}
# end of all others
print qq[
 
    </div>
</body>
</html>
];


  $db->Close();
  $db2->Close();
  $db3->Close();
