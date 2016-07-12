# w9_qwest.cgi   
#
#   TODO:
#       This is only slightly different from w9.cgi
#       Debug code, and it puts created_date in contact_personnel that can
#       be joined to dateentered in custw9 
#       Should be merged sometime after testing.


use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;

use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header('text/html');
my $cci_id = $cgi->param('cci_id')||'';
my $id = $cgi->param('id') ;
my $qwest = $cgi->param('qwest');

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

my $db = DBInterface->new();

require "$server/cgi-bin/init.cgi";
require "$server/cgi-bin/delimeter.cgi";
require "$server/cgi-bin/encryptdata.pm";

my $url = CCICryptography::getUrl_sites('lms');

############## validation ################
my $valid =1;# CCICryptography::validate_CL_sites($cci_id,'lms');


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

my $sql;
my ($cust_id, $encrypteddata, $contact_main_id, $contact_personnel_id, $msg, $strtest, $staff_id);
if ( $cgi->param('savedata') ne "" ) {

	$staff_id =   $cgi->param('id');
    $sql = " select cust.cust_id
				from cust with(nolock)
				inner join cust_contact cc with(nolock) on cc.cust_id = cust.cust_id
				inner join staff with (nolock) on staff.contact_info_id = cc.contact_info_id
				where  staff.staff_id =  $staff_id  ";
    $strtest .= " 73<pre> $sql</pre>\n";
	#print qq[73 qwest = $qwest<pre>$sql</pre> <br>];
	my $sth = $db->prepare($sql);
	$sth->execute();
	my $data = $sth->fetchrow_hashref();
	$cust_id = $data->{cust_id};
	$sth->finish();

    my $ssn = $cgi->param('ssn1').$cgi->param('ssn2').$cgi->param('ssn3');
    my $ein = $cgi->param('ein1').$cgi->param('ein2');
    if ( length($ein) > 0  ) {
        $encrypteddata = $ein;
    }else{
        $encrypteddata = $ssn;
    }
    #$encrypteddata = EncryptData($encrypteddata); # must run on 212 to find special file

    $sql = "select count(contact_main_id) as cnt from contact_main with (nolock) where cust_id = $cust_id";
	$sth = $db->prepare($sql);
	$sth->execute();
	$data = $sth->fetchrow_hashref();
    my $thecnt = $data->{cnt};
	$sth->finish();
	#print qq[95 <pre>$sql</pre> <br>];
    # check to see if they already have a record.  Why it would do this twice, I dunno, but just in case
    if ( $qwest == 1 ) {

        $sql = "select contact_main_id from contact_main with (nolock) where cust_id = ?";
       # $strtest .= "<pre>$sql</pre>\n";
		$sth = $db->prepare($sql);
		$sth->execute($cust_id);
		$data = $sth->fetchrow_hashref();
		$sth->finish();
        $contact_main_id = $data->{contact_main_id};
		
		# check if they have contact_personnel record 
        # 
		$sql = "select 0 as contact_personnel_id union select contact_personnel_id from contact_personnel with (nolock) where contact_main_id =  ? order by 1 desc ";
		$sth = $db->prepare($sql);
		$sth->execute($contact_main_id);
		$data = $sth->fetchrow_hashref();
		$sth->finish();
        $contact_personnel_id = $data->{contact_personnel_id};

		if ($contact_personnel_id == 0 ) { # does not exist - insert record
			$sql = "insert into contact_personnel (contact_main_id, ssn, created_date) values ($contact_main_id,'$encrypteddata', convert(varchar,getdate(),101))";
		}
		else { # update record
			$sql = "update contact_personnel set ssn = '$encrypteddata', last_modified_date = getdate() where contact_personnel_id = $contact_personnel_id";
		}

        $strtest .= "<pre>$sql</pre>\n";
		$sth = $db->prepare($sql);
		$sth->execute();
		$sth->finish();
	#print qq[123 <pre>$sql</pre> <br>];
        # update the cust W9 receipt table to show that this W9 has been received
        # Changed getdate() so the same value put in both tables, contact_personnel and custw9   prh
        $sql = "insert into custw9 (cust_id, w9type, w9other, dateentered) values ($cust_id, ".$cgi->param('classification').",'".$cgi->param('other')."', convert(varchar,getdate(),101))";
        $strtest .= "<pre>$sql</pre>\n";
		$sth = $db->prepare($sql);
		$sth->execute();
		$sth->finish();
	#print qq[135 <pre>$sql</pre> <br>];
        #Update the customer status to active
       # $sql = "update cust set cust_status = 1 where cust_id = $cust_id";
       # $strtest .= "<pre>$sql</pre>\n";
       # $db->Sql($sql) unless $IS_TEST;

        #print $strtest if $IS_TEST;
		$msg = "Your W9 information is updated - Thank you! <br><br>You can close this window and continue making referrals.";

    }else{
		$msg = "Please contact your program Administartor to update the information.";
    }
        #$db->Sql($sql);
=head
print<<"EOF";
<script language='javascript'>
    window.alert('Thank you.');
    window.close();
</script>

<!-- $strtest -->
EOF
=cut
print qq[ $msg	];
}else{

print qq[
<head>
<script language="javascript">
    function openwindow(URL) {
        win = window.open(URL, "pop", "width=800, height=600, resizable=yes, left=50, top=0, scrollbars=yes, toolbar=yes, menubar=yes, status=yes");
    }
</script>
</head>

<BODY bgcolor="#ffffff">
<form action='' method='post' name='taxform'>
<input type='hidden' name='qwest' value='$qwest'>
<input type='hidden' name='cci_id' value='$cci_id'>
<input type='hidden' name='id' value='$id'>
<style><!--
input.textfield {background-color: YELLOW; border: 1px solid #000000; color: #000000; font-family: "verdana, arial, helvetica,sans-serif";
         font-size: 12px;   }
}
--></style>

<table border=1 cellspacing=0 cellpadding=0 style='border-collapse:collapse;
 border:none;mso-border-alt:solid windowtext .5pt;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
  <TR>
    <TD vAlign=top width=250 height=100>
      <P><FONT face=Arial>Form <STRONG><FONT size=6>W-9<BR></FONT></STRONG><FONT
      size=1>Rev. January 2005)</FONT><BR></FONT></P></TD>
    <TD vAlign=top width='80%' height=100>
      <P><FONT face=Arial></FONT>&nbsp;</P>
      <P align=center><FONT face=Arial size=5><STRONG>Request for Taxpayer
      <BR></STRONG></FONT><FONT face=Arial size=5><STRONG>Identification Number
      and Certification</STRONG></FONT></P></TD>
    <TD vAlign=top width=250 height=100>Give form to the requester. Do not
      send to the IRS.</TD></TR>
      </TABLE>
<div class=Section1>
<table border=1 cellspacing=0 cellpadding=0 style='border-collapse:collapse;
 border:none;mso-border-alt:solid windowtext .5pt;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
 <tr>
  <td colspan=12 valign=top style='width:501pt;border:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>Name (as shown on your
  income tax return)<br><input type='text' name='w9name' class='textfield' size=150 maxlength=150><o:p></o:p></span></p>
    </td>
 </tr>
 <tr>
  <td colspan=12 valign=top style='width:501pt;border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>Business Name, if
  different from above
  <br><input type='text' name='w9busname'  class='textfield' size=150 maxlength=150>
  </td>
 </tr>
 <tr>
  <td width=111 colspan=2 valign=top style='width:82.95pt;border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>Check appropriate box: <o:p></o:p></span></p>
  </td>
  <td width=15 valign=top style='border-top:none;border-left:
  none;border-bottom:solid windowtext .5pt;border-right:none windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>
    <input type='radio' name='classification' value='1' class='textfield'>
     <o:p></o:p></span></p>
  </td>
  <td width=137 valign=top style='border-top:none;border-left:
  none;border-bottom:solid windowtext .5pt;border-right:none windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>Individual/Sole Proprietor<o:p></o:p></span></p>
  </td>
  <td colspan=2 valign=top style='border-top:none;
  border-left:none;border-bottom:solid windowtext .5pt;border-right:none windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>
    <input type='radio' name='classification' value='2' class='textfield'>Corporation<o:p></o:p></span></p>
  </td>
  <td width=103 valign=top style='width:77.4pt;border-top:none;border-left:
  none;border-bottom:solid windowtext .5pt;border-right:none windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>
    <input type='radio' name='classification' value='3' class='textfield'>Partnership<o:p></o:p></span></p>
  </td>
  <td width=84 valign=top style='width:63.0pt;border-top:none;border-left:none;
  border-bottom:solid windowtext .5pt;border-right:none windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'><input type='radio' name='classification' value='4' class='textfield'>Other<o:p></o:p></span></p>
  </td>
  <td width=106 colspan=2 valign=top style='width:79.15pt;border-top:none;
  border-left:none;border-bottom:solid windowtext .5pt;border-right:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'><input type='text' name='other' size=20 maxlength=20 class='textfield'><o:p></o:p></span></p>
  </td>
  <td width=26 valign=top style='width:19.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext .5pt;border-right:none windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'><input type='checkbox' name='exempt' class='textfield'> <o:p></o:p></span></p>
  </td>
  <td width=173 valign=top style='width:129.55pt;border-top:none;border-left:
  none;border-bottom:solid windowtext .5pt;border-right:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>Exempt from Backup
  Withholding<o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td width=556 colspan=9 valign=top style='width:500.4pt;border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>Address (number, street,
  and apt. or suite no)<br>
  <input type='text' name='address' class='textfield' size=95 maxlength=95>
  </td>
  <td width=100 colspan=3 rowspan=2 valign=top style='width:200.0pt;border-top:
  none;border-left:none;border-bottom:solid windowtext .5pt;border-right:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  &nbsp;
  </td>
 </tr>
 <tr>
  <td width=556 colspan=9 valign=top style='width:500.0pt;border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>City, state, and ZIP code<br>
      <input type='text' name='city' class='textfield' size=85 maxlength=85>
      <input type='text' name='state' class='textfield' size=2 maxlength=2>
      <input type='text' name='zip' class='textfield' size=5 maxlength=5>
      </td>
 </tr>
 <tr>
  <td colspan=12 valign=top style='width:501pt;border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial'>List account number(s)
  here (optional)<br>
  NOT REQUIRED <br>&nbsp;
  </td>
 </tr>
 <tr>
  <td width=67 valign=top style='width:.7in;border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;background:black;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial;color=white'>Part 1<o:p></o:p></span></p>
  </td>
  <td width=808 colspan=11 valign=top style='width:606.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext .5pt;border-right:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><b><span style='font-family:Arial'>Taxpayer Identification
  Number (TIN)<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr>
  <td width=595 colspan=9 valign=top style='width:6.2in;border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='mso-layout-grid-align:none;text-autospace:none'><span
  style='mso-bidi-font-size:8.0pt;font-family:Arial'>Enter your TIN in the
  appropriate box. The TIN provided must match the name given on Line 1 to
  avoid backup withholding. For individuals, this is your social security
  number (SSN). However, for a resident alien, sole proprietor, disregarded
  entity, or other entities, or if you do not have a number, please 
  see instructions at the 
 <a href=""  onclick="javascript: openwindow('http://www.irs.gov/instructions/iw9/index.html'); return false;">IRS Website</a>.
 
  <o:p></o:p></span><br><b><span
  style='mso-bidi-font-size:8.0pt;font-family:Arial'>Note. </span></b><i><span
  style='mso-bidi-font-size:8.0pt;font-family:Arial'>If the account is in more
  than one name, see the chart on the 
 
 <a href="" onclick="javascript: openwindow('http://www.irs.gov/instructions/iw9/index.html'); return false;">IRS Website</a>
 
  for guidelines on whose number to enter.</span></i><span
  style='mso-bidi-font-size:8.0pt;font-family:Arial'><o:p></o:p></span></p>
  </td>
  <td width=280 colspan=3 valign=top style='width:210.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext .5pt;border-right:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <b>Social Security Number<br>
  <span
  style='mso-bidi-font-size:8.0pt;font-family:Arial'>
  <input type='text' name='ssn1' class='textfield' size=3 maxlength=3> – <input type='text' name='ssn2' class='textfield' size=2 maxlength=2> - <input type='text' name='ssn3' class='textfield' size=4 maxlength=4><o:p></o:p></span>
  <br><b>or<br>Employer Identification Number<br>
  <input type='text' name='ein1' class='textfield' size=2 maxlength=2> - <input type='text' name='ein2' class='textfield' size=7 maxlength=7>
  </td>
 </tr>
 <tr>
  <td width=67 valign=top style='width:.7in;border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;background:black;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><span style='font-family:Arial;color:white'>Part 2<o:p></o:p></span></p>
  </td>
  <td width=808 colspan=11 valign=top style='width:606.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext .5pt;border-right:solid windowtext .5pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal><b><span style='font-family:Arial'>Certification<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr>
  <td colspan=13 valign=top style='border:solid windowtext .5pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;padding:0in 5.4pt 0in 5.4pt'>
  <p class=MsoNormal style='margin-left:.25in;mso-layout-grid-align:none;
  text-autospace:none'><span style='mso-bidi-font-size:8.0pt;font-family:Arial'>Under
  penalties of perjury, I certify that:<o:p></o:p></span></p>

  <ol style='margin-top:0in' start=1 type=1>
   <li class=MsoNormal style='mso-list:l0 level1 lfo1;tab-stops:list .5in;
       mso-layout-grid-align:none;text-autospace:none'><span style='mso-bidi-font-size:
       8.0pt;font-family:Arial'>The number shown on this form is my correct
       taxpayer identification number (or I am waiting for a number to be
       issued to me), and<o:p></o:p></span></li>
   <li class=MsoNormal style='mso-list:l0 level1 lfo1;tab-stops:list .5in;
       mso-layout-grid-align:none;text-autospace:none'><span style='mso-bidi-font-size:
       8.0pt;font-family:Arial'>I am not subject to backup withholding because:
       (a) I am exempt from backup withholding, or (b) I have not been notified
       by the Internal Revenue Service (IRS) that I am subject to backup
       withholding as a result of a failure to report all interest or
       dividends, or (c) the IRS has notified me that I am no longer subject to
       backup withholding, and<o:p></o:p></span></li>
   <li class=MsoNormal style='mso-list:l0 level1 lfo1;tab-stops:list .5in;
       mso-layout-grid-align:none;text-autospace:none'><span style='mso-bidi-font-size:
       8.0pt;font-family:Arial'>I am a U.S. person (including a U.S. resident
       alien).
  <p class=MsoNormal style='mso-layout-grid-align:none;text-autospace:none'><span
  style='mso-bidi-font-size:8.0pt;font-family:Arial'>Certification
  instructions. You must cross out item 2 above if you have been notified by
  the IRS that you are currently subject to backup withholding because you have
  failed to report all interest and dividends on your tax return. For real
  estate transactions, item 2 does not apply. For mortgage interest paid,
  acquisition or abandonment of secured property, cancellation of debt,
  contributions to an individual retirement arrangement (IRA), and generally,
  payments other than interest and dividends, you are not required to sign the
  Certification, but you must provide your correct TIN. (See the instructions on at the

 <a href="" onclick="javascript: openwindow('http://www.irs.gov/instructions/iw9/index.html'); return false;">IRS Website</a>
 
 .)<o:p></o:p></span></p>
  <table border=1 cellspacing=0 cellpadding=0 style='border-collapse:collapse;
   border:none;mso-border-alt:solid windowtext .5pt;mso-padding-alt:0in 5.4pt 0in 5.4pt'>
   <tr>
    <td width=844 valign=top style='width:632.8pt;border:solid windowtext .5pt;
    padding:0in 5.4pt 0in 5.4pt'>
    <h3>MY SUBMISSION OF THIS FORM ACKNOWLEDGES CONFIRMATION THAT PURSUANT TO
    THE CERTIFICATION IMMEDIATELY ABOVE I AM CERTIFYING THAT I AM THE PERSON
    REPRESENTED IN THE W-9 FORM BEING SUBMITTED. </h3>
    <p class=MsoNormal align=center style='text-align:center'><input type='submit' value='I confirm the above information is true and correct' name='savedata'></p>
    </td>
   </tr>
  </table>
  <p class=MsoNormal style='mso-layout-grid-align:none;text-autospace:none'><o:p></o:p></p>
  </td>
 </tr>
 <![if !supportMisalignedColumns]>
 <tr height=0>
  <td width=67 style='border:none'></td>
  <td width=43 style='border:none'></td>
  <td width=29 style='border:none'></td>
  <td width=137 style='border:none'></td>
  <td width=43 style='border:none'></td>
  <td width=65 style='border:none'></td>
  <td width=103 style='border:none'></td>
  <td width=84 style='border:none'></td>
  <td width=24 style='border:none'></td>
  <td width=82 style='border:none'></td>
  <td width=26 style='border:none'></td>
  <td width=173 style='border:none'></td>
 </tr>
 <![endif]>
</table>

<p class=MsoNormal style='mso-layout-grid-align:none;text-autospace:none'><![if !supportEmptyParas]>&nbsp;<![endif]><o:p></o:p></p>

</div>
</form>
</body>

</html>
];
}

