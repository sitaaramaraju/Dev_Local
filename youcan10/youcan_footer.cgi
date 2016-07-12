use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

my $myDB = Win32::ODBC->new($main::DSN);


sub showftr123(){
my ($session_id)=@_;
print<<"EOF";
    <div id="layout-footer">
    	<div id="footer-content">
        	<ul class="footer-links">
            	<li><a href="contact.cgi?session_id=$session_id">Contact Us</a></li>
                <li> | </li>
                <li><a href="faq.cgi?session_id=$session_id">FAQs</a></li>
                <li> | </li>
                <li><a href="site_map.cgi?session_id=$session_id">Site Map</a></li>
		<li><a href="legal.cgi?session_id=$session_id">Legal Notices</a></li>
                <li><a href="http://www.qwest.com/privacy/">Privacy Policy</a></li>
            </ul>
				<ul class="footer-legal"><li>&copy; <script type="text/javascript">document.write(new Date().getFullYear());</script> CenturyLink, Inc. All Rights Reserved. The CenturyLink mark, pathways logo, CenturyLink mark,<br />
               Q lightpath logo and certain CenturyLink product names are the property of CenturyLink, Inc.</li>
				</ul>
        </div><!--END FOOTER CONTENT-->
    </div><!--END LAYOUT-FOOTER-->

EOF

}
$myDB ->Close();
