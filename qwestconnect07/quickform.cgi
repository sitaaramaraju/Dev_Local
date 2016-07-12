use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
#use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||'';
my $redir = $cgi->param('redir')||0;
my $server ="";
my $msg ="";


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
my $thisfile = "quickform.cgi";
my $url = CCICryptography::getUrl_sites('lms');

############## validation ################
my $valid = 0;
if ($cci_id ne "") {
	$valid = 1;#CCICryptography::validate_CL_sites($cci_id,'lms');
}
else {
	$valid = 1;
}

if ($valid <= 0) {
  #my $url = "https://www.centurylinkconnect.com/";
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

#<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
my ($part_name,$part_email,$part_phone,$part_timetocall, $part_refnum , $issue, $explanation);

my $name;
print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>$PAGETITLE</title>
<script language="JavaScript" src="validate.js"></script>
<link href="Style.css" rel="stylesheet" type="text/css" />
</head>
<body>




];


print qq[	

      <tr>
        <td width="954" height="9" align="left" valign="top"><img src="images/topBumper.gif" width="954" height="9" /></td>
      </tr>
      <tr>
        <td background="images/background.gif"><table width="913" border="0" align="center" cellpadding="0" cellspacing="0">
          <tr>
            <td align="left" valign="top"><img src="images/Sub_titleTop.gif" width="913" height="16" /></td>
          </tr>
          <tr>
            <td background="images/Subtitle_tile.gif"><table width="900" border="0" cellspacing="1" cellpadding="1">
              <tr>
                <td width="10">&nbsp;</td>
                <td align="left" valign="top" class="BlueTitles">CenturyLink Referral Rewards Contact Us </td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td align="left" valign="top"><img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
          </tr>
          <tr>
            <td align="left" valign="middle" background="images/Sub_tile.gif"><table width="900" border="0" cellspacing="1" cellpadding="1">
              <tr>
                <td width="10" align="left" valign="top">&nbsp;</td>
                <td><table width="600" border="0" align="center" cellpadding="1" cellspacing="1">
];
if ($redir == 0) {
print qq[
                  <tr>
                    <td class="Enrollcopy">In order for us to properly address your concerns, please provide the following information and click the &quot;Send E-Mail&quot; button when complete.</td>
                  </tr>
]
}
print qq[
                  <tr>
                    <td>&nbsp;</td>
                  </tr>
                  <tr>
                    <td><table width="594" border="0" cellspacing="2" cellpadding="2">
];

if ($redir == 0) {
print qq[
<form name="contact" method="post" action="$thisfile">
                      <tr>
                        <td width="144" align="left" valign="top" class="FAQuestions">Your Name:* </td>
                        <td colspan="2" align="left" valign="top">
];
if ($name ne '') {
	print qq[
	<input name="part_name" type="text" value="$name" size="50" readonly/>
];
}
	else {
	print qq[
	<input name="part_name" type="text" size="50" />
];
	}
print qq[
						
						<span id='req_name'></span></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">E-Mail Address:* </td>
                        <td colspan="2" align="left" valign="top"><input name="email" type="text" size="50" /><span id='req_email'></span></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Phone Number (daytime):</td>
                        <td colspan="2" align="left" valign="top"><input name="phone" type="text" size="10" /></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Best Time to Call: </td>
                        <td colspan="2" align="left" valign="top"><input name="time_to_call" type="text" size="50" /></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Referral Number: </td>
                        <td colspan="2" align="left" valign="top"><input name="refnum" type="text" size="50" /></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td colspan="2" align="left" valign="top">&nbsp;</td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Help Topic:* </td>
                        <td colspan="2" align="left" valign="top">&nbsp;&nbsp;<span id='req_helpTopic'></span></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td width="24" align="left" valign="top"><input name="issue" type="radio" value="American Express Card" /></td>
                        <td width="387" align="left" valign="top" class="FAQuestions">Reward card </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top"><input name="issue" type="radio" value="Referral issue" /></td>
                        <td align="left" valign="top" class="FAQuestions">Referral issue </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top"><input name="issue" type="radio" value="General Program question" /></td>
                        <td align="left" valign="top" class="FAQuestions">General Program question </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top"><input name="issue" type="radio" value="Web site question" /></td>
                        <td align="left" valign="top" class="FAQuestions">Web site question </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top"><input name="issue" type="radio" value="Other issue" /></td>
                        <td align="left" valign="top" class="FAQuestions">Other issue or question </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top">&nbsp;</td>
                        <td align="left" valign="top">&nbsp;</td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top">&nbsp;</td>
                        <td align="left" valign="top">&nbsp;</td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Explanation:*</td>
                        <td colspan="2" align="left" valign="top"><textarea name="explanation" cols="50"></textarea><br><span id='req_text'></span></td>
                        </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td colspan="2" align="left" valign="top">&nbsp;</td>
                      </tr>
                      <tr>
                        <td colspan="3" align="center" valign="top">
							<input type="hidden" name="redir" value="">
							<input type="submit" name="Submit" value="Send E-Mail" onclick="checkContactform();"/></td>
                      </tr>
							</form>
                      <tr>
    <td colspan="3" align="right" class="FAQuestions" valign="top">
        *Required Fields
    </td>
</tr>

];
}
else { # redir == 1 so send email

	$part_name = $cgi->param('part_name');
	$part_email = $cgi->param('email');
	$part_phone = $cgi->param('phone');
	$part_timetocall = $cgi->param('time_to_call');
	$part_refnum = $cgi->param('refnum');
	$issue = $cgi->param('issue');
	$explanation = $cgi->param('explanation');


	 my $msg =   send_email( $part_name, $part_email, $part_phone, $part_timetocall, $part_refnum, $issue, $explanation );

		print qq [ $msg ];


}
	print qq[
					</table></td>
                  </tr>
                </table>
                  <br />
                  <br /></td>
              </tr>
            </table></td>
          </tr>
 ];
#getFooter($cci_id);
print qq[
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>
];

#---------------------------------------------------------------------------------------------------------------------------------------------



=head
my $style = 'style="display:none;"';
my $contacterror = $cgi->param('contacterror');
if ($redir == 1) {
	$style = "";

	$part_name = $cgi->param('part_name');
	$part_email = $cgi->param('email');
	$part_phone = $cgi->param('phone');
	$part_timetocall = $cgi->param('time_to_call');
	$part_refnum = $cgi->param('refnum');
	$issue = $cgi->param('issue');
	$explanation = $cgi->param('explanation');
}

	if ($redir == 0) {
	print qq[
				<form name="contact" action="$thisfile" method="post">
<input type="hidden" name="program_id" value="269"> 

                   <tr>
                    <td class="Enrollcopy" colspan="3">In order for us to properly address your concerns, please provide the following information and click the &quot;Send E-Mail&quot; button when complete.<br></td>
                  </tr>
				  <tr>
                        <td width="144" align="left" valign="top" class="FAQuestions">Your Name:* </td>
                        <td colspan="2" align="left" valign="top"><input name="part_name" type="text" size="50" /><span id='req_name'></span></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">E-Mail Address:* </td>
                        <td colspan="2" align="left" valign="top"><input name="email" type="text" size="50" /><span id='req_email'></span></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Phone Number (daytime):</td>
                        <td colspan="2" align="left" valign="top"><input name="phone" type="text" size="10" /></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Best Time to Call: </td>
                        <td colspan="2" align="left" valign="top"><input name="time_to_call" type="text" size="50" /></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Referral Number: </td>
                        <td colspan="2" align="left" valign="top"><input name="refnum" type="text" size="50" /></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td colspan="2" align="left" valign="top">&nbsp;</td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Help Topic:* </td>
                        <td colspan="2" align="left" valign="top">&nbsp;<span id='req_helpTopic'></span></td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td width="24" align="left" valign="top"><input name="issue" type="radio" value="Reward Card" /></td>
                        <td width="387" align="left" valign="top" class="FAQuestions">Reward card </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top"><input name="issue" type="radio" value="Referral issue" /></td>
                        <td align="left" valign="top" class="FAQuestions">Referral issue </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top"><input name="issue" type="radio" value="General Program question" /></td>
                        <td align="left" valign="top" class="FAQuestions">General Program question </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top"><input name="issue" type="radio" value="Web site question" /></td>
                        <td align="left" valign="top" class="FAQuestions">Web site question </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top"><input name="issue" type="radio" value="Other issue" /></td>
                        <td align="left" valign="top" class="FAQuestions">Other issue or question </td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top">&nbsp;</td>
                        <td align="left" valign="top">&nbsp;</td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td align="left" valign="top">&nbsp;</td>
                        <td align="left" valign="top">&nbsp;</td>
                      </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">Explanation:*</td>
                        <td colspan="2" align="left" valign="top"><textarea name="explanation" cols="50"></textarea><br><span id='req_text'></span></td>
                        </tr>
                      <tr>
                        <td align="left" valign="top" class="FAQuestions">&nbsp;</td>
                        <td colspan="2" align="left" valign="top">&nbsp;</td>
                      </tr>
                      <tr>
                        <td colspan="3" align="center" valign="top">
							<input type="hidden" name="redir" value="">
							<input type="hidden" name="contacterror" value="">
							<input type="submit" name="Submit" value="Send E-Mail" onclick="checkContactform();"/></td>
                      </tr>
                      <tr>
    <td colspan="3" align="right" class="FAQuestions" valign="top">
        *Required Fields
    </td>
</tr> ];
	}

else {
	   $msg =  send_email( $part_name, $part_email, $part_phone, $part_timetocall, $part_refnum, $issue, $explanation);

		print qq [   <tr>
                        <td colspan="3" align="center" valign="top">Thank You for your question.  <br><br>
			An email has been sent to the CenturyLink Connect Program Headquarters.<br><br>
			You will hear from us shortly.</td>
                      </tr>
			];

	}

=cut
