# lms_ref_email.cgi
#   Used in LMSI and LMSII
#   Sends an email to 
# Pass two parameters:
#   program_id
#   level

use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);

require "D:/centurylinkyoucan/cgi-bin/init.cgi";   # loads session
require "D:/centurylinkyoucan/cgi-bin/delimeter.cgi";

use DBInterface;



#my $db = new Win32::ODBC($main::DSN);
#my $db2 = new Win32::ODBC($main::DSN);
#my $db3 = new Win32::ODBC($main::DSN);

# Constants/Globals
#my $IS_TEST   = 1;

sub DUPLICATE_CHK {
    my ($lastfour, $phone1) = @_;
	#my $myDB3 = Win32::ODBC->new($main::DSN);
	my $myDB = DBInterface->new();

    my $msg;

    # Validate that the last four SSN isn't totally bogus, like 'abc '
    unless ( length($lastfour) == 4 and $lastfour =~ /\d\d\d\d/ ){
        $msg = 'Please enter valid 4 Last Digits of your Social Security number or Individual Taxpayer Identification Number ';
    }

    # Duplicate registration Validation. Should not be registred in any RAF program
    my $sql = "select count(*) as dup_cnt from cust with(nolock), contact_main with(nolock)
             where cust.cust_id = contact_main.cust_id
               and custom3 in ( '649', '929', '1036', '941', '1151')
               and phone = '$phone1'
               and vccust21 = '$lastfour'
               and isnull(vccust21, '') <> ''
               and cust.name <> 'test'
			   and cust.cust_status = 1
    ";
    #$myDB3->Sql($sql);
    #$myDB3->FetchRow();
	#my %dup_data = $myDB3->DataHash();
	
	my $sth = $myDB->prepare($sql);
	$sth->execute();
	my $dup_data = $sth->fetchrow_hashref();
	
    my $dup_cnt = $dup_data->{dup_cnt};

    if ( !$msg and $dup_cnt ) {
        $msg .= "Thank you for your interest in the Refer a Friend program.  Our records indicate that you have previously registered for Refer a Friend. Please log in with your registered user id and password or contact the Refer a Friend Program Headquarters at 866-968-2261 if you need assistance.";
    }
	
	$sth->finish();
    $myDB->disconnect();
    return $msg;

}
#---------------------------------------------------------------------
#   validate
#---------------------------------------------------------------------
sub DUPLICATE_CHK_QSC{
    my $lastfour = shift;
    my $phone1 = shift;
    my $osr_id = shift;
	#my $myDB3 = Win32::ODBC->new($main::DSN);
	my $myDB = DBInterface->new();

    my $msg;

    # Validate that the last four SSN isn't totally bogus, like 'abc '
    unless ( length($lastfour) == 4 and $lastfour =~ /\d\d\d\d/ ){
        $msg = 'Please enter valid 4 Last Digits of your Social Security number or Individual Taxpayer Identification Number ';
    }

    # Duplicate registration Validation. Should not be registred in any RAF program
    my $sql = "select count(*) as dup_cnt from cust with(nolock), contact_main with(nolock)
             where cust.cust_id = contact_main.cust_id
               and custom3 in ( '649', '929', '1036', '941', '1151')
               and phone = '$phone1'
               and vccust21 = '$lastfour'
               and isnull(vccust21, '') <> ''
               and cust.name <> 'test'
   			   and cust.cust_status = 1
    ";
    #$myDB3->Sql($sql);
    #$myDB3->FetchRow();
	#my %dup_data = $myDB3->DataHash();
    
	my $sth = $myDB->prepare($sql);
	$sth->execute();
	my $dup_data = $sth->fetchrow_hashref();
	my $dup_cnt = $dup_data->{dup_cnt};
	$sth->finish();
    if ( !$msg and $dup_cnt ) {
        $msg = "Thank you for your interest in the Refer a Friend program.  Our records indicate that you have previously registered for Refer a Friend. Please log in with your registered user id and password or contact the Refer a Friend Program Headquarters at 866-968-2261 if you need assistance.";
    }

    # CTA and QSC Retail.  Validate the rep id is not blank or spaces or 0
    #  prh took out formtype = 2 because  osr_id = emplid in a hidden
    unless ($msg){
        unless ( $osr_id ) {
            $msg = "The REP ID field requires an employee CUID. Contact the YOU CAN Program Headquarters at 866-968-2261 if you need assistance";
        }
    }

    # CTA and QSC Retail.  Validate the rep id is a valid CUID. Sales codes and other stuff coming in.
    #  prh took out formtype = 2 because  osr_id = emplid in a hidden
    unless ($msg){
        if ( $osr_id ) {
            $sql = "select cuid from qwesthr with (nolock) where emplid = $osr_id";
	        #$myDB3->Sql($sql);
			#$myDB3->FetchRow();
			#$myDB3->Sql($sql);
			#$myDB3->FetchRow();
			#my %cuid_data = $myDB3->DataHash();
			
			my $sth = $myDB->prepare($sql);
			$sth->execute();
			my $cuid_data = $sth->fetchrow_hashref();
			
			my $cuid = $cuid_data->{cuid};
			$sth->finish();

            unless ($cuid){
               $msg = "The REP ID field (has $osr_id) cuid $cuid requires a valid employee CUID. Contact the YOU CAN Program Headquarters at 866-968-2261 if you need assistance.";
            }
        }
    }

    $myDB->disconnect();
    return $msg;
}
#---------------------------------------------------------------------
#   validate
#---------------------------------------------------------------------
sub DUPLICATE_CHK_LMSI {
    my $lastfour = shift;
    my $phone1 = shift;
    my $osr_id = shift;
	#my $myDB3 = Win32::ODBC->new($main::DSN);
	
	my $myDB = DBInterface->new();

    my $msg;

    # Validate that the last four SSN isn't totally bogus, like 'abc '
    unless ( length($lastfour) == 4 and $lastfour =~ /\d\d\d\d/ ){
        $msg = 'Please enter valid 4 Last Digits of your Social Security number or Individual Taxpayer Identification Number ';
    }

    # Duplicate registration Validation. Should not be registred in any RAF program
    my $sql = "select count(*) as dup_cnt from cust with(nolock), contact_main with(nolock)
             where cust.cust_id = contact_main.cust_id
               and custom3 in ( '649', '929', '1036', '941', '1151')
               and phone = '$phone1'
               and vccust21 = '$lastfour'
               and isnull(vccust21, '') <> ''
               and cust.name <> 'test'
   			   and cust.cust_status = 1
    ";
    #$myDB3->Sql($sql);
    #$myDB3->FetchRow();
	#my %dup_data = $myDB3->DataHash();
	
	my $sth = $myDB->prepare($sql);
	$sth->execute();
	my $dup_data = $sth->fetchrow_hashref();
	$sth->finish();
    my $dup_cnt = $dup_data->{dup_cnt};
    if ( !$msg and $dup_cnt ) {
        $msg = "Thank you for your interest in the Refer a Friend program.  Our records indicate that you have previously registered for Refer a Friend. Please log in with your registered user id and password or contact the Refer a Friend Program Headquarters at 866-968-2261 if you need assistance.";
    }

    # CTA and QSC Retail.  Validate the rep id is not blank or spaces or 0
    #  prh took out formtype = 2 because  osr_id = emplid in a hidden
    unless ($msg){
        unless ( $osr_id ) {
            $msg = "The REP ID field requires an employee CUID. Contact the YOU CAN Program Headquarters at 866-968-2261 if you need assistance";
        }
    }

    # CTA and QSC Retail.  Validate the rep id is a valid CUID. Sales codes and other stuff coming in.
    #  prh took out formtype = 2 because  osr_id = emplid in a hidden
    unless ($msg){
        if ( $osr_id ) {
            $sql = "select cuid from qwesthr with (nolock) where emplid = $osr_id";
	
			#$myDB3->Sql($sql);
			#$myDB3->FetchRow();
			#my %osr_data = $myDB3->DataHash();
    
			my $sth = $myDB->prepare($sql);
			$sth->execute();
			my $osr_data = $sth->fetchrow_hashref();
			my $cuid = $osr_data->{cuid};


            unless ($cuid){
               $msg = "The REP ID field (has $osr_id) cuid $cuid requires a valid employee CUID. Contact the YOU CAN Program Headquarters at 866-968-2261 if you need assistance.";
            }
        }
    }

    $myDB->disconnect();
    return $msg;
}





