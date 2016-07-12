use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');

require "D:/centurylinkyoucan/cgi-bin/lp-validate.pm";

