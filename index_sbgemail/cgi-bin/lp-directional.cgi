# File used to direct traffic.  Each user has a user type..  the user type will
# specify the path/direction that the user will follow
# file name:  /lp_directional.cgi
# last modified 7/21/04  DLF
############################################################################
# following lines required on all pages
############################################################################
use strict;            #Enforce variable scoping to help prevent scoping errors
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');
require "D:/centurylinkyoucan/cgi-bin/lp-directional.pm";    #Initialize Co-opPro DSN

