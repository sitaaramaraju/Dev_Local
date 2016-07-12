use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

require "D:/xroot/cgi-bin/lp-init.pm";
require "d:/xroot/cgi-bin/delimeter.cgi";
#require "d:/xroot/qwest/lms_ref_email.cgi";
require "d:/xroot/cgi-bin/email.cgi";




my $session_id= $main::session{session_id}||$cgi->param('session_id'); 

my $SKIP_SETUP = 0; # set to zero for real insert
my $myDB = Win32::ODBC->new($main::DSN);
my $staff_id_real = $main::session{staff_id};
my $cuid =  $main::session{logonID} ;
my $client_id = 50;
my $program_id = 269;
my $fund_id = 1036;
my $password =  $main::session{'password'} || ''; #           Not SET    FIX
my $usertype = $main::session{'UserType'} || '';
my $navigation_version = $main::session{'navigation_version'} || '';
my $userid = $main::session{'logonID'} || ''; # hack
my $contact_info_id = $main::session{'contact_info_id'} || ''; # hack

#header();

#die;
#http://www.qwestyoucan.com/qwest/emp/promo2007/default.htm
# after </object> -- <script type="text/javascript" src="fixit.js"></script>
my $sql = "select name from cust_contact with (nolock) where contact_info_id in
(select contact_info_id from staff with (nolock)
where staff_id = $staff_id_real ) ";
$myDB->Sql($sql);
$myDB->FetchRow();
my %prog = $myDB->DataHash();
my $name = uc($prog{name});
#my $emplid = $prog{emplid};



$sql = "select personnel_first_name as fname
from contact_personnel with (nolock)
where contact_main_id in
( select contact_main_id from contact_main with (nolock) where cust_id in
( select cust_id from cust_contact with (nolock) where contact_info_id in
(select contact_info_id from staff with (nolock)
where staff_id = $staff_id_real)))
and isnull(personnel_first_name, '') <> '' ";
$myDB->Sql($sql);
$myDB->FetchRow();
my %name_data = $myDB->DataHash();
my $fname = uc($name_data{fname});
#my $emplid = $prog{emplid};


$sql = "select cust_id as cust_id from cust_contact with (nolock) where contact_info_id in
(select contact_info_id from staff with (nolock)
where staff_id = $staff_id_real) ";
$myDB->Sql($sql);
$myDB->FetchRow();
my %cust_data = $myDB->DataHash();
my $agency_id = $cust_data{cust_id};



my($msg, $lead_id, $cust_id) = do_submit ($cgi);

 LMS_EMAIL_NOTIFY( $lead_id, $myDB);
#$msg .= $email_sql1;
#$email_sql2
# for old browsers
my  $PAGETITLE = 'CenturyLink Connect-Thanks';


print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>$PAGETITLE</title>
<script language="JavaScript" src="qwestconnect07menus.js"></script>
<link href="Style.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="validate.js"></script>
<script language="JavaScript" src="mm_menu.js"></script>
</head>

<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif','images/SubmitNav1_top_on.gif','images/SubmitNav2_top_on.gif','images/SubmitNav3_top_on.gif','images/SubmitNav4_top_on.gif','images/SubmitNav5_top_on.gif')">
<script language="JavaScript1.2">mmLoadMenus();</script>
<table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td><table width="954" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td align="center" valign="top"><img src="images/ctl_con_logo4.png" width="954" height="324" /></td>
      </tr>
      <tr>
        <td align="left" valign="top"><table width="954" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td width="28" align="left" valign="top"><img src="images/nav_blank.gif" width="28" height="31" /></td>
            <td width="141" align="left" valign="top"><a href="landing.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image28','','images/Sub_nav_home_on.gif',1)"> <img src="images/Sub_nav_home_off.gif" name="Image28" width="141" height="31" border="0" id="Image28" /></a></td>
            <td width="257" align="left" valign="top"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','images/Sub_nav_about_on.gif',1)"> <img src="images/Sub_nav_about_off.gif" name="Image29" width="257" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>
            <td width="136" align="left" valign="top"><a href="faqs.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','images/Sub_nav_faq_on.gif',1)"> <img src="images/Sub_nav_faq_off.gif" name="Image30" width="136" height="31" border="0" id="Image30" /></a></td>
            <td width="194" align="left" valign="top"><a href="contact.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','images/Sub_nav_contact_on.gif',1)"> <img src="images/Sub_nav_contact_off.gif" name="Image31" width="194" height="31" border="0" id="Image31" /></a></td>
            <td width="198" align="left" valign="top"><a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image32','','images/Sub_nav_Products_on.gif',1)"> <img src="images/Sub_nav_Products_off.gif" name="Image32" width="198" height="31" border="0" id="Image32" onclick="MM_openBrWindow('http://www.qwest.com/residential/refer/index.html','','')" /></a></td>
          </tr>
        </table></td>
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
                <td align="left" valign="top" class="BlueTitles">WELCOME, $name </td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td width="913" height="376" align="left" valign="top" background="images/LoggedInback.gif">
              <table width="900" border="0" cellspacing="1" cellpadding="1">
                <tr>
                  <td width="10" align="left" valign="top">&nbsp;</td>
                  <td align="left" valign="top"><table width="790" border="0" cellspacing="0" cellpadding="0">

                    <tr>
                      <td>&nbsp;</td>
                      <td>&nbsp;</td>
                    </tr>
                    <tr>
                      <td width="203" align="left" valign="top"><table width="195" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td align="left" valign="top"><img src="images/SubmitNav_top.gif" width="195" height="22" /></td>
                        </tr>
                        <tr>
                          <td align="left" valign="top"><a href="lmsii_submitreferral.cgi?session_id=$session_id" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image15','','images/SubmitNav1_top_on.gif',1)"><img src="images/SubmitNav1_top_off.gif" name="Image15" width="195" height="28" border="0" id="Image15" /></a></td>
                        </tr>
                        <tr>
<!-- pass to leadpro_frame -->
<form name="lead" action="" method="post">
    <input type="hidden" name="client_id"  value="50">
<input type="hidden" name="session_id"  value="$session_id">
    <input type="hidden" name="program_id" value="$program_id">
    <input type="hidden" name="fund_id"    value="$fund_id">
    <input type="hidden" name="userid" value="$userid">
    <input type="hidden" name="password" value="$password">
    <input type="hidden" name="usertype" value="$usertype">
    <input type="hidden" name="navigation_version" value="$navigation_version">

                          <td align="left" valign="top"><a href="#" onclick="javascript:document.lead.target='_new';document.lead.action='http://www.qwestreferafriend.com/leadpro_frame.cgi';document.lead.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image16','','images/SubmitNav2_top_on.gif',1)"><img src="images/SubmitNav2_top_off.gif" name="Image16" width="195" height="33" border="0" id="Image16" /></a></td>
     </form>

			</tr>
                        <tr>
                          <td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('https://www.myprepaidcenter.com/site/balance','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image17','','images/SubmitNav3_top_on.gif',1)"><img src="images/SubmitNav3_top_off.gif" name="Image17" width="195" height="41" border="0" id="Image17" /></a></td>
                        </tr>
                        <tr>
                          <td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('https://www.myprepaidcenter.com/site/balance','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image18','','images/SubmitNav4_top_on.gif',1)"><img src="images/SubmitNav4_top_off.gif" name="Image18" width="195" height="45" border="0" id="Image18" /></a></td>
                        </tr>
                        <tr>
			<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('images/YC.005.LMS2BRO.0306_F1.pdf','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image19','','images/SubmitNav5_top_on.gif',1)"><img src="images/SubmitNav5_top_off.gif" name="Image19" width="195" height="27" border="0" id="Image19" /></a></td>
                        </tr>
                        <tr>
                          <td align="left" valign="top"><img src="images/SubmitNav_bot.gif" width="195" height="22" /></td>
                        </tr>
                      </table></td>
                      <td width="587" align="left" valign="top"><span class="BIGBoxTitles">Thank you, $fname for submitting a referral!<br>
							</span>
							<br>
							<span class="subTitles"> $msg </span></td>
                    </tr>
                  </table>
                  </td>
                </tr>
              </table></td>
          </tr>
          <tr>
            <td align="left" valign="middle">&nbsp;</td>
          </tr>
          <tr>
            <td align="left" valign="top">&nbsp;</td>
          </tr>
        </table></td>
      </tr>
      <tr>
    <td>
       <img src="images/bottombuffer.gif" width="954" height="15" /></td>
                    </tr>
                    <tr>
        <td width="954" height="66" align="center" valign="middle" background="images/bottom_amex.gif"><table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
EOF
require "d:/xroot/qwest/qwestconnect07/footer_loggedin.cgi";
print<<"EOF";
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>


EOF

#LMS_EMAIL_NOTIFY( $lead_id, $cust_id);

$myDB ->Close();
undef &getrouting_sql;
undef &getproductlist;
###########################################################################################################
sub do_submit {
my $cgi = shift; #
return ('') if $SKIP_SETUP;

	my $prod_int  = EscQuote($cgi->param('prod_int'));
	my $cust_name = EscQuote($cgi->param('cust_name'));
	my $phone1 = EscQuote($cgi->param('phone1'));
	my $phone2 = EscQuote($cgi->param('phone2'));
	my $time_to_call = EscQuote($cgi->param('time_to_call'));
	my $lp_notes = EscQuote($cgi->param('lp_notes'));
	my $lead_state = EscQuote($cgi->param('lead_state'));
	# LMS II is only residential referrals so no cust type
	my $cust_type = 'con' ; #EscQuote($cgi->param('cust_type'));
    my $lead_address = EscQuote($cgi->param('lead_addr'));
    my $lead_address2 = 'Apt/Unit :'.EscQuote($cgi->param('lead_addr2'));
	my $mindt = EscQuote($cgi->param('mindt'));
	my $legacy = 1;
    # following is copy over from b2b
	my $source=1;

    my $mainbtn = $phone1;
       #my ($validated, $mainbtn, $duplicate_lead, $sql) = check_mainbtn($phone1, $program_id, $fund_id, $myDB );

      # my $validated = 1;
       # if ( $validated == 0 ) {
       # $msg = "A referral duplicate_lead on this Billing Telephone Number mainbtn has already been placed and is still in an open status.
        #        Duplicate referral can not be placed until all open referrals for this number are closed. If you have any questions please call 1 800-362-1850.
        #        <br><br>";

        #}else{




# figure out values based on info that came in
	my $lead_group = 55 ;
	if ($cust_type eq 'con') {
		$lead_group = 56 ;
	}

	my $class1 = " and class1 = 'Residential' ";
	my $class2;
	my $have_interest = 1;
	if ($prod_int eq 'BRD' ) {
		$class2 = " and class2 = 'High Speed Internet' ";
	}
	elsif ($prod_int eq 'DTV') {
		$class2 = " and class2 = 'TV' ";
	}
	elsif ($prod_int eq 'WRL') {
		$class2 = " and class2 = 'Wireless' ";
	}
	elsif ($prod_int eq 'DIV') {
		$class2 = " and class2 = 'Long Distance' ";
	}
	else {
		$class2 = " and isnull(class2 , '') = '' ";
	}

	my @product;
	if ( $have_interest == 1) {
		my $prod_sql = " select prod.prod_id from prod with (nolock)
			where prod_id in
			(select prod_id from fund_prod with (nolock) where fund_id = $fund_id)
			and ProdIsActive = 1
			$class1
			$class2 ";

		$myDB->Sql($prod_sql);
		    while ($myDB->FetchRow()){
			push @product, $myDB->Data(); # all fields in one row
			}
	}

#post submission, insert records, route and print confirmation

            $sql = "insert into lp_lead (created_date, created_by, agency_id, lead_name, lead_company_name, lead_phone, lead_email,
                    lead_address,lead_address2,lead_city, lead_state, lead_zip, btn_id, main_btn, client_id,lp_changed_by, program_id,  fund_id, 
					warm_xfer, lead_group, source_id, lp_region_id, language_id)
                    values (getdate(), $staff_id_real, $agency_id , ltrim('".delim_return($cust_name)."'),'','$phone1','',
                    '".delim_return($lead_address)."','".delim_return($lead_address2)."','','$lead_state', '', '$phone1','$phone1', 50, $staff_id_real, 269, 1036,
                    0, $lead_group, $source, 5 ,1 )";
#print<<"EOF";
#insert lp_lead <pre>$sql</pre> <br>
#EOF


            if ($myDB->Sql($sql)) {
                if ($myDB->Sql($sql)) {
                    if ($myDB->Sql($sql)) {

                        #CommonStuff::buglog("d:/xroot/logs/deadlock.log", $sql, '154' );

                        if ( $ENV{REMOTE_ADDR} eq $main::CCIIP ) {  #prh
                            $myDB->DumpError();
                            print "<br>$sql<br>";
                            my $host   = 'HTTP_HOST ='   . (exists $ENV{HTTP_HOST}   ? $ENV{HTTP_HOST} : 'noexist');
                            my $server = 'SERVER_NAME =' . (exists $ENV{SERVER_NAME} ? $ENV{HTTP_HOST} : 'noexist');
                            print "<br>$host<br>$server<br>";
                        }
                        print $sql;
                        print "Unable to process.  3 Attempts complete.  Deadlock victim.  Please hit 'refresh' to try again.";
                        exit 0;
                    }
                }
            }
            $myDB->FetchRow();
            my %data = $myDB->DataHash();
            my $lead_id = $data{lp_lead_id};
#-----------------------------------------------------------------------
# adding the cdg/retail field ticket #53-2841
	    my $cdg = get_cdg ( $agency_id , $myDB);
#--------------------------------------------------------------------------
            ###################################################
            # extra optional fields
           # my $phone2 =         EscQuote($cgi->param('mobile_no'));
            my $best_contact_time = ''; #EscQuote($cgi->param('best_contact_time'));
            my $best_contact_date = ''; #EscQuote($cgi->param('best_contact_date'));
            my $lead_source =       EscQuote($cgi->param('lead_source'));
            #3my $local_service =     EscQuote($cgi->param('local_service'));
            my $sales_center =     '' ;# EscQuote($cgi->param('sales_center'));
            my $cust_type = $lead_group == 55? "Business" : "Residential";
            my $referral_source = 'other'; # Dont leave it blank
	my $BAN = EscQuote($cgi->param('ban'))||'';
	my $prop_name = EscQuote($cgi->param('prop_name'));
	my $exist_cust = 0;
	my $exist;
	if ($exist_cust eq 'yes') {$exist = 1;	}
	elsif ($exist_cust eq 'no') {$exist = 0;	}
            # Record the source website where the lead is submitted from. Eat 'www.' for uniformity.
            (my $server_name = lc($cgi->server_name()) || 'unknown_269isr_1036_929_'.$agency_id.'_'.$lead_id) =~ s/^www\.// ;
if ($main::cgi{exist_cust}  eq 'yes') { $exist_cust = 1;} 
$sql = "insert into lkup_qwest_opts (lp_lead_id, mobile_no, cust_type, best_contact_time, lead_source,  vccustom1, server_name, sales_center, vccustom2,
        referral_source, icustom1, employer, existing_customer, work_phone)
        values($lead_id, '$phone2', '$cust_type', '$time_to_call','$lead_source',  '', '$server_name','$sales_center','',
        '$referral_source' , $cdg, '".delim_return($prop_name)."', $exist_cust, '$BAN')";
#print<<"EOF";
#391 <pre>$sql</pre> <br>
#EOF
            if ($myDB->Sql($sql)) {
               $myDB->DumpError();
               print "<br>$sql<br>";
               print "Unable to process. Opts not created, partial record on file only.";

                my $body = "$sql <br>  $main::session{name}";

                $sql = "insert into lkup_qwest_opts (lp_lead_id)
                        values ($lead_id)";
                $myDB->Sql($sql);

               SendEmail("archanak\@channelmanagement.com", "", "archanak\@ccionline.biz", "do_not_reply\@ccionline.biz", "LMS II Submission on Opts Error", "$body");
            }


            $sql = "insert into lp_lead_history (lp_lead_id, action, staff_id, history_date, source_id, user_ip)
                    values ( $lead_id, 'Referral created', $main::session{staff_id}, getdate(), 1 , '$ENV{REMOTE_HOST}')";
            $myDB->Sql($sql);
			my $movindt = '';
			if ($mindt ne '' || length($mindt)>0) {
				$movindt = " Move In date $mindt";
			}
            if ( length($cgi->param('lp_notes')) > 0 || length($mindt)>0) {
                $sql = " update lp_lead set lp_notes = convert(varchar,getdate())+': ".$main::session{name} . "'+char(13)+char(10)+'" . delim_return($cgi->param('lp_notes')) . "$movindt'+char(13)+char(10)+'----------'+char(13)+char(10)+isnull(lp_notes,''), lead_status_change_dt = getdate() where lp_lead_id = " . $lead_id;
            }
			elsif (length($mindt)>0) {
                $sql = " update lp_lead set lp_notes = convert(varchar,getdate())+': ".$main::session{name} . "'+char(13)+char(10)+'". "$movindt'+char(13)+char(10)+'----------'+char(13)+char(10)+isnull(lp_notes,''), lead_status_change_dt = getdate() where lp_lead_id = " . $lead_id;
			}
			                $myDB->Sql($sql);

# prod interest set at the begining
#            my %product = $cgi->param('product');
            foreach my $prod (@product){
                $sql = "insert into lkup_lead_product_interest (prod_id, lp_lead_id)
                        values ($prod, $lead_id)";
                $myDB->Sql($sql);

            }
            my $prod_group = $lead_group;
                ###############################

$msg = "  <br> <br>  The information you provided has been routed to the
            appropriate CenturyLink service rep and your customer will be contacted within 2 business days.
		<br><br>
            Your reference number for this submission is $lead_id ";

        #}#end validate
return ($msg,  $lead_id, $agency_id);
}


############################################################################
sub check_mainbtn      #08/01/08 9:04:AM
############################################################################
 {

    my $phone1= shift;
    my $program_id = shift;
    my $fund_id = shift;
    my $myDB = shift;           # passed around
    my $sql;
    my $validated = 0;
    my $duplicate_lead = 0;
    my $mainbtn = $phone1;

    # Save original BTN to return
    my $origbtn = $mainbtn;

    # Forget trim, eat everything except digits
    $mainbtn =~ s/\D+//g;  # Then 'unknown' or 'new service' passes as '' case

    # Return a cleaned up BTN if numbers in it, else original
    my $clean_btn = $origbtn =~ /\d/ ? $mainbtn : $origbtn;

    if ( $mainbtn eq ''                ||   # text was stripped
        $mainbtn =~ /^999+$/          ||   # all nines (at least 3)
        $mainbtn =~ /^\d\d\d999+$/    ){   # areacode then all nines

        $validated = 1;
    }
    else{


        # The BTN has numbers in it    Check it out
        $sql = "select lp_lead.lp_lead_id
                from lp_lead with(nolock)
                where dbo.fnCleanPhone10(main_btn) = '$mainbtn'
                    and isnull(lead_status_id,0) < 50 and program_id = $program_id
                    and fund_id = $fund_id
                    and lead_name <> 'test'
                   and client_id = 50";

        $myDB->Sql($sql);
        $myDB->FetchRow();  # Just get one in case many, all I need
        my %datadon = $myDB->DataHash();
        if ( $datadon{'lp_lead_id'} ) {
            $duplicate_lead = $datadon{'lp_lead_id'};
        }

        if ( $duplicate_lead ) {
            $validated = 0;
        }
        else{
            # Not a duplicate
            $validated = 1;
        }
    }
    return ($validated, $clean_btn, $duplicate_lead, $sql);
}

############################################################################
sub get_cdg {
my $cust_id = shift;
my $db = shift;
my $cdg = 0;
my   $jt_sql = "select isnull(job_title, '') as job_title 
    from qwesthr with (nolock) where cuid in (
	select custom6 from cust with (nolock) where cust_id = $cust_id)";
    $db->Sql($jt_sql);
    $db->FetchRow();
    my %job_data = $db->DataHash();
    my $job_title = $job_data{job_title};
    if ($job_title eq 'Retail Store Manager' || $job_title eq 'Kiosk Sales Manager') {
	$cdg = 2;
    }
    else {
	$cdg = 1; # for Outside Sales Representative, Customer Account Consultant II or Sales and Service Consultant AND DEFAULT
    }
return $cdg;
}
sub LMS_EMAIL_NOTIFY 
 {
    my ($lead_id, $db) = @_;
    my $sql = "select qwesthr.email, qwesthrboss.email as bossemail, qwesthr.work_state
               from qwesthr with (nolock), qwesthr qwesthrboss with (nolock), lkup_qwest_opts with (nolock)
               where convert(int,qwesthr.emplid) = lkup_qwest_opts.out_region_sales
                    and qwesthr.super1 = qwesthrboss.emplid
                    and lp_lead_id = $lead_id";
        $db->Sql($sql);
        $db->FetchRow();
        my %checkit = $db->DataHash();

       # my $sendto = $checkit{email} . "," . $checkit{bossemail};
	my ( $sendto, $lead_open_flag) = get_emails($lead_id, $db);

        if (($checkit{work_state} eq 'UT') or( $checkit{work_state} eq 'ID') or ($checkit{work_state} eq 'MT')) {
            $sendto .= ",scott.Morgan\@centurylink.com" ;
        }


    $main::session{name} = EscQuote($main::session{name});
    $sql = "update lp_lead set lp_notes = convert(varchar,getdate())+': $main::session{name} '+char(13)+char(10)+'Email notification sent to $sendto.'+char(13)+char(10)+'----------'+char(13)+char(10)+isnull(lp_notes,'')
         where lp_lead_id = $lead_id";
    $db->Sql($sql);
    #--
#update lead status after sending email
if ($lead_open_flag == 1) {
        $sql = " update lp_lead set lead_status_id = 1 where lp_lead_id = " . $lead_id;
        $db->Sql($sql);
}
#--


    $sql = " select 1 as tbl_source, isnull(lp_lead.btn_id,'') as btn_id, isnull(lp_lead.lead_name,'') as lead_name, lp_lead.fund_id,
   isnull(lp_lead.lead_company_name,'') as lead_company_name,ISNULL(lp_lead.main_btn,'') as main_btn, lp_lead.language_id, isnull(lp_lead.warm_xfer,0) as warm_xfer,
   ISNULL(lp_lead.lead_phone,'') as lead_phone, ISNULL(lp_lead.lead_email,'') as lead_email, ISNULL(rtrim(lp_lead.lead_address),'') as lead_address,
   ISNULL(rtrim(lp_lead.lead_address2),'') as lead_address2, ISNULL(lp_lead.lead_city,'') as lead_city, ISNULL(lp_lead.lead_state,'') as lead_state,
   ISNULL(lp_lead.lead_zip,'') as lead_zip,ISNULL(lp_lead.lp_notes,'') as lp_notes,
isnull(opts.mobile_no,'') as mobile_no, ISNULL(opts.best_contact_time,'') as best_contact_time, 
ISNULL(opts.best_contact_date,'') as best_contact_date,ISNULL(opts.cust_type,'') as cust_type,ISNULL(opts.lead_source,'') as lead_source,
 isnull(lead_status_id,0) as lead_status_id, opts.server_name,
                  convert(varchar,created_date,1) + ' ' + convert(varchar,created_date,108) as date_created,
                  convert(varchar,lead_tickle_date,1) as lead_tickle_date,
                  convert(varchar,lead_check_date,1) as date_paid,
                  case when lp_lead.source_id = 1 then (select name+' ['+client_cust_no+']' as refname from cust with(nolock) where cust_id = lp_lead.agency_id)
                  else (select rtrim(qwesthr.first_name)+' '+ltrim(qwesthr.last_name)+' ['+cuid+']' as refname from qwesthr with(nolock) where emplid = lp_lead.agency_id)
                  end as refname,
                  case when isnull(lead_status_id,0) = 0 then 'New'
                  else (select status_name from lp_status with (nolock) where lead_status_id = lp_lead.lead_status_id
                        and (program_id = lp_lead.program_id or program_id is null)) end as status_name,
                  source_id,opts.out_region_sales as osr_id, employer
            from lp_lead lp_lead with (nolock)
			inner join lkup_qwest_opts opts with (nolock) on opts.lp_lead_id = lp_lead.lp_lead_id
			--left outer join staff with(nolock) on staff.staff_id = lp_lead.lp_isr_id
            where  lp_lead.lp_lead_id =   $lead_id";
    $db->Sql($sql);
    $db->FetchRow();
    my %data = $db->DataHash();
    my $language = $data{'language_id'} == 2 ? 'Spanish' : 'English';
    my $warm     = $data{'warm_xfer'}   == 1 ? 'Yes': 'No';
	my $program_id = $data{'program_id'} ;
    my $product_interest = '';
    $sql = "select dbo.fnGetLeadProductsInterest ($lead_id) as product";
    $db->Sql($sql);
    $db->FetchRow();
    my %prod_dt = $db->DataHash();


$sql = "select email_template_id as temp_id ,rtrim(email_templates.email_body) as body,
		rtrim(email_templates.email_subject) as subject, rtrim(email_templates.email_footer) as footer,
			rtrim(email_templates.email_from_address) as from_add
from email_templates with(nolock) 
where email_templates.program_id = 269
and email_templates.ext_status_id <1
and email_templates.fund_id = 1036
 and email_templates.is_active = 1 ";
    $db->Sql($sql);
    $db->FetchRow();
    my %email_dt = $db->DataHash();
my $body = $email_dt{body};
my $blank ='';
my $bcc='';


#replace
	my $temp_id = $email_dt{temp_id};
	my $subject = $email_dt{subject};
    my $from = $email_dt{from_add};
	#replace
   $subject =~ s/\$lead_id/$lead_id/gi;
   $body =~ s/\$footer/$email_dt{footer}/gi;
   $body =~ s/\$lead_id/$lead_id/gi;
   $body =~ s/\$date_created/$data{date_created}/gi; 
   $body =~ s/\$refname/$data{refname}/gi; 
   $body =~ s/\$product/$prod_dt{product}/gi; 
   $body =~ s/\$btn_id/$data{btn_id}/gi; 
   $body =~ s/\$warm/$warm /gi; 
   $body =~ s/\$language/$language/gi; 
   $body =~ s/\$lead_name/$data{lead_name}/gi;
   $body =~ s/\$lead_company_name/$data{lead_company_name}/gi; 
   $body =~ s/\$main_btn/$data{main_btn}/gi; 
   $body =~ s/\$mobile_no/$data{mobile_no}/gi; 
   $body =~ s/\$lead_phone/$data{lead_phone}/gi; 
   $body =~ s/\$lead_email/$data{lead_email}/gi; 
   $body =~ s/\$best_contact_time/$data{best_contact_time}/gi; 
   $body =~ s/\$prop_name/$data{employer}/gi; 
   $body =~ s/\$addr1/$data{lead_address}/gi; 
   $body =~ s/\$addr2/$data{lead_address2}/gi; 
   $body =~ s/\$best_contact_date/$data{best_contact_date}/gi; 
   $body =~ s/\$lead_state/$data{lead_state}/gi; 
   $body =~ s/\$cust_type/$data{cust_type}/gi; 
   $body =~ s/\$lead_source/$data{lead_source}/gi; 
   $body =~ s/\$lp_notes/$data{lp_notes}/gi; 
   $body =~ s/\$email_footer/$blank/gi; 
   $body =~ s/\$server_name/$data{server_name}/gi; 
 
	$body = EscQuote($body);
   #$body.="
   #when live will go to $sendto ";
   #$sendto = "archanak\@ccionline.biz";
#-- email thru db
		 $sql = "insert into lp_comm(lp_lead_id, staff_from_id, email_template_id, email_body, email_subject, date_created, email_format)
                values($lead_id, $main::session{staff_id}, $temp_id, '$body', '$subject', getdate(), '1')";

       $db->Sql($sql);
       $db->FetchRow();
        my %commid = $db->DataHash();
        $sql = "insert into lp_comm_to(lp_comm_id, lp_lead_id, date_sent, sentto_staff_id, sentto_name, sentto_address, sentto, ccto, bccto)
                values($commid{lp_comm_id}, $lead_id, getdate(), 0, '$sendto', '$sendto', 1, 0, 0)";

       $db->Sql($sql);
        $sql = "insert into lp_lead_history(lp_lead_id, action, staff_id,source_id, history_date)
                values($lead_id, 'Email sent to $sendto: $subject', 34081, 1,getdate())";
        $db->Sql($sql);
		 $sql = "insert into ccimail (client_id, program_id, date_created, lp_lead_id, staff_id, subject, tofield, ccfield, bccfield, fromfield, longbody, ctype)
					values (50, 269, getdate(), $lead_id, 1, '$subject', '$sendto', '','$bcc', '$from','$body','text/html') ";
        $db->Sql($sql);

print "623 $sql	<br>";

#return $sql;
#-- end email thru db
#SendEmail($sendto, "","","refer.friend\@qwest.com","$subject",$body."\n");
}   ##LMS_email2
sub get_emails 
############################################################################
{ my ($lead_id, $dbx) = @_;
  my $emp_email = '';
  my $job_title = '';
  my $lead_open_flag = 0;
    my $fund_sql = "select fund_id, agency_id from lp_lead with (nolock) where lp_lead_id = $lead_id ";
$dbx->Sql($fund_sql);
$dbx->FetchRow();
my %fund_data = $dbx->DataHash();
my $fund_id = $fund_data{fund_id};
my $agency_id = $fund_data{agency_id};
my $cust_sql="select  ISNULL(custom6,'') as custom6 from cust with (nolock) where cust_id = $agency_id";
$dbx->Sql($cust_sql);
$dbx->FetchRow();
my %cust_data = $dbx->DataHash();
my $cac_cuid = uc($cust_data{custom6});

if ($cac_cuid ne "") {
	$cust_sql = "select  isnull(qwesthr.email,'') as email, rtrim(qwesthr.job_title) as job_title
 from qwesthr with (nolock)
where cuid = '$cac_cuid' ";

$dbx->Sql($cust_sql);
$dbx->FetchRow();
%cust_data = $dbx->DataHash();
$emp_email = EscQuote($cust_data{email});
$job_title = $cust_data{job_title};

}
else {
$emp_email="";
}


if ($emp_email eq "") {
$emp_email = "Laura.Graber\@centurylink.com";
}

if ($job_title eq 'Outside Sales Representative' && $fund_id == 1036) {
	$emp_email.= ', cdgraf@centurylink.com';
}
if (($job_title eq 'Retail Store Manager') || ($job_title eq 'Kiosk Sales Manager')) {
 $lead_open_flag=1;
}
if ($job_title eq 'Customer Relations Specialist') {
	$emp_email.= ', cdgraf@centurylink.com , Lisa.Gereg@centurylink.com';
	$lead_open_flag=1;
}

return ($emp_email, $lead_open_flag);

}
