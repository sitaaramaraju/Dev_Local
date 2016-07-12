use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');
#require "D:/centurylinkyoucan/cgi-bin/init.cgi";
#my $myDB = Win32::ODBC->new($main::DSN);

my  $PAGETITLE = 'CenturyLink Business - Tech Service Tool';

=head
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;
=cut

my $user_type = $cgi->param('user_type')||'';
my $msg = '';
if ($user_type eq 'Invalid') {
	$msg = '<small><em>Invalid Logon</em></small><br>';
}

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
<!--JAVASCRIPT-->
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="/assets/js/functions.js"></script>
<script type="text/javascript" src="sbgvalidate.js"></script>
		<script type="text/javascript" src="http://centurylinkyoucan.com/jquery/simplemodal/simplemodal.js"></script>
		<link rel="stylesheet" type="text/css" href="http://centurylinkyoucan.com/jquery/simplemodal/simplemodal.css"/>
<!--[if lte IE 7]>
	<script type="text/javascript" src="/assets/js/ie-fix.js"></script>
<![endif]-->
</head>
<body>
<div id="layout">
		<div id="layout-header">
    	<img src="assets/img/logo-centurylink.png" width="242px"/>
    </div>
    <div id="layout-body">
    	<h2>Login to Your Account</h2><br>
		<h4>Business Offer Optimization Sales Tool</h4><br>$msg
        	<table width="100%" border="0" class="form-table">
              <tr>
 <form name="login" action="/cgi-bin/lp-validate.cgi" method="post"> 
                     <input type="hidden" name="source_id" id="source_id" value="2" />
                     <input type="hidden" name="program_id" value="447">
                     <input type="hidden" name="fund_id" value="3223">
                <td width="42%" align="right"><p><label for="username">Username (CUID or SAP ID)</label></p></td>
                <td width="58%"><input name="userid" id="userid" type="text" tabindex="1" class="text-field"/>
				<span id='reqUser'>  </span></td>
              </tr>
              <tr>
                <td align="right"><p><label for="password">Password</label></p></td>
                <td><input name="password" id="password" type="password" tabindex="2" class="text-field" />
				<span id='reqPass'>  </span>
				<small><em><a href="#" onclick="openModalmedium('forgotpwd.cgi');return false;">I forgot my password</a></em></small></td>
              </tr>
              <tr>
                <td align="center" colspan="2"><p><input name="stayloggedin" id="stayloggedin" type="checkbox" tabindex="3" value="" /> <label for="stayloggedin">Keep me Logged In</label></p></td>
              </tr>
              <tr>
                <td align="center" colspan="2"><input type="submit" tabindex="4" class="button-login" onclick="checkLogin()"/></td>
              </tr>
            </table>
        </form>
    </div>
    <div id="layout-footer">
    <p>&copy;<script language="javascript">var currentTime = new Date(); var year = currentTime.getFullYear();document.write(year);</script>
	CenturyLink, Inc. All Rights Reserved.</p>
    </div>
</div>
</body>
</html>
EOF
#$myDB ->Close();
