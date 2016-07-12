use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

my $myDB = Win32::ODBC->new($main::DSN);


sub show_rttbl123(){
my ($session_id, $emplid)=@_;
if ($session_id > 0 || $emplid > 0) {

print<<"EOF";
        	<div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Referrals</h3>
                </div>
                <div class="capsule-content">
                	<p><a href="welcome.cgi?session_id=$session_id&emplid=$emplid">Start a New Referral.</a></p>
                    <hr class="brk-grey" />
                    <p><a href="ref_hist.cgi?session_id=$session_id&emplid=$emplid">Generate Referral Report.</a></p>
                </div>
            </div><!--END CAPSULE-->
EOF
}

				print<<"EOF";
            <div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Important Info</h3>
                </div>
                <div class="capsule-content">
                	<p><a href="tax_info.cgi?session_id=$session_id&emplid=$emplid">YOUCAN Tax Implications</a></p>
                    <hr class="brk-grey" />
                    <p><a href="pdf/Fee_Down_Universal_ATM_T&C_4_12.pdf" target="_blank">YOUCAN Visa Terms and Conditions</a></p>
                </div>
            </div><!--END CAPSULE-->
EOF

}
$myDB ->Close();
# was in between Tax implication and Visa T&C CL-1438
#                    <p><a href="pdf/YOUCAN_ref_TC_amex.pdf" target="_blank">Terms and Conditions</a></p>
 #                   <hr class="brk-grey" />

