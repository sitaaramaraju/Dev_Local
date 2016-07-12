use strict; 
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');

my  $PAGETITLE = 'CenturyLink Refer A Friend-Choose Team';

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
                <td align="left" valign="top" class="BlueTitles">Help us identify who you are:<br /></td>
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
                    <td><br />
                      <table width="600" border="0" cellspacing="2" cellpadding="2">
                        <tr>
                          <td colspan="2" align="left" valign="top" class="subTitles">Please Select One:</td>
                          </tr>
<form action="newenroll.cgi" method="post" name="myform">
<input type="hidden" name="submitted" value="1">

						<!--
                        <tr>
                          <td width="20" align="left" valign="top"><input name="special"  type="radio" value="customer"/></td>
                          <td align="left" valign="top" class="Enrollcopy"> I will refer my friends and family </td>
                        </tr>  -->
                        
                        <tr>
                          <td align="left" valign="top"><input name="special" type="radio" value="vendor" /></td>
                          <td align="left" valign="top" class="Enrollcopy">CenturyLink Vendors &nbsp; <select name="specialselect" >
                            <option class="FAQLink" value="">-Select One-</option>
				 <option class="FAQLink" value="Alliance One">Alliance One</option>
				 <option class="FAQLink" value="Arizona Public Service">Arizona Public Service</option>
       			    <option class="FAQLink" value="AFNI">AFNI</option> 
                            <option class="FAQLink" value="Allied">Allied</option>			    
                            <option class="FAQLink" value="CCS">CCS</option>
                            <option class="FAQLink" value="CSD">CSD</option>
			    <option class="FAQLink" value="Dex">Dex</option>
				<option class="FAQLink" value="EOS">EOS</option> 
				<option class="FAQLink" value="EOS-CCA Tertiary">EOS-CCA Tertiary</option> 
                            <option class="FAQLink" value="ER Solutions">ER Solutions</option>
                            <option class="FAQLink" value="Focus">Focus</option>
			    <option class="FAQLink" value="GCServ">GCServ</option> 
			    <option class="FAQLink" value="Oxford">Oxford</option>
			    <option class="FAQLink" value="Pinnacle Financial Group">Pinnacle Financial Group</option>
			     <option class="FAQLink" value="South West Credit">South West Credit</option>
			    
                            <option class="FAQLink" value="Startek">Startek</option>
							<option class="FAQLink" value="Teleperformance">Teleperformance</option>
                            <option class="FAQLink" value="West Manage">West Manage</option>
			  </select>  </td>
                        </tr>
                        <tr>
                          <td align="left" valign="top">&nbsp;</td>
                          <td align="left" valign="top">&nbsp;</td>
                        </tr>
                        <tr>
                          <td align="left" valign="top">&nbsp;</td>
                          <td align="left" valign="top">&nbsp;</td>
                        </tr>
                        <tr>
                          <td align="left" valign="top">&nbsp;</td>
                          <td align="left" valign="top"><input name="Submit" type="submit" onclick="OnSubmitForm();return false;"  value="Continue..." /></td>
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


