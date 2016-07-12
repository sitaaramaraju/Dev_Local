use strict;
############################################################################
sub HTML2PDF($)     #10/13/04 2:28:PM
{
    #Value passed in is the HTML file
    my $file =  @_[0];
	my $pdf = $file;
	
	$pdf =~ s/html/pdf/;
	
	my $directory = 'd:/centurylinkyoucan/sbgemailbuilder/tmp/';
	my $fullfile = $directory.$file;
	my $fullpdf = $directory.$pdf;
	
	# command line
	my $cmd = 'D:/centurylinkyoucan/wkhtmltopdf/bin/wkhtmltopdf.exe ' . $fullfile . ' ' . $fullpdf;
	
    my $return = `$cmd`;
	
	
	return $pdf;
}
return 1;
