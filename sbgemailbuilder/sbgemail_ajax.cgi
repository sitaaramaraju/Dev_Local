#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use CGI qw(:standard);
my $cgi = CGI->new();

	
#	use Date::Calc qw(Today Add_Delta_Days);
#	my $cgi = CGI->new();
#    use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
#    $main::DriverType = "SQL Server";
#	$main::ServerIP = $ENV{'HTTP_HOST'};
	# require "G:/CenturyLink/xroot/cgi-bin/delimeter.cgi";
  #  require "G:/CenturyLink/xroot/cgi-bin/lp-init.pm";    #Initialize Co-opPro DSN
#	require "G:/CenturyLink/xroot/cgi-bin/lp-prog-opts.pm";

my $server;

if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
#else{
#    $server = "d:/xroot";
#}

require "$server/cgi-bin/init.cgi";
require "$server/cgi-bin/delimeter.cgi";
require "$server/sbgemailbuilder/sbgemail_subs.cgi";

	my $db          = DBInterface->new();
	my $db2         = DBInterface->new();
	my $myDB1		= DBInterface->new();
	my $myDB3		= DBInterface->new();

#my ($db, $db2, $myDB1, $myDB3);

	my $thisfile = "sbgemail_ajax.cgi";
    my $url_prefix;

#my $cgi = CGI->new();
#my ($name, $value);
#%main::cgi;
#foreach $name ($cgi->param) {
#        foreach $value ($cgi->param($name)) {
#              $main::cgi{$name} = $value;
#        }
#}

#print "Content-type:text/html\n\n";print "outside".$main::cgi{getform};exit();

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{getTrack} == 1 ) {
if ($cgi->param('getTrack') == 1 ) {
 	my $source_id =  $cgi->param('source_id');

my $cci_id = EscQuote($cgi->param('cci_id'));

my $n = "no id";
 if ($cci_id eq "") { $n = "got it";
 }

	my ($emplid ) = 1;#getEmpID_SourceID ($cci_id);

	my ($chk_box, $status, $mail_id, $propid);
	my $sql = " select count( mail_id) as cnt
				from ctl_sbgemail with (nolock) 
				inner join ctl_sbgEmail_status cs with (nolock) on cs.status_id = ctl_sbgemail.email_status_id
				where createdby_emplid = ? and source_id = ?
				and cs.is_active = 1";

	my $sth = $db->prepare($sql);
	$sth->execute($emplid, $source_id);
	my $qty_dt = $sth->fetchrow_hashref();
	$sth->finish();
	$n=$qty_dt->{cnt};
	my $string = qq[
		<table width="100%" border="0" class="tracker"><tr>
                    <td colspan="3"><strong>Emails</strong></td>
                  </tr>
				  <tr>
                    <td width="10%"><p>&nbsp;</p></td>
                    <td width="63%"><p>Name</p></td>
                    <td width="27%" align="right"><p>Date Sent</p></td>
                  </tr>
		<tr>
                    <td colspan="3"><p>under construction</p> </td>
                  </tr></table>
		];



#		print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
  }
#------------------------------------------------------------------------------------------------------------------------------------------------------------
=head
#if ($main::cgi{getTrack} == 100 ) {
if	($cgi->param('getTrack') == 100){

	my $cci_id =  $cgi->param('cci_id');
#	my $session_id =  $main::session{session_id};
	my $source_id =  $cgi->param('source_id') || 2;

my ($session_id,$emplid) = CCICryptography::getEmpid($cci_id); 

	my (%data, $chk_box, $status, $mail_id, $propid);

	my $string = qq[
		<table width="100%" border="0" class="tracker"><tr>
                    <td colspan="3"><strong>Emails</strong></td>
                  </tr>
				  <tr>
                    <td width="10%"><p>&nbsp;</p></td>
                    <td width="63%"><p>Name</p></td>
                    <td width="27%" align="right"><p>Date Sent</p></td>
                  </tr>
		];
#and DATEDIFF (dd, email_status_chng_dt, getdate()) < 15 
	my $sql = "select top 3 mail_id, rtrim(first_name)+' '+RTRIM(last_name) as cname, RTRIM(company_name) as company_name, 
convert(varchar,date_created,101) as date_sent, RTRIM(status_name) as status_name, ctl_sbgemail.email_status_id
 from ctl_sbgemail with (nolock) 
 inner join ctl_sbgEmail_status cs with (nolock) on cs.status_id = ctl_sbgemail.email_status_id
 where createdby_emplid = ? and source_id = ?
 and cs.is_active = 1
 --and date_created > dateadd(day,-15,GETDATE())
 order by date_created desc  ";


	my $sth = $myDB->prepare($sql);
	$sth->execute($emplid, $source_id);


			while (my $data = $sth->fetchrow_hashref) {
				#%state = $db->DataHash();
			$mail_id = $data{mail_id};
			if ($data{email_status_id} == 2) {
				$status = '<span class="sold">SOLD</span>';
				$chk_box='';
			}
			else {
				$status = "";
				$chk_box = '<input name="mail_id" type="checkbox" id="mail_id" value="'.$mail_id.'" onclick="updatestatus(this.value )"/>' ;
			}
			$string .= qq[<tr><td>$chk_box</td>
							<td><p>$data->{cname}$status <br /><small>$data->{company_name}</small></p></td>
							<td ><p>$data->{date_sent}</p></td>
							</tr> ];
			}
			$sth->finish();


 $string .= qq[ <tr>
                    <td colspan="3"><strong>Proposals</strong></td>
                  </tr>
				  <tr>
                    <td width="10%"><p>&nbsp;</p></td>
                    <td width="63%"><p>Name</p></td>
                    <td width="27%" align="right"><p>Date Sent</p></td>
                  </tr> ];

	$sql = "select top 3 proposalID, rtrim(first_name)+' '+RTRIM(last_name) as cname, RTRIM(company_name) as company_name, 
convert(varchar,date_created,101) as date_sent, RTRIM(status_name) as status_name, ctl_sbgProposal.proposal_status_id
 from ctl_sbgProposal with (nolock) 
 inner join ctl_sbgEmail_status cs with (nolock) on cs.status_id = ctl_sbgProposal.proposal_status_id
 where createdby_emplid =? and source_id = ?
 and cs.is_active = 1
-- and date_created > dateadd(day,-15,GETDATE())
 order by date_created desc ";





	my $sth2 = $myDB->prepare($sql);
	$sth2->execute($emplid, $source_id);


			while (my $data2 = $sth2->fetchrow_hashref) {
			$propid = $data2->{proposalID};
			if ($data->{proposal_status_id} == 2) {
				$status = '<span class="sold">SOLD</span>';
				$chk_box='';
			}
			else {
				$status = "";
				$chk_box = '<input name="propid" type="checkbox" id="propid" value="'.$propid.'" onclick="updatestatus_proposal(this.value,'.$cci_id.' )"/>' ;
			}
			$string .= qq[<tr><td>$chk_box</td>
							<td><p>$data->{cname}$status <br /><small>$data->{company_name}</small></p></td>
							<td ><p>$data->{date_sent}</p></td>
							</tr> ];
			}
			$sth->finish();



 $string .= qq[</table>];

  print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
  print $string;
  $db->Close();
  $db2->Close();
  $myDB1->Close();
  $myDB3->Close();
  exit;
}
=cut
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{getform} == 1 && $main::cgi{flowID} == 1  ) { # BAU
if ($cgi->param('getform') == 1 && $cgi->param('flowID') == 1  ) { # BAU
	my $language_id = $cgi->param('language_id'); #$main::cgi{language_id};
	my $legacy =  $cgi->param('legacy');#$main::cgi{legacy};
	my $cci_id = $cgi->param('cci_id');
 # formID == 1 is email builder
 # formID == 2 is Proposal maker

	my $string = qq[

                <h3>Step 2. Theme Selection <small class="orange"><em>must select one</em><label><span id='req_theme'></span></label></small></h3>
                <table width="100%" border="0" class="form-table">

                  <tr>
                  	<td><a class="button-contentmap" href="#" onclick="openWin('content_map.cgi')">Content Map</a></td>
                  </tr>
];
my ($sql2,  $theme_id);
$sql2="select theme_id, RTRIM(description) as description from ctl_sbgEmail_theme with (nolock) where is_active = 1 order by theme_id";
my $id = '';
my $description = '';
#print qq[<!--	$sql2	-->];


my $sth = $db->prepare($sql2);
	$sth->execute();

	while (my $data2 = $sth->fetchrow_hashref) {
		$id= 'RadioGroup2_'.$data2->{theme_id};
		$description = $data2->{description};
		$theme_id = $data2->{theme_id};
		$string .= qq[ <tr><td><p><label><input type="radio" name="theme" value="$theme_id" id="$id" onClick="showTopic($theme_id)" class="radio-button"/>$description</label></p></td></tr>];
	}
	$sth->finish();



$string .= qq[
	 </table>
                <hr />
                <h3>Step 3. Topic Selection <small class="orange"><em>must select one or more</em></small><label><span id='req_topic'></span></label></h3>
            <!--GENERAL PRODUCT INFORMATION-->
			<div style="height:0;overflow:hidden;visibility:hidden;">&nbsp;</div>
			<div id="themediv" name="themediv" class="form-table"><!--	--> </div>

<!--	ajax table above this	-->

<hr />
 <table width="100%" border="0" class="form-table">

                  <tr>
                    <td colspan="3"><small><em>personal note - up to 600 characters max.<br />
					<span id="charcount">0</span> characters entered.   |   <span id="remaining">600</span> characters remaining.</em></small></td>
                  </tr>
                  <tr>
                    <td colspan="3"><textarea name="note" cols="" rows="10" class="text-box" id="note"
					onkeyup="CheckFieldLength(note, 'charcount', 'remaining', 600);" 
					onkeydown="CheckFieldLength(note, 'charcount', 'remaining', 600);" 
					onmouseout="CheckFieldLength(note, 'charcount', 'remaining', 600);"></textarea>
                  <tr>
                    <td colspan="3" align="right"><input type="button" value="Spell Check" onclick="\$Spelling.SpellCheckInWindow('note')" /></td>
                  </tr>
		
					</td>

                  </tr>
                </table>
              <table width="100%" border="0" class="form-table">
                  <tr>
                  	<td colspan="3" align="center">
					<h3>ALL USERS ARE PERSONALLY RESPONSIBLE FOR ADHERENCE TO THE CPNI RULES.</h3>
					<h4>Be sure to review your input and selections. If everything is complete and correct click "Send" below. </h4></td>
                  </tr>
				  <tr><td>
					</td></tr>

                  <tr>
                	<td align="center" colspan="3">
					<input type="hidden" name="confirming" value=""> 
		<input name="send" type="button" value="" class="button-send" onclick="getconfirm()"/> 
					</td>
              	  </tr>
				  <tr><td colspan="3"></td></tr>
                </table>

];

#print "Content-type:text/html\n\n";print "outside".$main::cgi{getform};exit();
  #print "Content-type:text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{getTopicList} == 1 && $main::cgi{theme_id} == 1) { # 3 columns
if ($cgi->param('getTopicList') == 1 && $cgi->param('theme_id') == 1 ) {

	my $theme_id = $cgi->param('theme_id');
	my $language_id = $cgi->param('language_id');
	my $legacy =  $cgi->param('legacy');
	my $string = qq[
		<table width="100%" border="0" id="topic-1" class="form-table"><tr> 
		];
my $clause = '';

if ($language_id == 2) { #spanish
	if ($legacy == 1) {  #qwest
		$clause = "and LQ_spanish = 1 ";
	}
	elsif ($legacy == 2) {
		$clause = "and LCTL_spanish = 1 ";
	}
}
else { #language is english
	if ($legacy == 1) {  #qwest
		$clause = "and LQ_english = 1 ";
	}
	elsif ($legacy == 2) {
		$clause = "and LCTL_english = 1 ";
	}
}
my ( $sql2,$descr1, $descr2, $topic_id, $url, $topic_head, $topic_name, $pdf_str, $pdf_name,$heading, $description, $pdf_url, $ss_id);
my $cnt = 1;
my $sql = "select ss_id, heading, description
 from  ctl_sbgEmail_sellsheets with (nolock) where is_active = 1
$clause
order by heading, item_order";


my $sth = $db->prepare($sql);
	$sth->execute();

	while (my $data = $sth->fetchrow_hashref) {
	$description = $data->{description};
	$ss_id = $data->{ss_id};
	$pdf_url = $data->{pdf_url};
	$pdf_str = '';
	
	if ($heading ne $data->{heading} && $cnt == 1) {
		$string .= qq [<td colspan="3"><h4>$data->{heading} </h4></td>  </tr><tr> ];
	}
	elsif ($heading ne $data->{heading} && $cnt > 1) {
		$string .= qq [</td></tr><tr> <td colspan="3"><h4>$data->{heading} </h4></td>  </tr><tr> ];
	}
	if (  $cnt > 1 && ($cnt % 3) == 1) {
				$string.= qq[</td></tr><tr>  ];

	}
	elsif (  $cnt > 1 && (($cnt % 3)== 0  || ($cnt % 3)== 2) ) {
				$string.= qq[</td>]; 

	}
	$string.= qq[ 
        <td width="33%"><p style="margin-bottom:2px;"><p>
		<label for="$descr1">
		<input name="ss_id" id="$ss_id" type="checkbox" value="$ss_id" />
		$description </p>$pdf_str
		</label>
		];


		$heading = $data->{heading};
		$cnt++;
	}
	$sth->finish();


	$string .= qq[</td></tr></table> ];
	$string .= qq [ <h3>Step 4. Add  a Personalized Note</h3>               
		];
 
#		print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{getTopicList} == 1 && $main::cgi{theme_id} > 1) { #&& $main::cgi{theme_id} > 1
if ($cgi->param('getTopicList') == 1 && $cgi->param('theme_id') > 1) {

	my $theme_id = $cgi->param('theme_id');
	my $language_id = $cgi->param('language_id');
	my $legacy =  $cgi->param('legacy');
	my $clause = '';

if ($language_id == 2) { #spanish
	if ($legacy == 1) {  #qwest
		$clause = "and LQ_spanish = 1 ";
	}
	elsif ($legacy == 2) {
		$clause = "and LCTL_spanish = 1 ";
	}
}
else { #language is english
	if ($legacy == 1) {  #qwest
		$clause = "and LQ_english = 1 ";
	}
	elsif ($legacy == 2) {
		$clause = "and LCTL_english = 1 ";
	}
}

	my $string = qq[
		<table width="100%" border="0" id="topic-1" class="form-table"><tr> 
		];
my ( %data, %data2, $sql2,$descr1, $descr2, $topic_id, $url, $pdf_name, $topic_name);
my $cnt = 1;
my $sql = "select distinct RTRIM(description) as descr , 
(select top 1 topic_id from ctl_sbgEmail_topic cst2 with (nolock) where cst2.theme_id = ctl_sbgEmail_topic.theme_id 
and cst2.is_active = 1 and cst2.description = ctl_sbgEmail_topic.description) as topic_id
from ctl_sbgEmail_topic with (nolock)
where theme_id = $theme_id and is_active = 1
order by descr";

my $sth2;
my $sth = $db->prepare($sql);
	$sth->execute();
	while (my $data = $sth->fetchrow_hashref) {
		$descr1 = $data->{descr};
		$topic_id = $data->{topic_id};
		$topic_name = 'topic_name_'.$cnt;


		if (  $cnt > 1 && ($cnt % 2) == 0) {
			$string.= qq[</td>]; 
		}
		elsif (  $cnt > 1 && ($cnt % 2) == 1) {
			$string.= qq[</td></tr><tr>  ];
		}
		$string.= qq[ 
			<td width="50%"><p style="margin-bottom:2px;">
			<label for="$descr1">
			<input name="topic_name" id="$topic_id" type="checkbox" value="$topic_id" />
			$descr1
			</label></p>
		];

		$sql2 = "select topic_id,  RTRIM(pdf_url) as url, RTRIM(pdf_name) as pdf_name from ctl_sbgEmail_topic with (nolock)
					where is_active = 1 and theme_id = $theme_id and description = '$descr1'
					order by pdf_name";

		$sth2 = $db2->prepare($sql2);
		$sth2->execute();

		while (my $data2 = $sth2->fetchrow_hashref) {
			$url = $data2->{url};
			$pdf_name = $data2->{pdf_name};

			$string.= qq[
				 <p class="included"><a class="inline" href="$url"target="_blank">$pdf_name </a></p>
			];
		}
		$sth2->finish();
		$cnt++;
		$descr1 = $data->{descr};

	}

	$sth->finish();

	$string .= qq[</td></tr></table> ];

	$string .= qq[
		 <h3>Step 4. Add  Sell Sheets and/or Personalized Note</h3>
                <small style="margin-top:12px;"><em>attach product sell sheets</em></small>
                <table width="100%" border="0" class="form-table"><tr>
		];

$sql = "select ss_id, heading, description
 from  ctl_sbgEmail_sellsheets with (nolock) where is_active = 1
$clause
order by heading, item_order";

$cnt = 1;
my ($heading, $description, $pdf_url, $ss_id, $pdf_str);

my $sth3 = $db->prepare($sql);
	$sth3->execute();
	while (my $data3 = $sth3->fetchrow_hashref) {
	$description = $data3->{description};
	$ss_id = $data3->{ss_id};
	$pdf_url = $data3->{pdf_url};
	
	if ($heading ne $data3->{heading} && $cnt == 1) {
		$string .= qq [<td colspan="3"><h4>$data3->{heading}</h4></td>  </tr><tr> ];
	}
	elsif ($heading ne $data3->{heading} && $cnt > 1) {
		$string .= qq [</td></tr><tr> <td colspan="3"><h4>$data3->{heading}</h4></td>  </tr><tr> ];
	}
	if (  $cnt > 1 && ($cnt % 3) == 1) {
				$string.= qq[</td></tr><tr>  ];

	}
	elsif (  $cnt > 1 && (($cnt % 3)== 0  || ($cnt % 3)== 2) ) {
				$string.= qq[</td>]; 

	}
#	$pdf_str = "<small><em>";
	$string.= qq[ 
        <td width="33%"><p style="margin-bottom:2px;"><p>
		<label for="$descr1">
		<input name="ss_id" id="$ss_id" type="checkbox" value="$ss_id" />
		$description </p>$pdf_str
		</label>
		];

		$heading = $data3->{heading};
		$cnt++;
	}
	$sth3->finish();

$string .= qq[                  
                </table>
		];

#		print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{getform} == 1 && $main::cgi{flowID} == 3  ) { # Confirmation
if ($cgi->param('getform') == 1 && $cgi->param('flowID') == 3) {
	my $language_id = $cgi->param('language_id');
	my $legacy =  $cgi->param('legacy');
 # formID == 1 is email builder
 # formID == 2 is Proposal maker
 # formID == 3 is Order Confirmation
	my $legacy_clause = "and ISNULL(is_LCTL,0)= 1";
	if ($legacy == 1) {
		$legacy_clause = "and ISNULL(is_LQ,0)= 1";
	}

	my $string = qq[

		    <script>
        jQuery(function() {
 
        
        jQuery( "#datepicker" ).datepicker();
           
               
        jQuery("#cleardates").click(function() {
        
            jQuery("#datepicker").val("");
            
            return false; // Do not submit
        });
        
        jQuery("#preview").click(function() {
            
            jQuery("#tipwindow").html(jQuery("#message").val());
           return false; 
        });

          jQuery(".rte-zone").rte({
               media_url: "/jquery/rte/",
               content_css_url: "/jquery/rte/rte_centurylink.css"
            });

       
    });
    </script>
    <style>
    .shadow {
    background-color:white;
    border-width:1px;
    border-style:solid;
    -moz-box-shadow: 3px 3px 4px #000;
    -webkit-box-shadow: 3px 3px 4px #000;
    box-shadow: 3px 3px 4px #000;
    /* For IE 8 */
    -ms-filter: "progid:DXImageTransform.Microsoft.Shadow(Strength=4, Direction=135, Color='#000000')";
    /* For IE 5.5 - 7 */
    filter: progid:DXImageTransform.Microsoft.Shadow(Strength=4, Direction=135, Color='#000000');
    width:250px;
    height;100px;
    padding:10px;
    float:left;
    border-radius: 15px;
    font-size:14px;
    font-family:"Comic Sans MS"; 
    }

</style>
<!--[if gte IE 6]> 
<style>
.shadow {
background-color:white;
border-width:1px;
border-style:solid;
-moz-box-shadow: 3px 3px 4px #000;
-webkit-box-shadow: 3px 3px 4px #000;
box-shadow: 3px 3px 4px #000;
/* For IE 8 */
-ms-filter: "progid:DXImageTransform.Microsoft.Shadow(Strength=4, Direction=135, Color='#000000')";
/* For IE 5.5 - 7 */
filter: progid:DXImageTransform.Microsoft.Shadow(Strength=4, Direction=135, Color='#000000');
width:250px;
height;100px;
padding:10px;
float:left;
margin-left:-75px;
font-size:14px;
font-family:"Comic Sans MS"; 
}
</style>
<![endif]-->



                <h3>Step 2. Order Details <small class="orange"><em>must select one </em><label><span id='req_sod'></span></label></small></h3>
                <table width="100%" border="0" class="form-table">
					<tr>
                    <td width="38%" align="right"><p>
                      <label for="btn"><span class="orange">*</span>Billing Telephone Number </label></p></td>
                    <td width="62%"><input name="btn1" id="btn1" type="text" tabindex="1" class="btn-field" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3"/>&nbsp;
				<input name="btn2" id="btn2" type="text" tabindex="1" class="btn-field" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3"/>&nbsp;
				<input name="btn3" id="btn3" type="text" tabindex="1" class="btn3-field" maxlength="4"/>
					<label><span id='req_btn'></label></td>
                  </tr>

					<tr>
                    <td width="38%" align="right"><p>
                      <label for="order_number"><span class="orange">*</span>Order Number</label></p></td>
                    <td width="62%"><input name="order_number" id="order_number" type="text" tabindex="1" class="text-field"/>
					<label><span id='req_order_number'></label></td>
                  </tr>


					<tr>
                    <td width="38%" align="right"><p>
                      <label for="date"><span class="orange">*</span>Installation Date</label></p></td>
                    <td width="62%"><input name="install_date" id="install_date" type="text" tabindex="1" class="text-field" readonly="true" style="background:#E6E6E6;"/>
<a href="javascript:show_calendar('frm.install_date');" onmouseover="window.status='Date Picker'; return true;" onmouseout="window.status=''; return true;">(mm/dd/yy)</a>
						<label><span id='req_install_date'></label></td>
                  </tr>


					<tr>
                    <td width="38%" align="right"><p>
                      <label for="btn"><span class="orange">*</span>Products Ordered</label></p></td>
                    <td width="62%">&nbsp;<small class="orange"><em>must select one</em></small>
					<label><span id='req_prod'></label></td>
                  </tr>
];

my ($sql2,$productID);
#print qq[<!--	$id	-->];

$sql2 = "select productID, RTRIM(description) as description
		from ctl_sbgOrderConfirm_product with (nolock)
		where ISNULL(is_active,0) = 1 $legacy_clause
		order by item_order";
#$string .= qq[ <tr><td colspn="2">$sql2</td></tr>];

my $sth = $db->prepare($sql2);
	$sth->execute();
	while (my $data = $sth->fetchrow_hashref) {
			$productID = $data->{productID};
			$string .= qq[<tr> <td width="38%" align="right"><input name="productID" id="$productID" type="checkbox" value="$productID"></td>
							<td width="62%" align="left">$data->{description}</td>];
	}
	$sth->finish();

$string .= qq[
 <table width="100%" border="0" class="form-table">

                  <tr>
                    <td colspan="3"><small><em>personal note - up to 600 characters max.<br />
					<span id="charcount">0</span> characters entered.   |   <span id="remaining">600</span> characters remaining.</em></small></td>
                  </tr>
                  <tr>
                    <td colspan="3"><textarea name="noteOC" cols="" rows="10" class="text-box" id="noteOC"
					onkeyup="CheckFieldLength(noteOC, 'charcount', 'remaining', 600);" 
					onkeydown="CheckFieldLength(noteOC, 'charcount', 'remaining', 600);" 
					onmouseout="CheckFieldLength(noteOC, 'charcount', 'remaining', 600);"></textarea>
                  <tr>
                    <td colspan="3" align="right"><input type="button" value="Spell Check" onclick="\$Spelling.SpellCheckInWindow('noteOC')" /></td>
                  </tr>
		
					</td>

                  </tr>
                </table>
              <table width="100%" border="0" class="form-table">

                  <tr>
                	<td align="center" colspan="3">
						<input type="hidden" name="goWhere" value="0">
		<input name="send" type="button" value="" class="button-send" onclick="getProdEmailConfirm()"/> 
					</td>
              	  </tr>
				  <tr><td colspan="3"></td></tr>
                </table>

];


#		print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{getform} == 1 && $main::cgi{flowID} == 2 ) { # PB
if ($cgi->param('getform') == 1 && $cgi->param('flowID') == 2 ) { # PB
	my $language_id = $cgi->param('language_id');
	my $legacy =  $cgi->param('legacy');
	my $legacy_clause = "and ISNULL(is_LCTL,0)= 1";

	if ($legacy == 1) {
		$legacy_clause = "and ISNULL(is_LQ,0)= 1";
	}
	#style="width:869px; height:380px; vertical-align:top;"
	my ( $heading, $descr, $selection, $sub_selection, $close_div, $sql);
	my ($productID, $called, $cnt, $nrc_name, $mrc_name, $term_name, $speed_name, $ship_name,$id, $qty_name,$reqd_note, $hide_show_div, $detaildiv);
	my ($hdr_sql,  $header_id,  $subdetaildiv, $termSpanName , $qtyclause, $termclause, $nrcclause ,$mrcclause, $shipclause, $speedclause ,$addNote);

	my ($req_qty,$req_term ,$req_nrc ,$req_mrc ,$req_ship ,$req_speed);

	my $counter = 0;
	my $tab = 0;
	my $string = qq[	<h3>Step 2. Product Selection <small class="orange"><em>must select one or more </em>
							<label><span id='req_prod'></span></label></small>
						</h3>
						];
	$hdr_sql = "select rtrim(description) as heading, rtrim(ISNULL(reqd_note,'')) as reqd_note , header_id
				from ctl_sbgProposal_header with (nolock) where is_active = 1 $legacy_clause order by hdr_order";


my ($sth2,$pdf_eng,$pdf_span) ;
my $sth = $db->prepare($hdr_sql);
	$sth->execute();

	while (my $hdr_dt = $sth->fetchrow_hashref) {
		$heading = $hdr_dt->{heading};
		$reqd_note = $hdr_dt->{reqd_note};
		$header_id = $hdr_dt->{header_id};
		if ($reqd_note ne "") {
			$reqd_note = '<small><em>'.$reqd_note.'</em></small>';
		}
		#style="border-color:black;"
		$hide_show_div = 'hide_show_'.$counter;
			$string .= qq[<table width="100%" border="0" class="email-content" > 
						<tr><td><h4>$heading  $reqd_note
						<small><a href="javascript:void(0)" onclick="toggleDiv('$hide_show_div',this);">Show Product List</a></small></h4></td></tr>
				</table>
						 <div id="$hide_show_div" style="display: none;">];

		$sql = "select productID, rtrim(prod_selection) as selection, RTRIM(description) as descr,
				ISNULL(prod_sub_selection,'') as sub_selection, isnull(prod_note_line,'') as prod_note_line,
				isnull((select count(prod_sub_selection) from ctl_sbgProposal_product b with (nolock) where b.prod_selection = 
				ctl_sbgProposal_product.prod_selection and ISNULL(prod_sub_selection,'')<>''  $legacy_clause) ,0) as cnt,
					ISNULL(show_nrc,0) as show_nrc, ISNULL(show_mrc,0) as show_mrc,
				ISNULL(show_shipping,0) as show_shipping, ISNULL(show_term,0) as show_term, ISNULL(show_qty,0) as show_qty,isnull(show_speed,0) as show_speed,
				ISNULL(is_LCTL,0) as is_LCTL, ISNULL(is_LQ,0) as is_LQ,
				case when (ISNULL(show_nrc,0) =0 and ISNULL(show_mrc,0) =0 and
				ISNULL(show_speed,0) =0 and ISNULL(show_term,0) =0 and ISNULL(show_qty,0) =0 ) then 0 else 1 end as flag,
					rtrim(isnull(reqd_note,'')) as reqd_note,
					(select pdf_name from ctl_sbgProposal_pdf s1 with (nolock) where s1.prop_prod_id = ctl_sbgProposal_product.productId) as pdf_name,
					(select pdf_english from ctl_sbgProposal_pdf s2 with (nolock) where s2.prop_prod_id = ctl_sbgProposal_product.productId) as pdf_eng,
					  (select pdf_spanish from ctl_sbgProposal_pdf s3 with (nolock) where s3.prop_prod_id = ctl_sbgProposal_product.productId) as pdf_span
				from ctl_sbgProposal_product with (nolock) where is_active = 1  $legacy_clause
				and prod_heading = '$heading'
				order by item_order";
			

	$sth2 = $db2->prepare($sql);
	$sth2->execute();

	while (my $data = $sth2->fetchrow_hashref) {

			$productID = $data->{productID};
			$cnt = $data->{cnt};
			$detaildiv = 'detaildiv_'.$productID;
			$subdetaildiv = 'subdetaildiv_'.$productID;
		$req_qty = "req_qty_".$productID;
		$req_term = "req_term_".$productID;
		$req_nrc = "req_nrc_".$productID;
		$req_mrc = "req_mrc_".$productID;
		$req_ship = "req_ship_".$productID;
		$req_speed = "req_speed_".$productID;
		( $qtyclause, $termclause, $nrcclause ,$mrcclause, $shipclause, $speedclause , $addNote,$pdf_eng,$pdf_span)=('','','','','','','','','');

		if ($data->{show_qty} == 1) { $qtyclause = "<span id='".$req_qty."'></span>"; }
		if ($data->{show_term} == 1) { $termclause = "<span id='".$req_term."'></span>"; }
		if ($data->{show_nrc} == 1) { $nrcclause = "<span id='".$req_nrc."'></span>"; }
		if ($data->{show_mrc} == 1) { $mrcclause = "<span id='".$req_mrc."'></span>"; }
		if ($data->{show_shipping} == 1) { $shipclause = "<span id='".$req_ship."'></span>"; }
		if ($data->{show_speed} == 1) { $speedclause = "<span id='".$req_speed."'></span>"; }
		if ($data->{prod_note_line} ne "") { $addNote =  "<small class=\"orange\"><em>$data->{prod_note_line}</em></small>";	}
				if ($selection ne $data->{selection}) {
			$string .= qq[<tr> <td>  ];
			if ($cnt == 0 ) {
				$string .= qq[ <input name="productID" id="$productID" type="checkbox" value="$productID" onClick="toggleVisibility('$detaildiv');"> ];
			}
			else {
				$string .= qq[ <input name="productID" id="$productID" type="checkbox" value="$productID" onClick="toggleVisibility('$subdetaildiv');"> ];
			}
		
			$string .= qq[$data->{selection}  $addNote $qtyclause $termclause $nrcclause $mrcclause $shipclause $speedclause<br></td></tr>];
=head
#uncomment this to see sell sheets associated
			if ($data{pdf_eng} ne "" || $data{pdf_span} ne "") {
				$string.= qq[ <tr><td><em>Product Sheets: ];
				if ($data{pdf_eng} ne "") {
					$pdf_eng = $data{pdf_eng};
					$string .= qq[ English - <a href="$pdf_eng" target="_blank">$data{pdf_name}</a>&nbsp;];
				}
				if ($data{pdf_span} ne "") {
					$pdf_span = $data{pdf_span};
					$string .= qq[Spanish - <a href="$pdf_span" target="_blank">$data{pdf_name}</a>];
				}
				$string .= qq[</td></tr>];
			}
=cut
			if ( $cnt == 0 && $data->{flag} > 0) {
				$string .= qq[<tr><td><div id="$detaildiv" name="$detaildiv" style="display: none;">
										<table width="100%" border="0" class="email-content" > <tr>];
				$string .= printQtyBar ($productID, $tab, $myDB1);
					$string .= qq[</tr></table>
									</div><!-- for qtys	--></td></tr> ];
			}
			elsif  ($cnt > 0 && $selection ne $data->{selection})  {
					$string .= qq[<tr><td><!-- open sub div $subdetaildiv -->
									<div id="$subdetaildiv" name="$subdetaildiv" style="display: none;"> ];# at 253 should call get_sub_products 
					if ($data->{sub_selection} eq "Main Prod") {
						$string .= printQtyBar ($productID, $tab, $myDB1);
					}
					$string .= get_sub_products ($heading, $data->{selection}, $legacy, $language_id, $header_id, $myDB1, $myDB3);
					$string .= qq[<!-- close sub div $subdetaildiv --></div></td></tr>];
			}
		}
			$selection = $data->{selection};
			$counter++;

#close prod selections
		}
		$sth2->finish();
		$string .= qq[<tr><td><h4> $heading - Promotions  </h4></td></tr><tr><td>  ];
		$string .= getPromos ($heading,$header_id,$language_id,$legacy, $myDB1, $myDB3);
		#$string .= qq[ promo here ];
		$string .= qq[</td></tr></table></div>];
	}
	#----
	$sth->finish();

	$string .= qq[  </table>
		  
		  
		  <hr />
 <table width="100%" border="0" class="form-table">
                <tr>
                    <td colspan="3"><h3>Step 3. Add a Personalized Note</h3> <small> Notes will be included in the email sent.</small>
			  <br><small><em>personal note - up to 600 characters max.<br />
					<span id="perscount">0</span> characters entered.   |   <span id="persremain">600</span> characters remaining.</em></small></td>
                  </tr>
                  <tr>
                    <td colspan="3"><textarea name="personal_note" cols="" rows="10" class="text-box" id="personal_note"
					onkeyup="CheckFieldLength(personal_note, 'perscount', 'persremain', 600);" 
					onkeydown="CheckFieldLength(personal_note, 'perscount', 'persremain', 600);" 
					onmouseout="CheckFieldLength(personal_note, 'perscount', 'persremain', 600);"></textarea>
						</td>
                  </tr>
                  <tr>
                    <td colspan="3" align="right"><input type="button" value="Spell Check" onclick="\$Spelling.SpellCheckInWindow('personal_note')" /></td>
                  </tr>
                </table>
              <table width="100%" border="0" class="form-table">
                  <tr>
                  	<td colspan="3" align="center">
					<h3>ALL USERS ARE PERSONALLY RESPONSIBLE FOR ADHERENCE TO THE CPNI RULES.</h3>
					<h4>Review your completed proposal before you send it by clicking "Review" below.</h4>
						
					</td>
                  </tr>
				  <tr><td>
					</td></tr>

                  <tr>
                	<td align="center" colspan="3">
		<input name="review" type="" value="" class="button-review" onclick="proposalCheck();"/> 
					</td>
              	  </tr>

				  <tr><td colspan="3"></td></tr>
                </table>
];
  
#		print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{dowhat} == 2 ) { # Show OC email
if ($cgi->param('dowhat') ==  2 ) { # Show OC email
	my $pre_oc_ID = $cgi->param('pre_oc_ID');
	
	my ( $prodlist, $noteList, $string, $string2 );
	#$string = qq[ <table width="90%" border="0" class="form-table" align="right"> <tr> <td align="left">test</td> </tr></table>];
	
	my $sql = " select prod.description  
				from ctl_sbg_OC_prod_interest oc_int with (nolock)
				inner join ctl_sbgOrderConfirm_product prod with (nolock) on prod.productID = oc_int.productID
				where oc_int.oc_id = ?
				order by prod.item_order";

	my $sth = $myDB1->prepare($sql);
	$sth->execute($pre_oc_ID);
	while (my $dt = $sth->fetchrow_hashref) {
		if ($dt->{description} ne "") {
			$prodlist .= qq[ <tr><td>&bull;$dt->{description}</td></tr>];
		}
	}
	$sth->finish();
	$sql = "select distinct rtrim(ISNULL(email_note,'')) as email_note
				from ctl_sbg_OC_prod_interest oc_int with (nolock)
				inner join ctl_sbgOrderConfirm_product prod with (nolock) on prod.productID = oc_int.productID
				where oc_int.oc_id = ?";

	my $sth = $myDB1->prepare($sql);
	$sth->execute($pre_oc_ID);
	while (my $dt = $sth->fetchrow_hashref) {
		if ($dt->{email_note} ne "") {
			$noteList .= qq[ <tr><td>$dt->{email_note}</td></tr>];
		}
	}
	$sth->finish();

	my $sql2 = "select convert(varchar, date_created,101) as dt ,datepart(yyyy,getdate()) as year , rtrim(first_name) as first_name, rtrim(btn) as btn,
				rtrim(last_name) as last_name,	rtrim(company_name) as company_name, RTRIM(tofield) as tofield, createdby_emplid as emplid,source_id, 
					rtrim(order_number) as order_number, convert(varchar,install_date, 101) as install_date, rtrim(personal_note) as personal_note
				from ctl_sbg_PreOC with (nolock)
				where pre_oc_id =  ?";

	my $sth2 = $db2->prepare($sql2);
		$sth2->execute($pre_oc_ID);
	my	$dt2 = $sth2->fetchrow_hashref();
	$sth2->finish();

	my $year = $dt2->{year};
	my $company_name = $dt2->{company_name};
	my $first_name = $dt2->{first_name};
	my $last_name = $dt2->{last_name};
	my $tofield = $dt2->{tofield};
	my $source_id = $dt2->{source_id};
	my $btn = $dt2->{btn};
	my $order_number = $dt2->{order_number};
	my $install_date = $dt2->{install_date};
	my $personal_note = $dt2->{personal_note};
	my $emplid = $dt2->{emplid};
	my $pdt =  $dt2->{dt};

	my $sql3 = "";
	if ($source_id == 2) {
		$sql3 = " select 2 as source_id, SAP_ID as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail , 
					case when isnull(work_phone,'') = '' then ''
						when isnull(work_phone,'') = '0000000000' then ''
						else SUBSTRING ( work_phone ,1 , 3 )+'-'+SUBSTRING ( work_phone ,4 , 3 )+'-'+SUBSTRING ( work_phone ,7 , 4 )end  as work_phone
				from qwesthr with (nolock) where convert( int, emplid ) = ?";
	}
	else {
			$sql3 = " select 8 as source_id, cuid as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail,
						'' as work_phone
						from ctl_floaters with (nolock) where floater_id = ? ";
	}

	my $sth3 = $db2->prepare($sql3);
		$sth3->execute($emplid);
	my	$emp_dt = $sth3->fetchrow_hashref();
	$sth3->finish();
	my $emp_email = $emp_dt->{emp_email};
	my $SAP_ID = $emp_dt->{SAP_ID};
	my $wk_phone = $emp_dt->{work_phone};
	if ($wk_phone eq "") {
		$wk_phone = $emp_email;
	}


	$string = qq[ <table width="90%" border="0" class="form-table" align="right">
	<tr> <td align="left">$pdt</td> </tr>
	<tr> <td align="left"><b> $first_name $last_name </b></td> </tr>
	<tr> <td align="left"><b> $company_name  </b></td> </tr>
	<tr> <td align="left"><b>  $tofield </b></td> </tr>
	<tr> <td align="left">Dear<b> $first_name $last_name</b>,</td> </tr>
	<tr> <td align="left">Thank you for choosing CenturyLink for your business services.</td></tr>
	<tr><td>Your order is being processed.  Please review a summary of your order below.</td></tr>
	<tr><td>Billing Telephone Number:  $btn<br><small><em>(Phone numbers are not guaranteed until installation is completed.)</td></tr>
	<tr><td>Order Number:  $order_number </td></tr>
	<tr><td> Installation Date:  $install_date</td></tr>
	<tr><td>Order:  $order_number</td></tr>
		$prodlist];
	if ($noteList ne "") {
		$string .= $noteList ;
	}
	$string .= qq[<tr><td>$personal_note</td></tr><tr><td>Thank you for choosing CenturyLink.</td></tr>];


#print "Content-type:text/html\n\n";print "outside".$main::cgi{getform};exit();
  #print "Content-type:text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{dowhat} == 1 ) { # Edit OC email
if ($cgi->param('dowhat') == 1 ) { # 
	my $pre_oc_ID = $cgi->param('pre_oc_ID');
	my $string = "";

	my $sql2 = "select convert(varchar, date_created,101) as dt ,datepart(yyyy,getdate()) as year , rtrim(first_name) as first_name, legacy,
				rtrim(last_name) as last_name,	rtrim(company_name) as company_name, RTRIM(tofield) as tofield, 
					createdby_emplid as emplid,source_id, rtrim(order_number) as order_number, convert(varchar,install_date, 1) as install_date,
					SUBSTRING ( btn ,1 , 3 ) as btn1,SUBSTRING ( btn ,4 , 3 ) as btn2,SUBSTRING ( btn ,7 , 4 ) as btn3 ,RTRIM(personal_note) as pnote
				from ctl_sbg_PreOC with (nolock)
				where pre_oc_id =  ?";
	my $sth = $db->prepare($sql2);
		$sth->execute($pre_oc_ID);
	my	$dt = $sth->fetchrow_hashref();
	$sth->finish();

	my $year = $dt->{year};
	my $company_name = $dt->{company_name};
	my $first_name = $dt->{first_name};
	my $last_name = $dt->{last_name};
	my $tofield = $dt->{tofield};
	my $source_id = $dt->{source_id};
	my $btn1 = $dt->{btn1};
	my $btn2 = $dt->{btn2};
	my $btn3 = $dt->{btn3};
	my $order_number = $dt->{order_number};
	my $install_date = $dt->{install_date};
	my $pnote= $dt->{pnote};
	my $emplid = $dt->{emplid};
	my $legacy_clause = " prod.is_LCTL = 1";
	if ($dt->{legacy} == 1) { $legacy_clause = " prod.is_LQ = 1"; 	}

	my $sql3 = "";
	if ($source_id == 2) {
		$sql3 = " select 2 as source_id, SAP_ID as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail , 
					case when isnull(work_phone,'') = '' then ''
						when isnull(work_phone,'') = '0000000000' then ''
						else SUBSTRING ( work_phone ,1 , 3 )+'-'+SUBSTRING ( work_phone ,4 , 3 )+'-'+SUBSTRING ( work_phone ,7 , 4 )end  as work_phone
				from qwesthr with (nolock) where convert( int, emplid ) = ?";
	}
	else {
			$sql3 = " select 0 as source_id, cuid as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail,
						'' as work_phone
						from ctl_floaters with (nolock) where floater_id = ? ";
	}
	 $sth = $db->prepare($sql3);
	 $sth->execute($emplid);
	my	$emp_dt = $sth->fetchrow_hashref();
	$sth->finish();

	my $emp_email = $emp_dt->{emp_email};
	my $SAP_ID = $emp_dt->{SAP_ID};
	my $wk_phone = $emp_dt->{work_phone};
	if ($wk_phone eq "") {
		$wk_phone = $emp_email;
	}

	$string .= qq[ <table width="90%" border="0" class="form-table" align="right">
						<tr> <td colspan="2"> <p>Click Review to see saved changes.</p></td></tr>
						<tr>
							<td width="38%" align="right"><p>
								<label for="company-name"><span class="orange">*</span>Company Name</label></p></td>
							<td width="62%"><input name="company_name" id="company_name" type="text" tabindex="1" class="text-field" value="$company_name"/>
								<label><span id='req_company_name'></span></label></td>
						</tr>
						<tr>
							<td align="right"><p>
								<label for="first-name"><span class="orange">*</span>Recipient First Name</label></p></td>
							<td><input name="first_name" id="first_name" type="text" tabindex="2" class="text-field" value="$first_name"/>
								<label><span id='req_first_name'></span></label></td>
						</tr>
						<tr>
							<td align="right"><p>
								<label for="last-name"><span class="orange">*</span>Recipient Last Name</label></p></td>
							<td><input name="last_name" id="last_name" type="text" tabindex="3" class="text-field" value="$last_name"/>
								<label><span id='req_last_name'></span></label></td>
						</tr>
						<tr>
							<td align="right"><p>
								<label for="email"><span class="orange">*</span>Recipient Email Address</label></p></td>
							<td><input name="email" id="email" type="text" tabindex="4" class="text-field" value="$tofield"/>
								<label><span id='req_email'></span></label></td>
						</tr>
						<tr>
							<td width="38%" align="right"><p>
								<label for="btn"><span class="orange">*</span>Billing Telephone Number </label></p></td>
							<td width="62%">
								<input name="btn1" id="btn1" type="text" tabindex="1" class="btn-field" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" value="$btn1"/>&nbsp;
								<input name="btn2" id="btn2" type="text" tabindex="1" class="btn-field" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" value="$btn2"/>&nbsp;
								<input name="btn3" id="btn3" type="text" tabindex="1" class="btn3-field" maxlength="4" value="$btn3"/>
								<label><span id='req_btn'></span></label></td>
						</tr>
						<tr>
							<td width="38%" align="right"><p>
								<label for="order_number"><span class="orange">*</span>Order Number</label></p></td>
							<td width="62%"><input name="order_number" id="order_number" type="text" tabindex="1" class="text-field" value="$order_number"/>
								<label><span id='req_order_number'></span></label></td>
						</tr>
						<tr>
							<td width="38%" align="right"><p>
								<label for="install_date"><span class="orange">*</span>Installation Date</label></p></td>
							<td width="62%"><input name="install_date" id="install_date" type="text" tabindex="1" class="text-field" value="$install_date" />
								(mm/dd/yy)
								<label><span id='req_install_date'></span></label></td>
						</tr> 
						<tr><td width="38%" align="right"><p>
								<label for="prods"><span class="orange">*</span>Products :</label></p></td>
									<td><small>selected products are checked</small><span id='req_prod'></span></td></tr>];

			my $checked="";
			my $entryID = 1;
			my $productID=0;
			$sql2 = "select prod.productID,  prod.description	,
					isnull((select tbl_id from ctl_sbg_OC_prod_interest oc_int with (nolock) 
							where oc_int.productId = prod.productID and oc_int.oc_id = ?),0) as tbl_id
					from ctl_sbgOrderConfirm_product prod with (nolock)	
					where  $legacy_clause
					order by prod.item_order ";

		my $sth3 = $myDB1->prepare($sql2);
		$sth3->execute($pre_oc_ID);
		while (my $dt = $sth3->fetchrow_hashref) {
				$checked = "";
				$productID = $dt->{productID};
				if ($dt->{tbl_id} > 0 ) { $checked = "checked"; 				}
					$string .= qq[<tr><td align="right"><p>
						<input name="productID" id="productID" value="$productID" type="checkbox" $checked></p></td><td>$dt->{description}</td></tr>];
				 $entryID++;
		}
		$sth->finish();

			
			$string .= qq[ <tr>
                    <td colspan="3"><small><em>personal note - up to 600 characters max.<br />
					<span id="charcount">0</span> characters entered.   |   <span id="remaining">600</span> characters remaining.</em></small></td>
                  </tr>
                  <tr>
                    <td colspan="3"><textarea name="noteOC" cols="" rows="10" class="text-box" id="noteOC"
					onkeyup="CheckFieldLength(noteOC, 'charcount', 'remaining', 600);" 
					onkeydown="CheckFieldLength(noteOC, 'charcount', 'remaining', 600);" 
					onmouseout="CheckFieldLength(noteOC, 'charcount', 'remaining', 600);" >$pnote</textarea>
                  <tr>
                    <td colspan="3" align="right"><input type="button" value="Spell Check" onclick="\$Spelling.SpellCheckInWindow('noteOC')" /></td>
                  </tr> 
									<tr>
                <td align="center" colspan="2">
						<input type="hidden" name="goWhere" value="1">
					<input name="review" type="" value="" class="button-review" onclick="getProdEmailConfirm();"/> 


				</td>
             </tr>
					</table>
];

			
#print "Content-type:text/html\n\n";print "outside".$main::cgi{getform};exit();
 # print "Content-type:text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{editPart} == 1  ) { # ContactInfo
if ($cgi->param('editPart') == 1) {
	my $prePropID = $cgi->param('preProposalID');#$main::cgi{preProposalID};
	my $source_id = $cgi->param('source_id');#$main::cgi{source_id};

	my $string = qq[ <table width="100%" border="0" class="form-table"> ];

	my $sql = "select first_name, last_name, company_name, tofield, RTRIM(personal_note) as personal_note, 
			createdby_emplid as emplid
			from ctl_sbg_PreProposal pre with (nolock) where pre_id = ?";
	my $sth = $db->prepare($sql);
	$sth->execute($prePropID);
	my $dt = $sth->fetchrow_hashref();
	$sth->finish();

	$string.= qq[


			<tr>
				<td width="25%"align="right">Company Name</td>
				<td width="75%"align="left">
					<input name="company_name" id="company_name" type="text" tabindex="1" class="text-field" value="$dt->{company_name}"/>
					<span id='req_company_name'></span>
				</td>
			</tr>
			<tr>
				<td width="25%"align="right">Recipient Email Address:</td>	
				<td width="75%" align="left"><input name="email" id="email" type="text" tabindex="4" class="text-field" value="$dt->{tofield}"/>
					<span id='req_email'></span>
				</td>
			</tr>
			<tr>
				<td width="25%"align="right">Recipient First Name:</td>
				<td width="75%" align="left"><input name="first_name" id="first_name" type="text" tabindex="2" class="text-field" value="$dt->{first_name}"/>
					<span id='req_first_name'></span> 
				</td>
			</tr>
			<tr>
				<td width="25%" align="right">Recipient Last Name:</td>
				<td  width="75%" align="left"> <input name="last_name" id="last_name" type="text" tabindex="2" class="text-field" value="$dt->{last_name}"/>
					<span id='req_last_name'></span> 
				</td>
			</tr>
			<tr> <td colspan="2" align="left">
				<table width="100%" border="0" class="form-table">

                  <tr> 
                    <td colspan="2">Personal Note:<br><small><em>up to 600 characters max.<br />
					<span id="charcount">0</span> characters entered.   |   <span id="remaining">600</span> characters remaining.</em></small></td>
                  </tr>
                  <tr>
                    <td colspan="3"><textarea name="edit_personal_note" cols="" rows="10" class="text-box" id="personal_note"
					onkeyup="CheckFieldLength(edit_personal_note, 'charcount', 'remaining', 600);" 
					onkeydown="CheckFieldLength(edit_personal_note, 'charcount', 'remaining', 600);" 
					onmouseout="CheckFieldLength(edit_personal_note, 'charcount', 'remaining', 600);" >$dt->{personal_note}</textarea>
				</td>
                  </tr>
                  <tr>
                    <td colspan="3" align="right"><input type="button" value="Spell Check" onclick="\$Spelling.SpellCheckInWindow('edit_personal_note')" /></td>
                  </tr>
                </table>
				</td>
			</tr>
			<tr>
                <td align="center" colspan="2"><small><em>Clicking Review will update Contact Information and display proposal</em</small>
				</td>
             </tr>
			<tr>
                <td align="center" colspan="2">
					<input name="review" type="" value="" class="button-review" onclick="editContactCheck();"/> 


				</td>
             </tr>
			</table>

		];


#print "Content-type:text/html\n\n";print "outside".$main::cgi{getform};exit();
 # print "Content-type:text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;

}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{editPart} == 2 ) { # Product Info
if ($cgi->param('editPart') == 2) {
	my $prePropID = $cgi->param('preProposalID');

	my $sql = "select language_id, legacy from ctl_sbg_PreProposal with (nolock) where pre_id = ?";
	my $sth = $db->prepare($sql);
	$sth->execute($prePropID);
	my $dt = $sth->fetchrow_hashref();
	$sth->finish();

	my $legacy = $dt->{legacy};
	my $legacy_clause = "and ISNULL(is_LCTL,0)= 1";
	if ($legacy == 1) {
		$legacy_clause = "and ISNULL(is_LQ,0)= 1";
	}
	my $string = "";#qq[<table width="100%" border="0" class="email-content" > ];
	my ($heading, $descr, $selection, $sub_selection, $close_div, $counter, $tab, $language_id, $hdr_id, %prod_dt);
	my ($productID, $called, $cnt, $nrc_name, $mrc_name, $term_name, $speed_name, $ship_name,$id, $qty_name,$reqd_note, $hide_show_div, $detaildiv);
	my ($hdr_sql,  $header_id,  $subdetaildiv, $termSpanName , $qtyclause, $termclause, $nrcclause ,$mrcclause, $shipclause, $speedclause );
	my ($req_qty,$req_term ,$req_nrc ,$req_mrc ,$req_ship ,$req_speed, $sth2, $data);

	$string .= qq[	<h3>Product Selection for current Proposal:</h3> ];

	$string .= showSelectedProducts($prePropID);


	#----------------------------------------------------
	$string .= qq[	<h3><input type="checkbox" name="needNewProd" id="neednewProd" value="yes" onclick="toggleVisibility('prodDiv');">
						New Product Selection <small class="orange"><em>must select one or more</em>
							<label><span id='req_prod'></span></label></small>
						</h3>
						<!--	start div for editprods	-->
							<div id="prodDiv" name="prodDiv" style="display: none;">
						];
	$hdr_sql = "select rtrim(description) as heading, rtrim(ISNULL(reqd_note,'')) as reqd_note , header_id
				from ctl_sbgProposal_header with (nolock) where is_active = 1 $legacy_clause order by hdr_order";

	$sth = $db->prepare($hdr_sql);
	$sth->execute();

	while (my $hdr_dt = $sth->fetchrow_hashref) {
		$heading = $hdr_dt->{heading};
		$reqd_note = $hdr_dt->{reqd_note};
		$header_id = $hdr_dt->{header_id};
		if ($reqd_note ne "") {
			$reqd_note = '<small><em>'.$reqd_note.'</em></small>';
		}
		#style="border-color:black;"
		$hide_show_div = 'hide_show_'.$counter;
			$string .= qq[  <table width="100%" border="0" class="email-content"> 
						<tr><td><h4>$heading  $reqd_note
						<small><a href="javascript:void(0)" onclick="toggleDiv('$hide_show_div',this);">Show Product List</a></small></h4></td></tr>
						</table>
						 <div id="$hide_show_div" style="display: none;">];

		$sql = "select productID, rtrim(prod_selection) as selection, RTRIM(description) as descr,
				ISNULL(prod_sub_selection,'') as sub_selection,
				isnull((select count(prod_sub_selection) from ctl_sbgProposal_product b with (nolock) where b.prod_selection = 
				ctl_sbgProposal_product.prod_selection and ISNULL(prod_sub_selection,'')<>''  $legacy_clause) ,0) as cnt,
					ISNULL(show_nrc,0) as show_nrc, ISNULL(show_mrc,0) as show_mrc,
				ISNULL(show_shipping,0) as show_shipping, ISNULL(show_term,0) as show_term, ISNULL(show_qty,0) as show_qty,isnull(show_speed,0) as show_speed,
				ISNULL(is_LCTL,0) as is_LCTL, ISNULL(is_LQ,0) as is_LQ,
				case when (ISNULL(show_nrc,0) =0 and ISNULL(show_mrc,0) =0 and
				ISNULL(show_speed,0) =0 and ISNULL(show_term,0) =0 and ISNULL(show_qty,0) =0 ) then 0 else 1 end as flag,
					rtrim(isnull(reqd_note,'')) as reqd_note
				from ctl_sbgProposal_product with (nolock) where is_active = 1  $legacy_clause
				and prod_heading = '$heading'
				order by item_order";
			
	#	$string .= ' 764 <pre>'.$sql.'</pre><br>';
					$string.= qq[ <table width="100%" border="0" class="email-content" >];
# prod selections
#onClick="showPromo($header_id,$productID, $main::session{session_id})"  was before changes
	$sth2 = $db->prepare($sql);
	$sth2->execute();

	while ( $data = $sth2->fetchrow_hashref) {
			$productID = $data->{productID};
			$cnt = $data->{cnt};
			$detaildiv = 'detaildiv_'.$productID;
			$subdetaildiv = 'subdetaildiv_'.$productID;
		$req_qty = "req_qty_".$productID;
		$req_term = "req_term_".$productID;
		$req_nrc = "req_nrc_".$productID;
		$req_mrc = "req_mrc_".$productID;
		$req_ship = "req_ship_".$productID;
		$req_speed = "req_speed_".$productID;
		( $qtyclause, $termclause, $nrcclause ,$mrcclause, $shipclause, $speedclause)=('','','','','','');

		if ($data->{show_qty} == 1) { $qtyclause = "<span id='".$req_qty."'></span>"; }
		if ($data->{show_term} == 1) { $termclause = "<span id='".$req_term."'></span>"; }
		if ($data->{show_nrc} == 1) { $nrcclause = "<span id='".$req_nrc."'></span>"; }
		if ($data->{show_mrc} == 1) { $mrcclause = "<span id='".$req_mrc."'></span>"; }
		if ($data->{show_shipping} == 1) { $shipclause = "<span id='".$req_ship."'></span>"; }
		if ($data->{show_speed} == 1) { $speedclause = "<span id='".$req_speed."'></span>"; }
				if ($selection ne $data->{selection}) {
			$string .= qq[<tr> <td>  ];
			if ($cnt == 0 ) {
				$string .= qq[ <input name="productID" id="$productID" type="checkbox" value="$productID" onClick="toggleVisibility('$detaildiv');"> ];
			}
			else {
				$string .= qq[ <input name="productID" id="$productID" type="checkbox" value="$productID" onClick="toggleVisibility('$subdetaildiv');"> ];
			}
		
			$string .= qq[$data->{selection} $qtyclause $termclause $nrcclause $mrcclause $shipclause $speedclause</td></tr>];

			if ( $cnt == 0 && $data->{flag} > 0) {
				$string .= qq[<tr><td><div id="$detaildiv" name="$detaildiv" style="display: none;">
										<table width="100%" border="2" class="email-content" > <tr>];
				$string .= printQtyBar ($productID, $tab, $myDB1);
					$string .= qq[</tr></table>
									</div><!-- for qtys	--></td></tr> ];
			}
			elsif  ($cnt > 0 && $selection ne $data->{selection})  {
					$string .= qq[<tr><td><!-- open sub div $subdetaildiv -->
									<div id="$subdetaildiv" name="$subdetaildiv" style="display: none;"> ];# at 253 should call get_sub_products 
					if ($data->{sub_selection} eq "Main Prod") {
						$string .= printQtyBar ($productID, $tab, $myDB1);
					}
					$string .= get_sub_products ($heading, $data->{selection}, $legacy, $language_id, $header_id, $myDB1, $myDB3);
					$string .= qq[<!-- close sub div $subdetaildiv --></div></td></tr>];
			}
		}
			$selection = $data->{selection};
			$counter++;

#close prod selections
		}
		$sth2->finish();

		$string .= qq[<tr><td><h4> $heading - Promotions  </h4></td></tr><tr><td>  ];
		$string .= getPromos ($heading,$header_id,$language_id,$legacy);
		#$string .= qq[ promo here ];
		$string .= qq[</td></tr></table></div>];
	}
	$sth->finish();
	$string .= qq[	              <table width="100%" border="0" class="form-table">
					<tr>
                <td align="center" colspan="2"><small><em>Clicking Review will update Product Information and display proposal</em</small>
				</td>
             </tr>
			<tr>
                <td align="center" colspan="2">
					<input name="review" type="" value="" class="button-review" onclick="editProductCheck();"/> 


				</td>
             </tr>
				</table>	</div><!--	end div for editprods	-->];

#print "Content-type:text/html\n\n";print "outside".$main::cgi{getform};exit();
 # print "Content-type:text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{editPart} == 3 ) { # Show Proposal
if ($cgi->param('editPart') == 3) { # Show Proposal
	my $prePropID = $cgi->param('preProposalID');

my ($proposal_body, $promo_disclaimer, $prod_disclaimer, $hdr_prod_disclaimer) = getProposalbody ($prePropID);
if ($promo_disclaimer ne "") {
	$promo_disclaimer = '<br><b>Promotion Disclaimers:</b><br>'.$promo_disclaimer;
}
if ($hdr_prod_disclaimer ne "") {
	$hdr_prod_disclaimer = '<br><b>Product Disclaimers:</b><br>'.$hdr_prod_disclaimer;
}
elsif ($prod_disclaimer ne "") {
	$prod_disclaimer = '<br><b>Product Disclaimers:</b><br>'.$prod_disclaimer;
}

=head
	if ($hdr_prod_disclaimer ne "") {
		$hdr_prod_disclaimer = '<tr><td>'. $hdr_prod_disclaimer.'</td></tr>';
	}
	if ($prod_disclaimer ne "") {
		$prod_disclaimer = '<tr><td>'. $prod_disclaimer.'</td></tr>';
	}
	if ($promo_disclaimer ne "") {
		$promo_disclaimer = '<tr><td>'. $promo_disclaimer.'</td></tr>';
	}
=cut

	my $sql2 = "select convert(varchar, date_created,101) as dt ,datepart(yyyy,getdate()) as year , first_name, last_name, rtrim(company_name) as company_name,
				tofield, personal_note, 
			createdby_emplid as emplid, source_id
			from ctl_sbg_PreProposal pre with (nolock) where pre_id = ?";
	my $sth = $db->prepare($sql2);
	$sth->execute($prePropID);
	my $dt = $sth->fetchrow_hashref();
	$sth->finish();

	my $year = $dt->{year};
	my $company_name = $dt->{company_name};
	my $first_name = $dt->{first_name};
	my $last_name = $dt->{last_name};
	my $tofield = $dt->{tofield};
	my $source_id = $dt->{source_id};
	my $emplid = $dt->{emplid};
	my $date = $dt->{dt};

	my $sql3 = "";
	if ($source_id == 2) {
		$sql3 = " select 2 as source_id, SAP_ID as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail , 
					case when isnull(work_phone,'') = '' then ''
						when isnull(work_phone,'') = '0000000000' then ''
						else SUBSTRING ( work_phone ,1 , 3 )+'-'+SUBSTRING ( work_phone ,4 , 3 )+'-'+SUBSTRING ( work_phone ,7 , 4 )end  as work_phone
				from qwesthr with (nolock) where convert( int, emplid ) = ?";
	}
	else {
			$sql3 = " select 0 as source_id, cuid as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail,
						'' as work_phone
						from ctl_floaters with (nolock) where floater_id = ?";
	}

	my $sth = $db->prepare($sql3);
	$sth->execute($emplid);
	my $emp_dt = $sth->fetchrow_hashref();
	$sth->finish();
	my $emp_email = $emp_dt->{emp_email};
	my $SAP_ID = $emp_dt->{SAP_ID};
	my $wk_phone = $emp_dt->{work_phone};
	if ($wk_phone eq "") {
		$wk_phone = $emp_email;
	}
	my $intro_body = getIntro($company_name);

	my $end_body = getEnd( $emp_dt->{empName}, $emp_dt->{work_phone});


my $generalTandC = '<br><b>Terms and Conditions '. $year.' </b>:';
$generalTandC .= getGeneralTandC();
	
	$generalTandC .= $year;
	$generalTandC .= " CenturyLink.  All Rights Reserved. ";


	#$end_body = $disclaimer .'<br><br>'. $end_body ;

#<tr> <td align="left" valign="top">$proposal_body</td></tr>
	my $string .= qq[ <table width="90%" border="0" class="form-table" align="right">
	<tr> <td align="left">$date</td> </tr>
	<tr> <td align="left"><b> $first_name $last_name </b></td> </tr>
	<tr> <td align="left"><b> $company_name  </b></td> </tr>
	<tr> <td align="left"><b>  $tofield </b></td> </tr>
	<tr> <td align="left">Dear<b> $first_name $last_name</b>,</td> </tr>
	<tr> <td align="left"> $intro_body </td> </tr> $proposal_body <tr> <td align="left"> $end_body </td></tr>
	<tr><td>$hdr_prod_disclaimer
	$prod_disclaimer
	$promo_disclaimer</td></tr>
	<tr><td>$generalTandC</td></tr>
</table>
	];

#print "Content-type:text/html\n\n";print "outside".$main::cgi{getform};exit();
 # print "Content-type:text/html\n\n";
  print $string;
   $db->disconnect();
  $db2->disconnect();
  $myDB1->disconnect();
  $myDB3->disconnect();

  exit;
}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
1;

