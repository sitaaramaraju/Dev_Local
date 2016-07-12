use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

require "G:/CenturyLink/xroot/cgi-bin/init.cgi";
#require "G:/CenturyLink/xroot/cgi-bin/email.cgi";

print $cgi->header('text/html');

my $myDB = Win32::ODBC->new($main::DSN);
my $myDB2 = Win32::ODBC->new($main::DSN);
my $emplid = $cgi->param('emplid')||0;
my $session_id = $cgi->param('session_id')||0;

my $redir = $cgi->param('redir') ||0;
my $login = $cgi->param('login') ||'';
my $msg = '';

my $thisfile="forgot_pwd.cgi";
my  $PAGETITLE = 'YOUCAN | Deliver the VIP Experience.';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;




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
<link href="assets/css/iefix.css" type="text/css" rel="stylesheet" />
<!--JAVASCRIPT-->
<script type="text/javascript" src="assets/js/jquery.js"></script>
<script type="text/javascript" src="assets/js/functions.js"></script>
<script type="text/JavaScript">
<!--

function checkcuid() {
        document.get_login.redir.value = 1;
	if( document.get_login.login.value == "" ){
            document.get_login.redir.value = 0;
            window.alert('Please enter your Login ID');
	}

	if ( document.get_login.redir.value == 0 ) {
            return false;
        }
        else{
            document.get_login.submit();
            return true;
        }

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
</head>

<body>

    
    	<div id="body-left-sec">
        	<div class="capsule-710">
            	<div class="capsule-710-header">
                	<h2>Forgot Password</h2>
                </div>
				                <div class="capsule-content">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" class="login-entry">

EOF
       if ($redir == 0) {

print<<"EOF";
                      <tr>
                        <td colspan="2" align="center"><p>Please enter your SAP ID to retrieve your password</p></td>
                      </tr>

      <form name="get_login" action="$thisfile" method="post">
                      </tr>
                      <tr>
                        <td colspan="2" align="center"><p>SAP ID: &nbsp;&nbsp;<input name="login" type="text" size="12" class="ins" /><br>
		  &nbsp;<small>Enter your full alpha numeric SAP ID. This is your ID formatted similar to ABC123456.</small>
						  <input type="hidden" name="redir" value=""></td>
                      </tr>
                    
                      <tr>
                        <td colspan="2" align="center"><input name="" type="submit" class="but-submit" value="" onclick="checkcuid();"/></td>
                      </tr>
					                      </form>

EOF
	}
if ($redir == 1) {

$msg = check_login( $login, $myDB);

print<<"EOF";        

                      <tr>
                        <td colspan="2" align="center"><p>$msg</p></td>
                      </tr>
                    
EOF
	}

print<<"EOF";
                    </table>
                </div>
            </div><!--END CAPSULE-->	
        </div><!--END BODY-LEFT-SEC-->
        <br class="clear" />

</body>
</html>
EOF
$myDB ->Close();
$myDB2 ->Close();

sub check_login{
my $login = shift;
my $db2 = shift;
my $msg = '';
my ($sql,  $email);
my ($ret, $to, $cc, $bcc, $from, $subject, $body);
my(%pwd_data, $pwd);
my $sql = "select isnull(qwesthr_my.email, '') as m_email, isnull(qwesthr.email, '') as o_email, 
isnull(qwesthr_password.password, '') as m_pwd, isnull(qwesthr.home_zip, '') as o_pwd
 from qwesthr_my with (nolock) , qwesthr with (nolock), qwesthr_password with (nolock)
where  (isnull(qwesthr.cuid, '') = '$login' or qwesthr.SAP_ID = '$login')
and qwesthr.cuid *= qwesthr_my.cuid
and qwesthr.cuid *= qwesthr_password.cuid
and qwesthr.emp_status = 'A' ";

$sql = "select isnull(qm.email, '') as m_email, isnull(qwesthr.email, '') as o_email, 
isnull(qp.password, '') as m_pwd, isnull(qwesthr.home_zip, '') as o_pwd
 from  qwesthr with (nolock)
 left outer join qwesthr_my qm with (nolock) on qm.cuid = qwesthr.cuid
  left outer join qwesthr_password qp with (nolock) on qp.cuid = qwesthr.cuid
where  (isnull(qwesthr.cuid, '') = '$login' or qwesthr.SAP_ID = '$login')
and qwesthr.emp_status = 'A' ";


$db2->Sql($sql);
$db2->FetchRow();
my %m_data = $db2->DataHash();
my $m_email = $m_data{m_email};
my $m_pwd = $m_data{m_pwd};
my $o_email = $m_data{o_email};
my $o_pwd = $m_data{o_pwd};

if ($o_email eq '' and $m_email eq '' ) {
	$msg = 'Due to error, we are not able to retrieve this information.';
	#$msg .= $sql;
}
elsif ( $o_pwd eq '' and $m_pwd eq '') {
	$msg = 'Due to error, we are not able to retrieve this information.';
	#$msg .= $sql;
}


if ($m_email eq '' and $o_email ne '') {
 $email = $o_email;
}
else {
$email = $m_email;
}
if ($m_pwd eq '' and $o_pwd ne '') {
$pwd = $o_pwd;
}
else {
$pwd = $m_pwd;
}
if ($pwd ne '') {
	$msg = "Your password will be sent to the default e-mail address you set on your MyYOUCAN page. <br>
	If you have not made any revisions to the default, it will be sent to your work email address (firstname.lastname\@CenturyLink.com). 
";

	$bcc = '';#archanak@ccionline.biz, scotts@ccionline.biz';
	$from = 'youcan@centurylinkyoucan.com';
	$cc =  '';#'archanak@ccionline.biz';
	$subject = 'YOUCAN Information';
	$body = ' Following is your login/password information
	
	Login : ';
	$body .= $login ;
	$body .= "\n Password: ";
	$body .= $pwd;
	$body .= "\n If you have any questions email us or call us at 1 866-8YOUCAN \n\n YOUCAN Team ";
	#$body .=$email;
	$sql = "insert into ccimail (date_created, client_id, program_id, subject, tofield, fromfield, ctype, longbody, bccfield)
	values(GETDATE(), 50, 154, 'YOUCAN Information', '$email', '$from', 'application/octet-stream','$body', '$bcc')";
	#send email to archanak
	#$sql = "insert into ccimail (date_created, client_id, program_id, subject, tofield, fromfield, ctype, longbody)
	#values(GETDATE(), 50, 154, 'YOUCAN Information', '$to', '$from', 'application/octet-stream','$body')";

	$db2->Sql($sql);
	$db2->FetchRow();


}
else {
	$msg = 'Due to error, we are not able to retrieve this information.';

}

return $msg;

}