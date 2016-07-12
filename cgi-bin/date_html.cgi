######################################################################################
#   Function:
#       getDateHTML($datefmt, $formname, $fieldname, $defaultdate, $yearspast, $yearsfuture, $class)
#
#   Parameters:
#       $datefmt    - 1 for mm/dd/yy or 3 for dd/mm/yy (both input and display)
#       $fieldname  - the INPUT field in which to output the selected date (always in
#           mm/dd/yy format).
#       $formname   - the form that contains the INPUT fields
#       $defaultdate - the date to start with. If NULL, the current date (on the server)
#           is used.
#       $yearspast  - number of years to display in the year pull down before the
#           default year
#       $yearsfuture - number of years to display in the year pull down after the
#           default year
#       $class - CLASS attribute to use in HTML INPUT fields.
#       $maxdate    -  date cannot exceed this date
#
#   Notes:
#       This subroutine creates four new variables based on the fieldname. In
#       particular, if foo is passed as the fieldname, the following html
#       names are used: monthfoo, dayfoo, and yearfoo. These are the names for
#       the INPUT fields for month, day, and year respectively. In addition,
#       a javascript function called buildDatefoo is created.
#
#       This approach creates uniqueness so multiple date inputs can appear on the
#       same html page. However, these names cannot be used elsewhere on the page.
#
#   History:
#       11/03/03    added max date support (ahk)
#
#       10/31/03    added date verification (ahk)
#
#       10/30/03    created (ahk)
#
######################################################################################

# for debugging
use strict;
use CGI::Carp qw/ fatalsToBrowser /;
require 'D:/centurylinkyoucan/cgi-bin/xlate.cgi';
# the subroutine
sub getDateHTML($$$$$$$$) {

    # get the arguments
    my ($datefmt, $formname, $fieldname, $defaultdate, $yearspast, $yearsfuture, $class, $maxdate) = @_;

    # need the date in these three variables
    my $defaultmonth;
    my $defaultday;
    my $defaultyear;        # short version of date (e.g. 03)
    my $defaultlongyear;    # long version of date (e.g. 2003)

    # if no default date, use the current date (on the server)
    if (!$defaultdate) {

        # get the date
        my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);

        # convert month names to numbers
        my %monthnum = (
            "Jan" => "01",
            "Feb" => "02",
            "Mar" => "03",
            "Apr" => "04",
            "May" => "05",
            "Jun" => "06",
            "Jul" => "07",
            "Aug" => "08",
            "Sep" => "09",
            "Oct" => "10",
            "Nov" => "11",
            "Dec" => "12"
        );

        # set the current date as default
        $defaultmonth = $monthnum{$month};
        $defaultday = $dayofMonth;
        $defaultlongyear = $year;

    }
    else {

        # there is a default date so parse the date string
        my @datestr;
        @datestr = split (/\//, $defaultdate);

        # european date format was passed, so set this way
        # Euro format is never passed in; don't bother checking for it; DonBar & Adam 2/17/06
#        if ($datefmt == 3) {
#            $defaultday = $datestr[0];
#            $defaultmonth = $datestr[1];
#            $defaultyear = $datestr[2];
#        }
#        # otherwise, assume US format, so set this way
#        else {
            $defaultmonth = $datestr[0];
            $defaultday = $datestr[1];
            $defaultyear = $datestr[2];
#        }

        # assume dates over 90 are from the 1900s. This will break in 2090 and does not support dates prior to 1990
        if ($defaultyear > 90 ) {
            $defaultlongyear = $defaultyear + 1900;
        }
        else {
            $defaultlongyear = $defaultyear + 2000;
        }
    }

    # if european, display like this: dd/mm/yy
    if ($datefmt == 3) {

        # get the day in a pull down menu
        getDayHTML($formname, $fieldname, $defaultday, $class);

        # get the month in a pull down menu
        getMonthHTML($formname,$fieldname, $defaultmonth, $class);

        # get the year in a pull down menu
        getYearHTML($formname,$fieldname, $defaultlongyear, $yearspast, $yearsfuture, $class);

    }
    # otherwise, assume US format: mm/dd/yy
    else {

        # get the month in a pull down menu
        getMonthHTML($formname,$fieldname, $defaultmonth, $class);

        # get the day in a pull down menu
        getDayHTML($formname,$fieldname, $defaultday, $class);

        # get the year in a pull down menu
        getYearHTML($formname,$fieldname, $defaultlongyear, $yearspast, $yearsfuture, $class);

    }

# this part of the JavaScript function buildDate checks to make sure the date entered is valid
print<<EOF;
<script language="javascript">
function buildDate$fieldname() {

    // multiply by 1 to force to integer
    var longyear = document.$formname.year$fieldname.value * 1;

    // assume any yy greater than 90 is last century
    if ( longyear > 90 ) {
            longyear = longyear + 1900;
    }
    else {
            longyear = longyear + 2000;
    }

    // is this a leap year?
    var isleapyear = 0;
    isleapyear = (longyear % 4 == 0) && ((longyear % 100 != 0) || (longyear % 400 == 0));

    // check to see if day is valid for this month and year
    switch (document.$formname.month$fieldname.value) {
        case "04":
        case "06":
        case "09":
        case "11":

            if (document.$formname.day$fieldname.value > 30) {

                // let the user know
                alert("Please enter a valid date");

                // set the day to the 30th (IE sets the pull down)
                document.$formname.day$fieldname.value = "30";

            }
            break;

        case "02":
            // if this isn't leap year
            if (!isleapyear) {

                // only dates below 28 are ok
                if (document.$formname.day$fieldname.value > 28)  {

                    // let the user know
                    alert("Please enter a valid date");

                    // set the day to the 27th (IE sets the pull down)
                    document.$formname.day$fieldname.value = "28";
                }
            }

            // if this is leap year
            else {

                // the 29th is OK
                if (document.$formname.day$fieldname.value > 29)  {

                    // let the user know
                    alert("Please enter a valid date");

                    // set the day to the 28th (IE sets the pull down)
                    document.$formname.day$fieldname.value = "29";
                }
            }
            break;
    }
EOF

    # if a maxdate has been specified, caclulate max date and include the code to ensure date is less than maxdate
    if ($maxdate) {

        # parse the date string
        my @maxdatestr;
        @maxdatestr = split (/\//, $maxdate);

        # put the month, day, and year here
        my $maxday;
        my $maxmonth;
        my $maxyear;
        my $maxlongyear;

        # european date format was passed
        if ($datefmt == 3) {
            $maxday = $maxdatestr[0];
            $maxmonth = $maxdatestr[1];
            $maxyear = $maxdatestr[2];
        }
        # otherwise, assume US format
        else {
            $maxmonth = $maxdatestr[0];
            $maxday = $maxdatestr[1];
            $maxyear = $maxdatestr[2];
        }

        # assume dates over 90 are from the 1900s. This will break in 2090 and does not support dates prior to 1990
        if ($maxyear > 90 ) {
            $maxlongyear = $maxyear + 1900;
        }
        else {
            $maxlongyear = $maxyear + 2000;
        }

        # this part of the JavaScript function buildDate checks to make sure the date does not exceed
        # the maximum date
print<<EOF;

    // see if the date entered exceeds the maximum date
    var months = new Array( "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" );

    // get the dates into JS date object
    var currdate = new Date(months[document.$formname.month$fieldname.value - 1] + " " + document.$formname.day$fieldname.value + ", " + longyear.toString() );
    var maxdate = new Date(months["$maxmonth"-1] + " " + "$maxday" + ", " + "$maxlongyear" );

    // if the date entered exceeds the maximum date allowed
    if (currdate.valueOf() > maxdate.valueOf()) {

        // let the user know
        alert("Date entered exceeds maximum date allowed");

        // set the month to the max allowed (IE sets the pull down)
        document.$formname.month$fieldname.value = "$maxmonth";

        // set the day to the max allowed (IE sets the pull down)
        document.$formname.day$fieldname.value = "$maxday";

        // set the year to the max allowed (IE sets the pull down)
        document.$formname.year$fieldname.value = "$maxyear";

    }

EOF

    }

print<<EOF;
    // the new valid date
    return (document.$formname.month$fieldname.value + '/' + document.$formname.day$fieldname.value + '/' + document.$formname.year$fieldname.value);
}

// preset to the default value (this will be set before user clicks on anything)
document.$formname.$fieldname.value = buildDate$fieldname();

</script>
EOF

}



####
# display the month pulldown menu.
####
sub getMonthHTML($$$$) {


    # get the arguments
    my ($formname,$fieldname,$defaultmonth,$class) = @_;

    # the months of the year
    my @monthlist = (   xlate("January"),
                        xlate("February"),
                        xlate("March"),
                        xlate("April"),
                        xlate("May"),
                        xlate("June"),
                        xlate("July"),
                        xlate("August"),
                        xlate("September"),
                        xlate("October"),
                        xlate("November"),
                        xlate("December")
                        );

    # start of select statement. any change modifies $fieldname

print qq[
    <SELECT NAME="month$fieldname" CLASS="$class" onChange="document.$formname.$fieldname.value = buildDate$fieldname();">];
    # use dispmonth for the formatted month string (i.e. 01 instead of just 1)
    my $dispmonth;

    # create an option for each month
    for (my $i = 0; $i < 12; ++$i) {

        # get the formatted version. use $+1 due to 0 based array
        $dispmonth = sprintf "%.2d", $i+1;

        # if this is the default month, display as selected
        if ($i+1 == $defaultmonth) {
print qq[
            <OPTION VALUE="$dispmonth" SELECTED>$monthlist[$i]</option>];
        }
        else {
print qq[
            <OPTION VALUE="$dispmonth">$monthlist[$i]</option>];
        }
    }

# end of select statement
print<<EOF;
    </SELECT>
EOF

}


####
# display the day pulldown menu
####
sub getDayHTML($$$$) {


    # get the arguments
    my ($formname,$fieldname,$defaultday,$class) = @_;

print<<EOF;
    <SELECT NAME="day$fieldname" CLASS="$class" onChange="document.$formname.$fieldname.value =  buildDate$fieldname();">
EOF

    # use dispday for the formatted day string (i.e. 01 instead of just 1)
    my $dispday;

    # create an option for each day of the month
    for (my $i = 0; $i < 31; ++$i) {

        # get the formatted version. use $+1 due to 0 based array
        $dispday = sprintf "%.2d", $i+1;

        # if this is the default day, display as selected
        if ($i+1 == $defaultday) {
print<<EOF;
            <OPTION VALUE="$dispday" SELECTED>$dispday
EOF
        }
        else {
print<<EOF;
            <OPTION VALUE="$dispday">$dispday
EOF
        }
    }

# end of select statement
print<<EOF;
    </SELECT>
EOF


}


####
# display the year pulldown menu
####
sub getYearHTML($$$$$$) {

    # get the arguments
    my ($formname,$fieldname,$defaultlongyear,$yearspast,$yearsfuture,$class) = @_;


print<<EOF;
    <SELECT NAME="year$fieldname" CLASS="$class" onChange="document.$formname.$fieldname.value = buildDate$fieldname();">
EOF

    my $shortyear;    # year without the hundreds or thousands digits
    my $dispyear;     # two digit year with 0 for leading digit (e.g. 01 instead of 1)

    # create an option for each year within the range specified
    for (my $i = $defaultlongyear - $yearspast; $i <= $defaultlongyear + $yearsfuture; ++$i) {

        # get the short version
        $shortyear = substr $i, 2;

        # create dispyear of short version (i.e. 01 instead of just 1)
        $dispyear = sprintf "%.2d", $shortyear;

        # if this is the default year, display as selected
        if ($i == $defaultlongyear) {
print<<EOF;
            <OPTION VALUE="$dispyear" SELECTED>$i
EOF
        }
        else {
print<<EOF;
            <OPTION VALUE="$dispyear">$i
EOF
        }
    }

print<<EOF;
</SELECT>
EOF

}

return 1;
