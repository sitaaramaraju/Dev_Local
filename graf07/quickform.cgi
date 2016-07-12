use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
my $cgi = CGI->new();
use HTML::Strip;

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
else {
	$server = "D:/centurylinkyoucan";
}

require "$server/graf07/graf_subs.cgi";

my $thisfile = "quickform.cgi";
my ($session_id,$staff_id); 
my $chk = 0;
my $url = "../index_raf.cgi";

if (length($cci_id) != 0) {
	($session_id,$staff_id) = CCICryptography::getEmpid($cci_id);
	$chk = CCICryptography::validate_CL_sites($cci_id,'graf03');
}

=head
if ($chk <= 0 || length($cci_id) == 0){
  print qq[
  <form name="lead" action="" method="post">
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
=cut


my  $PAGETITLE = 'CenturyLink Pass It On Rewards';

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
	
	my $hs = HTML::Strip->new();

	$part_name = $hs->parse($cgi->param('part_name'));
	$part_email = $hs->parse($cgi->param('email'));
	$part_phone = $hs->parse($cgi->param('phone'));
	$part_timetocall = $hs->parse($cgi->param('time_to_call'));
	$part_refnum = $hs->parse($cgi->param('refnum'));
	$issue = $hs->parse($cgi->param('issue'));
	$explanation = $hs->parse($cgi->param('explanation'));

	$hs->eof;

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
print qq[
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>
];

