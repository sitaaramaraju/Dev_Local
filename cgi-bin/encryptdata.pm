use strict;
############################################################################
sub EncryptData($)     #10/13/04 2:28:PM
{
    #Use for numeric values only
    my $data =  @_[0];
	# workaround for new perl version
	my $cmd = 'c:\perl.old\bin\perl.exe d:\xroot\cgi-bin\encryptdatapm.cgi ' . $data;
    my $encrypteddata = `$cmd`;
	#open (D, "<D:/cci-keepme.pwd") || die "Can't open file\n";

    #my $buffer .= $_;
    #my $passkey;
    #while (<D>) {
    #$passkey .= $_;
    #}
    #close D;

    #use Math::XOR;
    #return xor_buf($data,$passkey);
	return $encrypteddata;
}
return 1;
