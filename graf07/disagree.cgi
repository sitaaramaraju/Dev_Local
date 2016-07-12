use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');

my  $PAGETITLE = 'Partner Referral Program-Disagree';

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
                <td align="left" valign="top" class="BlueTitles">CenturyLink Partner Referral Program</td>
              </tr>
            </table></td>
          </tr>
          
          <tr>
            <td width="913" height="376" align="center" valign="top" background="images/LoggedInback.gif"><br />
                <br />
                    <br />
                      <table width="700" border="0" align="center" cellpadding="0" cellspacing="0">
              <tr>
                <td align="left" valign="top"><span class="BlueTitles">Thank you for your interest in the CENTURYLINK<sup>&reg;</sup> Partner Referral Program.</span><br />
            <br />
            <ul>
              <li>
                <div class="Enrollcopy">Unfortunately, we are unable to continue your application for enrollment because the "I Agree" button was not selected.</div>
                <br />
              </li>
              <li>
                <div class="Enrollcopy">To return to the enrollment page and continue, please click here. <a href='agreement.cgi' class='linkon'>Back to Enrollment</a><br />
                    <br />
                </div>
              </li>
			  <li>
                <div class="Enrollcopy">If you have questions about the CenturyLink<sup>&reg;</sup> Partner Referral Program please contact the CenturyLink<sup>&reg;</sup> Partner Referral Program headquarters at 1 866-968-2261.</div>
                <br />
              </li>

            </ul></td>
              </tr>
            </table></td>
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

