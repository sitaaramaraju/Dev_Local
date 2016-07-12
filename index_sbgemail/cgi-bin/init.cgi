# File: /cgi-bin/init.cgi
##########################
use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use DBInterface;
use CGI qw(:standard);

my $cgi = CGI->new();
print $cgi->header('text/html');

require "D:/centurylinkyoucan/cgi-bin/init.pm";

