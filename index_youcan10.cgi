use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');
use CCICryptography;
my $url = CCICryptography::getUrl();
my  $PAGETITLE = 'YOUCAN | Deliver the VIP Experience.';

print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>YOUCAN | Deliver the VIP Experience</title>

<!--FAVICON-->
<link href="/favicon.ico" rel="shortcut icon" type="image/x-icon" />

<!--CSS-->
<link type="text/css" href="youcan10/assets/css/style.css" rel="stylesheet" />

<!--JAVASCRIPT-->
<script type="text/javascript" src="youcan10/assets/js/jquery.js"></script>
<script type="text/javascript" src="youcan10/assets/js/functions.js"></script>
<script type="text/javascript" src="youcan10/assets/js/youcan_functions.js"></script>
<script type="text/javascript" src="jquery/simplemodal/simplemodal.js"></script>
<link rel="stylesheet" type="text/css" href="jquery/simplemodal/simplemodal.css"/>


<script type="text/javascript">
	animatedcollapse.addDiv('nav-sec-1', 'fade=0,speed=500,group=nav,hide=1,height=22px,persist=1')
	animatedcollapse.addDiv('nav-sec-2', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-3', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-4', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-5', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-6', 'fade=0,speed=500,group=nav,hide=1,height=22px')

	animatedcollapse.init()
</script>

</head>

<body onload="onPageLoaded()">
<div id="layout">

	<div id="layout-header">
    	<div id="header-content">
       		<a href="$url"><img src="/youcan10/assets/img/header.gif" alt="$PAGETITLE" title="$PAGETITLE" class="youcan-logo" /></a>
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
                        <td colspan="2" align="right"></td>
                      </tr>
 <form name="logon" action="/cgi-bin/lp-validate.cgi" method="post">
     <input type='hidden' name='program_id' value="154">
     <input type="hidden" name="fund_id" value="511">
     <input type="hidden" name="source_id" value="2">
	<input type="hidden" name="redir" value="">
<!-- login	-->
                      <tr>
                        <td width="33%" align="right"><p>YOUCAN Login: </p></td>
                        <td >
						<input type="text" name="logid" id="logid"  value="SAP ID OR CUID" class="ins" size="15" onfocus="swapLoginBoxes('click')"
						style="font-style:oblique;color:#585858;font-size:10px;display:none;width:130px;height:18px;" >
						<input type="text" name="userid" id="userid" value="" size="15" class="ins" onblur="swapLoginBoxes('blur')" 
						style="width:130px;height:18px;" onKeyPress="catchEnter();"/>&nbsp;<small>Your YOUCAN Login is your CUID or your SAP ID.</small><br><span id='reqd_login'></span>

						</td>
                      </tr>

<!-- pwd	-->

<tr>
                        <td align="right"><p>Password: </p></td>
                        <td>
<input type="text" name="pwdPlain" id="pwdPlain" value="Home Zip Code" size="15" class="ins" onfocus="swapPasswordBoxes('click')"
style="font-style:oblique;color:#585858;font-size:10px;display:none;width:130px;height:18px;"/>
<input type="password" name="password" id="password" value="" size="15" class="ins" onblur="swapPasswordBoxes('blur')" 
style="width:130px;height:18px;" onKeyPress="catchEnter();"/>&nbsp;<small>Your default password is your home zip code.</small>
<br><span id='reqd_pwd'></span></td>
<td>
                      </tr>
<!--	-->
                      <tr>
                        <td colspan="2" align="center"><p>
										If you&rsquo;ve changed your password and need a reminder,
										<a href="#" onclick="toggleMsg('fgtPwdMsg');">Click here</a>.
										</p>
										</td>
                      </tr>
					  <tr>
					    <td colspan="2" align="center"><div id="fgtPwdMsg" name="fgtPwdMsg" style="display:none;">
								<p>Please email <a href="mailto:Youcan.Support\@centurylink.com">Youcan.Support\@centurylink.com</a> to request a reset of your current password.</p></div>
										
										</td>
                      </tr>
                      <tr>
                        <td colspan="2" align="center"><input name="" type="submit" class="but-login" value="" onsubmit="checkform()"/></td>
                      </tr>
                    </table>
                    </form>
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
