use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
use DBInterface;
my $myDB = DBInterface->new();
#---------------------------------------------------------------------------
#Populate preferences for current program
#---------------------------------------------------------------------------
my $program_id = $main::cgi{program_id};
my (%prog_opts, $sql);
%main::prog_opts;
if ( length($program_id) > 0 ) {
    my $srchfund = $main::cgi{search_fund}||0;
    my $fund = $main::cgi{fund_id}||0;
	
    $sql = "exec splp_ProgOpts $program_id, $fund , $srchfund, $main::session{staff_id}";
	
	my $sth = $myDB->prepare($sql);

    if ($sth->execute()) {
      my $prog_opts_ref = $sth->fetchrow_hashref();
	  %prog_opts = %{$prog_opts_ref};
      my $key;
          foreach $key(keys %prog_opts){
            $main::prog_opts{$key} = $prog_opts{$key};
          }

    }
}	

$myDB->disconnect;
1;


