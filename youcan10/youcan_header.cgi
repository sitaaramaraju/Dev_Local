use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();


sub showhdr(){
my ($PAGETITLE, $cci_id)=@_;

my $show = CCICryptography::validate_CL($cci_id); 
my $url = CCICryptography::getUrl();

my ( $session_id, $emplid) = CCICryptography::getEmpid( $cci_id);


print<<"EOF";
<form name="lead123" action="" method="post">
	<input type="hidden" name="cci_id" value="$cci_id">
	</form>
    	<div id="header-content">
<script type="text/javascript" src="assets/js/youcan_functions.js"></script>		
EOF
	if ($show >0) {
		print<<"EOF"; 
				<a href="#" onClick="document.lead123.action='welcome.cgi';document.lead123.submit();"><img src="assets/img/header.gif" alt="$PAGETITLE" title="$PAGETITLE" class="youcan-logo" /></a>
            <div id="header-logout">
            	<p><a href="#" onclick="logoutUser($emplid, $session_id);">Logout</a></p>	
            </div><!--END HEADER-LOGOUT-->

EOF
	}
	else {
		print<<"EOF";
       		<a href="$url"><img src="assets/img/header.gif" alt="$PAGETITLE" title="$PAGETITLE" class="youcan-logo" /></a>
EOF
	}
			#               	  	<li class="nav-main-2"><a href="index.html">Get Started</a></li>

print<<"EOF";
            <div id="header-nav-main">
                <ul class="nav-main">
                    <li class="nav-main-1"><a href="javascript:animatedcollapse.toggle('nav-sec-1')">My YOUCAN</a></li>
					<li class="nav-main-5"><a href="#" onClick="document.lead123.action='mkt_materials.cgi';document.lead123.submit();">Marketing Materials</a></li>
                    <li class="nav-main-6"><a href="javascript:animatedcollapse.toggle('nav-sec-6')">You Need to Know</a></li>
                </ul>
            </div><!--END HEADER-NAV-MAIN-->
            <div id="header-nav-sec">
            	<div id="nav-sec-1">
                    <ul>

EOF
#<li><a href="http://lqweb.qintra.com/loopqual-webapp/pages/ProductQual/QualCheck/Qualify.faces" target="_blank">High-Speed Internet Availability </a>| </li>
#                        <li><a href="contest_winners.cgi?session_id=$session_id">Contest Winners</a> |</li>
# <li><a href="#" onClick="document.lead.action='welcome.cgi';document.lead.submit();">Make a Referral</a> |</li>
#<li><a href="#" onClick="document.lead.action='ref_report.cgi';document.lead.submit();">Referral Report</a> |</li>
#<li><a href="#" onClick="document.lead.action='ref_hist.cgi';document.lead.submit();">Referral History</a> |</li>
#<li><a href="#" onClick="document.lead.action='acct_preference.cgi';document.lead.submit();">Account Preference</a> |</li>

if ($show > 0) {

#<li><a href="#" 
#onclick="javascript:document.lead.target='_new';document.lead.action='http://www.qwestyoucan.com/leadpro/reports/emp_drill.cgi?program_id=154';
#document.lead.submit();" >Referral Report</a> |</li>
print<<"EOF";
<li><a href="#" onClick="document.lead123.action='welcome.cgi';document.lead123.submit();">Make a Referral</a> |</li>
<li><a href="#" onClick="document.lead123.action='ref_hist.cgi';document.lead123.submit();">Referral History</a> </li>
EOF
}

# below link removed from below section CL-1438
#                        <li><a href="pdf/YOUCAN_ref_TC_amex.pdf" target="_blank">Terms &amp; Conditions</a> | </li>


print<<"EOF";
                        
                    </ul>
                </div>
                <div id="nav-sec-6">
                    <ul>
						<li><a href="#" onClick="document.lead123.action='news.cgi';document.lead123.submit();">News</a> |</li>
					  <li><a href="#" onClick="document.lead123.action='tax_info.cgi';document.lead123.submit();">Tax Implications</a> |</li>
						<li><a href="#" onClick="document.lead123.action='res_biz_awards.cgi';document.lead123.submit();">Award Values</a> |</li>
						<li><a href="#" onClick="document.lead123.action='my_youcan.cgi';document.lead123.submit();">Program Eligibility</a> </li>

                    </ul>
                </div>
            </div><!--END NAV-SEC-->
      </div><!--END HEADER-CONTENT-->
EOF

}


sub showftr(){
my ($cci_id)=@_;
my $show = CCICryptography::validate_CL($cci_id); 
if ($show > 0 ){
print<<"EOF";

    	<div id="header-content">

    <div id="layout-footer">
    	<div id="footer-content">
        	<ul class="footer-links">
            	<li><a href="#" onClick="document.lead123.action='contact.cgi';document.lead123.submit();">Contact Us</a></li>
                <li> | </li>
                <li><a href="#" onClick="document.lead123.action='faq.cgi';document.lead123.submit();">FAQs</a></li>
                <li> | </li>
                <li><a href="#" onClick="document.lead123.action='site_map.cgi';document.lead123.submit();">Site Map</a></li>
				<li> | </li>
		<li><a href="#" onClick="document.lead123.action='legal.cgi';document.lead123.submit();">Legal Notices</a></li>
		<li> | </li>
                <li><a href="http://www.qwest.com/privacy/" target="_blank">Privacy Policy</a></li>
            </ul>
				<ul class="footer-legal"><li>&copy; <script type="text/javascript">document.write(new Date().getFullYear());</script> CenturyLink, Inc. All Rights Reserved. The CenturyLink mark, pathways logo, CenturyLink mark,<br />
               Q lightpath logo and certain CenturyLink product names are the property of CenturyLink, Inc.</li>
				</ul>
        </div><!--END FOOTER CONTENT-->
    </div><!--END LAYOUT-FOOTER-->

EOF
}
}

#                    <hr class="brk-grey" />
#                    <p><a href="ref_hist.cgi?session_id=$session_id&emplid=$emplid">Generate Referral Report.</a></p>

sub show_rttbl(){
my ($cci_id)=@_;
my $show = CCICryptography::validate_CL($cci_id); 
if ($show > 0 ){
print<<"EOF";
        	<div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Referrals</h3>
                </div>
                <div class="capsule-content">
                	<p><a href="#" onClick="document.lead123.action='welcome.cgi';document.lead123.submit();">Start a New Referral.</a></p>
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
                	<p><a href="#" onClick="document.lead123.action='tax_info.cgi';document.lead123.submit();">YOUCAN Tax Implications</a></p>
                    <hr class="brk-grey" />
                    <p><a href="pdf/Universal_VPC_carrier_ATM_02172016.pdf" target="_blank">YOUCAN Visa Terms and Conditions</a></p>

                </div>
            </div><!--END CAPSULE-->
EOF
}
#$myDB ->Close();
