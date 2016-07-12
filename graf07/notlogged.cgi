use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

require "D:/centurylinkyoucan/cgi-bin/init.cgi";

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
                <td align="left" valign="top" class="BlueTitles">You are not logged in </td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td width="913" height="376" align="left" valign="top" background="images/Sub_tile.gif"><br />
                <br />
                    <br />
                      <table width="571" border="0" align="center" cellpadding="2" cellspacing="2">
              <tr>
                <td colspan="2" align="left" valign="top" class="BlueTitles">Log in here to create a referral or check your account:</td>
              </tr>
              <tr>
                <td colspan="2" align="left" valign="top">&nbsp;</td>
              </tr>
<form name="login" action="../cgi-bin/lp-validate.cgi" method="post">
<input type="hidden" name="program_id" value="154">
<input type="hidden" name="fund_id" value="649">
<input type="hidden" name="site" value="new">
<input type="hidden" name="source_id" value="1"><!-- force staff not qwesthr login -->
              <tr>
                <td width="90" align="left" valign="top" class="subTitles">User ID: </td>
                <td width="596" align="left" valign="top"><input name="userid" id="username" type="text" size="20" /></td>
              </tr>
              <tr>
                <td align="left" valign="top" class="subTitles">Password:</td>
                <td align="left" valign="top"><input name="password" type="password" id="password" size="20" /></td>
              </tr>
              <tr>
                <td colspan="2" align="left" valign="top">&nbsp;</td>
              </tr>
              <tr>
                <td colspan="2" align="left" valign="top"><table width="547" border="0" cellspacing="1" cellpadding="1">
                    <tr>
                      <td width="243">&nbsp;</td>
                      <td width="297"><input type="submit" name="Submit" value="Log In" /></td>
                    </tr>
</form>
                </table></td>
              </tr>
              <tr>
                <td colspan="2" align="left" valign="top" class="FAQuestions">Not enrolled yet?  Start earning money for your referrals <a class="FAQLink" href="agreement.cgi">here</a>!</td>
              </tr>
            </table></td>
          </tr>
        </table></td>
      </tr>
      <tr>
        <td><img src="images/bottombuffer.gif" width="954" height="15" /></td>
      </tr>
      <tr>
        <td width="954" height="35" align="center" valign="middle" background="images/bottom_green.gif"><table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
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


