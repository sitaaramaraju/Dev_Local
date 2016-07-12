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
#my $db;
############## validation ################
my $valid = 0;
if ($cci_id ne "") {
	$valid = CCICryptography::validate_CL_sites($cci_id,'lms');
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
print $header;
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
                                                <td width="10">&nbsp;</td>
                                                <td align="left" valign="top" class="BlueTitles">NEW ENROLLMENT PAGE&nbsp;</td>
                                            </tr>
                                        </table>
									</td>
                                </tr>
                                <tr>
                                    <td align="left" valign="top"><img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
                                </tr>
                                <tr>
                                    <td align="left" valign="middle" background="images/Sub_tile.gif">
                                        <table width="900" border="0" cellspacing="1" cellpadding="1">
                                            <tr>
                                                <td width="10" align="left" valign="top">&nbsp;</td>
                                                <td align="left" valign="top">
                                                    <table width="875" border="0" align="center" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td>&nbsp;
																<table align="center" border="0" cellpadding="1" cellspacing="1" width="850">
                                                                   <tr>
																	<td align="left" valign="top">
<form name="regi" action="welcome.cgi" method="post">
																		<table border="0" cellpadding="1" cellspacing="1" class="Enrollcopy" width="860">
																			<tr>
																				<td width="405" align="right" valign="top" class="FAQuestions">CUID / Reference Code</td>
                                                                                <td width="2">&nbsp;</td>
                                                                                <td width="443" align="left" valign="top" class="LEQuiz">
																					<div align="left">
                                                                                          <input name="osr_id" class="FAQuestions" type="text" style="width: 100px" />*
                                                                                     </div><span class="bodycopy" id="req_osr"></span>                                                                    
																				</td>
																			</tr>
                                                                             <tr>
                                                                                <td align="left" class="FAQuestions" valign="top">
                                                                                  <div align="right">First Name:</div></td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left"><input name="first" class="FAQuestions" type="text" style="width: 100px" />*</div><span class="bodycopy" id="req_name"></span></td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">Last Name: </div>                                     
																					</td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left">
                                                                                            <input type="text" name="last" class="FAQuestions" style="width: 100px" />*</div>  
																					</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">Home Address:</div> </td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left"><input name="addr1" type="text" class="FAQuestions" style="width: 230px" />*<br />
																						<input name="addr2" type="text" class="FAQuestions" style="width: 229px" /></div> 
																					</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">City: </div>  
																					</td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left">
                                                                                            <input name="city" type="text" class="FAQuestions" style="width: 97px" />*</div> 
																						</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">State: </div>  
																					</td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left">
                                                                                            <select class="FAQuestions" name="state" style="width: 138px">
																								 <option value="" selected="selected">--Select State--</option>
];



	my	$sql = "select distinct state, abbreviation  from lp_states with (nolock) where program_id = 154  order by state";
			my $sth = $db->prepare($sql);
			$sth->execute();

			while (my $state = $sth->fetchrow_hashref) {
				#%state = $db->DataHash();
				print qq[<option name='state' value='$state->{abbreviation}' >$state->{state}</option>];
			}
			$sth->finish();
	print qq[
					 </select>  *</div>     
																					</td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td class="FAQuestions"><div align="right">Zip:</div></td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td><div align="left"><input name="zip" type="text" class="FAQuestions" style="width: 57px" />*</div><span class="bodycopy" id="req_addr"></span>
																					</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">Home Phone: </div> 
																					</td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                      <div align="left">

<input type="text" name="home_phone1" class="FAQuestions" value="" size="3" maxlength="3"  onKeyUp="return autoTab(this,3,event);">-
        <input type="text" name="home_phone2" class="FAQuestions" value="" size="3" maxlength="3" onKeyUp="return autoTab(this,3,event);">-
        <input type="text" name="home_phone3" class="FAQuestions" value="" size="4" maxlength="4">
                                                                                      *</div><span class="bodycopy" id="req_hp"></span>    
																					 </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">Mobile Phone: </div>  
																					</td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left">
                                                                                          <input type="text" name="cell_phone1" class="FAQuestions" value="" size="3" maxlength="3"  onKeyUp="return autoTab(this,3,event);">-
        <input type="text" name="cell_phone2" class="FAQuestions" value="" size="3" maxlength="3" onKeyUp="return autoTab(this,3,event);">-
        <input type="text" name ="cell_phone3" class="FAQuestions" value="" size="4" maxlength="4">
                                                                                        </div>                                                                        
																					</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">Email: </div>
	                                                                                 </td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left">
                                                                                            <input name="email" type="text" class="FAQuestions" style="width: 232px" />*</div> <span class="bodycopy" id="req_email"></span>
																					</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">Last 4 Digits of Social Security Number<br />
                                                                                            (SSN) or Individual Taxpayer Identification Number (ITIN): </div>
																					</td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left">
                                                                                            <input name="ssn4" type="text" class="FAQuestions" size="4" />*</div>
																							<span class="bodycopy" id="req_last4"></span>
																					</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="left" class="FAQuestions" valign="top">
                                                                                        <div align="right">Date of Birth (D.O.B.)</div> 
																					</td>
                                                                                    <td>&nbsp;</td>
                                                                                    <td align="left" valign="top">
                                                                                        <div align="left">
<input type="hidden" name="dob" value=""  maxlength="8">
<!-- dob insert start  -->

    <SELECT NAME="monthdob" CLASS="FAQuestions" onClick="document.regi.dob.value = buildDatedob();">

<OPTION VALUE="">--
            <OPTION VALUE="01">January
            <OPTION VALUE="02">February
            <OPTION VALUE="03">March
            <OPTION VALUE="04">April
            <OPTION VALUE="05">May
            <OPTION VALUE="06">June
            <OPTION VALUE="07">July
            <OPTION VALUE="08">August
            <OPTION VALUE="09">September
            <OPTION VALUE="10">October
            <OPTION VALUE="11">November
            <OPTION VALUE="12">December
    </SELECT>
    <SELECT NAME="daydob" CLASS="FAQuestions" onClick="document.regi.dob.value =  buildDatedob();">

<OPTION VALUE="">--
            <OPTION VALUE="01">01
            <OPTION VALUE="02">02
            <OPTION VALUE="03">03
            <OPTION VALUE="04">04
            <OPTION VALUE="05">05
            <OPTION VALUE="06">06
            <OPTION VALUE="07">07
            <OPTION VALUE="08">08
            <OPTION VALUE="09">09
            <OPTION VALUE="10">10
            <OPTION VALUE="11">11
            <OPTION VALUE="12">12
            <OPTION VALUE="13">13
            <OPTION VALUE="14">14
            <OPTION VALUE="15">15
            <OPTION VALUE="16">16
            <OPTION VALUE="17">17
            <OPTION VALUE="18">18
            <OPTION VALUE="19">19
            <OPTION VALUE="20">20
            <OPTION VALUE="21">21
            <OPTION VALUE="22">22
            <OPTION VALUE="23">23
            <OPTION VALUE="24">24
            <OPTION VALUE="25">25
            <OPTION VALUE="26">26
            <OPTION VALUE="27">27
            <OPTION VALUE="28">28
            <OPTION VALUE="29">29
            <OPTION VALUE="30">30
            <OPTION VALUE="31">31
                                                                                            </select>
    <SELECT NAME="yeardob" CLASS="FAQuestions" onClick="document.regi.dob.value = buildDatedob();">

<OPTION VALUE="">--
            <OPTION VALUE="1908">1908
            <OPTION VALUE="1909">1909
            <OPTION VALUE="1910">1910
            <OPTION VALUE="1911">1911
            <OPTION VALUE="1912">1912
            <OPTION VALUE="1913">1913
            <OPTION VALUE="1914">1914
            <OPTION VALUE="1915">1915
            <OPTION VALUE="1916">1916
            <OPTION VALUE="1917">1917
            <OPTION VALUE="1918">1918
            <OPTION VALUE="1919">1919
            <OPTION VALUE="1920">1920
            <OPTION VALUE="1921">1921
            <OPTION VALUE="1922">1922
            <OPTION VALUE="1923">1923
            <OPTION VALUE="1924">1924
            <OPTION VALUE="1925">1925
            <OPTION VALUE="1926">1926
            <OPTION VALUE="1927">1927
            <OPTION VALUE="1928">1928
            <OPTION VALUE="1929">1929
            <OPTION VALUE="1930">1930
            <OPTION VALUE="1931">1931
            <OPTION VALUE="1932">1932
            <OPTION VALUE="1933">1933
            <OPTION VALUE="1934">1934
            <OPTION VALUE="1935">1935
            <OPTION VALUE="1936">1936
            <OPTION VALUE="1937">1937
            <OPTION VALUE="1938">1938
            <OPTION VALUE="1939">1939
            <OPTION VALUE="1940">1940
            <OPTION VALUE="1941">1941
            <OPTION VALUE="1942">1942
            <OPTION VALUE="1943">1943
            <OPTION VALUE="1944">1944
            <OPTION VALUE="1945">1945
            <OPTION VALUE="1946">1946
            <OPTION VALUE="1947">1947
            <OPTION VALUE="1948">1948
            <OPTION VALUE="1949">1949
            <OPTION VALUE="1950">1950
            <OPTION VALUE="1951">1951
            <OPTION VALUE="1952">1952
            <OPTION VALUE="1953">1953
            <OPTION VALUE="1954">1954
            <OPTION VALUE="1955">1955
            <OPTION VALUE="1956">1956
            <OPTION VALUE="1957">1957
            <OPTION VALUE="1958">1958
            <OPTION VALUE="1959">1959
            <OPTION VALUE="1960">1960
            <OPTION VALUE="1961">1961
            <OPTION VALUE="1962">1962
            <OPTION VALUE="1963">1963
            <OPTION VALUE="1964">1964
            <OPTION VALUE="1965">1965
            <OPTION VALUE="1966">1966
            <OPTION VALUE="1967">1967
            <OPTION VALUE="1968">1968
            <OPTION VALUE="1969">1969
            <OPTION VALUE="1970">1970
            <OPTION VALUE="1971">1971
            <OPTION VALUE="1972">1972
            <OPTION VALUE="1973">1973
            <OPTION VALUE="1974">1974
            <OPTION VALUE="1975">1975
            <OPTION VALUE="1976">1976
            <OPTION VALUE="1977">1977
            <OPTION VALUE="1978">1978
            <OPTION VALUE="1979">1979
            <OPTION VALUE="1980">1980
            <OPTION VALUE="1981">1981
            <OPTION VALUE="1982">1982
            <OPTION VALUE="1983">1983
            <OPTION VALUE="1984">1984
            <OPTION VALUE="1985">1985
            <OPTION VALUE="1986">1986
            <OPTION VALUE="1987">1987
            <OPTION VALUE="1988">1988
            <OPTION VALUE="1989">1989
            <OPTION VALUE="1990">1990
            <OPTION VALUE="1991">1991
            <OPTION VALUE="1992">1992
            <OPTION VALUE="1993">1993
            <OPTION VALUE="1994">1994
            <OPTION VALUE="1995">1995
            <OPTION VALUE="1996">1996
            <OPTION VALUE="1997">1997
            <OPTION VALUE="1998">1998
            <OPTION VALUE="1999">1999
            <OPTION VALUE="2000">2000
            <OPTION VALUE="2001">2001
            <OPTION VALUE="2002">2002
            <OPTION VALUE="2003">2003
            <OPTION VALUE="2004">2004
            <OPTION VALUE="2005">2005
                                                                                            </select>
                                                                                            *</div>                                                                                  <span class="bodycopy" id="req_dob"></span>  </td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="left" class="FAQuestions" valign="top">&nbsp;</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top">&nbsp;</td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">Business/Property Name: </td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top"><input name="property_name" type="text" class="FAQuestions" size="35" />
                                                                                  *<span class="bodycopy" id="req_propname"></span></td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">Employer Name: </td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top"><input name="bus_name" type="text" class="FAQuestions" size="35" />
                                                                                  *<span class="bodycopy" id="req_bossname"></span></td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">Employment Address: </td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="middle"><input name="bus_addr1" type="text" class="FAQuestions" size="35" />
                                                                                  *</td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">&nbsp;</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top"><input name="bus_addr2" type="text" class="FAQuestions" size="35" /></td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">City:</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top"><input name="bus_city" type="text" class="FAQuestions" size="35" />
                                                                                  *</td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">State:</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top"><select class="FAQuestions" name="bus_state" style="width: 138px">
                            <option value="">--select--</option>
];



			$sql = "select distinct state, abbreviation  from lp_states with (nolock) where program_id = 154  order by state";
			$sth = $db->prepare($sql);
			$sth->execute();

			while (my $state = $sth->fetchrow_hashref) {
				print qq[<option name='bus_state' value='$state->{abbreviation}' >$state->{state}</option>];
			}
			$sth->finish();
	print qq[
					 </select></td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">Zip:</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top"><input name="bus_zip" type="text" class="FAQuestions" size="5" />*<span class="bodycopy" id="req_bizaddr"></span></td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">Employment Phone: </td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top"><input name="bus_phone"  class="FAQuestions"  type="text" size="10" />
                                                                                </tr>
																				<tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">I am an employee of a Multi-Dwelling Unit (MDU) property</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top">
																				  <input name="yes_mdu"  class="FAQuestions"  type="radio" value="1"/>&nbsp; Yes
																				   <input name="yes_mdu"  class="FAQuestions"  type="radio" value="0"/>&nbsp; No&nbsp;*<span class="bodycopy" id="req_mdu"></span></td>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">&nbsp; </td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top">&nbsp;</td>
										  </tr>

                                                                                <tr>
                                                                                  <td colspan="3" align="center" valign="top" class="FAQuestions">
										  <input type="hidden" name="redir" value=""><input type="hidden" name="enrollType" value="bau">
										  <INPUT TYPE="text" NAME="NameForBotsBAU" SIZE="48" style='display:none;'>
										  <input type="button" name="go" value="REGISTER NOW" class="btnon"
											onMouseOver="this.className='btnoff';"
											onMouseOut="this.className='btnon';" onclick="checkform_bau();"></td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td colspan="3" align="center" valign="top" class="Earncopy">* Required * </td>
                                                                                </tr>
                                                                                <tr>
                                                                                  <td align="right" class="FAQuestions" valign="top">&nbsp;</td>
                                                                                  <td>&nbsp;</td>
                                                                                  <td align="left" valign="top">&nbsp;</td>
                                                                                </tr>
                                                                            </table>
</form>                                                                        </td>
                                                                    </tr>
                                                                </table>
															</td>
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
