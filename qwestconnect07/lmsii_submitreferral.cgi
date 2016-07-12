use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use Try::Tiny;

use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $cci_id = $main::session{cci_id}||$cgi->param('cci_id'); 

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
require "$server/cgi-bin/inccalendar.cgi";


#my $url = "centurylinkyoucandev.com/index_lmsii07.cgi";
my $url = CCICryptography::getUrl_sites('lms');

my $db = DBInterface->new();
my $thisfile="lmsii_submitreferral.cgi";

my $redir = $cgi->param('redir')||0;
#my $db;
############## validation ################
my $valid  = CCICryptography::validate_CL_sites($cci_id,'lms');
my ($s,$e);
if ($valid <= 0) {
  headernocss();
  print qq[
  <form name="lead" action="$url" method="post">
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
if ($valid > 0) {
	($s, $e) = CCICryptography::getEmpid($cci_id); 
}

my  $PAGETITLE = 'CenturyLink Connect-Referral Form';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;

my $msg = "";
if ($redir == 1) {
	$msg =  submitLead();
	$redir = 0;
}

print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>$PAGETITLE</title>
<script language="JavaScript" src="qwestconnect07menus.js"></script>
<script language="JavaScript" src="validate.js"></script>
<link href="Style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="mm_menu.js"></script>
<script type="text/javascript" src="../../javascript/jquery-1.4.1.min.js"></script>		
<script  type="text/javascript" src="../../jquery/jquery.js"></script>
<script  type="text/javascript" src="../../jquery/simplemodal/simplemodal.js"></script>
<link rel="stylesheet" type="text/css" href="../../jquery/simplemodal/simplemodal.css"/>
</head>

<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif')">
<script language="JavaScript1.2">mmLoadMenus();</script>
<table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr><!--	cci_id = $cci_id	-->
    <td>
];
getHeader($cci_id, $s, $e);
my ($str, $needw9 , $id) = getLeadFormHeader($cci_id);
my $fillw9 = "";
if ($needw9 > 0) {
	$fillw9 = qq [
			<br />Once you hit \$500 please click <a class="BIG" href="#" onclick="openModalLarge('w9_qwest.cgi?id=$id');return false;">here</a> to fill out the required W-9.<br />
			If this is not done before you earn \$600, you will not be eligible for referral awards until the form is filled out.
		];
}
my $leftTable = getLeftTable(1 , $cci_id);

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
                                                    SUBMIT A REFERRAL&nbsp;                                                </td>
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
                                                <td width="10" align="left" valign="top">&nbsp;                                              </td>
                                              <td align="left" valign="top"><table width="881" height="19" border="0" cellpadding="0" cellspacing="0">
                                                <tr>
                                                  <td colspan="2" align="left" valign="top">&nbsp;</td>
                                                </tr>
						<tr>
                                                  <td colspan="2" align="left" valign="top" class="subTitles">
$str
$fillw9

													</td>
                                                </tr>
                                                <tr>
                                                  <td colspan="2" align="left" valign="top"><span class="subTitles">$msg</span></td>
                                                </tr>

                                                <tr>
                                                  <td colspan="2" align="left" valign="top"><span class="subTitles">Be sure to review the information under &quot;About the Program&quot; menu above for updates.<br>
												  Questions about your Referral Rewards Card Expiration, <a class="BIG" href="card_expire_raf_mdu_04142016.pdf" target="_blank">click here</a>.</span></td>
                                                </tr>
                                                <tr>
                                                  <td align="left" valign="top">&nbsp;</td>
                                                  <td align="left" valign="top">&nbsp;</td>
                                                </tr>
                                                <tr>
                                                  <td align="left" valign="top" colspan="2">&nbsp;</td>
                                                </tr>
                                                <tr>
                                                  <td width="225" align="left" valign="top"> $leftTable </td>
                                                  <td width="656" align="left" valign="top"><table width="650" border="0" align="right" cellpadding="1" cellspacing="1" class="Enrollcopy">
<form name="lead_lmsii" action="" method="post">
<input type='hidden' name='cci_id' value="$cci_id">
<input type='hidden' name='prodvalidate' value=0>



                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                      <td align="left" class="LELeadIn" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                      <td align="left" class="LELeadIn" valign="top">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Products of Interest: </td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="BRD" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Broadband <br />
                                                      (High-Speed Internet)  </td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="DTV" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Digital TV </td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="WRL" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Wireless</td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="DIV" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Digital Voice </td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" class="LEQuiz" valign="top"><input name="prod_int" type="checkbox" value="OTH" /></td>
                                                      <td align="left" class="LELeadIn" valign="top"> Other</td>
                                                      <td align="left" class="LEQuiz" valign="top">&nbsp;</td>
                                                      <td align="left" class="LEQuiz" valign="top">&nbsp;<span id="req_prod"></span></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Customer Name: </td>
                                                      <td align="left" colspan="4" valign="top"><input class="FAQuestions" name="cust_name" size="35" type="text" /><font color="red">*</font><span id="req_name"></span></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Property Name: </td>
                                                      <td align="left" colspan="4" valign="top"><input class="FAQuestions" name="prop_name" size="35" type="text" /><font color="red">*</font><span id="req_prop"></span></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Customer Address: </td>
                                                      <td align="left" colspan="4" valign="top"><input class="FAQuestions" name="lead_addr" size="35" type="text" /></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Apt/Unit\#: </td>
                                                      <td align="left" colspan="4" valign="top"><input class="FAQuestions" name="lead_addr2" size="35" type="text" /></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Customer State: </td>
                                                      <td align="left" colspan="4" valign="top">
						     <select class="FAQuestions" name="lead_state">
                            <option value="">-- Select --</option>
<!--	start state	-->
];
		my $sql = "select distinct abbreviation from lp_states with (nolock) where isnull(abbreviation,'')<> '' order by abbreviation";
		my $success = eval {
		my $sth = $db->prepare($sql) or die $db->errstr;
			$sth->{PrintError} = 0;
			$sth->execute()  or die $sth->errstr;

		while(my $state = $sth->fetchrow_hashref){
				print qq[<option name='lead_state' value='$state->{abbreviation}' >$state->{abbreviation}</option>];
		}
		$sth->finish();	

	};
	unless($success) {
		DBInterface::writelog('youcan10',"$thisfile", $@ );
	}

print qq[
<!--	end state	-->
                          </select><font color="red">*</font><span id="req_st"></span>
</td>
                                                    </tr>
   
     <tr>
 <td align="left" class="LEtitle" valign="top" width="204"> Customer&rsquo;s address is serviced by: 2<font color="red">*</font> </td>
 <td align="left" class="LEQuiz" valign="top" width="31"><input type="radio" checked onclick="showHide2();" name="legacy"  value="1" id="crisChk"/></td>
 <td align="left" class="LELeadIn" valign="top" width="147"> CRIS</td>
  <td align="left" class="LEQuiz" valign="top" width="42"><input type="radio" onclick="showHide2();" name="legacy" value="2" id="ensChk"/></td>
 <td align="left" class="LELeadIn" valign="top" width="210"> Ensemble</td>
   </tr> 
                          <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                      <td align="left" valign="top">&nbsp;</td>
                                                    </tr>
						<tr>
                                                      <td align="left" class="LEtitle" valign="top"> Existing CenturyLink Customer: </td>
                                                      <td align="left" colspan="4" valign="top"><select class="FAQuestions" name="exist_cust">
                                                          <option value="unknown">Unknown</option>
                                                          <option value="Yes">Yes</option>
                                                          <option value="No">No</option>
                                                        </select>
														</td></tr>
                                                   <tr>
                                                      <td align="left" class="LEtitle" valign="top">Move In Date: </td>
<td align="left" colspan="4" valign="top">  <input type="text" name="mindt" class="FAQuestions" size="8" maxlength="8"onclick='document.lead_lmsii.mindt.select()'>
        <a href="" class="link4" onClick="javascript:opencal('lead_lmsii','mindt'); return false">(mm/dd/yy)</a>
   </td>
                                                    </tr>

                                                   <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Primary Phone Number: </td>
                                                      <td align="left" colspan="4" valign="top"><input class="FAQuestions" name="phone1" size="10" type="text" /><font color="red">*</font><span id="req_ph1"></span></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Secondary Phone Number: </td>
                                                      <td align="left" colspan="4" valign="top"><input class="FAQuestions" name="phone2" size="10" type="text" /></td>
                                                    </tr>
													
                                                    <tr><td colspan="5"><div name="banDiv" id="banDiv" style="display: none;">
														<table width="100%" align="right" cellpadding="1" cellspacing="1" class="Enrollcopy">
													<tr>
                                                      <td align="left" class="LEtitle" valign="top" > BAN \#: </td>
                                                      <td align="left" colspan="4" valign="top" >
													  <input class="FAQuestions" name="ban" size="10" type="text" /><font color="red">*</font><span id="req_ban"></span></td>
													</tr>
														</table>
													</div>
                                                   </td>
												   </tr>

                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Best Time to Call: </td>
                                                      <td align="left" colspan="4" valign="top"><select class="FAQuestions" name="time_to_call">
                                                          <option value="">-Select One-</option>
                                                          <option value="Anytime">Anytime</option>
                                                          <option value="Morning 8am-noon Mountain Time">Morning 8am-noon Mountain Time</option>
                                                          <option value="Afternoon Noon-5pm Mountain Time">Afternoon Noon-5pm Mountain Time</option>
                                                          <option value="Evening After 5pm Mountain Time">Evening After 5pm Mountain Time</option>
                                                        </select> <font color="red">*</font><span id="req_ttc"></span> </td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top">&nbsp;</td>
                                                      <td align="left" class="littleLinks" colspan="4" valign="top"> Please include additional information that will be helpful for us to reach your customer or better understand her or his needs</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEtitle" valign="top"> Notes:</td>
                                                      <td align="left" colspan="4" valign="top"><textarea class="littleLinks" cols="30" name="lp_notes"></textarea></td>
                                                    </tr>
                                                    <tr>
                                                      <td align="left" class="LEQuiz" valign="top">&nbsp;</td>
                                                      <td align="left" colspan="4" valign="top">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="center" class="LEQuiz" colspan="5" valign="top">&nbsp;</td>
                                                    </tr>
                                                    <tr>
                                                      <td align="center" class="LEQuiz" colspan="5" valign="top">
						      <input type="hidden" name="redir" value="">
            <input type="button" name="go" value="Submit to CenturyLink " class="btnon"
            onMouseOver="this.className='btnoff';"
            onMouseOut="this.className='btnon';" onclick="checkLeadform();"></td>
                                                    </tr>
                                                  </table></td>
                                                </tr>

                                              </table></td>
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
