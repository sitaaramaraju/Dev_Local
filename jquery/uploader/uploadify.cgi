$| = 1;

use strict;
require "g:/cox/xroot/cgi-bin/encrypt.cgi";
require "g:/cox/xroot/cgi-bin/init.cgi";
use File::Copy;
require "g:/cox/xroot/cgi-bin/CoxConfig.pm";


use CGI::Carp qw/ fatalsToBrowser /;
use CGI qw(:standard);      #required to use the param call later

$CGI::POST_MAX = 26214400; # 25MB max upload file size
my $cgi = CGI->new();


my $file = $cgi->param('name');
my $targetPath = $cgi->param('folder');
my $ext = substr($file,rindex($file,'.'),5);
my $fn = $main::session{session_id} . "_" . substr(time(),3,7).$ext;

if ($fn =~ /^([-\@\w.]+)$/) {
    $fn = $1; # $fn now untainted.
} else {
    if($fn ne undef) { # Ignore if undef, probably first run.
        die "'$fn' is an illegal filename.";
    }
}

if (ref $file) {
    if(open (OUT, ">$targetPath$fn"))
	{
		binmode(OUT);
		my $bytesread;
		my $buffer;
		while ($bytesread=read($file,$buffer,4096)) {
			print OUT $buffer;
		}
	}else{die "couldnt open file";}
}else{

	die "issue";
	return -1;

}



