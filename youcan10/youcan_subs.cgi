#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw/ fatalsToBrowser /;
use HTML::Strip;
use CCICryptography;
use DBInterface;
use Try::Tiny;
use Date::Calc qw(Today Add_Delta_Days);

use CGI qw(:standard);

my $cgi = CGI->new();
print $cgi->header('text/html');

my $db  = DBInterface->new();

my $thisfile = "youcan_subs.cgi";


#------------------------------------------------------------------------------------------------------------------------------------------------------------
#if ($main::cgi{getform} == 1 && $main::cgi{lead_group} == 55) {  # 55 = Business
if ($cgi->param('getform') == 1 && $cgi->param('lead_group') == 55){
	my ($sql , %state);
#my $session_id= $main::session{session_id}||$cgi->param('session_id'); 
my $session_id=  $cgi->param('session_id'); 
my $program_id = 154;

=head
    <table width="100%" border="1" id="resform" cellspacing="0" cellpadding="0" class="referral-entry">
		 <tr><br><span id='req_medLg'></span><span id='req_medLg2'></span><span id='req_medLg3'></span>
               <td width="60%"><p><span class="blue">*</span>Commercial/Enterprise Business?</p></td>
               <td width="20%"><p><label><input type="radio" name="medLg" value="1" id="medLgBiz_yes"/>Yes</label></p></td>
               <td width="20%"><p><label><input type="radio" name="medLg" value="0" id="medLgBiz_no" checked/>No</label></p></td>
      </tr>
			<tr><td colspan="3"><p>
			<span style="font-family:Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;color:#0E82C6">
					Select &ldquo;Yes&rdquo; if the customer has an assigned Account Manager, is utilizing or is seeking complex business products (for example, CPE and data circuits). 
          A typical Commercial/Enterprise customer spends \$500 or more in monthly telecom expense.</span></p></td>
      </tr>
    </table>	

=cut
	my $string = qq[
    <table width="100%" border="1" id="resform" cellspacing="0" cellpadding="0" class="referral-entry">

			<tr>
        <td width="35%"><p class="alignright"><span class="blue">*</span>Business Name: </p></td>
				<td colspan="2"><label><input name="lead_company_name" type="text" size="30" /><br><span id='req_bizname'></span></label></td>
      </tr>
			<tr>
        <td width="35%"><p class="alignright"><span class="blue">*</span>State: </p></td>
				<td colspan="2">
							<select name="lead_state" size="1" onchange="javascript:checkLegacy(this.value , $session_id);">
							<option value="" selected="selected">-Select State-</option>
					];

			$sql = "select distinct state, abbreviation, route_var1 from lp_states with (nolock) where program_id = ? and isnull(route_var1,0)<> 0 order by state";
		my $success = eval {
		my $sth = $db->prepare($sql) or die $db->errstr;
			$sth->{PrintError} = 0;
			$sth->execute($program_id)  or die $sth->errstr;

		while(my $state = $sth->fetchrow_hashref){
				$string.= qq[<option name='lead_state' value='$state->{abbreviation}' >$state->{state}</option>];
		}
		$sth->finish();	

	};
	unless($success) {
		DBInterface::writelog('youcan10',"$thisfile", $@ );
	}

	$string.= qq[
					</select><span id='req_state'></span><input type="hidden" name="ctl_radio_notOn" value="1">

				</td>
            </tr>
			<tr><td colspan="3"><div id="showLegacyRadio" name="showLegacyRadio"><!--	-->  </div></td></tr>
	<!--		</table>	-->
	<!--		<table width="100%" border="1" cellspacing="0" cellpadding="0" class="referral-entry">		-->
			<tr>
				<td width="60%"><p class="alignright"><span class="blue">*</span>Customer Name: </p></td>
				<td colspan="2"><p><label><input name="lead_name" type="text" size="30" /><br><span id='req_leadname'></span></label></p></td>
            </tr>
            <tr>
                <td><p class="alignright"><span class="blue">*</span>Main Phone: </p></td>
                <td colspan="2"><label><input name="main_btn1" type="text" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" />-
				<input name="main_btn2" type="text" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" />-
				<input name="main_btn3" type="text" size="4" maxlength="4" /><br><span id='req_phone'></span></label>
				</td>
            </tr>
			<tr>
                <td><p class="alignright"><span class="blue">*</span>Address: </p></td>
				<td colspan="2"><label><input name="lead_address" type="text" size="30" /><br><span id='req_addr'></span></label>
				</td>
            </tr>
			<tr>
                <td><p class="alignright"><span class="blue">*</span>City: </p></td>
				<td colspan="2"><label><input name="lead_city" type="text" size="30" /><br><span id='req_city'></span></label>
				</td>
             </tr>
			 <tr>
                <td><p class="alignright"><span class="blue">*</span>ZIP: </p></td>
				<td colspan="2"><label><input name="lead_zip" type="text" size="30" maxlength="10"/><br><span id='req_zip'></span></label>
				</td>
             </tr>
             <tr>
                <td><p class="alignright">Customer Email: </p></td>
				<td colspan="2"><label><input name="lead_email" id="lead_email" type="text" size="30"/><br></label>
				</td>
             </tr>
             <tr>
                <td><p class="alignright">Alternate Phone: </p></td>
                <td colspan="2"><label><input name="lead_phone1" type="text" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" />-
				<input name="lead_phone2" type="text" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" />-
				<input name="lead_phone3" type="text" size="4" maxlength="4" /></label></td>
             </tr>
             <tr>
                <td><p class="alignright">Best Time to Call: </p></td>
                <td><p><label><input type="radio" name="call_time" value="AM" id="call-time_0" />AM</label></p></td>
                <td><p><label><input type="radio" name="call_time" value="PM" id="call-time_1" />PM</label></p></td>
             </tr>
             <tr>
                <td><p class="alignright">Customer&rsquo;s Language: </p></td>
                <td><p><label><input type="radio" name="language" value="1" id="language_0" />English</label></p></td>
                <td><p><label><input type="radio" name="language" value="2" id="language_1" />Spanish</label></p></td>
             </tr>
            <tr>
               <td width="60%" class="alignright"><p><span class="blue">*</span>Customer has given permission to call?</p></td>
               <td width="14%"><p><label><input type="radio" name="contact_permission" value="1" id="permission-type_0"/>Yes</label></p></td>
               <td width="25%"><p><label><input type="radio" name="contact_permission" value="2" id="permission-type_1"/>No</label></p></td>
            </tr>
		</table>
<!--	-->


		<hr class="brk-grey" />
    <table width="100%" border="1" id="resform" cellspacing="0" cellpadding="0" class="referral-entry">
			<tr>
               <td colspan="3"><p><span class="blue">*</span>These questions help YOUCAN find the correct salesperson for your lead.</p></td>
            </tr>
<!-- CL-1687 start	-->
			<tr>
			   <td width="60%"><p class="alignright"><span class="blue">*</span>Is this a government account?<br>
																				<small>(includes city, county, state or federal)</small></p></td>
				<td width="14%"><p><label><input type="radio" name="govt_acct" value="yes" />Yes</label></p></td>
               <td width="25%"><p><label><input type="radio" name="govt_acct" value="no" checked="checked"/>No</label></p></td>
			</tr>
			<tr>
			   <td width="60%"><p class="alignright"><span class="blue">*</span>Is this an educational account?<br>
																				<small>(includes public or private schools, all levels)</small></p></td>
				<td width="14%"><p><label><input type="radio" name="school_acct" value="yes" />Yes</label></p></td>
               <td width="25%"><p><label><input type="radio" name="school_acct" value="no"checked="checked"/>No</label></p></td>
			</tr>
<!-- CL-1687 end	-->
			<tr>
			   <td width="55%"><p class="alignright"><span class="blue">*</span>How many locations does this business have? </p></td>
				<td colspan="2">
							<select name="numOfLoc" size="1" required>
							<option value="" selected="selected">-Select -</option>
							<option name='numOfLoc' value='1 or 2' >1 or 2</option>
							<option name='numOfLoc' value='3 or more' >3 or more</option>
							<option name='numOfLoc' value='donotknow' >I don&rsquo;t know</option>
							</select><span id='req_numOfLoc'></span>
				</td>
			</tr>
			<tr>
			   <td><p class="alignright"><span class="blue">*</span>How many employees? </p></td>
				<td colspan="2"><p><label>
							<select name="numOfEmp" size="1" required>
							<option value="" selected="selected">-Select -</option>
							<option name='numOfEmp' value='1-99' >1 &ndash; 99</option>
							<option name='numOfEmp' value='100 or more' >100 or more</option>
							<option name='numOfEmp' value='donotknow' >I don&rsquo;t know</option>
							</select><span id='req_numOfEmp'></span></label></p>
				</td>
			</tr>
			<tr>
			   <td width="35%"><p class="alignright">Billing Account Number or Billing Account ID<br>
									<small>Enter the customer&rsquo;s BAN or Account ID if you know it. Leave it blank if you do not.</small></p></td>
				<td colspan="2"><input name="ban" type="text" size="30" maxlength="15" />
				</td>
			</tr>
		</table>
        <hr class="brk-grey" />
			<table width="100%" border="0" cellspacing="0" cellpadding="0" class="referral-entry">
            <tr>
               <td><p><span class="blue">*</span>What product(s) did you discuss with the customer? <br>(check all that apply):
					<br><span style="font-family:Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;color:#0E82C6">At least one product is required.</span>
					<br><span id='req_prod'></span></p></td> 
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="Voice" />Voice</label>
				<span style="font-family:Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;color:#0E82C6">
					Includes lines, bundles, features, long distance, wire maintenance, temporary service</span></p>
			</td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="High Speed Internet" />High Speed Internet</label>
					<span style="font-family:Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;color:#0E82C6">
					New HSI and Upgrades</span></p>
			</td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="Video" />Video</label>
				<span style="font-family:Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;color:#0E82C6">
					Prism TV, DirecTV</span></p>
			</td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="Cloud Services" />Cloud Services</label>
				<span style="font-family:Helvetica, Arial, sans-serif;font-size:10px;line-height:12px;color:#0E82C6">
					Web hosting, Internet Security, Remote IT support</span></p>
			</td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="Managed Office" />Managed Office</label></p>
			</td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="VoIP" />VoIP</label></p>
			</td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="Voice or Data Equipment" />Voice or Data Equipment</label></p>
			</td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="Other" />Other (Explain below)</label></p>
			</td>
            </tr>
	</table>
			        <hr class="brk-grey" />
        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="referral-entry">
            <tr>
               <td colspan="3"><span id='req_permission'></span><br><p>Notes or Comments:</p></td>
            </tr>
            <tr>
               <td colspan="3"><textarea class="text-area" name="comment" cols="" rows="5"></textarea></td>
            </tr>
            <tr>
               <td colspan="3" class="aligncenter"><input name="submitbtn" type="button" class="but-submit-referral" value="" onClick="checkformBiz();"/></td>
			   
            </tr>
        </table>

		];
  #print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
  print $string;
  $db->disconnect();
  #$db2->Close();
  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#if ($main::cgi{getform} == 1 && $main::cgi{lead_group} == 56) { # 56 = Residential
if ($cgi->param('getform') == 1 && $cgi->param('lead_group') == 56){
	my ($sql , %state);
#my $session_id= $main::session{session_id}||$cgi->param('session_id'); 
my $session_id=  $cgi->param('session_id'); 
my $program_id = 154;

	my $string = qq[
		<table width="100%" border="0" id="bizform" >
			<tr>
				
				<td width="35%"><p class="alignright"><span class="blue">*</span>Customer Name: </p></td>
				<td colspan="2"><label><input name="lead_name" type="text" size="30" /><br><span id='req_leadname'></span></label></td>
            </tr>
			<tr>
                <td width="35%"><p class="alignright"><span class="blue">*</span>State: </p></td>
				<td colspan="2"><input type="hidden" name="ctl_radio_notOn" value="1">
							<select name="lead_state" size="1" onchange="javascript:checkLegacy(this.value , $session_id);">
							<option value="" selected="selected">-Select State-</option>
					];


			$sql = "select distinct state, abbreviation, route_var1 from lp_states with (nolock) where program_id = ? and isnull(route_var1,0)<> 0 order by state";
		my $success = eval {
		my $sth = $db->prepare($sql) or die $db->errstr;
			$sth->{PrintError} = 0;
			$sth->execute($program_id)  or die $sth->errstr;

		while(my $state = $sth->fetchrow_hashref){
				$string.= qq[<option name='lead_state' value='$state->{abbreviation}' >$state->{state}</option>];
		}
		$sth->finish();	

	};
	unless($success) {
		DBInterface::writelog('youcan10',"$thisfile", $@ );
	}

	$string.= qq[
					</select><span id='req_state'></span>
				</td>
            </tr>
			<tr><td colspan="3"><div id="showLegacyRadio" name="showLegacyRadio"><!--	-->  </div></td></tr>
			</table>
			<table width="100%" border="0" cellspacing="0" cellpadding="0" class="referral-entry">
            <tr>
                <td><p class="alignright"><span class="blue">*</span>Main Phone: </p></td>
                <td colspan="2"><label><input name="main_btn1" type="text" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" />-
				<input name="main_btn2" type="text" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" />-
				<input name="main_btn3" type="text" size="4" maxlength="4" /><br><span id='req_phone'></span></label>
				</td>
             </tr>
             <tr>
                <td><p class="alignright">Alternate Phone: </p></td>
                <td colspan="2"><label><input name="lead_phone1" type="text" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" />-
				<input name="lead_phone2" type="text" onKeyUp="return autoTab(this, 3, event);"  size="3" maxlength="3" />-
				<input name="lead_phone3" type="text" size="4" maxlength="4" /></label></td>
             </tr>
             <tr>
                <td><p class="alignright">Best Time to Call: </p></td>
                <td><p><label><input type="radio" name="call_time" value="AM" id="call-time_0" />AM</label></p></td>
                <td><p><label><input type="radio" name="call_time" value="PM" id="call-time_1" />PM</label></p></td>
             </tr>
             <tr>
                <td><p class="alignright">Customer's Language: </p></td>
                <td><p><label><input type="radio" name="language" value="1" id="language_0" />English</label></p></td>
                <td><p><label><input type="radio" name="language" value="2" id="language_1" />Spanish</label></p></td>
             </tr>
			</table>
			<hr class="brk-grey" />
			<table width="100%" border="0" cellspacing="0" cellpadding="0" class="referral-entry">
            <tr>
               <td><p><span class="blue">*</span>Product of Interest (check all that apply):<span id='req_prod'></span></p></td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="High Speed Internet" />New High Speed Internet</label></p></td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="High-Speed Internet Speed Upgrade" />High-Speed Internet Speed Upgrade</label></p></td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="New Voice Line/Features/Long Distance" />New Voice Line/Features/Long Distance</label></p></td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="Upgrade Voice Features" />Upgrade Voice Features</label></p></td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="PRISM TV or DirecTV" />PRISM TV or DirecTV</label></p></td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="PRISM TV Upgrade" />PRISM TV Upgrade</label></p></td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="PRISM Stream" />PRISM Stream</label></p></td>
            </tr>
			<tr>
               <td><p><label><input type="checkbox" name="product" value="Smart Home Security" />Smart Home Security</label></p></td>
            </tr>
		</table>
        <hr class="brk-grey" />
        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="referral-entry">
            <tr>
               <td width="61%"><p><span class="blue">*</span>Customer has given permission to call?</p></td>
               <td width="14%"><p><label><input type="radio" name="contact_permission" value="1" id="permission-type_0"/>Yes</label></p></td>
               <td width="25%"><p><label><input type="radio" name="contact_permission" value="2" id="permission-type_1"/>No</label></p></td>
            </tr>
            <tr>
               <td colspan="3"><span id='req_permission'></span><br><p>Notes or Comments:</p></td>
            </tr>
            <tr>
               <td colspan="3"><textarea class="text-area" name="comment" cols="" rows="5"></textarea></td>
            </tr>
            <tr>
               <td colspan="3" class="aligncenter"><input name="submitbtn" type="button" class="but-submit-referral" value="" onClick="checkformRes();"/></td>
			 
            </tr>
        </table>
		];
  #print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";

	print $string;
  $db->disconnect();
  #$db2->Close();
  exit;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
if ($cgi->param('getLegacy') == 1) { 
	my $st = $cgi->param('val');
	my $program_id = 154;
	my $string = '';
	my $sql = "select isnull(route_var1,0) as route_var1 from lp_states with (nolock) where program_id = ? and abbreviation = ?";
	my ($sth, $state);
#############
try {
$sth = $db->prepare($sql);
$sth->execute($program_id , $st) or die $sth->errstr;
$state = $sth->fetchrow_hashref();
$sth->finish();
}
catch {
	DBInterface::writelog('youcan10',"$thisfile", $_ );
};
##############

	
 
	my $legacy = $state->{route_var1};

		if ($legacy != 1 && $legacy != 2) {
			$string .= qq[	<hr class="brk-grey" />
						<table width="100%" border="0" cellspacing="0" cellpadding="0" class="referral-entry">
						<tr>
							<td>
						<p><input type="hidden" name="ctl_radio" value="1"><input type="radio" name="ctl_legacy_radio" value="1" /><label>Customer&rsquo;s address is serviced by Legacy Qwest/CRIS markets.</label></p></td>
						</tr>
						<tr>
							<td><p><input type="radio" name="ctl_legacy_radio" value="2" /><label>Customer&rsquo;s address is serviced by Legacy CenturyLink/Ensemble markets</label></p></td>
						</tr><br><span id='req_legacy'></span>
						</table>
						<hr class="brk-grey" />
				];	
		}
		else {
			$string .= qq[<input type="hidden" name="ctl_radio" value="0"><input type="hidden" name="ctl_legacy" value="$legacy"><span id='req_legacy'></span>];

		}


  #print "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
	print $string;
  $db->disconnect();
  #$db2->Close();
  exit;

}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub submitLead {
my ($myDB) = @_;

my $hs = HTML::Strip->new();

my ($message);
my $cci_id = EscQuote($cgi->param('cci_id'));
my ($session_id,$emplid) = CCICryptography::getEmpid($cci_id); 
	my $cuid = $cgi->param('userid');
	#my $emplid = $cgi->param('emplid');

    my $lead_name = EscQuote($hs->parse( $cgi->param('lead_name') ));
	my $lead_company_name = EscQuote($hs->parse( $cgi->param('lead_company_name') ));
 	my $lead_address = EscQuote($hs->parse( $cgi->param('lead_address') ));
 	my $lead_city = EscQuote($hs->parse( $cgi->param('lead_city') ));
 	my $lead_state = EscQuote($hs->parse( $cgi->param('lead_state') ));
	my $lead_zip = EscQuote($hs->parse( $cgi->param('lead_zip') ));
 	my $lead_email = EscQuote($hs->parse( $cgi->param('lead_email') ));
 	my $main_btn = EscQuote($hs->parse( $cgi->param('main_btn1') )).EscQuote($hs->parse( $cgi->param('main_btn2') )).EscQuote($hs->parse( $cgi->param('main_btn3') ));
	my $lead_phone = EscQuote($hs->parse( $cgi->param('lead_phone1') )).EscQuote($hs->parse( $cgi->param('lead_phone2') )).EscQuote($hs->parse( $cgi->param('lead_phone3') ));
    my $BAN = EscQuote($hs->parse( $cgi->param('ban') ));
    my $best_time = EscQuote($hs->parse( $cgi->param('call_time') ));
    my $contact_permission = EscQuote($hs->parse( $cgi->param('contact_permission') ));
    my $lead_group = EscQuote($hs->parse( $cgi->param('cust_type') ));
    my $cust_type = $lead_group == 55 ? "Business":"Residential";


    my $referral_source = 'centurylinkyoucan.com';
    my ($validbtn, $duplicate_lead) = check_mainbtn($main_btn, $myDB );
    my $comment = EscQuote($hs->parse( $cgi->param('comment') ));
    my $language_id = $cgi->param('language')||1;
	my $agency_name = EscQuote($main::session{name});
	my $ctl_legacy ;
	my $govt_acct = $cgi->param('govt_acct')||'no';
	my $school_acct = $cgi->param('school_acct')||'no';
	my $numOfLoc = EscQuote($cgi->param('numOfLoc'));
	my $numOfEmp = EscQuote($cgi->param('numOfEmp'));
	my $ctl_radio =  $cgi->param('ctl_radio') ||0;
	my @pl = $cgi->param('product');
	my $prod_list = '';
	my $isCommEnt = 0;

 	$hs->eof;
	#print "432 isCommEnt = $isCommEnt <br>";
	my ($lp_note, $sql,$ast_note,$medLg) = ("","","","");

	if ($ctl_radio == 0) {
		$ctl_legacy =  $cgi->param('ctl_legacy');
	}
	else {
		$ctl_legacy =  $cgi->param('ctl_legacy_radio');
	}

    if ( $validbtn == 0 ) {#cannot submit another lead on an existing open btn
      $message = "
      <span class='REDcopy'>Error Report</span> <p>

      A referral ($duplicate_lead) on this Billing Telephone Number ($main_btn) has already been placed and is still in an open status.
      Duplicate referrals cannot be placed until all open referrals for this number are closed.
      If you have any questions, please call 1-866-8YOUCAN";

    }else{ #good btn, add lead
	  # If Biz chk for Comm/Ent or AST2
      # ------------------------------------------------------------

      # products
	  my $prism_stream_flag = 0;
			foreach my $pid (@pl) {
				if ($pid eq "Cloud Services" || $pid eq "Managed Office" || $pid eq "VoIP" || $pid eq "Voice or Data Equipment") {
					$isCommEnt++;

				}
				if ( $pid eq "PRISM Stream") { $prism_stream_flag++;				}
			#	print "460 pid = $pid  isCommEnt = $isCommEnt <br>";
				if ($prod_list eq "") {
					$prod_list .= $pid ;
				}
				else {
					$prod_list .=  ', ' . $pid;
				}
			}
			$prod_list = 'Products interested:  '.$prod_list;


      # ------------------------------------------------------------------
      # primary lead body, insert
		 $prod_list = EscQuote($prod_list);
		if ($lead_group == 55) {
		  $ast_note = "Number of locations: ";
		  if ($numOfLoc eq "donotknow") { $ast_note .= "Do not know. ";  }
		  else { $ast_note .= $numOfLoc; }
		  $ast_note .= chr(13).chr(10)."Number of Employees: ";
		  if ($numOfEmp eq "donotknow" ) { $ast_note .= "Do not know. "; }
		  else { $ast_note .= $numOfEmp; }
		}
#print "483 ast_note = $ast_note <br>";
		 $lp_note = ": $agency_name".chr(13).chr(10).$comment.chr(13).chr(10)."----------".chr(13).chr(10).$prod_list;
		 if ($ast_note ne "") {
			 $lp_note .= chr(13).chr(10)."----------".chr(13).chr(10).$ast_note;
		 }
		 if ($BAN ne "") {
			 $lp_note .= chr(13).chr(10)."----------".chr(13).chr(10)."BAN : ".$BAN;
		 }
		 if ($school_acct eq "yes") {
			 $lp_note .= chr(13).chr(10)."----------".chr(13).chr(10)."School Account";
		 }
		 if ($govt_acct eq "yes") {
			 $lp_note .= chr(13).chr(10)."----------".chr(13).chr(10)."Government Account";
		 }
      my $sql = "insert into lp_lead (created_date, agency_id, lead_name, lead_company_name,lead_address, 
					lead_city,lead_state,lead_zip,lead_email, lead_phone, main_btn, 
					client_id, program_id, fund_id, language_id, warm_xfer, 
					contact_permission, lead_group, source_id, lp_region_id, original_note, 
					lp_notes)
                values (getdate(), ?, ?, ?,?, 
					?,?,?,?,?, ?, 
					50, 154, 511,?, 0, 
					?,? , ?, ?,
				convert(varchar,getdate())+'$lp_note', convert(varchar,getdate())+'$lp_note')";
					my ($data, $alt_email, $sth);
##############
			try {
				$sth = $myDB->prepare($sql);
				$sth->execute($emplid, $lead_name , $lead_company_name,$lead_address, $lead_city, $lead_state, $lead_zip, $lead_email, $lead_phone, $main_btn , $language_id, $contact_permission, $lead_group, 2,5  ) or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############

		my $lead_id = $data->{lp_lead_id};

            # prep fields for opts table
	    # adding check to see if user has entered alternate email
	    my $alt_exists = "select 0 as ecnt UNION
				select count(emplid) as ecnt from
				qwesthr_my with (nolock) where emplid = ?
				and isnull(email, '') <> ''
				order by 1 desc  ";
##############
			try {
				$sth = $myDB->prepare($alt_exists);
				$sth->execute($emplid ) or die $sth->errstr;
				$alt_email = $sth->fetchrow_hashref();
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
			
            my $found_email = $alt_email->{ecnt};
            my $notify_email = "select email from qwesthr with (nolock) where emplid = ?";
	    if ($found_email == 1) {
             $notify_email = "select email from qwesthr_my with (nolock) where emplid = ?";
	    }
 
##############
			try {
				$sth = $myDB->prepare($notify_email);
				$sth->execute($emplid ) or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
			
             $notify_email = EscQuote($data->{email});

            $sql = "insert into lkup_qwest_opts (lp_lead_id, mobile_no, cust_type, best_contact_time, best_contact_date,
                    lead_source, local_service, vccustom1, server_name, sales_center, vccustom2, intdonatecharity, charity_id,
                    referral_source, legacy)
                    values(?, '', ?, ?, '',  '', '', ?, 'centurylinkyoucan.com','General Referral','',
                    0, 0, ?, ? )";
##############
			try {
				$sth = $myDB->prepare($sql);
				$sth->execute($lead_id,$cust_type, $best_time,$notify_email, $referral_source, $ctl_legacy    ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
			
	    # -----------------------------------------------------------
	    # Michael whiteman to be emailed if lead by a dir or VP
    	    my ( $ccimail, $body, $to, $bcc,$cc, $subject);

			my $chk_dir = "exec sp_CTL_VIP_Alert ? ";
##############
			try {
				$sth = $myDB->prepare($chk_dir);
				$sth->execute($emplid) or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
             my $sp_msg = $chk_dir.$emplid.'<br>';
	    if ($data->{id} > 0 ){
			$to = "KRISTIE.VANENGELEN\@CENTURYLINK.COM";#"Michael.Whiteman\@centurylink.com";
			$cc = "Tami.Cordova\@CenturyLink.com";
			$subject = 'YOUCAN VIP Referral Alert: Lead '.$lead_id;
    	    $bcc = '';#'archanak@ccionline.biz';
    	    $body = " Lead number: ".$lead_id."\n Customer Type: ".$cust_type."\n Created for CUID: "; 
			$body .= $data->{cuid}."\n SAP ID: ".$data->{sap_id}. "\n Name: ".$data->{emp_name}." \n Job Title: ".$data->{job_title};
			$body .= " \n Website: centurylinkyoucan.com ";
			
			$ccimail = "insert into ccimail
			(client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) values
			(?, ?, ? , ?, ?, '',  'do_not_reply\@ccionline.biz', ?, ? ) ";
			$sp_msg .= $ccimail;

##############
			try {
				$sth = $myDB->prepare($ccimail);
				$sth->execute(50, 154, $lead_id, $to,$cc, $subject, $body ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
	    }
	    else { $body = ''; }
	    
	    $chk_dir = "select cuid, sap_id, lead_name, main_btn , convert(varchar,created_date,101) as ctdt
					from lp_lead with (nolock) 
					inner join qwesthr with (nolock) on agency_id = emplid
					where lp_lead_id = ?";
##############
			try {
				$sth = $myDB->prepare($chk_dir);
				$sth->execute($lead_id) or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
           
		if ($prism_stream_flag > 0 && $lead_group == 56 && $lead_state eq "NV" ) {

			$to = 'Tami.Cordova@CenturyLink.com';
			$subject = 'YOUCAN Prism Stream: Lead '.$lead_id;
    		$bcc = 'CTLReports@channelmanagement.com';#'archanak@ccionline.biz';
    	    $body = " Lead number: ".$lead_id."\n Customer Type: ".$cust_type."\n Lead Name: ".$data->{lead_name}."\nCreated for CUID: ";
			$body .= $data->{cuid}. "\n SAP ID : ".$data->{sap_id}."\n Main BTN: ".$data->{main_btn}." \n Created Date: ".$data->{ctdt};
			$body .= " \n Website: YC Employee Site ";
			$ccimail = "insert into ccimail (client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) 
						values (?, ?, ? , ?, '', ?,  'do_not_reply\@ccionline.biz', ?, ? ) ";
##############
			try {
				$sth = $myDB->prepare($ccimail);
				$sth->execute(50, 154, $lead_id, $to, $bcc, $subject,$body ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############

		}
            # ------------------------------------------------------------
            # history tag
            $sql = "insert into lp_lead_history (lp_lead_id, action, staff_id, history_date, source_id, user_ip)
                    values ( ?, 'Referral created:  No Referral Type.', ?, getdate(), ?, ?)";
##############
			try {
				$sth = $myDB->prepare($sql);
				$sth->execute($lead_id, $emplid, 2, $ENV{REMOTE_HOST}) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############


            # ------------------------------------------------------------
			# figure out what lead
	#	print "555 isCommEnt = $isCommEnt , isAST2_prod = $isAST2_prod , \$numOfLoc = $numOfLoc , \$numOfEmp = $numOfEmp , \$ctl_legacy = $ctl_legacy , \$isAST_other = $isAST_other<br>";
	if ($numOfLoc eq "3 or more" || $numOfEmp eq "100 or more" || $govt_acct eq "yes" || $school_acct eq "yes") {
		$isCommEnt++;;
		$medLg = "Med-Lg";
		#print "582 isCommEnt = $isCommEnt  <br>";
	}
	#elsif ($ctl_legacy == 1 && $isAST2_prod > 0) {
	#	$isCommEnt = 1;
	#	$medLg = "Med-Lg";
	#	print "565 isCommEnt = $isCommEnt , isAST2_prod = $isAST2_prod , \$isAST_other = $isAST_other<br>";
	#}
	#	print "567 isCommEnt = $isCommEnt , isAST2_prod = $isAST2_prod , \$isAST_other = $isAST_other <br>";

            #  get isr id
              #  my $isrsql = get_routing_sql( $lead_id, $isCommEnt, $isAST_other ,$myDB);
                my $isrsql = get_routing_sql("$lead_id", "$isCommEnt", $myDB);
	#print "594  isCommEnt = $isCommEnt just before routing <br>";
		
##############
			try {
				$sth = $myDB->prepare($isrsql);
				$sth->execute() or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############

              
                my $new_isr_id = $data->{isr_id};
                my $lp_region_id = $data->{lp_region_id}||5;
                $sql = "update lp_lead set lp_region_id = ?, lp_isr_id = ?
                        where lp_lead_id = ?";
##############
			try {
				$sth = $myDB->prepare($sql);
				$sth->execute($lp_region_id, $new_isr_id,$lead_id ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
 				
                
		
		            # ------------------------------------------------------------
			#print " 587 lead_group = $lead_group , isCommEnt=  $isCommEnt , isAST_other = $isAST_other <br>";
			if ($lead_group == 55 ) {
				$sql = "insert into lkup_qwest_sfdc_opts ( lp_lead_id, insert_date,sfdc_lead, last_update, ast_lead)
						values ('$lead_id', getdate(), $isCommEnt, getdate() ,0)";
			}
			else {
				$sql = "insert into lkup_qwest_sfdc_opts ( lp_lead_id, insert_date,sfdc_lead, last_update, ast_lead)
				values ('$lead_id', getdate(), -1, getdate(),0 )";
			}
##############
			try {
				$sth = $myDB->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
 				if ($lead_group == 55 ) {
					$sql = "update lkup_qwest_opts set cust_budget = '$medLg' where lp_lead_id = $lead_id";
					
##############
			try {
				$sth = $myDB->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
				}
		#	print "601 $sql <br>";
                $message = "
                Thank you for submitting your Referral.  Your reference number is $lead_id.
                If you have any questions, please call 1-866-8YOUCAN.<hr class='brk-grey' />";

    }#end of validated condition
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub CommaFormatted        #06/27/07 9:28:AM
 {
	my $delimiter = ','; # replace comma if desired
	my($n,$d) = split /\./,shift,2;
	my @a = ();
	while($n =~ /\d\d\d\d/)
	{
		$n =~ s/(\d\d\d)$//;
		unshift @a,$1;
	}
	unshift @a,$n;
	$n = join $delimiter,@a;
	$n = "$n\.$d" if $d =~ /\d/;
	return $n;
}   ##hold

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub check_mainbtn       #06/15/07 9:40:AM
 {
    my ($main_btn, $myDB) = @_;

    my $sql = "select top 1 lp_lead.lp_lead_id
               from lp_lead with(nolock), lkup_qwest_opts with(nolock)
                where lp_lead.lp_lead_id = lkup_qwest_opts.lp_lead_id
                    and replace(replace(replace(replace(replace(main_btn,   '(',''),' ',''),'-',''),')',''),'.','') =
                            replace(replace(replace(replace(replace('$main_btn', '(',''),' ',''),'-',''),')',''),'.','')
                    and isnull(lead_status_id,0) < 50
                    and lead_source <> 'Completed Work Order'
                    and client_id = 50";
	my ($sth, $data);
##############
			try {
				$sth = $myDB->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$data = $sth->fetchrow_hashref(); 
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
     
	my $dupe_lead_id = $data->{lp_lead_id} || 0;
    my $validated = $dupe_lead_id > 0 ? 0 : 1;

    return ($validated, $dupe_lead_id);
}   ##check_mainbtn

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub get_routing_sql{       #06/15/07 9:40:AM
    my ( $lead_id, $isCommEnt, $myDB) = @_;

    my ($sql, $language_id);
	my $team_id = 2;
    $sql = "select isnull(lead_group,56) as lead_group , legacy, language_id
	   from lp_lead with(nolock) inner join lkup_qwest_opts opts with (nolock) on opts.lp_Lead_id = lp_lead.lp_lead_id
				where lp_lead.lp_lead_id = '$lead_id'";
	my ($sth, $data);
##############
			try {
				$sth = $myDB->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$data = $sth->fetchrow_hashref(); 
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
        
	   $language_id = $data->{language_id};

        if ( $data->{lead_group} == 56 && $data->{legacy} == 2) { # Legacy CTL rep
			$sql = "select 318049 as isr_id, 0, 5 as lp_region_id"; # coop: 318049, staging: 309193

		}
         elsif ( $data->{lead_group} == 56 && $data->{legacy} == 1 ) { # Legacy Q rep
                $sql = "select 318050 as isr_id, 0, 5 as lp_region_id"; # coop: 318050, staging:309192
              
        }elsif ( $data->{lead_group} == 55) {
			if ($isCommEnt > 0) {
				# was savvis
				#$sql = "select 395106  as isr_id,0,0,'CenturyLink Technology Solutions' as staff_name,5 as lp_region_id";
				$sql = "select 333606  as isr_id,0,0,'MED/LG ISR' as staff_name,5 as lp_region_id";
			}
			else {
            $sql = "exec splp_yc_empsite_bizroute $lead_id , $team_id,$language_id ";
		#	$sql = "exec splp_yc_bizroute_savvis $lead_id ";
            $sql = "exec splp_yc_bizroute $lead_id";
			}
        }

    return $sql;
}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub get_header
{

	my %hash  = @_;
	my $title = $hash{title} || '';
	my $css   = $hash{css} || '';
	my $more  = $hash{more} || '';

	$css = "<link rel=\"stylesheet\" href=\"$css\" type=\"text/css\">\n" if $css;

	#my $str = "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
	my $str = <<EOF;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>$title</title>
$css$more
<meta name=robots content=noindex>
<meta name="MSSmartTagsPreventParsing" content="TRUE">
<meta http-equiv="pragma" content="no-cache">
<script language="javascript">
  function openwindow(URL) {
    win = window.open(URL, "pop", "width=800, height=550, left=50, top=50, scrollbars=yes, toolbar=yes, menubar=yes, status=yes");
  }
</script>

</head>
EOF
	return $str;
}

sub sendCCIDebug {
 
	my ($myDB,$to,$subject,$body) = @_;
 
	$body =~ s/'/''/g;
 
	my $ccimail = "insert into ccimail
			(client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) values
			(50, 154, '' , '$to', '', '',  'do_not_reply\@ccionline.biz', '$subject', '$body' ) ";
		
		
	my $sth = $myDB->prepare($ccimail);
	$sth->execute();		
	$sth->finish();	   
  
 # print $ccimail;  
}

############################################################################
sub EscQuote($)    # 03/30/01 5:40PM  -- RF
                   # Escapes single quotes
                   # Use for preparing strings for SQL statements.
############################################################################
{
    my ($delim_return) = @_;
    $delim_return =~ s/[']/''/gi;
    return $delim_return;
}                  ##EscQuote($)


#================================================================#
#THIS IS TO LOGOUT - CL Security
#================================================================#
if ($cgi->param('logout') == 1) { 
		my $staff_id = param('staff_id');
		my $session_id = param('session_id');
		my $db = DBInterface->new();
		
		my $sql1 = "delete from user_session where user_session_id = ?";
		my $sql2 = "delete from cookie_session where session_id = ?";
		my $sth;
##############
			try {
				$sth = $db->prepare($sql1);
				$sth->execute($session_id) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
			try {
				$sth = $db->prepare($sql2);
				$sth->execute($session_id) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('youcan10',"$thisfile", $_ );
			};
##############
		
		$db->disconnect;	
		exit;
 }

1;

