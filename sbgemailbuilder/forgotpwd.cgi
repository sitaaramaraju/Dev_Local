use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use CGI qw(:standard);
my $cgi = CGI->new();
my $myDB = DBInterface->new();


my  $PAGETITLE = 'CenturyLink Business - Tech Service Tool';


my $sql;
my $redir = $cgi->param('redir')||0;
my $thisfile="forgotpwd.cgi";


	print qq [
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" itemscope itemtype="http://schema.org/Event">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<title>$PAGETITLE</title>

<!--FAVICON-->
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<!--CSS-->
<link type="text/css" href="assets/css/style.css" rel="stylesheet" title="print" media="screen" />
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
<form name="fpwd" action="$thisfile" method="post">
<input type="hidden" name="redir" value="$redir">
<table width="600" border="0" cellspacing="0" cellpadding="0">
<tr align="right">
<td><img src="emails/logo-centurylink.gif" alt="CenturyLink Business" border="0" style="margin-top:6px;" /></td></tr>
<tr><td>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr><td width="600" height="39" background="emails/body-top.gif">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>
<tr><td width="600" background="emails/body-center.gif">
<div style="padding:0 12px;"><font size="+3" face="Arial, Helvetica, sans-serif" color="#00853F">
<strong>Retrieve Password,</strong></font></div></td>
];

	print qq [
<tr><td><br><br>&nbsp;&nbsp;<font size="+1" face="Arial, Helvetica, sans-serif"><label for="username">Username (CUID or SAP ID)</label></font>
<input name="loginid" id="loginid" type="text" tabindex="1" class="text-field"/>
		<label><span id='req_someID'></span></label></td></tr>
<tr><td align="center" ><br><br><br><strong><a href="#" onclick="getpwd()">Send Login Credentials</a></strong></td></tr>
		];


	print qq [
<tr><td width="600" height="39" background="http://www.smallbizmailtool.com/emails/body-bottom.gif">&nbsp;</td>  
    </tr></table></td></tr>
  </table>  </center>
</form>

</body>
</html>
];
