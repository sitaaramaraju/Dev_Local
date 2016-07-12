use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;

use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||'';

my $server;
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnectuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
	$server = "/centurylinkyoucan/";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnect.com'){
    $server = "D:/centurylinkyoucan";
}
else {
    $server = "D:/centurylinkyoucan";
	#$server = "/centurylinkyoucan";
}

#require "$server/cgi-bin/init.cgi";
require "$server/qwestconnect07/subs.cgi";
#my $url = "centurylinkyoucandev.com/index_lmsii07.cgi";
my $url = CCICryptography::getUrl_sites('lms');

my $db = DBInterface->new();
############## validation ################
my $valid = 0;
if ($cci_id ne "") {
	$valid =  CCICryptography::validate_CL_sites($cci_id,'lms');
}
else {
	$valid = 1;
}

if ($valid <= 0) {
  headernocss();
  print qq[
  <form name="lead" action="" method="post">
  <input type="hidden" name="session_id" value="0">
    <script language='javascript'>
      alert("There was an error loading the page.  Please log in and try again.");
      document.lead.action='$url';
      document.lead.submit();
    </script>
  </form>
 </body>
</html>];
exit();

}


my  $PAGETITLE = 'CenturyLink Connect';
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
#print $header;
my $special = $cgi->param('special');






my $special= $cgi->param('special');
 
my  $PAGETITLE = 'CenturyLink Connect-New Enrollment';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;


print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>$PAGETITLE</title>
<script language="JavaScript" src="qwestconnect07menus.js"></script>
<script language="JavaScript" src="validate.js"></script>
<link href="Style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="mm_menu.js"></script>
</head>

<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif')">
<script language="JavaScript1.2">mmLoadMenus();</script>
<table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td>
];
getHeader($cci_id);

print qq[	
	</td>
      </tr>
                    <tr>
                        <td width="954" height="9" align="left" valign="top">
                            <img src="images/topBumper.gif" width="954" height="9" /></td>
                    </tr>
                    <tr>
                        <td background="images/background.gif">
                            <table width="913" border="0" align="center" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/Sub_titleTop.gif" width="913" height="16" /></td>
                                </tr>
                                <tr>
                                    <td background="images/Subtitle_tile.gif">
                                        <table width="900" border="0" cellspacing="1" cellpadding="1">
                                            <tr>
                                                <td width="10">&nbsp;                                                    </td>
                                                <td align="left" valign="top" class="BlueTitles">
                                                    $PAGETITLE&nbsp;                                                </td>
                                            </tr>
                                        </table>                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
                                </tr>
                                <tr>
                                    <td align="left" valign="middle" background="images/Sub_tile.gif">
                                        <table width="900" border="0" cellspacing="1" cellpadding="1">
                                            <tr>
                                                <td width="10" align="left" valign="top">&nbsp;                                                    </td>
                                                <td align="left" valign="top">
                                                    <table width="875" border="0" align="center" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td>
                                                                &nbsp;<table align="center" border="0" cellpadding="1" cellspacing="1" width="850">
                                                                        <td align="left" valign="top">
                                                                            <table border="0" cellpadding="1" cellspacing="1" class="Enrollcopy" width="860">
<form name="regi_b2c" action="welcome.cgi" method="post">

<tr>
<td width="405" align="right" valign="top" class="FAQuestions">CUID / Reference Code</td>
<td width="2">&nbsp;</td>
<td width="443" align="left" valign="top" class="LEQuiz">
<div align="left">
<input name="osr_id" class="FAQuestions" type="text" style="width: 100px" />*<span id="req_osr"></span>
</div>
</td>
</tr>


<tr>
<td align="left" class="BlueTitles" valign="top" colspan="3"><div align="center">Business Information:</div></td>
</tr>


<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Business Name:<br>(as it should appear on Reward check)</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="bus_name" class="FAQuestions" type="text" style="width: 232px" />*<span id="req_bus_name"></span></div></td>
</tr>

<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Business Address:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top">
<div align="left"><input name="bus_addr1" type="text" class="FAQuestions" style="width: 230px" />*<br />
					<input name="bus_addr2" type="text" class="FAQuestions" style="width: 229px" /></div>                                                                                    </td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">City:</div> </td>
<td>&nbsp;</td>
 <td align="left" valign="top"><div align="left"><input name="bus_city" type="text" class="FAQuestions" style="width: 97px" />*</div>                                                                                    </td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">State:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left">
<select class="FAQuestions" name="bus_state" style="width: 138px"><option value="" selected="selected">--Select State--</option>
];



	my	$sql = "select distinct state, abbreviation  from lp_states with (nolock) where program_id = 154  order by state";
			my $sth = $db->prepare($sql);
			$sth->execute();

			while (my $state = $sth->fetchrow_hashref) {
 				print qq[<option name='state' value='$state->{abbreviation}' >$state->{state}</option>];
			}
			$sth->finish();
	print qq[
					 </select>*</div> </td>
</tr>
<tr>
<td class="FAQuestions"><div align="right">Zip:</div></td>
<td>&nbsp;</td>
<td><div align="left"><input name="bus_zip" type="text" class="FAQuestions" style="width: 57px" />*<span id="req_bus_addr"></span></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Primary Phone Number:</div> </td>
<td>&nbsp;</td>
 <td align="left" valign="top"><div align="left">
		<input type="text" name = "bus_prim_phone1" class="FAQuestions" value=""size="3" maxlength="3"  onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "bus_prim_phone2" class="FAQuestions" value=""size="3" maxlength="3" onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "bus_prim_phone3" class="FAQuestions" value=""size="4" maxlength="4">*<span id="req_p1"></span></div> </td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Secondary Phone Number:</div> </td>
<td>&nbsp;</td>
 <td align="left" valign="top"><div align="left">
		<input type="text" name = "bus_sec_phone1" class="FAQuestions" value=""size="3" maxlength="3"  onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "bus_sec_phone2" class="FAQuestions" value=""size="3" maxlength="3" onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "bus_sec_phone3" class="FAQuestions" value=""size="4" maxlength="4"></div></td>
</tr>
<tr>
<td width="405" align="right" valign="top" class="FAQuestions">Please select your Industry:</td>
<td width="2">&nbsp;</td>
<td width="443" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="industry">
<option value="">-- Select --</option>
<option value="Advertising/Public Relations">Advertising/Public Relations</option>
<option value="Construction/Mining">Construction/Mining</option>
<option value="Agriculture">Agriculture</option>
<option value="Finance">Finance</option>
<option value="Insurance">Insurance</option>
<option value="Real Estate/Leasing Agent">Real Estate / Leasing Agent</option>
<option value="General Retail">General Retail</option>
<option value="Manufacturing">Manufacturing</option>
<option value="Transportation">Transportation</option>
<option value="Wholesale">Wholesale</option>
<option value="Legal Service">Legal Service</option>
<option value="Medical/Health Services">Medical/Health Services</option>
<option value="Other Professional Services">Other Professional Services</option>
<option value="Business Services">Business Services</option>
<option value="Entertainment/Travel Services">Entertainment/Travel Services</option>
<option value="Maintenance/Repair Services">Maintenance/Repair Services</option>
<option value="Telecommunications">Telecommunications (e.g. Telephone, Internet, Cable, Satellite TV)</option>
<option value="Other">Other</option>
</select>*<span id="req_indus"></span>
</div>
</td>
</tr>

<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Business is a Multi-Dwelling Unit (MDU) property:</div> </td>
<td>&nbsp;</td>
 <td align="left" valign="top"><div align="left"> 
	<input name="yes_mdu"  class="FAQuestions"  type="radio" value="1"/>&nbsp; Yes
	<input name="yes_mdu"  class="FAQuestions"  type="radio" value="0"/>&nbsp; No</div>*</td>
</tr>

<tr>
<td align="left" class="BlueTitles" valign="top" colspan="3"><div align="center">Primary Contact Information:</div></td>
</tr>

<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">First Name: </div> </td>
 <td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input type="text" name="first" class="FAQuestions" style="width: 100px" />*</div></td>
 </tr>

<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Last Name: </div> </td>
 <td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input type="text" name="last" class="FAQuestions" style="width: 100px" />*<span id="req_cont_name"></span></div></td>
 </tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Email:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="email" type="text" class="FAQuestions" style="width: 232px" />*<span id="req_email"></span></div></td>
</tr>
<tr>
<td width="405" align="right" valign="top" class="FAQuestions">Salutation:</td>
<td width="2">&nbsp;</td>
<td width="443" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="salutation">
<option value=""> - Select Your Title - </option>
	<option value="Mr.">Mr.</option>
	<option value="Mrs.">Mrs.</option>
	<option value="Miss">Miss</option>
	<option value="Ms.">Ms.</option>
	<option value="Dr.">Dr.</option>
        <option value="Prof.">Prof.</option>
        <option value="Rev.">Rev.</option>
	<option value="Other">Other</option>

</select>
</div>
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Job Title:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="job_title" type="text" class="FAQuestions" style="width: 232px" />*</div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Contact Number:</div> </td>
<td>&nbsp;</td>
 <td align="left" valign="top"><div align="left">
		<input type="text" name = "contact_phone1" class="FAQuestions" value=""size="3" maxlength="3"  onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "contact_phone2" class="FAQuestions" value=""size="3" maxlength="3" onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "contact_phone3" class="FAQuestions" value=""size="4" maxlength="4">*<span id="req_contact_phone"></span></div></td>
</tr>

<!--	--------------------------------------------------------------------------	-->
<!--	BELOW IS W9	-->
<tr>
<td align="left" class="BlueTitles" valign="top" colspan="3"><div align="center">W9 Information - Request for Taxpayer Identification Number and Certification:</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Business Name (as shown on your Income tax Return):</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="bus_name_w9" type="text" class="FAQuestions" style="width: 232px" />*<span id="req_w9name"></span></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Check appropriate box:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="bus_type" type="radio" value="1" />
	<span class="FAQuestions" valign="top">Individual/Sole Proprietor</span></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">&nbsp;</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="bus_type" type="radio" value="2" />
	<span class="FAQuestions" valign="top">Corporation</span></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">&nbsp;</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="bus_type" type="radio" value="3" />
	<span class="FAQuestions" valign="top">Partnership</span></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Other:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="bus_type" valign="top" type="radio" value="4" />
	<input name="bus_type_other_w9" type="text" class="FAQuestions" style="width: 232px" /></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Exempt from Backup Withholding:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><input name="withold_w9" type="checkbox" class="FAQuestions" value="yes" /></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">&nbsp;</td>
</tr>

<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">Part 1: Taxpayer Identification Number </td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">Enter your TIN in the
  appropriate box. The TIN provided must match the name given on Line 1 to
  avoid backup withholding. For individuals, this is your social security
  number (SSN). However, for a resident alien, sole proprietor, or disregarded
  entity, or other entities, or if you do not have a number, please see instructions at the IRS website</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">Note: If the account is in more than one name,
	see the chart on the IRS Website for guidelines on whose number to enter.</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Social Security number:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left">
		<input type="text" name = "ssn1" value="" class="FAQuestions" size="3" maxlength="3"  onKeyUp="return autoTab(this, 3, event);">-
        <input type="text" name = "ssn2" value="" class="FAQuestions" size="2" maxlength="2" onKeyUp="return autoTab(this, 2, event);">-
        <input type="text" name = "ssn3" value="" class="FAQuestions" size="4" maxlength="4"></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="center">OR:<span id="req_ssn"></span> </td>
</tr>

<tr>
<td align="left" class="FAQuestions" valign="top"><div align="right">Employer Identification number:</div></td>
<td>&nbsp;</td>
<td align="left" valign="top"><div align="left"><div align="left">
		<input type="text" name = "ein1" value="" class="FAQuestions" size="2" maxlength="2"  onKeyUp="return autoTab(this, 2, event);">-
        <input type="text" name = "ein2" value="" class="FAQuestions" size="7" maxlength="7"></div></div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">&nbsp;</td>
</tr>

<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">Part 2: Certification Under penalties of perjury, I certify that:</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">
<ol align="left" class="FAQuestions" valign="top" colspan="3">
   <li >The number shown on this form is my correct taxpayer identification number (or I am waiting for a number to be issued to me), and</li>
   <li >I am not subject to backup withholding because: (a) I am exempt from backup withholding, or (b) I have not been notified by the Internal Revenue Service (IRS) that I am subject to backup
       withholding as a result of a failure to report all interest or dividends, or (c) the IRS has notified me that I am no longer subject to backup withholding, and</li>
   <li>I am a U.S. person (including a U.S. resident alien).
</ol>
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">Certification instructions. You must cross out item 2 above if you have been notified by
  the IRS that you are currently subject to backup withholding because you have failed to report all interest and dividends on your tax return. For real
  estate transactions, item 2 does not apply. For mortgage interest paid, acquisition or abandonment of secured property, cancellation of debt,
  contributions to an individual retirement arrangement (IRA), and generally, payments other than interest and dividends, you are not required to sign the
  Certification, but you must provide your correct TIN. (See the instructions at the IRS website.)</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">I CERTIFY THAT I AM THE PERSON (OR AUTHORISED REPRESENTATIVE OF THE ENTITY)
	IDENTIFIED IN THIS FORM W-9 AND THAT THE INFORMATION PROVIDED HEREIN IS TRUE AND CORRECT</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top" colspan="3"><div align="left">&#91;The Internal Revenue Service does not require your consent to any
provision of this document other than the certification required to avoid backup witholding.&#93;</td>
</tr>
<!--	ABOVE IS W9	-->

<!--	-------------------------------------------------------------------	-->

                                                                                <tr>
                                                                                  <td align="left" class="FAQuestions" valign="top">&nbsp;</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top">&nbsp;</td>
                                                                                </tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">&nbsp; </td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top">&nbsp;</td>
										  </tr>

                                                                                <tr>
                                                                                  <td colspan="3" align="center" valign="top" class="FAQuestions">
										  <input type="hidden" name="redir" value=""><input type="hidden" name="enrollType" value="b2c">
										  <INPUT TYPE="text" NAME="NameForBotsB2C" SIZE="48" style='display:none;'>
										  <input type="button" name="go" value="REGISTER NOW" class="btnon"
											onMouseOver="this.className='btnoff';"
											onMouseOut="this.className='btnon';" onclick="checkform_b2c();"></td>
                                                                                </tr>
</form>

                                                                                <tr>
                                                                                  <td colspan="3" align="center" valign="top" class="Earncopy">* Required * </td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">&nbsp;</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top">&nbsp;</td>
                                                                                </tr>
		                                                                      </td>
                                                                            </table>
												</tr>                                                                </table>                                                            </td>
                                                        </tr>
                                                        <tr>
                                                             <td colspan="2" align="center">&nbsp;</td>
                                                        </tr>
                                                  </table>                                                </td>
                                            </tr>
                                        </table>                                    </td>
                                </tr>
];
getFooter($cci_id);
print qq[
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>
]

