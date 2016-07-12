#Filename: /cgi-bin/delimeter.cgi
# NOLOCK Added

use Date::Calc qw(:all);
############################################################################
sub delim_exch($)       #02/28/01 10:38:AM
# Use this sub when passing data between forms using the action and input
# types to pass data.  This will allow the quotes and double quotes to
# display properly and pass cleanly,
############################################################################
 {
    my ($new_delim) = @_;
    if ($new_delim =~ m/["]/gi) {
        $new_delim =~ s/["]/&~034;/gi;
    }
    if ($new_delim =~ m/[']/gi) {
        $new_delim =~ s/[']/&~039;/gi;
    }
    if ($new_delim =~ m/!!amp!!/gi) {
        $new_delim =~ s/!!amp!!/&/gi;
    }
    if ($new_delim =~ m/!!equ!!/gi) {
        $new_delim =~ s/!!equ!!/=/gi;
    }
    if ($new_delim =~ m/!!plu!!/gi) {
        $new_delim =~ s/!!plu!!/+/gi;
    }
    return $new_delim;
}   ##delim_exch($)

############################################################################
sub js_delim_exch($)        #02/28/01 11:08:AM
# Use this sub when passing data through an Anchor tag <a>.  This will
# give the single quote and excape function that will allow it to display
# properly and pass cleanly.  The double quote works the same as above.
############################################################################
 {
    my ($js_new_delim) = @_;
    if ($js_new_delim =~ m/[']/gi) {
        $js_new_delim =~ s/[']/&~039;/gi;
    }
    if ($js_new_delim =~ m/[&]/gi) {
        $js_new_delim =~ s/[&]/!!amp!!/gi;
    }
    if ($js_new_delim =~ m/[=]/gi) {
        $js_new_delim =~ s/[=]/!!equ!!/gi;
    }
    if ($js_new_delim =~ m/[+]/gi) {
        $js_new_delim =~ s/[+]/!!plu!!/gi;
    }
    if ($js_new_delim =~ m/[#]/gi) {
        $js_new_delim =~ s/[#]/!!pnd!!/gi;
    }
    if ($js_new_delim =~ m/["]/gi) {
        #$js_new_delim =~ s/["]/&~034;/gi;
        $js_new_delim =~ s/["]/&quot;/gi;
    }



    return $js_new_delim;
}   ##js_delim_exch($)

############################################################################
sub undo_js_delim_exch($)        #05/20/05 pfk
# Use this sub to undo the mangling by js_delim_exch.
############################################################################
 {
    my ($js_new_delim) = @_;
    if ($js_new_delim =~ m/&~039;/gi) {
        $js_new_delim =~ s/&~039;/'/gi;
    }
    if ($js_new_delim =~ m/!!amp!!/gi) {
        $js_new_delim =~ s/!!amp!!/&/gi;
    }
    if ($js_new_delim =~ m/!!equ!!/gi) {
        $js_new_delim =~ s/!!equ!!/=/gi;
    }
    if ($js_new_delim =~ m/!!plu!!/gi) {
        $js_new_delim =~ s/!!plu!!/+/gi;
    }
    if ($js_new_delim =~ m/!!pnd!!/gi) {
        $js_new_delim =~ s/!!pnd!!/#/gi;
    }
    if ($js_new_delim =~ m/&quot;/gi) {
        $js_new_delim =~ s/&quot;/"/gi;
    }

    return $js_new_delim;
}   ##undo_js_delim_exch($)

############################################################################
sub delim_return($)     #02/28/01 11:21:AM
# To insert data into database, need to transform the ASCII characters back
# to their original form and turn the single quotes to double single quotes
# for an escape.
############################################################################
 {
    my ($delim_return) = @_;
    if ($delim_return =~ m/!!amp!!!!pnd!!039;/gi) {
        $delim_return =~ s/!!amp!!!!pnd!!039;/''/gi;
    }
    if ($delim_return =~ m/!!amp!!/gi) {
        $delim_return =~ s/!!amp!!/&/gi;
    }
    if ($delim_return =~ m/!!pnd!!/gi) {
        $delim_return =~ s/!!pnd!!/#/gi;
    }
    if ($delim_return =~ m/&~034;/gi) {
        $delim_return =~ s/&~034;/"/gi;
    }
    if ($delim_return =~ m/&~039;/gi) {
        $delim_return =~ s/&~039;/'/gi;
    }
    if ($delim_return =~ m/&quot;/gi) {
        $delim_return =~ s/&quot;/"/gi;
    }
    if ($delim_return =~ m/[']/gi) {
        $delim_return =~ s/[']/''/gi;
    }
    if ($delim_return =~ m/!!equ!!/gi) {
        $delim_return =~ s/!!equ!!/=/gi;
    }
    if ($delim_return =~ m/!!plu!!/gi) {
        $delim_return =~ s/!!plu!!/+/gi;
    }


=head
    if ($delim_return =~ m/[>]/gi) {
        $delim_return =~ s/[>]/&gt;/gi;
    }
    if ($delim_return =~ m/[<]/gi) {
        $delim_return =~ s/[<]/&lt;/gi;
    }
=cut

    return $delim_return;

}   ##delim_return($)
############################################################################
sub cleanHash(%)        #03/01/01 3:29:PM
#this sub will take the values of a hash and search and replace double and
# single quotes by way of the delim_exch sub..
############################################################################
 {
    my (%hashRef) = @_;
    my $key;
    my $value;
    while (($key, $value) = each(%hashRef)) {
    $hashRef{$key} = delim_exch($value);
}
    return %hashRef;
}   ##cleanHash(%)
############################################################################

############################################################################
sub cleanHashCGI(%)        # 10/31/01 4:35 PM
						   # Uses CGI::escape to clean incoming hash to pass
						   # as a URL
						   # CURRENTLY NOT FUNCTIONAL because CGI messes up
						   # postInputs.
{
#	use CGI;

    my (%hashRef) = @_;
    my $key;
    my $value;
    while (($key, $value) = each(%hashRef)) {
    	$hashRef{$key} = ($value);
	}

	return %hashRef;

}   ##cleanHashCGI(%)
############################################################################

############################################################################
sub returnHash(%)       #03/02/01 9:20:AM
#Same as above sub except that this will return values for the database
# insertion...
############################################################################
 {
    my (%hashRef) =@_;
    my $key;
    my $value;
    while (($key, $value) = each(%hashRef)) {
        $hashRef{$key} = delim_return($value);
    }
    return %hashRef;
}   ##returnHash(%)
############################################################################

############################################################################
sub js_cleanHash(%)        #03/01/01 3:29:PM
#this sub will take the values of a hash and search and replace double and
# single quotes by way of the delim_exch sub..USE ONLY FOR JAVASCRIPT LINKS
# SEE JS_DELIM_EXCH FOR DETAILS.....
############################################################################
 {
    my (%hashRef) = @_;
    my $key;
    my $value;
    while (($key, $value) = each(%hashRef)) {
    $hashRef{$key} = js_delim_exch($value);
}
    return %hashRef;
}   ##cleanHash(%)
############################################################################

############################################################################
sub checkDate($)        #03/16/01 9:32:AM
############################################################################
 {
    my ($dateCheck) = @_;

    my @date_value = (split /\//, $dateCheck);
    my ($month, $day, $year);
        $month = $date_value[0];
        $day = $date_value[1];
        $year = $date_value[2];
        if ( length($month) > 0 && length($day) > 0 && length($year) > 0 ) {
            if ( $year >= 90 && $year < 100 ) {
                $year += 1900;
            }elsif ( $year >= 0 && $year <= 89 ) {
                $year += 2000;
            }

            if (check_date($year, $month, $day) == 1) {
                $dateCheck = $dateCheck;
            } else {
                $dateCheck = -1;
            }
        }else{
            $dateCheck = -1;
        }
    return $dateCheck;

}   ##checkDate($)


############################################################################
sub get_date()      #04/04/01 2:24:PM
############################################################################
 {
my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);
$year = substr ($year, 2, 2);
$dayofMonth = sprintf("%02s",$dayofMonth);
my $monthval = get_month();

#my $db_mnth = new Win32::ODBC($main::DSN);
#my $mnth = "Select number From month  with (nolock) Where nameAbrev = '$month'";
#            $db_mnth->Sql($mnth);
#            $db_mnth->FetchRow();
#                my %mnthHash = $db_mnth->DataHash();
#            $db_mnth->Close();

	my $new_date;
	if ($main::cust{date_type} > 0 ) {
		if ( $main::cust{date_type} == 1 ) {
			$new_date = "$monthval\/$dayofMonth\/$year";
		}else{
			$new_date = "$dayofMonth\/$monthval\/$year";
		}
	}else{
		if ( $main::session{date_type} == 3 ) {
			$new_date = "$dayofMonth\/$monthval\/$year";
		}else{
			$new_date = "$monthval\/$dayofMonth\/$year";
		}
	}

return $new_date;

}   ##get_date()
############################################################################
sub get_datedb()      #04/04/01 2:24:PM
############################################################################
 {
my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);
$year = substr ($year, 2, 2);
$dayofMonth = sprintf("%02s",$dayofMonth);
my $monthval = get_month();
#my $db_mnth = new Win32::ODBC($main::DSN);
#my $mnth = "Select number From month  with (nolock) Where nameAbrev = '$month'";
#            $db_mnth->Sql($mnth);
#            $db_mnth->FetchRow();
#                my %mnthHash = $db_mnth->DataHash();
#            $db_mnth->Close();

	my $new_date;
	$new_date = "$monthval\/$dayofMonth\/$year";

return $new_date;

}   ##get_date()
############################################################################
sub get_year()      #04/04/01 2:24:PM
############################################################################
 {
my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);
my $new_year = $year;
return $new_year;
}   ##get_date()
############################################################################
sub get_month()      #7/5/01 1:30pm DLF
############################################################################
 {
my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);
my %months = ('Jan' => '01',
	'Feb' => '02',
	'Mar' => '03',
	'Apr' => '04',
	'May' => '05',
	'Jun' => '06',
	'Jul' => '07',
	'Aug' => '08',
	'Sep' => '09',
	'Oct' => '10',
	'Nov' => '11',
	'Dec' => '12');

#my $db_mnth = new Win32::ODBC($main::DSN);
#my $mnth = "Select number From month  with (nolock) Where nameAbrev = '$month'";
#            $db_mnth->Sql($mnth);
#            $db_mnth->FetchRow();
#                my %mnthHash = $db_mnth->DataHash();
#            $db_mnth->Close();
my $new_month = $months{$month};
#$db_mnth->Close();
return $new_month;
}   ##get_date()
############################################################################
sub get_day()      #7/5/01 1:30pm DLF
############################################################################
 {
my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);
my $new_day = $dayofMonth;
return $new_day;
}   ##get_date()

############################################################################
sub get_datetime()      #09/26/01 7:30PM
############################################################################
 {
my ($day, $month, $dayofMonth, $time, $year) = split(/\s+/,localtime(time),5);
$year = substr ($year, 2, 2);
my $monthval = get_month();

#my $db_mnth = new Win32::ODBC($main::DSN);
#my $mnth = "Select number From month  with (nolock) Where nameAbrev = '$month'";
#            $db_mnth->Sql($mnth);
#            $db_mnth->FetchRow();
#                my %mnthHash = $db_mnth->DataHash();
#            $db_mnth->Close();
my $new_date = "$monthval\/$dayofMonth\/$year $time";
#$db_mnth->Close();
return $new_date;

}   ##get_date()

############################################################################
sub EscQuote($)     # 03/30/01 5:40PM  -- RF
					# Escapes single quotes
					# Use for preparing strings for SQL statements.
############################################################################
{
    my ($delim_return) = @_;
	$delim_return =~ s/[']/''/gi;
    return $delim_return;
}   ##EscQuote($)

############################################################################
sub EscQuoteHash(%)       #03/02/01 9:20:AM
# Runs EscQuote on a hash
############################################################################
 {
    my (%hashRef) =@_;
    my $key;
    my $value;
    while (($key, $value) = each(%hashRef)) {
        $hashRef{$key} = EscQuote($value);
    }
    return %hashRef;
}   ##returnHash(%)
############################################################################

############################################################################
sub JSEscQuote ($)		# 11/01/01 10:51:PM
						# Escapes both single and double quotes.
						# Use this function to make strings usable within
						# JavaScript functions.
############################################################################
{
    my ($delim_return) = @_;
	$delim_return =~ s/[']/\\'/gi;
	$delim_return =~ s/["]/\\\\"/gi;
    return $delim_return;
}	##JSEscQuote ($)

############################################################################
sub StripQuote($)     #03/30/01 5:40PM  -- RF
############################################################################
{
    my ($delim_return) = @_;
	$delim_return =~ s/[']//gi;
    return $delim_return;
}   ##StripQuote($)


############################################################################
sub valEmail()      #06/27/01 11:15:AM
############################################################################
 {
    my ($email) = @_;
        ## First strip out all unwanted characters ##
        $email =~ s/[\'\$\"\*\~\`\!\#\%\^\*\(\)\+\=\|\\\{\}\[\]\:\;\?\/\>\<\,]//gi;

        ## check for the @ sign ##
        if ( $email !~ s/@/\@/gi ) {$email = -1;}else{$email = $email;}

        ## check for the period ##
        if ( $email !~ m/\./ ) {$email = -1;}else{$email = $email;}

    return $email;
}   ##valEmail()

############################################################################
sub ad_delim_return($)     #08/15/01 1:08:PM
############################################################################
 {
    my $ad_delim_return = @_[0];
    if ($ad_delim_return =~ m/&~034;/gi) {
        $ad_delim_return =~ s/&~034;/"/gi;
    }
    if ($ad_delim_return =~ m/[']/gi) {
        $ad_delim_return =~ s/[']/''/gi;
    }
    if ($ad_delim_return =~ m/=/gi) {
        $ad_delim_return =~ s/=/!!equ!!/gi;
    }
    if ($ad_delim_return =~ m/[&]/gi) {
        $ad_delim_return =~ s/[&]/!!amp!!/gi;
    }

    return $ad_delim_return;
}   ##ad_delim_return
############################################################################
sub ad_delim_normal($)     #08/15/01 1:08:PM
############################################################################
 {
    my $ad_delim_normal = @_[0];
    if ($ad_delim_normal =~ m/!!equ!!/gi) {
        $ad_delim_normal =~ s/!!equ!!/=/gi;
    }
    if ($ad_delim_normal =~ m/[!!amp!!]/gi) {
        $ad_delim_normal =~ s/!!amp!!/&/gi;
    }
    if ($ad_delim_normal =~ m/"/gi) {
        $ad_delim_normal =~ s/"/&quot;/gi;
    }
    return $ad_delim_normal;
}   ##ad_delim_return
############################################################################
sub doublesingle($)        #08/15/01 5:51:PM
############################################################################
 {
    my $doublesingle = @_[0];
    if ($doublesingle =~ m/[']/gi) {
        $doublesingle =~ s/[']/\''/gi;
    }
    if ($doublesingle =~ m/&quot;/gi) {
        $doublesingle =~ s/&quot;/"/gi;
    }
    return $doublesingle;
}   ##doublesingle

###############################################################
# Various Usage of String Manipulation Functions
# $ to SQL: EscQuote($)
# $ to HTML text or option field: EE($)
# $ to HTML textarea field: $ (no change)
# $ to JavaScript URL (i.e. window.open) : CGI::escape($)
# $ to JavaScript string: JSEscQuote($)
# $ to JavaScript string within HTML event: EE(JSEscQuote($))
###############################################################

############################################################################
sub get_path($$)		# 05/21/02 12:49:PM RF
					# Given path + filename and delimiter character (usually / or \),
					# returns the path
					# e.g. "/dir1/dir2/myfile.txt" returns "/dir1/dir2/"
############################################################################
 {
	my ($fullpathname, $delimiter) = @_;
	if ( $delimiter eq '' ) {
		$delimiter = '/';
	}
	my $pos = length($fullpathname)-1;
	my $result = -1;
	my $path = "";  #If slash isn't found, return empty string
	while ( $pos >= 0 && $result == -1) {
		$result = index($fullpathname, $delimiter, $pos);
		$pos--;
	}
	if ( $result > -1 ) {
		$path = substr($fullpathname, 0, $result + 1);
	}
	return $path;
}	##get_path($)

############################################################################
sub get_filename($$)		# 05/21/02 12:49:PM RF
					    # Given path + filename and delimiter character (usually / or \),
						# returns the filename
					    # e.g. "/dir1/dir2/myfile.txt" returns "myfile.txt"
############################################################################
 {
	my ($fullpathname, $delimiter) = @_;
	if ( $delimiter eq '' ) {
		$delimiter = '/';
	}
	my $pos = length($fullpathname)-1;
	my $result = -1;
	my $filename = $fullpathname;  #If slash isn't found, default to $fullpathname
	while ( $pos >= 0 && $result == -1) {
		$result = index($fullpathname, $delimiter, $pos);
		$pos--;
	}
	if ( $result > -1 ) {
		$filename = substr($fullpathname, $result + 1, (length($fullpathname) - $result));
	}
	return $filename;
}	##get_filename($)

############################################################################
sub checkNumber($)        # 6/28/02 RF
						  # Validates a number.  Allows digits, '-', and '.'
						  # Returns 1 if valid, 0 if not.
############################################################################
{
	my $num = @_[0];
	my $result;
	# Strip out all valid number characters.  If any characters are left, then
	# the number is invalid.
	$num =~ s/[0-9,.-]//gi;
    if (length($num) == 0) {
		$result = 1;
	}
	else {
		$result = 0;
	}
    return $result;

}   ##checkNumber($)

############################################################################
sub ShortDate($)		# 10/14/02 3:24:PM
						# Truncates 4-digit year to 2-digit year;
						# e.g. '10/14/2002' returns '10/14/02'
						# e.g. '9/15/02' returns '9/15/02' (no change)
						# Used in imports as for some undetermined reason,
						# 4-digit years poses a problem for some imports
############################################################################
{
	my ($date) = @_;

	my @parts = split (/\//, $date);
	my $month = $parts[0];
	my $day = $parts[1];
	my $year = $parts[2];
	my $shortyear = substr($year, length($year)-2, 2);
	my $result = $month . "/" . $day . "/" . $shortyear;
	return ($result);
}	##ShortDate($)

############################################################################
sub ExcelColLetter($)	# 03/18/04 3:35:PM
						# Given a zero-indexed column number, returns its corresponding Excel column letter.
						# Reciprocal sub is ExcelColNum($).
						# Example:
						# 0 =>   A
						# 1 =>   B
						# ...
						# 25 =>  Z
						# 26 => AA
						# 27 => AB
						# ...
						# 52 => BA
						# 53 => BB
						# ...
						# 255 => IV
############################################################################
{
	my ($col) = @_;

	my $result = '';
	my $letter1 = chr(($col % 26) + 65);
	my $letter2 = '';
	my $pos2 = int($col/26);
	if ( $pos2 > 0 ) {
		$letter2 = chr($pos2+64);
	}

	$result = "$letter2$letter1";
	return ($result);
}	##ExcelColLetter($)

############################################################################
sub ExcelColNum($)		# 03/24/04 2:45:PM
						# Given an Excel column letter, returns its corresponding zero-indexed column number.
						# Reciprocal sub is ExcelColLetter($).
						# Example:
						# 0 <=   A
						# 1 <=   B
						# ...
						# 25 <=  Z
						# 26 <= AA
						# 27 <= AB
						# ...
						# 52 <= BA
						# 53 <= BB
						# ...
						# 255 <= IV
############################################################################
{
	my ($letter) = @_;
	my $result;
	if ( length($letter) == 1 ) {
		$result = ord($letter) - 65;
	}
	else {
		$result = ((ord(substr($letter, 0, 1)) - 64) * 26) + (ord(substr($letter, 1, 1)) - 65);
	}
	return ($result);
} ##ExcelColNum($)

return 1;
