##### File: cgi-bin/excel.pm
#
# Provides functions useful for Excel file generation.
#
# Last Revised 10/13/04

use strict;
############################################################################
sub ExcelCreate     #10/13/04 2:28:PM
############################################################################
 {
    $main::excelfile = '/tmp/' . $main::session{session_id} ."_" . time() . ".xls";
    unless(open(CSVDATA, '>D:/xroot' . $main::excelfile))
    {
        print "Could not open user database";
        die;
    }
return 1;
}   ##ExcelCreate

############################################################################
sub ExcelWrite($)      #10/13/04 2:29:PM
############################################################################
 {
    print CSVDATA @_;
    return 1;
}   ##ExcelWrite

############################################################################
sub ExcelClose($)       #10/13/04 2:29:PM
############################################################################
 {
    close CSVDATA;
    return 1;
}   ##ExcelClose($)
return 1;
