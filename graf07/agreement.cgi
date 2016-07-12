use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');

my  $PAGETITLE = 'CenturyLink Refer A Friend-Agreement';

require "graf07/header.cgi";
print<<"EOF";
</td>
      </tr>
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
                <td align="left" valign="top" class="BlueTitles">CenturyLink Partner Referral Program Agreement </td>
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
                <td><table width="650" border="0" align="center" cellpadding="1" cellspacing="1">
                  <tr>
                    <td><span class="BlueTitles">Please review the following. If you understand and agree, click on the &ldquo;I Agree&rdquo; button to enroll and continue. </span><br />
                      <br />
                      <table width="600" border="0" cellspacing="3" cellpadding="3">
						<tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">I ACKNOWLEDGE</span> that I am not a CenturyLink employee.</td>
                       </tr>
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">I AGREE TO</span> talk to friends, family and businesses about their telecommunications needs.</td>
                          </tr>
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">I AGREE TO </span>obtain the prospective customer's verbal permission to make a referral, as well as some basic information about the customer, including their name, address and billing telephone number; and the services they are interested in.</td>
                          </tr>
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">I AGREE TO </span>use only information that is publicly available to develop referrals and contacts.</td>
                          </tr>
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">I AGREE TO</span> protect customer privacy by adhering to all program Terms and Conditions of the Partner Referral Program.</td>
                          </tr>
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">I AGREE TO</span> abide by the VISA branded Rewards Card Agreement.</td>
                          </tr>
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">I ACKNOWLEDGE</span> that I will receive the appropriate tax documentation for cumulative awards over \$600 for the calendar year.</td>
                          </tr>                        
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><p><span class="Enrollcopy">I WILL NOT </span>represent myself as an authorized CenturyLink sales representative, nor provide customers with price quotes for CenturyLink products and services. Only a CenturyLink sales representative can provide exact pricing.</p></td>
                          </tr>
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">I AGREE TO</span> conduct myself in a professional manner and WILL NOT make any false, misleading or disparaging statements regarding any CenturyLink competitor or any other individual or organization as it relates to any activity associated with the Partner Referral Program.</td>
                        </tr>
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><table width="300" border="0" align="center" cellpadding="1" cellspacing="1">
                            <tr>
<form name="agree" action="whichteam.cgi" method="post">
                              <td align="center" valign="top"><input name="Submit" type="submit"  value="I Agree" /></td>
</form>
<form name="agree" action="disagree.cgi" method="post">
							  <td align="center" valign="top"><input type="submit" name="Submit2" value="I Disagree" /></td>
</form                           
							</tr>
                          </table></td>
                        </tr>
                      </table></td>
                  </tr>
                </table></td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td align="left" valign="top"><img src="images/Sub_bottom.gif" width="913" height="16" /></td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td><img src="images/bottombuffer.gif" width="954" height="15" /></td>
      </tr>
      <tr>
        <td width="904" height="66" align="center" valign="middle" background="images/bottom_amex.gif"><table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
EOF
require "graf07/footer.cgi";
print<<"EOF";
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>


EOF

