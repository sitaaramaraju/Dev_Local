#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use HTML::Strip;
use CCICryptography;
use DBInterface;
use Try::Tiny;
use CGI qw(:standard);
my $cgi = CGI->new();


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
	#$server = "/centurylinkyoucan/";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnect.com'){
    $server = "D:/centurylinkyoucan";
}
else {
    $server = "D:/centurylinkyoucan";
	#$server = "/centurylinkyoucan";
}

require "$server/cgi-bin/init.cgi";
require "$server/cgi-bin/delimeter.cgi";
require "$server/cgi-bin/contact.cgi";
require "$server/cgi-bin/encryptdata.pm";


my $db = DBInterface->new();
my $db2 = DBInterface->new();
my $myDB2 = DBInterface->new();

#my ( $db, $db2, $myDB2);
	my $thisfile = "subs.cgi";
	############################################################################
sub EscQuote($)     # 03/30/01 5:40PM  -- RF
					# Escapes single quotes
					# Use for preparing strings for SQL statements.
############################################################################
{
    my ($delim_return) = @_;
	$delim_return =~ s/[']/''/gi;
    return $delim_return;
}   ##EscQuote($)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub enrollBAU {

	my ($logon, $pwd, $name, $msg);
	my $hs = HTML::Strip->new();
	if ($cgi->param('NameForBotsBAU') eq "") {
		my $first = EscQuote($hs->parse( $cgi->param('first') ));
		my $osr_id = EscQuote($hs->parse( $cgi->param('osr_id') ));
		my $last = EscQuote($hs->parse( $cgi->param('last') ));
		   $name = "$first $last";
		my $vc1 = EscQuote($hs->parse( $cgi->param('addr1') ));
		my $vc2 = EscQuote($hs->parse( $cgi->param('addr2') ));
		my $vc3 = EscQuote($hs->parse( $cgi->param('city') ));
		my $vc4 = EscQuote($hs->parse( $cgi->param('state') ));
		my $vc5 = EscQuote($hs->parse( $cgi->param('zip') ));
		my $email = EscQuote($hs->parse( $cgi->param('email') ));
		my $lastfour = EscQuote($hs->parse( $cgi->param('ssn4') ));
		my $vc7 = EscQuote($hs->parse( $cgi->param('monthdob') )).'/'.EscQuote($hs->parse( $cgi->param('daydob') )).'/'.EscQuote($hs->parse( $cgi->param('yeardob') ));
 		my $bd =  EscQuote($hs->parse( $cgi->param('monthdob') )).'/'.EscQuote($hs->parse( $cgi->param('daydob') )).'/'.EscQuote($hs->parse( $cgi->param('yeardob') ));
 		my $phone1 =  EscQuote($hs->parse( $cgi->param('home_phone1') )).EscQuote($hs->parse( $cgi->param('home_phone2') )).EscQuote($hs->parse( $cgi->param('home_phone3') ));
			$phone1 =~ s/\D+//g; # eat non digits in this phone number
 		my $phone2 =  EscQuote($hs->parse( $cgi->param('cell_phone1') )).EscQuote($hs->parse( $cgi->param('cell_phone2') )).EscQuote($hs->parse( $cgi->param('cell_phone3') ));
		$phone2 =~ s/\D+//g; # eat non digits in this phone number
		my $vccust25 =  '' ; #$cgi->param('hear_about_us');
		my $vc8 = EscQuote($hs->parse( $cgi->param('bus_addr1') ));
		my $vc9 = EscQuote($hs->parse( $cgi->param('bus_addr2') ));
		my $vc10 = EscQuote($hs->parse( $cgi->param('bus_city') ));
		my $vc11 = EscQuote($hs->parse( $cgi->param('bus_state') ));
		my $vc12 = EscQuote($hs->parse( $cgi->param('bus_zip') ));
		my $vc13 = EscQuote($hs->parse( $cgi->param('bus_phone') ));
 		$vc13 =~ s/\D+//g; # eat non digits in this phone number
		my $vc14 = EscQuote($hs->parse( $cgi->param('bus_name') ));
		my $vc15 = EscQuote($hs->parse( $cgi->param('property_name') ));
		my $server_name = $cgi->server_name();  # server name for debug
		$server_name =~ s/www\.//i;
		my $custtype = $cgi->param('yes_mdu') || 0;
		if ($custtype eq "1") { $custtype = 479; 	 } else { $custtype = "null";}

		my $dup = check_enroll( $first, $last, $phone1, $email ) ;
		my ($to, $subject,$body, $sql, $sth, $data, $cust_id, $clientcust, $from, $contact_main_id, $sth2,$sql2); 
		if ($dup > 0) {
			$to = "james.miroslaw\@CenturyLink.com ";
			$from = "do_not_reply\@channelmanagement.com";
			$subject="CenturyLink® LMS Referral Program - Registration[Duplicate]";
			$body = "Please note $email made an attempt to enroll in the CenturyLink LMS Referral Program. ";
			$sql = "insert into ccimail (client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) values
			(50, 269, 0,'" . EscQuote($to) . "','','','" . EscQuote($from). "','" .EscQuote($subject). "','" . EscQuote($body). "')";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			$msg = qq[ There is an existing account associated with the email address entered.</br>
			Please contact the CenturyLink&reg; Program Headquarters at 1-877-299-0980 for assistance.<br> ];
		}
		else { # inserts start here
			$sql = "exec GetNextCustID";
			#$msg .= '101 '.$sql;
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$sth->finish();
				$cust_id = $data->{cust_id};
				$clientcust = "CON".$cust_id  ;
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

=head
	   $sql="Insert into cust(cust_id, client_id, client_cust_no, cust_status, name,
              Address1, Address2, City, State, Zip,
              Phone,Fax,Email,custom1,custom5,
              custom3, custom2, custom6, StoreType, cust_url, 
				payment_mode_id, cust_type_id)
              values ( ? ,50,? ,1, ?,
               ?,?,?,?,?,
               ?,?,?,'269','customer',
                '1036',?,?,'Residential',? ,
				11, ?)";
=cut
	   $sql2="Insert into cust(cust_id, client_id, client_cust_no, cust_status, name,
              Address1, Address2, City, State, Zip,
              Phone,Fax,Email,custom1,custom5,
              custom3, custom2, custom6, StoreType, cust_url, 
				payment_mode_id, cust_type_id)
              values ( $cust_id ,50, '$clientcust' ,1, '$name', '$vc1','$vc2','$vc3','$vc4','$vc5', '$phone1','$phone2','$email','269','customer', '1036','$cust_id','$osr_id','Residential','$server_name' , 11, $custtype)";
		#$msg .= '127 '.$sql2;

# $cust_id ,50, '$clientcust' ,1, '$name', '$vc1','$vc2','$vc3','$vc4','$vc5', '$phone1','$phone2','$email','269','customer', '1036','$cust_id','$osr_id','Residential',$server_name , 11, $custtype
=head
$cust_id , $clientcust, $name,
								$vc1,$vc2,$vc3,$vc4,$vc5,
								$phone1,$phone2,$email,
								$cust_id,$osr_id,$server_name ,
								$custtype
=cut
		#############
			try {
				$sth2 = $db2->prepare($sql2);
				$sth2->execute() or die $sth2->errstr;
				$sth2->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############


			my $contact_info_id = CreateContact( 50, '', $first, '',$last, '', 
									'', delim_return($vc1), delim_return($vc2), delim_return($vc3), delim_return($vc4),
									delim_return($vc5), '', delim_return($phone1), delim_return($phone2), '',
									delim_return($email), '', 'NULL', $cust_id, 1,
									0 );

			LinkContactToCust($contact_info_id, $cust_id, -1, 1);
			my $staff_id = CreateStaffRecords(-1, $first, 1, -1, 50, 'CU', -1, -1 );
			$pwd =  delim_return($phone1);
			$pwd =~ s/\D//g;
			$pwd = $first unless ( $pwd );
			$sql = "update staff set LogonID = ?, password = ?, contact_info_id = ?, name = ? where staff_id = ?";
			#$msg .= '156 '.$sql;
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($staff_id, $pwd, $contact_info_id, $name, $staff_id ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			#insert into contact_main
			$sql = "insert into contact_main(cust_id, vccust1, vccust2, vccust3, vccust4, vccust5, vccust6, vccust7, vccust8, vccust9, vccust10, vccust11, vccust12, vccust13, vccust14, vccust15, vccust18, vccust19, vccust20, vccust21, vccust23)
                    values(?, ?,?,?,?,?,'',?,?,?,?,?,?,?,?, ?, '', '', '',?,'')";
			#$msg .= '171 '.$sql;
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($cust_id,$vc1,$vc2, $vc3 , $vc4,$vc5, $vc7,$vc8,$vc9, $vc10 , $vc11, $vc12 ,$vc13,$vc14,$vc15, $lastfour    ) or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$contact_main_id = $data->{contact_main_id};
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			#insert into contact_personnel
			$sql = "insert into contact_personnel(contact_main_id,personnel_first_name, personnel_last_name,personnel_phone1, personnel_phone2,personnel_email,staff_id)
                    values(?,?,?,?,?,?,?)";

			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($contact_main_id, $first,$last,$phone1,$phone2, $email, $staff_id ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			$sql = "insert into lkup_staff_application(staff_id, application_id)values (?,?)";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($staff_id, 3 ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			$sql = "insert into account(cust_id, fund_id, is_active, payment_mode)  values($cust_id, 1036, 1, 11)";
			#$msg .= '213 '.$sql;
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############


			$logon = $staff_id;

			$msg = getEnrollMsg ($logon, $pwd);
			LMS_ENROLL_EMAIL ( $name, $email, $logon, $pwd);

		}# inserts end here

		#	($logon, $pwd, $name, $msg) = ('baulogon','baupwd','bauname','');

	}

	return ($logon, $pwd, $name, $msg);
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub enrollB2C {


	my ($logon, $pwd, $name, $msg);
	my $hs = HTML::Strip->new();
	if ($cgi->param('NameForBotsB2C') eq "") {
		my $prefix = EscQuote($hs->parse( $cgi->param('salutation') ));
		my $job_title = EscQuote($hs->parse( $cgi->param('job_title') ));
		my $first = EscQuote($hs->parse( $cgi->param('first') ));
		my $osr_id = EscQuote($hs->parse( $cgi->param('osr_id') ));
		my $last = EscQuote($hs->parse( $cgi->param('last') ));
		   $name = "$first $last";
		my $vc1 = EscQuote($hs->parse( $cgi->param('bus_addr1') ));
		my $vc2 = EscQuote($hs->parse( $cgi->param('bus_addr2') ));
		my $vc3 = EscQuote($hs->parse( $cgi->param('bus_city') ));
		my $vc4 = EscQuote($hs->parse( $cgi->param('bus_state') ));
		my $vc5 = EscQuote($hs->parse( $cgi->param('bus_zip') ));
		my $email = EscQuote($hs->parse( $cgi->param('email') ));
 		my $phone1 =  EscQuote($hs->parse( $cgi->param('bus_prim_phone1') )).'/'.EscQuote($hs->parse( $cgi->param('bus_prim_phone2') )).'/'.EscQuote($hs->parse( $cgi->param('bus_prim_phone3') ));
		$phone1 =~ s/\D+//g; # eat non digits in this phone number
 		my $phone2 =  EscQuote($hs->parse( $cgi->param('bus_sec_phone1') )).EscQuote($hs->parse( $cgi->param('bus_sec_phone2') )).EscQuote($hs->parse( $cgi->param('bus_sec_phone3') ));
 		my $contact_phone =  EscQuote($hs->parse( $cgi->param('contact_phone1') )).EscQuote($hs->parse( $cgi->param('contact_phone2') )).EscQuote($hs->parse( $cgi->param('contact_phone3') ));
		my $vccust25 = EscQuote($hs->parse( $cgi->param('hear_about_us') ));
		my $vc8 = EscQuote($hs->parse( $cgi->param('bus_addr1') ));
		my $vc9 = EscQuote($hs->parse( $cgi->param('bus_addr2') ));
		my $vc10 = EscQuote($hs->parse( $cgi->param('bus_city') ));
		my $vc11 = EscQuote($hs->parse( $cgi->param('bus_state') ));
		my $vc12 = EscQuote($hs->parse( $cgi->param('bus_zip') ));
		my $cust_name = EscQuote($hs->parse( $cgi->param('bus_name') ));
		my $vc14 = EscQuote($hs->parse( $cgi->param('bus_name_w9') ));
		my $vc15 = EscQuote($hs->parse( $cgi->param('property_name') ));
		my $vc18 = EscQuote($hs->parse( $cgi->param('industry') ));
		my $bus_type = EscQuote($hs->parse( $cgi->param('bus_type') ));
		my $withold_w9 = EscQuote($hs->parse( $cgi->param('withold_w9') ));
		my $bus_other_type = EscQuote($hs->parse( $cgi->param('bus_type_other_w9') ));
			if ($bus_type != 4) { $bus_other_type = ''; }
		my $ssn = EscQuote($hs->parse( $cgi->param('ssn1') )).EscQuote($hs->parse( $cgi->param('ssn2') )).EscQuote($hs->parse( $cgi->param('ssn3') ));
		my $ein = EscQuote($hs->parse( $cgi->param('ein1') )).EscQuote($hs->parse( $cgi->param('ein2') ));
		my $encrypteddata ;
		my $lastfour = EscQuote($hs->parse( $cgi->param('ssn3') ));
	if ($lastfour eq "") {
		$lastfour = substr(EscQuote($hs->parse( $cgi->param('ein2') )), 3, 4);
	}

	if ( length($ein) > 0 ) {
		$encrypteddata = $ein;
	} else {
		$encrypteddata = $ssn;
	}
	#$encrypteddata = EncryptData($encrypteddata);



		my $server_name = $cgi->server_name();  # server name for debug
		$server_name =~ s/www\.//i;
		my $custtype = $cgi->param('yes_mdu') || 0;
		if ($custtype eq "1") { $custtype = 479; 	 } else { $custtype = "null";}

		my $dup = check_enroll( $first, $last, $phone1, $email ) ;
		my ($to, $subject,$body, $sql, $sth, $data, $cust_id, $clientcust, $from, $contact_main_id, $sql2, $sth2); 
		if ($dup > 0) {
			$to = "james.miroslaw\@CenturyLink.com ";
			$from = "do_not_reply\@channelmanagement.com";
			$subject="CenturyLink® LMS Referral Program - Registration[Duplicate]";
			$body = "Please note $email made an attempt to enroll in the CenturyLink LMS Referral Program. ";
			$sql = "insert into ccimail (client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) values
			(50, 269, 0,'" . EscQuote($to) . "','','','" . EscQuote($from). "','" .EscQuote($subject). "','" . EscQuote($body). "')";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			$msg = qq[ There is an existing account associated with the email address entered.</br>
			Please contact the CenturyLink&reg; Program Headquarters at 1-877-299-0980 for assistance.<br> ];
		}
		else { # inserts start here
			$sql = "exec GetNextCustID";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$sth->finish();
				$cust_id = $data->{cust_id};
				$clientcust = "CON".$cust_id  ;
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

=head
	   $sql2="Insert into cust(cust_id, client_id, client_cust_no, cust_status, name,
              Address1, Address2, City, State, Zip,
              Phone,Fax,Email,custom1,custom5,
              custom3, custom2, custom6, StoreType, cust_url, 
				payment_mode_id, cust_type_id)
              values ( ? ,50,? ,1, ?,
               ?,?,?,?,?,
               ?,?,?,'269','customer',
                '1036',?,?,'Business',? ,
				1, ?)";
			  $cust_id , $clientcust, $name,
								$vc1,$vc2,$vc3,$vc4,$vc5,
								$phone1,$phone2,$email,
								$cust_id,$osr_id,$server_name ,
								$custtype
=cut
	   $sql2="Insert into cust(cust_id, client_id, client_cust_no, cust_status, name,
              Address1, Address2, City, State, Zip,
              Phone,Fax,Email,custom1,custom5,
              custom3, custom2, custom6, StoreType, cust_url, 
				payment_mode_id, cust_type_id)
              values ( $cust_id ,50, '$clientcust' ,1, '$name', '$vc1','$vc2','$vc3','$vc4','$vc5', '$phone1','$phone2','$email','269','customer', '1036','$cust_id','$osr_id','Business','$server_name' , 1, $custtype)";
			#############
			try {
				$sth2 = $db2->prepare($sql2);
				$sth2->execute() or die $sth2->errstr;
				$sth2->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			my $contact_info_id = CreateContact( 50, '', $first, '',$last, '', 
									'', delim_return($vc1), delim_return($vc2), delim_return($vc3), delim_return($vc4),
									delim_return($vc5), '', delim_return($phone1), delim_return($phone2), '',
									delim_return($email), '', 'NULL', $cust_id, 1,
									0 );

			LinkContactToCust($contact_info_id, $cust_id, -1, 1);
			my $staff_id = CreateStaffRecords(-1, $first, 1, -1, 50, 'CU', -1, -1 );
			
			$pwd =  delim_return($phone1);
			$pwd =~ s/\D//g;
			$pwd = $first unless ( $pwd );
			$sql = "update staff set LogonID = ?, password = ?, contact_info_id = ?, name = ? where staff_id = ?";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($staff_id, $pwd, $contact_info_id, $name, $staff_id ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############


			#insert into contact_main
			$sql = "insert into contact_main(cust_id, vccust1, vccust2, vccust3, vccust4, vccust5, vccust6, vccust7, vccust8, vccust9, vccust10, vccust11, vccust12, vccust13, vccust14, vccust15, vccust18, vccust19, vccust20, vccust21, vccust23)
                    values(?, ?,?,?,?,?,'','',?,?,?,?,?,?,?, ?, '', '', '',?,'')";

			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($cust_id,$vc1,$vc2, $vc3 , $vc4,$vc5, ,$vc8,$vc9, $vc10 , $vc11, $vc12 ,$phone1,$vc14,$vc15, $lastfour    ) or die $sth->errstr;
				$data = $sth->fetchrow_hashref();
				$contact_main_id = $data->{contact_main_id};
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			#insert into contact_personnel
			$sql = "insert into contact_personnel(contact_main_id,personnel_first_name, personnel_last_name,personnel_phone1, personnel_phone2,personnel_email,staff_id, ssn)
                    values(?,?,?,?,?,?,?, ?)";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($contact_main_id, $first,$last,$phone1,$phone2, $email, $staff_id, $encrypteddata ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############


			$sql = "insert into lkup_staff_application(staff_id, application_id)values (?,?)";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($staff_id, 3 ) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			$sql = "insert into account(cust_id, fund_id, is_active, payment_mode)  values(?, ?, ?, ?)";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($cust_id, 1036, 1, 1) or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			#$sql = "insert into custw9 (staff_id, cust_id, w9type, w9other, dateentered) values (?, ?, ? , ?,getdate())";
			$sql ="insert into custw9 (staff_id, cust_id, w9type, w9other, dateentered) values ($staff_id, $cust_id, $bus_type , '$bus_other_type',getdate())";
			#############
			try {
				$sth = $db->prepare($sql);
				#$sth->execute($staff_id, $cust_id, $bus_type , $bus_other_type) or die $sth->errstr;
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

			$logon = $staff_id;


			$msg = getEnrollMsg ($logon, $pwd);
			LMS_ENROLL_EMAIL ( $name, $email, $logon, $pwd);

		}# inserts end here

		#	($logon, $pwd, $name, $msg) = ('b2clogon','b2cpwd','b2cname','');

	}
	
	return ($logon, $pwd, $name, $msg);
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub check_enroll
{
	my ( $first, $last, $phone, $email )=@_;
	my $sql = "select 0 as cnt UNION
	select  count(staff_id) as cnt from staff with (nolock) where contact_info_id in (
	select contact_info_id from cust_contact with (nolock) where cust_id in (
	select cust_id from cust with (nolock) where custom1 = '269' and Phone=? and Email = ? )  ) order by 1 desc ";
	my ($sth, $data, $found);
	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute($phone, $email) or die $sth->errstr;
		$data = $sth->fetchrow_hashref();
		$found = $data->{cnt};
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############

	return $found;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub submitLead {

my $str = "";
my $hs = HTML::Strip->new();

	my ($s, $staff_id) =  CCICryptography::getEmpid($cgi->param('cci_id')); 
	my $prod_int  = EscQuote($cgi->param('prod_int'));

    my $cust_name = EscQuote($hs->parse( $cgi->param('cust_name') ));
    my $phone1 = EscQuote($hs->parse( $cgi->param('phone1') ));
    my $phone2 = EscQuote($hs->parse( $cgi->param('phone2') ));
    my $time_to_call = EscQuote($hs->parse( $cgi->param('time_to_call') ));
    my $lp_notes = EscQuote($hs->parse( $cgi->param('lp_notes') ));
    my $lead_state = EscQuote($hs->parse( $cgi->param('lead_state') ));
    my $lead_address = EscQuote($hs->parse( $cgi->param('lead_addr') )) ;
		if ($lead_address eq "") { $lead_address = "not provided";		}
    my $lead_address2 = 'Apt/Unit :'.EscQuote($hs->parse( $cgi->param('lead_addr2') ));
    my $mindt = EscQuote($hs->parse( $cgi->param('mindt') ));
	
	my $referral_source = 'Partner Site'; # Dont leave it blank
    my $BAN = EscQuote($hs->parse( $cgi->param('ban') ));
    my $prop_name = EscQuote($hs->parse( $cgi->param('prop_name') ));
    my $exist_cust = EscQuote($hs->parse( $cgi->param('exist_cust') ));
	
 	my $exist;
	if ($exist_cust eq 'yes') {$exist = 1;	}
	elsif ($exist_cust eq 'no') {$exist = 0;	}
            # Record the source website where the lead is submitted from. Eat 'www.' for uniformity.

	my $legacy = 1;
	#check for main_btn has been removed from LMSII - don't know when or why - keeping it that way for now
	#my ($validated, $mainbtn, $duplicate_lead, $sql) = check_mainbtn($phone1, $program_id, $fund_id, $myDB );


	my $class2 ="";
	if ($prod_int eq 'BRD' ) {
		$class2 .= qq [ 'High Speed Internet' ];
	}
	if ($prod_int eq 'DTV') {
		if ($class2 eq "") { $class2 .= qq [ 'TV' ]; }
		else {$class2 .= qq [ ,'TV' ];}
	}
	if ($prod_int eq 'WRL') {
		if ($class2 eq "") { $class2 .= qq [ 'Wireless' ]; }
		else {$class2 .= qq [ ,'Wireless' ];}
	}
	elsif ($prod_int eq 'DIV') {
		if ($class2 eq "") { $class2 .= qq [ 'Long Distance' ]; }
		else {$class2 .= qq [ ,'Long Distance' ];}
	}
	if ($class2 ne "") {
		$class2 = "and class2 in (".$class2.")";
	}
 	$hs->eof;
	my $sql = "select cust.cust_id as cust_id, staff.name
				from cust with(nolock)
				inner join cust_contact cc with(nolock) on cc.cust_id = cust.cust_id
				inner join staff with(nolock)on staff.contact_info_id = cc.contact_info_id
				where  staff.staff_id = ?";
	my ($sth, $data, $cust_id, $staff_name, $cdg,$lead_id,$prod_id, $sql2, $sth2, $pro_dt);
#############
try {
$sth = $db->prepare($sql);
$sth->execute($staff_id) or die $sth->errstr;
$data = $sth->fetchrow_hashref();
$cust_id = $data->{cust_id};
$staff_name = $data->{name};
$sth->finish();
}
catch {
	DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
};
##############

	$sql = "select case when job_title in ('Retail Store Manager','Kiosk Sales Manager') then 2 else 1 end as cdg
			from qwesthr with (nolock)
			inner join cust with (nolock) on (cust.custom6 = qwesthr.cuid or cust.custom6 = qwesthr.sap_id)
			and cust.cust_id = ?";
#############
try {
$sth = $db->prepare($sql);
$sth->execute($cust_id) or die $sth->errstr;
$data = $sth->fetchrow_hashref();
$cdg = $data->{cdg};
$sth->finish();
}
catch {
	DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
};
##############


			$sql = "insert into lp_lead (created_date, created_by, agency_id, lead_name,lead_phone, 
					lead_address,lead_address2,lead_city,lead_state, btn_id, 
					main_btn, client_id, lp_changed_by, program_id,  fund_id,
					warm_xfer, lead_group, source_id, lp_region_id, language_id)
                    values (getdate(), ?, ? , ?, ?,
                    ?, ?,'',?, ?,?, 50, ?, 269, 1036,
                    0, 56, 1, 5 ,1 )";

#############
try {
$sth = $db->prepare($sql);
$sth->execute($staff_id , $cust_id,$cust_name,$phone1, $lead_address, $lead_address2, $lead_state, $phone1,$phone1,$staff_id ) or die $sth->errstr;
$data = $sth->fetchrow_hashref();
$lead_id = $data->{lp_lead_id};
$sth->finish();
}
catch {
	DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
};
##############
            (my $server_name = lc($cgi->server_name()) || 'unknown_269isr_1036_929_'.$cust_id.'_'.$lead_id) =~ s/^www\.// ;

	$sql = "insert into lkup_qwest_opts (lp_lead_id, mobile_no, cust_type, best_contact_time, server_name, 
			referral_source, icustom1, employer, existing_customer, work_phone)
			values(? , ?, 'Residential', ?,  ?, 
				? , ?, ?, ? , ?)";
#############
try {
$sth = $db->prepare($sql);
$sth->execute($lead_id, $phone2, $time_to_call, $server_name, $referral_source, $cdg, $prop_name, $exist, $BAN  ) or die $sth->errstr;
$sth->finish();
}
catch {
	DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
};
##############

			
	$sql = "insert into lp_lead_history (lp_lead_id, action, staff_id, history_date, source_id, user_ip)
                    values (?, 'Referral created',?, getdate(), 1 , ?)";

#############
try {
$sth = $db->prepare($sql);
$sth->execute($lead_id, $staff_id, $ENV{REMOTE_HOST} ) or die $sth->errstr;
$sth->finish();
}
catch {
	DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
};
##############


	my $movindt = '';
			if ($mindt ne '' || length($mindt)>0) {
				$movindt = " Move In date $mindt";
			}
 	$sql = "update lp_lead set lead_status_change_dt = getdate(),
				lp_notes = (case when ISNULL(lp_notes,'')='' then 
				convert(varchar,getdate())+' $staff_name'+char(13)+char(10)+'$movindt'
				else 
				convert(varchar,getdate())+' $staff_name'+char(13)+char(10)+'$movindt'+char(13)+char(10)+'----------'+char(13)+char(10)+lp_notes
				end )
				where lp_Lead_id = ?";
#############
try {
$sth = $db->prepare($sql);
$sth->execute($lead_id ) or die $sth->errstr;
$sth->finish();
}
catch {
	DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
};
##############



			$sql="select prod.prod_id 
				from prod with (nolock)
				inner join fund_prod fp with (nolock) on fp.prod_id = prod.prod_id
				inner join lkup_prod_group lpg with (nolock) on lpg.prod_id = prod.prod_id
				where fp.fund_id = 1036 and lpg.prod_group_id = 56
				and ProdIsActive = 1 and leadpro_active = 1 $class2 order by prod.prod_id";
			my $success = eval {
			$sth = $db->prepare($sql) or die $db->errstr;
			$sth->{PrintError} = 0;
			$sth->execute()  or die $sth->errstr;

				while(my $pro_dt = $sth->fetchrow_hashref){
					$prod_id = $pro_dt->{prod_id};
					$sql2 = "insert into lkup_lead_product_interest (prod_id, lp_lead_id)
                        values ($prod_id, $lead_id)";

				#############
				try {
					$sth2 = $db2->prepare($sql2);
					$sth2->execute() or die $sth2->errstr;
					$sth2->finish();
				}
				catch {
					DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
				};
				##############

				}

			};
			unless($success) {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			}


$str = "  <br> <br>  The information you provided has been routed to the
            appropriate CenturyLink service rep and your customer will be contacted within 2 business days.	
            Your reference number for this submission is $lead_id ";

 my $str3 = LMS_EMAIL_NOTIFY( $lead_id , $staff_name, $staff_id);

return $str;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub LMS_EMAIL_NOTIFY  {
    my ($lead_id , $staff_name, $staff_id) = @_;

	my ( $sendto, $lead_open_flag) = get_emails($lead_id );


	my ($sth,  $prod_dt, $email_dt, $commid, $sth2, $sql);
    #--
#update lead status after sending email
if ($lead_open_flag == 1) {
        $sql = " update lp_lead set lead_status_id = 1 where lp_lead_id = ?" ;
	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute($lead_id) or die $sth->errstr;
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############


}
#--
	   my $sql = "update lp_lead set lp_notes = convert(varchar,getdate())+char(13)+char(10)+'Email notification sent to $sendto.'+char(13)+char(10)+'----------'+char(13)+char(10)+isnull(lp_notes,'')
         where lp_lead_id = ?";

	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute( $lead_id) or die $sth->errstr;
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############


my $str;
my ( $date_created , $data);

#	 , opts.server_name,  lp_lead.lp_notes as lp_notes,
#   opts.best_contact_time as best_contact_time,  opts.cust_type  as cust_type


my	$sql2 = " select  isnull(lp_lead.btn_id,'') as btn_id, isnull(lp_lead.lead_name,'') as lead_name,
	convert(varchar,created_date,1) + ' ' + convert(varchar,created_date,108) as date_created ,
		(select name+' ['+client_cust_no+']' as refname from cust with(nolock) where cust.client_id = 50 and cust_id = lp_lead.agency_id)  as refname,
		ISNULL(rtrim(lp_lead.lead_address),'') as lead_address,   ISNULL(rtrim(lp_lead.lead_address2),'') as lead_address2, 
		ISNULL(lp_lead.lead_state,'') as lead_state, employer, main_btn, opts.server_name,
 	rtrim(lp_lead.lp_notes) as lp_notes, opts.best_contact_time as best_contact_time,
		 ISNULL(opts.best_contact_time,'') as best_contact_time, ISNULL(opts.cust_type,'') as cust_type 
            from lp_lead with (nolock)
			inner join lkup_qwest_opts opts with (nolock) on opts.lp_lead_id = lp_lead.lp_lead_id
             where  lp_lead.lp_lead_id = $lead_id";
	$sql2 = "  select lp_lead.btn_id  as btn_id,  lp_lead.lead_name  as lead_name, 
 convert(varchar,created_date,1) + ' ' + convert(varchar,created_date,108) as date_created , 
 (select name+' ['+client_cust_no+']' as refname from cust with(nolock) where cust.client_id = 50 and cust_id = lp_lead.agency_id) as refname, 
 lp_lead.lead_address  as lead_address,  lp_lead.lead_address2  as lead_address2, 
  lp_lead.lead_state  as lead_state, employer, main_btn

   from lp_lead with (nolock) inner join lkup_qwest_opts opts with (nolock) on opts.lp_lead_id = lp_lead.lp_lead_id where lp_lead.lp_lead_id = $lead_id";

	#$str .= $sql2;
	my $data2;
	#############
	try {
		$sth2 = $db2->prepare($sql2);
		$sth2->execute() or die $sth2->errstr;
		$data2 = $sth2->fetchrow_hashref(); 
		$date_created = $data2->{date_created};
		$sth2->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############


    my $language = $data2->{language_id} == 2 ? 'Spanish' : 'English';
    my $warm     = 'No';
	my $program_id = 269 ;
    my $product_interest = '';
    $sql = "select dbo.fnGetLeadProductsInterest (?) as product";
	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute($lead_id) or die $sth->errstr;
		$prod_dt = $sth->fetchrow_hashref();
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############

$sql = "select email_template_id as temp_id ,rtrim(email_templates.email_body) as body,
		rtrim(email_templates.email_subject) as subject, rtrim(email_templates.email_footer) as footer,
			rtrim(email_templates.email_from_address) as from_add
		from email_templates with(nolock) 
		where email_templates.program_id = 269
		and email_templates.ext_status_id <1
		and email_templates.fund_id = 1036
		and email_templates.is_active = 1 ";
#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute() or die $sth->errstr;
		$email_dt = $sth->fetchrow_hashref();
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
##############


	my $body = $email_dt->{body};
	my $blank ='';
	my $bcc='';

	$str .= 'dtct = '.$date_created.' company = '.$data2->{lead_company_name};
#replace
	my $temp_id = $email_dt->{temp_id};
	my $subject = $email_dt->{subject};
    my $from = $email_dt->{from_add};
	#replace


   $subject =~ s/\$lead_id/$lead_id/gi;
   $body =~ s/\$footer/$email_dt->{footer}/gi;
   $body =~ s/\$lead_id/$lead_id/gi;
   $body =~ s/\$date_created/$data2->{date_created}/gi; 
   $body =~ s/\$refname/$data2->{refname}/gi; 
   $body =~ s/\$product/$prod_dt->{product}/gi; 
   $body =~ s/\$btn_id/$data2->{btn_id}/gi; 
   $body =~ s/\$warm/$warm /gi; 
   $body =~ s/\$language/$language/gi; 
   $body =~ s/\$lead_name/$data2->{lead_name}/gi;
   $body =~ s/\$lead_company_name/$blank/gi; 
   $body =~ s/\$main_btn/$data2->{main_btn}/gi; 
   $body =~ s/\$mobile_no/$blank/gi; 
   $body =~ s/\$lead_phone/$blank/gi; 
   $body =~ s/\$lead_email/$blank/gi; 
   $body =~ s/\$best_contact_time/$data2->{best_contact_time}/gi; 
   $body =~ s/\$prop_name/$data2->{employer}/gi; 
   $body =~ s/\$addr1/$data2->{lead_address}/gi; 
   $body =~ s/\$addr2/$data2->{lead_address2}/gi; 
   $body =~ s/\$best_contact_date/$blank/gi; 
   $body =~ s/\$lead_state/$data2->{lead_state}/gi; 
   $body =~ s/\$cust_type/$data2->{cust_type}/gi; 
   $body =~ s/\$lead_source/$blank/gi; 
   $body =~ s/\$lp_notes/$data2->{lp_notes}/gi; 
   $body =~ s/\$email_footer/$blank/gi; 
   $body =~ s/\$server_name/$data2->{server_name}/gi; 
 
	$body = EscQuote($body);
   #$body.="
   #when live will go to $sendto ";
   #$sendto = "archanak\@ccionline.biz";
#-- email thru db
		$sql = "insert into lp_comm(lp_lead_id, staff_from_id, email_template_id, email_body, email_subject, date_created, email_format)
                values(?, ?, ?, ?, ?, getdate(), '1')";
			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute($lead_id, $staff_id, $temp_id, $body, $subject) or die $sth->errstr;
				$commid = $sth->fetchrow_hashref();
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############


        $sql = "insert into lp_comm_to(lp_comm_id, lp_lead_id, date_sent, sentto_staff_id, sentto_name, sentto_address, sentto, ccto, bccto)
                values($commid->{lp_comm_id}, $lead_id, getdate(), 0, '$sendto', '$sendto', 1, 0, 0)";

			#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
			##############

		$sql = "insert into lp_lead_history(lp_lead_id, action, staff_id,source_id, history_date)
                values($lead_id, 'Email sent to $sendto: $subject', 34081, 1,getdate())";

		#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
		##############


		 $sql = "insert into ccimail (client_id, program_id, date_created, lp_lead_id, staff_id, subject, tofield, ccfield, bccfield, fromfield, longbody, ctype)
					values (50, 269, getdate(), $lead_id, 1, '$subject', '$sendto', '','$bcc', '$from','$body','text/html') ";
		#$str .= '937 '.$sql;
		#############
			try {
				$sth = $db->prepare($sql);
				$sth->execute() or die $sth->errstr;
				$sth->finish();
			}
			catch {
				DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
			};
		##############
		
		return $str;

 }    
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub get_emails  { 
	my ($lead_id) = @_;
	my $emp_email = '';
	my $job_title = '';
	my $lead_open_flag = 0;
	my ($sth, $dt, $cac_cuid);
    my $sql = "select agency_id, lp_lead_id,cust.custom6 ,
				case when isnull(custom6,'') <> '' then 
				(select job_title from qwesthr with (nolock) where (isnull(cuid,'') = cust.custom6 or isnull(sap_id,'') = cust.custom6) )
				else '' end as job_title,
				case when isnull(custom6,'') <> '' then 
				(select email from qwesthr with (nolock) where (isnull(cuid,'') = cust.custom6 or isnull(sap_id,'') = cust.custom6) )
				else '' end as 	email
				from lp_lead with (nolock) 
				inner join cust with (nolock) on cust.cust_id = lp_Lead.agency_id
				where lp_Lead_id = ?";
	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute($lead_id) or die $sth->errstr;
		$dt = $sth->fetchrow_hashref();
		$cac_cuid = uc($dt->{custom6});
		$emp_email = $dt->{email};
		$job_title = $dt->{job_title};
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############

	if ($emp_email eq "") {
		$emp_email = "Laura.Graber\@centurylink.com";
	}

	if ($job_title eq 'Outside Sales Representative' || $job_title eq 'Customer Relations Specialist') {
		$emp_email.= ', cdgraf@centurylink.com';
	}
	if (($job_title eq 'Retail Store Manager') || ($job_title eq 'Kiosk Sales Manager')) {
		$lead_open_flag=1;
	}
	if ($job_title eq 'Customer Relations Specialist') {
		$emp_email.= ' , Lisa.Gereg@centurylink.com';
		$lead_open_flag=1;
	}

return ($emp_email, $lead_open_flag);

}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getEnrollMsg {
my ($logon, $pwd) = @_;
=head
                          <tr><td align="left" valign="top">&nbsp; </td></tr>
                           <tr><td align="left" valign="top">User ID: $logon  </td> </tr>
							<tr><td align="left" valign="top">&nbsp; </td></tr>
						<tr><td align="left" valign="top">Password:  $pwd </td></tr>
=cut						
my $str = qq[ <tr> <td align="left" valign="top" class="Enrollcopy">
                          Thank you for enrolling in the CenturyLink Referral Rewards Program. 
							  <a href="../index_lmsii07.cgi"  class="FAQLink">Click here</a> to get started.                                                                                    </td>
                          </tr>

                     <tr>
 <td align="left" valign="top"><table width="500" border="0" cellspacing="2" cellpadding="2">
  <tr><td width="146">&nbsp;</td><td width="354"></td></tr></table></td>
</tr>
<tr>
<td align="left" valign="top">Your Login Credentials are emailed to the email address provided on enrollment form. Use your user ID and password to participate in the program on this Web site or through the toll free number. You can do all of this:                                                                                    </td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr><td align="center"><div align="left"><ul>
<li>Make referrals</li>
<li>Track your previous referrals</li>
<li>Get program guidelines and updates</li>
<li>Print helpful marketing materials to assist in your referrals </li>
</ul>
</div></td>
</tr> ];

return $str;
}
 #------------------------------------------------------------------------------------------------------------------------------------------------------------
 sub getLeadList {
	 	my $cci_id = @_;
	my ($s, $staff_id) =  CCICryptography::getEmpid($cgi->param('cci_id')); 
		my $str = "";
		my $sql = "select cust.cust_id as cust_id, staff.name
				from cust with(nolock)
				inner join cust_contact cc with(nolock) on cc.cust_id = cust.cust_id
				inner join staff with(nolock)on staff.contact_info_id = cc.contact_info_id
				where  staff.staff_id = ?";
my ($sth, $data, $cust_id , $ldt);
#############
try {
$sth = $db->prepare($sql);
$sth->execute($staff_id ) or die $sth->errstr;
$data = $sth->fetchrow_hashref();
$cust_id = $data->{cust_id};
$sth->finish();
}
catch {
	DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
};
##############
  $sql = "select lp_lead.lp_lead_id, convert(varchar,created_date,1) as ctdt,lead_name, main_btn, 
		case when isnull(lead_status_id ,0) = 0 then 'New'
		when isnull(lead_status_id ,0) = 1 then 'Open' else dbo.func_getstatus (lead_status_id, 154) end as ldst
		from lp_lead with (nolock) 
		inner join lkup_qwest_opts opts with (nolock) on opts.lp_lead_id = lp_lead.lp_lead_id
		where program_id = 269 and agency_id = ?
		order by lp_lead_id desc";

	my $success = eval {
			$sth = $db->prepare($sql) or die $db->errstr;
			$sth->{PrintError} = 0;
			$sth->execute($cust_id)  or die $sth->errstr;

		while( $ldt = $sth->fetchrow_hashref){
				$str .= qq[
						<tr>
							<td align="left" class="LEtitle" valign="top" >$ldt->{lp_lead_id}</td>
							<td align="left" class="LEtitle" valign="top" >$ldt->{ctdt}</td>
							<td align="left"  class="LEtitle" valign="top" >$ldt->{lead_name}</td>
							<td align="left"  class="LEtitle" valign="top" >$ldt->{main_btn}</td>
							<td align="left"  class="LEtitle" valign="top" >$ldt->{ldst}</td>
						</tr>
				];
		}
		$sth->finish();	

	};
	unless($success) {
		DBInterface::writelog('qwestconnect07',"$thisfile", $@ );
	}

	return $str;
 }
 #------------------------------------------------------------------------------------------------------------------------------------------------------------
 sub send_email {
    my($name ,$email ,$phone , $timetocall ,$refnum , $issue , $explanation ) = @_;


 	my $bcc = '';# 'archanak@ccionline.biz';
	my $msg  = qq[<tr>
                        <td colspan="3" align="center" valign="top">Thank You for your question.  <br><br>
			An email has been sent to the CenturyLink Connect Program Headquarters.<br><br>
			You will hear from us shortly.</td>
                      </tr>];

 my $sendto = 'refer.friend@centurylink.com';

    my $subject = "CenturyLink Connect : Quick Form";
 
          my $sql = "select convert(datetime, getdate() ) as thd ";
		  my ($sth,$data,$date);
	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute() or die $sth->errstr;
		$data = $sth->fetchrow_hashref();
		$date = $data->{thd};
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
##############
 
	  my $bodymsg = "
CenturyLink Connect Quick Form 

Sent:           $date
From:           $name
Email:          $email
Phone:          $phone
Time to call:   $timetocall
Referral:       $refnum
Issue:          $issue
Explanation:        $explanation

";

         $sql = "insert into ccimail (client_id, program_id,  tofield, ccfield, bccfield, fromfield, subject,longbody) values
				(50, 269, '$sendto', '', '$bcc',  'do_not_reply\@ccionline.biz', '$subject', '$bodymsg' ) ";
#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute() or die $sth->errstr;
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
##############


		#$msg = $msg . $sql;
	return $msg;
}
 #------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getFooter {
	my $cci_id = @_;

print qq[
	                                <tr>
                                    <td align="left" valign="top">
           <img src="images/Sub_bottom.gif" width="913" height="16" /></td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
<td>
  <img src="images/bottombuffer.gif" width="954" height="15" /></td>
  </tr>
   <tr>
   <td width="954" height="66" align="center" valign="middle" background="images/bottom_amex.gif"><table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
<tr>
<td align="center" valign="top" class="Legalcopy" nowrap>&copy;<script type="text/javascript">
    var dteNow = new Date();
    var intYear = dteNow.getFullYear();
    document.write(intYear);
</script> CenturyLink, Inc. All Rights Reserved. The CenturyLink mark, pathways logo, CenturyLink mark,
               Q lightpath logo and certain CenturyLink product names are the property of CenturyLink, Inc.</td>
</tr>
<tr>
<td align="center" valign="top" class="Legalcopy">
<a href="#" class="revLink" onclick="MM_openBrWindow('http://www.centurylink.com/legal/','','')">Legal Notices</a>
| <a href="#" class="revLink" onclick="MM_openBrWindow('http://www.centurylink.com/privacy/','','')">Privacy Policy</a>

];
#if ($cci_id ne "") {
#	print qq[ | <a href="../raf_logout.cgi" class="revLink">Logout</a>| <a href="SiteMap.cgi" class="revLink">Site Map </a>];
#}
print qq[
</td>
</tr>
</table>
<table width="954">

];
#| <a href="../raf_logout.cgi" class="revLink">Logout</a>

}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getHeader {
	my ($cci_id, $s, $staff_id) = @_;
 

print qq[
	
	<table width="954" border="0" cellspacing="0" cellpadding="0"> 
	<form name="navForm" action="" method="post">
		<input type="hidden" name="cci_id" value="$cci_id">
     <tr>
			<td align="center" valign="top"><img src="images/ctl_con_logo4.png" width="954" height="324" /></td>
      </tr>
      <tr>

			<td align="left" valign="top"><table width="954" border="0" cellspacing="0" cellpadding="0">
       <tr bgcolor="#b0c716" >
            <td width="35" align="left" valign="top"><img src="images/nav_blank.gif" width="35" height="31" /></td>
            <td width="187" align="left" valign="top">
	];

if ($staff_id > 100 and $s > 100) {
	print qq [
		<a href="#" onclick="logoutUser($s, $staff_id);" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image58','','images/Logout_blue.jpg',1)"><img src="images/Logout_white.jpg" name="Image58" width="113" height="29" border="0" id="Image58" /></a>
		];
}
else {
	print qq [
		<a href="../index_lmsii07.cgi" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image28','','images/Sub_nav_home_on.gif',1)"><img src="images/Sub_nav_home_off.gif" name="Image28" width="187" height="31" border="0" id="Image28" /></a>
		];
}

#should be 187 X 31
				
print qq[
			</td>
            <td width="311" align="left" valign="top">
				<a href="#" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image29','','images/Sub_nav_about_on.gif',1)"><img src="images/Sub_nav_about_off.gif" name="Image29" width="311" height="31" border="0" id="Image29" onmouseover="MM_showMenu(window.mm_menu_0221111945_0,0,31,null,'Image29')" onmouseout="MM_startTimeout();" /></a></td>
            <td width="177" align="left" valign="top">
				<a href="#" onClick="document.navForm.action='faqs.cgi';document.navForm.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image30','','images/Sub_nav_faq_on.gif',1)"><img src="images/Sub_nav_faq_off.gif" name="Image30" width="177" height="31" border="0" id="Image30" /></a>
			</td>
            <td width="244" align="left" valign="top"> 
				<a href="#" onClick="document.navForm.action='contact.cgi';document.navForm.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image31','','images/Sub_nav_contact_on.gif',1)"><img src="images/Sub_nav_contact_off.gif" name="Image31" width="244" height="31" border="0" id="Image31" /></a>
			</td>            
          </tr>
		</form>

        </table>
	];

}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
if ($cgi->param('logout') == 1) { 
		my $staff_id = param('staff_id');
		my $session_id = param('session_id');
		
		my $sql1 = "delete from user_session where user_session_id = ?";
		my $sql2 = "delete from cookie_session where session_id = ?";
		my $sth1 = $db->prepare($sql1);
		my $sth2 = $db->prepare($sql2);
		
		$sth1->execute($session_id);
		$sth2->execute($session_id);
				
		$sth1->finish();	
		$sth2->finish();
		
		exit;
 }

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getLeadFormHeader {
	my ($cci_id) = @_;
	my ($s, $staff_id) =  CCICryptography::getEmpid($cci_id); 

	my ($program_id, $fund_id) = (269, 1036);
	my ($ref, $year, $ref_award, $name, $cust_id);
	my $needW9 = -1;

	my $sql = "select cust.cust_id as cust_id
				from cust with(nolock)
				inner join cust_contact cc with(nolock) on cc.cust_id = cust.cust_id
				inner join staff with(nolock)on staff.contact_info_id = cc.contact_info_id
				where  staff.staff_id = ? ";
	my $sth = $db->prepare($sql);
			$sth->execute( $staff_id  );
		my  $data = $sth->fetchrow_hashref();
			$cust_id = $data->{cust_id};
			$sth->finish();
		$sql = "select 0 as cnt UNION 
				select count(lp_Lead.lp_lead_id) as cnt
				from lp_lead with (nolock)
				inner join lkup_qwest_opts opts with (nolock) on opts.lp_lead_id = lp_lead.lp_Lead_id
				where agency_id = ? and program_id = ? and fund_id = ?
				and created_date > convert(datetime, '1/1/' + convert(varchar(4), datepart(yyyy, getdate()-1)))	
				order by 1 desc	";
		$sth = $db->prepare($sql);
		$sth->execute( $cust_id,$program_id, $fund_id );
		$data = $sth->fetchrow_hashref();
		$ref = $data->{cnt};
		$sth->finish();
		$sql = "select 0 as pmt UNION select isnull(sum( isnull(net,0) ),0) as pmt
				from qwest_visa_load with (nolock)
				where cust_id = ? and program_id = ? and fund_id = ?
				and created_date > convert(datetime, '1/1/' + convert(varchar(4), datepart(yyyy, getdate()-1)))	
				and eligible = 1 order by 1 desc	";
		$sth = $db->prepare($sql);
			$sth->execute( $cust_id,$program_id, $fund_id );
			$data = $sth->fetchrow_hashref();
			$ref_award = $data->{pmt};
			$sth->finish();
		$sql = " select cc.name ,convert(varchar(4), datepart(yyyy, getdate()-1)), 
				isnull((select count(custw9_id) from custw9 with (nolock) where custw9.cust_id = cust.cust_id),0) as haveEntry,
				case when isnull(dateentered,'01/01/1900') = '01/01/1900'then 0 else 1 end as haveW9,
				case when isnull( cp.ssn,'') = '' then 0 else 1 end as haveSSN
				from cust with (nolock)
				inner join contact_main cm with (nolock) on cm.cust_id = cust.cust_id
				inner join cust_contact cc with (nolock) on cc.cust_id = cust.cust_id
				inner join account with (nolock) on account.cust_id = cust.cust_id
				left outer join contact_personnel cp with (nolock) on cp.contact_main_id = cm.contact_main_id
				left outer join custw9 with (nolock) on custw9.cust_id = cust.cust_id
				where cust.cust_id =  ? and account.fund_id = ?";
		$sth = $db->prepare($sql);
			$sth->execute( $cust_id, $fund_id );
			$data = $sth->fetchrow_hashref();
			$name = $data->{name};
			$year = $data->{yr};
			$sth->finish();
		if ($data->{haveEntry} > 0  && $data->{haveSSN} > 0) {
			$needW9 = -1;
		}
		else {
			$needW9 = 1;
		}
	my $str = "Welcome, $name <br />
				You have submitted $ref referrals in $year.<br /> 
				Your $year awards total is \$$ref_award for sold leads.";
	if ($needW9 <= 0) { $staff_id = -1; }
	return ($str, $needW9, $staff_id);
	
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getLeftTable {

	my ($id, $cci_id) = @_; 

	my $td = qq[<a href="#" onClick="document.navForm2.action='lmsii_leadchk.cgi';document.navForm2.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image16','','images/SubmitNav2_top_on.gif',1)"><img src="images/SubmitNav2_top_off.gif" name="Image16" width="195" height="33" border="0" id="Image16" /></a> ];
	if ($id == 2) { # on lead list - send lead form
		$td = qq[<a href="#" onclick="document.navForm2.action='lmsii_submitreferral.cgi';document.navForm2.submit();" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image15','','images/SubmitNav1_top_on.gif',1)"><img src="images/SubmitNav1_top_off.gif" name="Image15" width="195" height="28" border="0" id="Image15" /></a> ];
	}


	my $str = qq[
			<form name="navForm2" action="" method="post">
		<input type="hidden" name="cci_id" value="$cci_id">
	
		<table width="195" border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td align="left" valign="top"><img src="images/SubmitNav_top.gif" width="195" height="22" /></td>
			</tr>
			<tr> 
				<td align="left" valign="top">$td</td>
			</tr>
			<tr>
				<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('https://www.myprepaidcenter.com/','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image17','','images/checkbalance_on.gif',1)"><img src="images/checkbalance_off.gif" name="Image17" width="195" height="41" border="0" id="Image17" /></a></td>
			</tr>
			</form>
			<tr>
				<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('https://www.myprepaidcenter.com/','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image22','','images/transactionsummary_on.gif',1)"><img src="images/transactionsummary_off.gif" name="Image22" width="195" height="45" border="0" id="Image22" /></a></td>
			</tr>
			<tr>
				<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('https://www.myprepaidcenter.com/','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image18','','images/SubmitNav4_top_on.gif',1)"><img src="images/SubmitNav4_top_off.gif" name="Image18" width="195" height="45" border="0" id="Image18" /></a></td>
			</tr>
			<tr>
				<td align="left" valign="top"><a href="#" onclick="MM_openBrWindow('images/MDUSlick.pdf','','')" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('Image19','','images/SubmitNav5_top_on.gif',1)"><img src="images/SubmitNav5_top_off.gif" name="Image19" width="195" height="27" border="0" id="Image19" /></a></td>
			</tr>
			<tr>
				<td align="left" valign="top"><img src="images/SubmitNav_bot.gif" width="195" height="22" /></td>
			</tr>
	</table> ];

return $str;


}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub LMS_ENROLL_EMAIL {
	my ( $name, $email, $logon, $pwd) = @_;
	my $sql = "select DATEPART(yyyy,getdate()) as yr";
	
	my ($sth, $data, $year);
	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute() or die $sth->errstr;
		$data = $sth->fetchrow_hashref();
		$year = $data->{yr};
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############

	my $body = "
$name,

Your registration is complete!

Your registration for the CenturyLink LMS Referral Program is complete. Please access the Program’s website to make referrals, track referrals, and grow your referral network. Get started now!

3 Easy Steps to Get Started

1. Go to http://centurylinkconnect.com/

2. Enter your login information: 
	Username: $logon
	(Password will be sent in a separate email).

3. Make your first referral!

Contact us at refer.friend\@centurylink.com if you have questions.

Disclaimer: 
Please do not reply to this email. It is automatically generated.

© $year CenturyLink, Inc. All Rights Reserved.

You are receiving this email because of your business relationship with us. If you do not wish to receive future marketing emails, please use the unsubscribe link or you can also respond to this email by writing us:

CenturyLink Customer Response Team
P.O. Box 4259
Monroe, LA 71211

";
my ($bcc)="";
	my	$from = "do_not_reply\@channelmanagement.com";
	my	$subject="CenturyLink® LMS Referral Program - Registration";
		$sql = "insert into ccimail (client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) values
			(50, 269, 0,'" . EscQuote($email) . "','','".EscQuote($bcc)."','" . EscQuote($from). "','" .EscQuote($subject). "','" . EscQuote($body). "')";

	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute() or die $sth->errstr;
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############
$body = "
$name,

Your registration is complete!
Go to http://centurylinkconnect.com/
	Login: was sent in separate email.
Password: $pwd

	Contact us at refer.friend\@centurylink.com if you have questions.

Disclaimer: 
Please do not reply to this email. It is automatically generated.

© $year CenturyLink, Inc. All Rights Reserved.

You are receiving this email because of your business relationship with us. If you do not wish to receive future marketing emails, please use the unsubscribe link or you can also respond to this email by writing us:

CenturyLink Customer Response Team
P.O. Box 4259
Monroe, LA 71211

";
	$from = "do_not_reply\@channelmanagement.com";
	$subject="CenturyLink® LMS Referral Program - Registration";
		$sql = "insert into ccimail (client_id, program_id, lp_lead_id, tofield, ccfield, bccfield, fromfield, subject,longbody) values
			(50, 269, 0,'" . EscQuote($email) . "','','".EscQuote($bcc)."','" . EscQuote($from). "','" .EscQuote($subject). "','" . EscQuote($body). "')";

	#############
	try {
		$sth = $db->prepare($sql);
		$sth->execute() or die $sth->errstr;
		$sth->finish();
	}
	catch {
		DBInterface::writelog('qwestconnect07',"$thisfile", $_ );
	};
	##############
}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
1;

