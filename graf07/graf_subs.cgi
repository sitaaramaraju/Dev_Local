#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use Try::Tiny;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');


my $server;
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

my $db = DBInterface->new();
my $thisfile = 'graf_subs';


#########################
# get_num_referrals
#########################
sub get_num_referrals {
	my $cust_id = shift;
	my $program_id = shift;
	my $fund_id = shift;
	
	my $myDB = DBInterface->new();
	
	my $sql = qq(
		select count(lp_lead_id)
		from lp_lead with (nolock)
		where agency_id = ?
		and program_id = ?
		and fund_id = ?
		and created_date > convert(datetime, '1/1/' + convert(varchar(4), datepart(yyyy, getdate()-1)))
	);
	
	my $sth = $myDB->prepare($sql);
	my $count; 
	try {
		$sth->execute($cust_id, $program_id, $fund_id) or die $sth->errstr;
		$count = $sth->fetchrow();
		$sth->finish();
		$myDB->disconnect();
	}
	catch {
		DBInterface::writelog('graf07',"$thisfile", $_ );
	};
	
	return $count;
}


#####################
# get_sum_net()
#####################
sub get_sum_net {
    my $cust_id = shift;
	my $myDB = DBInterface->new();

    my $sql = "select  getdate() as this_date, '1/1/'+convert(varchar(4),datepart(yyyy,getdate()-1)) as ytdstart";
	
	my $sth = $myDB->prepare($sql);
	$sth->execute();	
	my ($this_date, $this_year) = $sth->fetchrow();
	$sth->finish();
    

    $sql = "
			select isnull(sum( isnull(net,0) ),0)
			from qwest_visa_load with (nolock)
			where cust_id = ?
			and created_date > '$this_year'
			and eligible = 1
			";
			
    my $sth = $myDB->prepare($sql);
	$sth->execute($cust_id);
	my $sum = $sth->fetchrow();
	$sth->finish();
    $myDB->disconnect();
    
	return $sum;
}

##########################
# check_status
##########################
sub check_status {
    my $cust_id = shift;
    die "check_status error, no cust_id" unless $cust_id;

    my $myDB = DBInterface->new();

    my $sql = "	select count(*)
				from custw9 with(nolock) 
				where cust_id = ? 
				";

	my $sth = $myDB->prepare($sql);
	$sth->execute($cust_id);
	my $count = $sth->fetchrow();
	$sth->finish();
	
	$myDB->disconnect();
    return $count ? 1 : 0;
}

#################
#	logout
#################
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

 ######################
 #  send_email
 ######################
 sub send_email {
    my($name ,$email ,$phone , $timetocall ,$refnum , $issue , $explanation ) = @_;


 	my $bcc = '';
	my $msg  = qq[<tr>
                        <td colspan="3" align="center" valign="top">Thank You for your question.  <br><br>
			An email has been sent to the CenturyLink Connect Program Headquarters.<br><br>
			You will hear from us shortly.</td>
                      </tr>];

 my $sendto = 'refer.friend@centurylink.com';

    my $subject = "CenturyLink Connect : Quick Form";
 
          my $sql = "select convert(datetime, getdate() ) as thd ";
			my $sth = $db->prepare($sql);
			$sth->execute();
			my $data = $sth->fetchrow_hashref();
			$sth->finish();
			my $date = $data->{thd};
     my $bodymsg = "
CenturyLink PassItOnRewards Quick Form 

Sent:           $date
From:           $name
Email:          $email
Phone:          $phone
Time to call:   $timetocall
Referral:       $refnum
Issue:          $issue
Explanation:    $explanation

";

         $sql = "insert into ccimail (client_id, program_id,  tofield, ccfield, bccfield, fromfield, subject,longbody) values
				(50, 269, '$sendto', '', '$bcc',  'do_not_reply\@ccionline.biz', '$subject', '$bodymsg' ) ";

		$sth = $db->prepare($sql);
		$sth->execute();
		$sth->finish();
		
	return $msg;
} 

1;