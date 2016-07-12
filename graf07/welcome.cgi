#!/usr/bin/perl
use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
use CCICryptography;
use Try::Tiny;
use HTML::Strip;

use DBInterface;
my $myDB = DBInterface->new();

my $server ="";
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
else {
	$server = "D:/centurylinkyoucan";
}

require "$server/cgi-bin/email.cgi";
require "$server/cgi-bin/contact.cgi";
require "$server/graf07/qwest_duplicate_chk.cgi";

my $STATUS_OK = 1;
my $STATUS_INVALID = 2;
my $STATUS_ERROR = 3;
my $SKIP_SETUP = 0;
my  $IS_TEST = 1;
my $program_id = 154;
my $fund_id = 649;
my $client_id = 50;
my $thisfile = 'GRAF - Welcome';
my  $PAGETITLE = 'GRAF-Welcome';


my $link;

my $print_staff = '';
my $print_pwd = '';

my $url = CCICryptography::getUrl_sites('graf03');

my $checkwel = EscQuote( $cgi->param('first') );
if (length($checkwel) == 0){
	
	print qq[
	<html>
	<body>
	<form name="lead" action="" method="post">
    <script language='javascript'>
      alert("There was an error loading the page.  Please log in and try again.");
      document.lead.action='$url';
      document.lead.submit();
    </script>
	</form>
 </body>
</html>
  ];
exit();

}


my  ( $status, $msg, $email, $staff_id, $pwd, $name) = do_submit( $cgi );

       if ($status == $STATUS_OK ) {
	 my $email_status = emailit( $email, $staff_id, $pwd, $name );
	 $link = "../index_raf.cgi";
	 $msg = '
Thank you for enrolling in the CenturyLink Partner Referral Program. <br>
Your login credentials are emailed to the email address provided on enrollment form. <br>

<a href="'.$link.'" class="FAQLink" >Click here</a> to get started.';

       }

require "graf07/header.cgi";
print<<"EOF";
					  
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
                                                    WELCOME $name &nbsp;                                                </td>
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
                                                <td width="10" align="left" valign="top">&nbsp;                                                    </td>
                                                <td align="left" valign="top">
                                                    <table width="700" border="0" align="center" cellpadding="0" cellspacing="0">
                                                        <tr>
                                                            <td>
       &nbsp;<table align="center" border="0" cellpadding="1" cellspacing="1" width="650">
             <tr>
       <td align="left" valign="top">
 <table border="0" cellpadding="1" cellspacing="1" class="Enrollcopy" width="650">
<tr>
<td align="left" valign="top">&nbsp;</td>
</tr>
<tr>
<td align="left" valign="top">
$msg
</td>        
</tr>
<tr>
<td align="left" valign="top">&nbsp; </td>
</tr>
<tr>
<td align="left" valign="top">&nbsp;   </td>
</tr>
<tr>
<td align="left" valign="top"><table width="500" border="0" cellspacing="2" cellpadding="2">
<tr>
<td width="146">&nbsp;</td>
<td width="354">&nbsp;</td>
</tr>
</table></td>
</tr>
<tr>
<td align="left" valign="top">
Use your user ID and password to participate in the program on this Web site or through the toll free number. You can do all of this:                                                                                    </td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td align="center">
 <div align="left">
<ul>
 <li>Make referrals</li>
 <li>Track your previous referrals</li>
 <li>Get program guidelines and updates</li>
</ul>
 </div>                                                                                    </td>
         </tr>
                      <tr>
               <td align="center">&nbsp;</td>
                                            </tr>
                                                                            </table>
                                          </td>
                                                                    </tr>
                                                                </table>                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td colspan="2" align="center">                                                            </td>
                                                        </tr>
                                                    </table>                                                </td>
                                            </tr>
                                        </table>                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/Sub_bottom.gif" width="913" height="16" /></td>
                                </tr>
                            </table>                        </td>
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
$myDB->disconnect();

#--------------------------------------------------------------------
#   do_submit
#--------------------------------------------------------------------
sub do_submit{
    my $cgi = shift;
	my $hs = HTML::Strip->new();

 return( $STATUS_OK, '', 'archanak@ccionline.biz', 58299, 9, 'Archana') if $SKIP_SETUP;

    # ---------------------FIX  -------------------------------------- FIX
    # ---------------------FIX  -------------------------------------- FIX
    # ---------------------FIX  -------------------------------------- FIX
    #       Can't escape quote before testing!!
    #       Can't escape quote before testing!!
    #       Can't escape quote before testing!!
    # ---------------------FIX  -------------------------------------- FIX
    # ---------------------FIX  -------------------------------------- FIX
    # ---------------------FIX  -------------------------------------- FIX
    my $vccust28 = EscQuote( $hs->parse($cgi->param('sp_id')) );
    my $first = EscQuote( $hs->parse($cgi->param('first')) );
    my $osr_id = '';
    my $last = EscQuote( $hs->parse($cgi->param('last')) );
    my $name = "$first $last";
    my $vc1 = EscQuote( $hs->parse($cgi->param('addr1')) );
    my $vc2 = EscQuote( $hs->parse($cgi->param('addr2')) );
    my $vc3 = EscQuote( $hs->parse($cgi->param('city')) );
    my $vc4 = EscQuote( $hs->parse($cgi->param('state')) );
    my $vc5 = EscQuote( $hs->parse($cgi->param('zip')) );
    my $email = EscQuote( $hs->parse($cgi->param('email')) );
    my $lastfour =  $hs->parse($cgi->param('ssn4'));
	my $aps_rep_id = EscQuote( $hs->parse($cgi->param('aps_rep_id')) );

    # getDateHTML changed, doesn't return anything now  prh
    #my $vc7 = EscQuote($cgi->param('dob'));
    my $vc7 = $cgi->param('monthdob') .'/'. $cgi->param('daydob') .'/'. $cgi->param('yeardob');
    my $bd = $cgi->param('monthdob') .$cgi->param('daydob') .$cgi->param('yeardob');

	my $phone1 =  $hs->parse($cgi->param('phone1'));
    $phone1 =~ s/\D+//g; # eat non digits in this phone number
    my $phone2 =  $hs->parse($cgi->param('phone2'));
    $phone2 =~ s/\D+//g; # eat non digits in this phone number
# property - keep same fields as LMSII
    my $vc8 = EscQuote( $hs->parse($cgi->param('bus_addr1')) );
    my $vc9 = EscQuote( $hs->parse($cgi->param('bus_addr2')) );
    my $vc10 = EscQuote( $hs->parse($cgi->param('bus_city')) );
    my $vc11 = EscQuote( $hs->parse($cgi->param('bus_state')) );
    my $vc12 = EscQuote( $hs->parse($cgi->param('bus_zip')) );

#   my $vc8 = EscQuote($cgi->param('bus_addr1'));
#   my $vc9 = EscQuote($cgi->param('bus_addr2'));

#	my $vc10 = EscQuote($cgi->param('bus_city'));
#	my $vc11 = EscQuote($cgi->param('bus_state'));

	my $vccust25 = EscQuote( $hs->parse($cgi->param('hear_about_us')) );

	my $work_loc = '';
	if ( $cgi->param('specialselect') eq 'Startek' || $cgi->param('specialselect') eq 'CSD'
		|| $cgi->param('specialselect') eq 'West Corporation' ) {	
		my ($work_city, $work_state) = split (/_/,$cgi->param('work_loc'));
		$work_loc = $cgi->param('work_loc');
#		$vc10 = $work_city;
#		$vc11 = $work_state;
#		$osr_id = EscQuote($cgi->param('super1'));
		}
	
	
#   my $vc12 = EscQuote($cgi->param('bus_zip'));
#   my $vc13 = EscQuote($cgi->param('bus_phone'));
#	$vc13 =~ s/\D+//g; # eat non digits in this phone number

    my $vc14 = EscQuote( $hs->parse($cgi->param('bus_name')) );
#   my $vc15 = EscQuote($cgi->param('bus_tin'));
    ## $vc16   vccust16 IS RESERVED for date of $10 signup bonus promotion, DO not use
    ##         vccust17 IS RESERVED for date of $5  signup bonus for OSR/RSAs, DO not use  5/16/2004 prh

    my $super1 = EscQuote( $hs->parse($cgi->param('super1')) );
    my $super2 = EscQuote( $hs->parse($cgi->param('super2')) );
    my $super3 = EscQuote( $hs->parse($cgi->param('super3')) );


    my $cuid = EscQuote(  $hs->parse($cgi->param('cuid')) || '' ); # vccust22
	my $vccust23 = EscQuote( $hs->parse($cgi->param('work_city')) );

	my $special = $cgi->param('special') || 'customer'; # Default for this
	my $specialselect = $cgi->param('specialselect');

    my $team = EscQuote(  $hs->parse($cgi->param('team_name')) || ''); # vccust24
	
	$hs->eof;
	
	
	if ($specialselect eq 'ER Solutions') {
		$email = 'randerson@e-r-solutions.com';
		if ($team eq 'Other') {
			$vccust23 = '';
		}
#----------------------------------------------------------------------------
# following changed on 04/22/2008 tracker#2284971 
#$team eq 'First Party Collections' : $email = 'mgranberry@e-r-solutions.com';
#$team eq 'Third Party Collections' : $email = 'npetak@e-r-solutions.com';
#----------------------------------------------------------------------------
	}
	if ($specialselect eq 'Oxford') {
			$email = 'william.secor@oxfmgt.com';
			$vccust23 = 'FL-Fort Pierce';
	}
	if ($specialselect eq 'Focus') {
		if ($team eq 'Tampa') {
			$email = 'cgarner@focusrm.com';
			$vccust23 = 'FL-Tampa';
		}
		elsif ($team eq 'Albuquerque') {
			$email = 'jason@focusrm.com';
			$vccust23 = 'NM-Albuquerque';
		}
		elsif ($team eq 'Other') {
			$email = 'jason@focusrm.com';
			$vccust23 = 'Other';
		}

	}
	if ($specialselect eq 'Allied') {
		$email = 'Vanessa.Fargie@iqor.com';
		$vccust23 = 'AZ-Chandler';
	}
	if ($specialselect eq 'CSD') {
		$vccust23 = 'SD-Sioux Falls';
	}
	if ($specialselect eq 'StarTek') {
		$vccust23 = 'VA-Lynchburg';
	}
	if ($specialselect eq 'EOS' || $specialselect eq 'EOS-CCA Tertiary') {
		$email = 'BustinDennell@EOS-CCA.com';
		$vccust23 = '';
	}

	if ($specialselect eq 'CCS') {
		$email = 'ddudley@corporate-collections.com';
		$vccust23 = 'OH-Beachwood';
	}
	if ($specialselect eq 'Alliance One') {
		$email = 'rebecca.small@allianceoneinc.com';
		$vccust23 = 'WA-Gigg Harbor';
	}


	if ($specialselect eq 'GCServ') {
		$email = 'monica.mitchell@gcserv.com';
		#$vccust23 = 'OH-Beachwood';

	}
#	my $ER_team = EscQuote( $cgi->param('er_team_name') || ''); # vccust24
    my $msg = '';
    $msg = $email.$vccust23;

 return( $STATUS_OK, $msg, 'archanak@ccionline.biz', 58299, 9, 'Archana') if $SKIP_SETUP;


    #--------------------------------------------------------------------------#
    #  Validation
    #--------------------------------------------------------------------------#

    ($email, $msg) = validate_email($email);
    if ($msg){
        return( $STATUS_INVALID, $msg, '','','','');
    }

    $msg = DUPLICATE_CHK( $lastfour, $phone1);
    if ($msg){
        return( $STATUS_INVALID, $msg, '','','','');
    }

	# see if they are on qwesthr, if so error
	#
	     my $qwesthr_sql = "
	     select 0 as cnt UNION
	     select count(emplid) as cnt from qwesthr with(nolock)
			 where rtrim(first_name) = ?
				and rtrim(last_name) = ?
 				and dob = ?
				and rtrim(home_city) = ?
                and emp_status = 'A' 
		order by 1 desc";
	
	my $found_emp;
    try {
		my $sth = $myDB->prepare($qwesthr_sql);
		$sth->execute($first,$last,$bd,$vc3) or die $sth->errstr;
		my $in_qwesthr = $sth->fetchrow_hashref();		
		$found_emp = $in_qwesthr->{cnt};
		}
	catch {
		DBInterface::writelog('graf07',"$thisfile", $_ );
	};

	if ($found_emp > 0) {
		$msg = 'Thank you for your interest in the Refer a Friend program.  
        We are having a system problem in creating your enrollment. 
        Please contact the Refer a Friend Program Headquarters at 866-968-2261 for assistance.';
	}

    if ($msg ne ''){
        return( $STATUS_INVALID, $msg,  '','','','' );
    }



    #--------------------------------------------------------------------------#
    #  Validation ok, set em up
    #--------------------------------------------------------------------------#
    my $server_name = $cgi->server_name();  # server name for debug
    $server_name =~ s/www\.//i;

    my $custID = "Select IsNull(max(cust_id), 0)+1 as internal_id From cust with (nolock)";
    
	my $internal_id;
	try {
		my $sth = $myDB->prepare($custID);
		$sth->execute() or die $sth->errstr;
		my $idHash = $sth->fetchrow_hashref();
		$sth->finish();
		$internal_id = $idHash->{internal_id};
	}
	catch {
		DBInterface::writelog('graf07',"$thisfile", $_ );
	};
		
    my $qwest_id = "CON".$internal_id;
	
	my $cust_type_id = 'NULL';
	
	if ($specialselect eq 'StarTek'){
		$cust_type_id = 242;
	}
	if ($specialselect eq 'CSD'){
		$cust_type_id = 244;
	}
	if ($specialselect eq 'Focus'){
		$cust_type_id = 301;
	}
	if ($specialselect eq 'West Manage'){
		$cust_type_id = 302;
	}	
	if ($specialselect eq 'EOS' || $specialselect eq 'EOS-CCA Tertiary'){
		$cust_type_id = 303;
	}
	if ($specialselect eq 'ER Solutions'){
		$cust_type_id = 304;
	}
	if ($specialselect eq 'Allied'){
		$cust_type_id = 305;
	}
	if ($specialselect eq 'Dex'){
		$cust_type_id = 325;
	}
	if ($specialselect eq 'CCS'){
		$cust_type_id = 243;
	}
	if ($specialselect eq 'Oxford'){
		$cust_type_id = 363;
	}
	if ($specialselect eq 'GCServ'){
		$cust_type_id = 368;
	}
	if ($specialselect eq 'AFNI'){
		$cust_type_id = 383;
	}
	if ($specialselect eq 'Alliance One'){
		$cust_type_id = 417;
	}
	if ( $specialselect eq 'South West Credit') {
		$cust_type_id = 452;
	}
    if ($specialselect) {
    $special = $specialselect;
    }
    if ($special eq 'leasing') {
		$cust_type_id = 386;
    }
	if ($special eq 'Arizona Public Service') {
		$cust_type_id = 418;
	}
	if ($special eq 'Teleperformance') {
		$cust_type_id = 477 ; #staging = 456, coop = 477
	}
    my $cust_insert = "Insert into cust(cust_id, client_id,									
                                    client_cust_no, cust_status,									
                                    name, Address1,
                                    Address2, City,
                                    State, Zip,
                                    Phone, Fax,
                                    Email, custom1,
                                    custom5, custom3,
                                    custom2, custom6,
				    custom7, custom8,		
                                    cust_url, default_fund_id,
				cust_type_id, payment_mode_id )
				values
                                    (" . $internal_id . ",50,"
                                    . "'".$qwest_id . "',1,"
                                    . "'$name',"
                                    . "'".delim_return($vc1) . "',"
                                    . "'".delim_return($vc2) . "',"
                                    . "'".delim_return($vc3) . "',"
                                    . "'".delim_return($vc4)."',"
                                    . "'".delim_return($vc5)."',"
                                    . "'".delim_return($phone1)."',"
                                    . "'".delim_return($phone2)."',"
                                    . "'".delim_return($email) ."',"
                                    . "'$program_id',
                                    '$special',
                                    '$fund_id',
                                    '$internal_id',
                                    '$aps_rep_id',
									'$super2',
									'$super3',
                                    '$server_name',
									'',
									$cust_type_id, 11)";

    	
	try {
		my $sth = $myDB->prepare($cust_insert);
		$sth->execute() or die $sth->errstr;
		$sth->finish();
	}
	catch {
		DBInterface::writelog('graf07',"$thisfile", $_ );
	};

    my $sql = "select max(contact_info_id)+1 as contact_info_id from contact_info with (nolock)";
    #$myDB->Sql($sql);
    #$myDB->FetchRow();
    #my %data = $myDB->DataHash();
	
	my $data;
	try {
		my $sth = $myDB->prepare($sql);
		$sth->execute() or die $sth->errstr;
		$data = $sth->fetchrow_hashref();
		$sth->finish();
	}
	catch {
		DBInterface::writelog('graf07',"$thisfile", $_ );
	};
	
    my $new_contact_id = $data->{contact_info_id};

    my $contact_info_id = CreateContact(
        50,
        '',
        $cgi->param('first'),
        '',
        $cgi->param('last'),
        '',
        '',
        delim_return($vc1),
        delim_return($vc2),
        delim_return($vc3),
        delim_return($vc4),
        delim_return($vc5),
        '',
        delim_return($phone1),
        delim_return($phone2),
        '',
        delim_return($email),
        '',
        'NULL',
        $internal_id,
        1,
        0
    );
    LinkContactToCust($contact_info_id, $internal_id, -1, 1);


    # create staff_record -----------

    my $staff_id = CreateStaffRecords(-1, $first, 1, -1, $client_id, 'CU', -1, -1 );
    my $password =  delim_return($phone1);
    $password =~ s/\D//g;
    $password = $first unless ( $password );
    $main::session{'name'} = $first;                 ############ WHY  FIX
    my $update = "update staff set LogonID = '$staff_id', password = '$password', contact_info_id = $new_contact_id, name = '$name' where staff_id = $staff_id";

	my $sth = $myDB->prepare($update);

   #if ( $myDB->Sql($update) ) 
	 if ( ! $sth->execute() ) {
        my $err = "Unable to set logonID";
        my $msg = $myDB->Error();
        dienicely($err, $update, $msg, $thisfile, 0,0,0,0,0);
		DBInterface::writelog('graf07',"$thisfile", $sth->errstr );
    }
	$sth->finish();
	
    #insert into contact_main table #
    my $ins = "insert into contact_main(cust_id, vccust1, vccust2, vccust3, vccust4, vccust5, vccust6, vccust7, vccust8, vccust9, vccust10, vccust11, vccust12, vccust13, vccust14, vccust15, vccust21, vccust22,vccust23, vccust24, vccust25, vccust28)
                    values($internal_id, '$vc1','$vc2','$vc3','$vc4','$vc5','','$vc7','$vc8','$vc9','$vc10','$vc11','$vc12','','$vc14', '','$lastfour','$cuid','$vccust23', '$team', '$vccust25', '$vccust28')";
    
	my $sth = $myDB->prepare($ins);
	
	if ( ! $sth->execute() ) {
        my $err = "Unable to create contact main";
        my $msg = $myDB->Error();
        #dienicely($err, $ins, $msg, $thisfile, 0,0,0,0,0);
		DBInterface::writelog('graf07',"$thisfile", $sth->errstr );
        #print $ins . "<br><br>";
    }
	
    #$myDB->FetchRow();
    #my %main_id = $myDB->DataHash();
	
	$sth->execute();
	my $main_id = $sth->fetchrow_hashref();
	$sth->finish();

    #insert into contact personnel table #
    my $ins2 = "insert into contact_personnel(contact_main_id,personnel_first_name, personnel_last_name,personnel_phone1, personnel_phone2,personnel_email,staff_id)
                    values($main_id->{contact_main_id},'$first','$last','$phone1','$phone2','$email',$staff_id)";
					
	my $sth = $myDB->prepare($ins2);				
					
    if ( ! $sth->execute() ) {
        my $err = "Unable to create contact personnel";
        my $msg = $myDB->Error();
        #dienicely($err, $ins2, $msg, $thisfile, 0,0,0,0,0);
		DBInterface::writelog('graf07',"$thisfile", $sth->errstr );
        #print $ins2 . "<br><br>";
    }
	$sth->finish();
	
       #insert into lkup_staff_application table # 
    my $lkup_insert = "insert into lkup_staff_application(staff_id, application_id) 
            values ($staff_id, 3)";
			
	my $sth = $myDB->prepare($lkup_insert);			
			
    if ( ! $sth->execute()  ) {
        my $err = "Unable to create lkup_staff_application";
        my $msg = $myDB->Error();
        #dienicely($err, $lkup_insert, $msg, $thisfile, 0,0,0,0,0);
		DBInterface::writelog('graf07',"$thisfile", $sth->errstr );
        #print $lkup_insert . "<br><br>";
    }
	$sth->finish();
	
    #insert into account table # 
    my $account_insert = "insert into account(cust_id, fund_id, is_active, payment_mode) 
            values($internal_id, $fund_id, 1, 11)";
		
	my $sth = $myDB->prepare($account_insert);
			
    if ( ! $sth->execute()  ) {
        my $err = "Unable to create account";
        my $msg = $myDB->Error();
        #dienicely($err, $account_insert, $msg, $thisfile, 0,0,0,0,0);
		DBInterface::writelog('graf07',"$thisfile", $sth->errstr );
        #print $account_insert . "<br><br>";
    }
	$sth->finish();
	
    $main::session{'name'} = $first." ".$last;

    $myDB->disconnect();
	
    return( $STATUS_OK, '', $email, $staff_id, $password, $name );
}

# ----------------------------------------------------
# is_every_char_same
#       pass: string
#       Returns 1 if all chars the same
#       Returns 1 also if empty string, string with 1 char
#       Returns 0 if any one char is different
# ----------------------------------------------------
sub is_every_char_same{
    my $str = shift;
    # If undef, split breaks, so fix it
    $str = '' unless defined $str;
    my @ar = split //, $str;
    my $first;
    my $same = 1;
    foreach my $char (@ar){
        # print "$char \n";
        $first = $char unless defined $first; # load first time
        $same = 0 if $first ne $char;
    }
    return $same;

}

#---------------------------------------------------------------------
#   validate_email
#---------------------------------------------------------------------
sub validate_email{
    my $email = shift;

    my $msg = '';

    # Validate the email if they entered it
    if ( $email ) {
        my $emailtest = valEmail($email);
        if ( $emailtest == -1 ) {
            $msg = 'Please enter a valid email address';
        }
    }

    return ($email, $msg);
}

#---------------------------------------------------------------------
#   validate
#---------------------------------------------------------------------

#---------------------------------------------------------------------
#   validate vendor
#---------------------------------------------------------------------
sub validate_vendor{
    my $cuid = shift;
    my $specialselect = shift;

    my $msg;

    my $myDB = DBInterface->new();

    # Duplicate registration Validation. Should not be registred in any RAF program
    my $sql = "select count(*) from cust with(nolock), contact_main with(nolock)
             where cust.cust_id = contact_main.cust_id
               and custom3 =  '649'
               and vccust22 = '$cuid'
    ";
	
	my $count_dupes;
	try {
		my $sth = $myDB->prepare($sql);
		$sth->execute() or die $sth->errstr;
		my @ref = $sth->fetchrow_array();
		$count_dupes = $ref[0];
	}
	catch {
		DBInterface::writelog('graf07',"$thisfile", $_ );
	};
	
    
    if ( !$msg and $count_dupes ) {
        $msg = "Thank you for your interest in the $specialselect Refer a Friend program.
        Our records indicate that you have previously registered for $specialselect Refer a Friend program. 
        Please log in with your registered user id and password or 
        contact the Refer a Friend Program Headquarters
        at 866-968-2261 if you need assistance.";
    }

    return $msg;
}

#---------------------------------------------------------------------
#   emailit
#   Send email if its valid
#---------------------------------------------------------------------
sub emailit{
    my $email = shift; 
    my $staff_id = shift;
    my $password = shift;
	my $name = shift;
	
	my $myDB = DBInterface->new();
	
    my $subject = "Welcome to the CenturyLink Partner Referral Program";

    if ( $email ne '' ) {

        my $bodymsglogin = "
Welcome $name! Thank you for enrolling in the CenturyLink Partner Referral Program. 
Below you will find your unique user ID (Password will be sent in seperare email) 
which will enable you to participate in the program. 
On the program webite and through the toll free number, you can do the following:

 - Make referrals
 - Track your previous referrals
 - View your card balance

Log in to the Web site at $HOST/index_raf.cgi or call the toll free number, 1 866-968-2261, 
to perform these same functions. When you log on or call you will need your user ID and password. 
All of your referrals are tracked using your unique user ID.

Your unique user ID is:     $staff_id

To track the status of your referrals or change your password at any time just:
	1. Log on to $HOST/index_raf.cgi
	2. Enter user ID and password
	3. Click on 'Check Referral Status'
	4. Click on a specific referral for more details or click on the \"Change Password\" tab

Once you have a sold referral, an American Express® -branded reward card will be sent to you.  Please allow 4-6 weeks for delivery.

Once you have a sold referral, a VISA® branded reward card will be sent to you at the address on file. 
Please allow 4-6 weeks for delivery. 
If you have questions please contact the program headquarters at refer.friend\@centurylink.com  or by phone at 1 866-968-2261. 
We look forward to receiving your referrals.

Sincerely,
The CenturyLink Partner Referral Program Team

";

      my $bodymsgpwd = "
Welcome $name! Thank you for enrolling in the CenturyLink Partner Referral Program. 
Below you will find your unique password (User Id will be sent in seperate email)
which will enable you to participate in the program. 
On the program webite and through the toll free number, you can do the following:

 - Make referrals
 - Track your previous referrals
 - View your card balance

Log in to the Web site at $HOST/index_raf.cgi or call the toll free number, 1 866-968-2261, 
to perform these same functions. When you log on or call you will need your user ID and password. 
All of your referrals are tracked using your unique user ID.

Your unique password is:    $password

To track the status of your referrals or change your password at any time just:
	1. Log on to $HOST/index_raf.cgi
	2. Enter user ID and password
	3. Click on 'Check Referral Status'
	4. Click on a specific referral for more details or click on the \"Change Password\" tab

Once you have a sold referral, an American Express® -branded reward card will be sent to you.  Please allow 4-6 weeks for delivery.

Once you have a sold referral, a VISA® branded reward card will be sent to you at the address on file. 
Please allow 4-6 weeks for delivery. 
If you have questions please contact the program headquarters at refer.friend\@centurylink.com  or by phone at 1 866-968-2261. 
We look forward to receiving your referrals.

Sincerely,
The CenturyLink Partner Referral Program Team

";
        
        #SendEmail($email, "","","refer.friend\@centurylink.com","$subject",$bodymsglogin."\n");
		my $bcc = "";
		my $from = "refer.friend\@centurylink.com";
		
					
		my $sql = "insert into ccimail (client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) values
			(50, 154, 0,'" . EscQuote($email) . "','','".EscQuote($bcc)."','" . EscQuote($from). "','" .EscQuote($subject). "','" . EscQuote($bodymsglogin). "')";
			
				
		try {
			my $sth = $myDB->prepare($sql);
			$sth->execute() or die $sth->errstr;
			$sth->finish();
		}
		catch {
			DBInterface::writelog('graf07',"$thisfile", $_ );
		};
		
		my $sql = "insert into ccimail (client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) values
			(50, 154, 0,'" . EscQuote($email) . "','','".EscQuote($bcc)."','" . EscQuote($from). "','" .EscQuote($subject). "','" . EscQuote($bodymsgpwd). "')";
		
		try {
		my $sth = $myDB->prepare($sql);
		$sth->execute() or die $sth->errstr;
		$sth->finish();
		}
		catch {
			DBInterface::writelog('graf07',"$thisfile", $_ );
		};
		
		#SendEmail($email, "","","refer.friend\@centurylink.com","$subject",$bodymsgpwd."\n");
        return $STATUS_OK;
    }
    else{
        return $STATUS_ERROR;
    }
}

#######################################################################
sub EscQuote($)     # 03/30/01 5:40PM  -- RF
					# Escapes single quotes
					# Use for preparing strings for SQL statements.
#######################################################################
{
    my ($delim_return) = @_;
	$delim_return =~ s/[']/''/gi;
    return $delim_return;
}