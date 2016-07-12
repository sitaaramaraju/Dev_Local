# File: cgi-bin\contact.cgi
# Perl script that provides functions pertaining to contact, customer
# and group linkage management
#
# IMPORTANT NOTE: To create or break links between Contacts, Customers and Groups,
# you must use linking functions LinkContactToCust(), LinkGroupToContact(),
# LinkCustToGroup(), or LinkGroupToGroup() in order to ensure link integrity
# between those entities.
#
# Last revised 3/26/2001
# Added NOLOCKs 12/9/03

#use cgi::cookie;
use DBInterface;

############################################################################
sub CreateContact($$$$$$$$$$$$$$$$$$$)	#3/23/01 2:30 PM
# modified to go with DBI module
# Creates a contact_info record, provided the required 19 parameters:
#
# 1.  @client_id int
# 2.  @prefix varchar(25)
# 3.  @first_name varchar(50)
# 4.  @middle_name varchar(30)
# 5.  @last_name varchar(30)
# 6.  @suffix varchar(25)
# 7.  @title varchar(50)
# 8.  @address1 varchar(75)
# 9.  @address2 varchar(75)
# 10. @city varchar(50)
# 11. @state varchar(50)
# 12. @zip varchar(50)
# 13. @country varchar(50)
# 14. @phone varchar(50)
# 15. @fax varchar(50)
# 16. @cellular varchar(50)
# 17. @e_mail varchar(50)
# 18. @notes varchar(4000)
# 19. @session_id int
# 20. @cust_id
# 21. @contact_status
# 22. @is_primary_contact
# Returns contact_info_id for new contact created.  If SQL Server fails to
# create contact, -1 is returned.
############################################################################
{
	my ($client_id, $prefix, $first_name, $middle_name, $last_name, $suffix, $title,
		$address1, $address2, $city, $state, $zip, $country, $phone, $fax, $cellular,
        $e_mail, $notes, $session_id, $cust_id, $contact_status, $is_primary_contact) = @_;
	my $contact_info_id;

	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();


	# Stored Procedure call definition to ContactCreate
	# exec ContactCreate @client_id int = -1, @prefix varchar(25) = '', @first_name varchar(50) = '',
	# @middle_name varchar(30) = '', @last_name varchar(30) = '', @suffix varchar(25) = '',
	# @title varchar(50) = '', @address1 varchar(75) = '', @address2 varchar(75) = '',
	# @city varchar(50) = '', @state varchar(50) = '', @zip varchar(50) = '',
	# @country varchar(50) = '', @phone varchar(50) = '', @fax varchar(50) = '',
	# @cellular varchar(50), @e_mail varchar(50) = '', @notes varchar(4000) = '',
	# @session_id int, @contact_info_id int output as

	# Escape single quotes for all possible fields
	$prefix = EscQuote($prefix);
	$first_name = EscQuote($first_name);
	$middle_name = EscQuote($middle_name);
	$last_name = EscQuote($last_name);
	$suffix = EscQuote($suffix);
	$title = EscQuote($title);
	$address1 = EscQuote($address1);
	$address2 = EscQuote($address2);
	$city = EscQuote($city);
	$state = EscQuote($state);
	$zip = EscQuote($zip);
	$country = EscQuote($country);
	$phone = EscQuote($phone);
	$fax = EscQuote($fax);
	$cellular = EscQuote($cellular);
	$e_mail = EscQuote($e_mail);
	$notes = EscQuote($notes);
    $cust_id = EscQuote($cust_id);
    $contact_status = EscQuote($contact_status);
    $is_primary_contact = EscQuote($is_primary_contact);

	#Define SQL statement
	my $SQL = "declare \@contact_info_id int " .
		"execute ContactCreate $client_id, '$prefix', '$first_name', " .
		"'$middle_name', '$last_name', '$suffix', " .
		"'$title', '$address1', '$address2', " .
		"'$city', '$state', '$zip', " .
		"'$country', '$phone', '$fax', " .
		"'$cellular', '$e_mail', '$notes', " .
        "$session_id, $cust_id, $contact_status, $is_primary_contact, \@contact_info_id output " .
		"select \@contact_info_id as contact_info_id";
	#Execute SQL

		my $sth = $myDB->prepare($SQL);
		$sth->execute();
		my $user = $sth->fetchrow_hashref();
		$sth->finish();	
		$contact_info_id = $user->{contact_info_id};
		
		if ($contact_info_id <= 0) {
			$contact_info_id = -1;
		}

		$myDB->disconnect();

		return $contact_info_id;
	
}	##CreateContact

############################################################################
sub EditContact($$$$$$$$$$$$$$$$$$$$)	#3/23/01 2:30 PM
# Creates a contact_info record, provided the required 20 parameters:
#
# 1.  @contact_info_id int
# 2.  @client_id int
# 3.  @prefix varchar(25)
# 4.  @first_name varchar(50)
# 5.  @middle_name varchar(30)
# 6.  @last_name varchar(30)
# 7.  @suffix varchar(25)
# 8.  @title varchar(50)
# 9.  @address1 varchar(75)
# 10. @address2 varchar(75)
# 11. @city varchar(50)
# 12. @state varchar(50)
# 13. @zip varchar(50)
# 14. @country varchar(50)
# 15. @phone varchar(50)
# 16. @fax varchar(50)
# 17. @cellular varchar(50)
# 18. @e_mail varchar(50)
# 19. @notes varchar(4000)
# 20. @session_id int
############################################################################
{
	my ($contact_info_id, $client_id, $prefix, $first_name, $middle_name, $last_name,
		$suffix, $title, $address1, $address2, $city, $state, $zip, $country, $phone,
		$fax, $cellular, $e_mail, $notes, $session_id) = @_;

	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();
	# Stored Procedure call definition to ContactCreate
	# exec ContactEdit @contact_info_id int, @client_id int = -1, @prefix varchar(25) = '',
	# @first_name varchar(50) = '', @middle_name varchar(30) = '',
	# @last_name varchar(30) = '', @suffix varchar(25) = '', @title varchar(50) = '',
	# @address1 varchar(75) = '', @address2 varchar(75) = '', @city varchar(50) = '',
	# @state varchar(50) = '', @zip varchar(50) = '', @country varchar(50) = '',
	# @phone varchar(50) = '', @fax varchar(50) = '', @cellular varchar(50) = '',
	# @e_mail varchar(50) = '', @notes varchar(4000) = '', @session_id int as

	# Escape single quotes for all possible fields
	$prefix = EscQuote($prefix);
	$first_name = EscQuote($first_name);
	$middle_name = EscQuote($middle_name);
	$last_name = EscQuote($last_name);
	$suffix = EscQuote($suffix);
	$title = EscQuote($title);
	$address1 = EscQuote($address1);
	$address2 = EscQuote($address2);
	$city = EscQuote($city);
	$state = EscQuote($state);
	$zip = EscQuote($zip);
	$country = EscQuote($country);
	$phone = EscQuote($phone);
	$fax = EscQuote($fax);
	$cellular = EscQuote($cellular);
	$e_mail = EscQuote($e_mail);
	$notes = EscQuote($notes);

	#Define SQL statement
	my $SQL = "execute ContactEdit $contact_info_id, $client_id, '$prefix', '$first_name', " .
		"'$middle_name', '$last_name', '$suffix', " .
		"'$title', '$address1', '$address2', " .
		"'$city', '$state', '$zip', " .
		"'$country', '$phone', '$fax', " .
		"'$cellular', '$e_mail', '$notes', " .
		"$session_id";
		my $sth = $myDB->prepare($SQL);
		$sth->execute();
		$sth->finish();	
		$myDB->disconnect();

}	##EditContact

############################################################################
sub LinkContactToCust($$$$)		#03/26/01 12:57:PM
# Links or unlinks a Contact to a Customer, given contact_info_id, cust_id,
# session_id and construct bit (specifies whether to link or unlink)
#
# Argument list:
# 1. contact_info_id  int
# 2. cust_id          int
# 3. session_id       int
# 4. construct        bit (0 to unlink, 1 to link)
#
############################################################################
{
	my ($contact_info_id, $cust_id, $session_id, $construct) = @_;
	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();
	#SQL SP declaration:
	#CREATE procedure LinkContactToCust @ContactInfoID integer, @CustID integer, @SessionID integer, @Construct bit as

	#Define SQL statement
	my $SQL = "execute LinkContactToCust $contact_info_id, $cust_id, $session_id, $construct";
		my $sth = $myDB->prepare($SQL);
		$sth->execute();
		$sth->finish();	
		$myDB->disconnect();

}	##LinkContactToCust

############################################################################
sub LinkGroupToContact($$$$)		#03/26/01 1:25:PM
# Links or unlinks a Group to a Contact, given group_id, contact_info_id,
# session_id and construct bit (specifies whether to link or unlink)
#
# Argument list:
# 1. group_id         int
# 2. contact_info_id  int
# 3. session_id       int
# 4. construct        bit (0 to unlink, 1 to link)
#
############################################################################
{
	my ($group_id, $contact_info_id, $session_id, $construct) = @_;
	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();
	#SQL SP declaration:
	#CREATE procedure LinkGroupToContact @GroupID integer, @ContactInfoID integer, @SessionID integer, @Construct bit as

	#Define SQL statement
	my $SQL = "execute LinkGroupToContact $group_id, $contact_info_id, $session_id, $construct";
		my $sth = $myDB->prepare($SQL);
		$sth->execute();
		$sth->finish();	
		$myDB->disconnect();

}	##LinkGroupToContact

############################################################################
sub LinkCustToGroup($$$$)		#03/26/01 1:25:PM
# Links or unlinks a Customer to a Group, given cust_id, group_id,
# session_id and construct bit (specifies whether to link or unlink)
#
# Argument list:
# 1. cust_id          int
# 2. group_id         int
# 3. session_id       int
# 4. construct        bit (0 to unlink, 1 to link)
#
############################################################################
{
	my ($cust_id, $group_id, $session_id, $construct) = @_;
	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();
	#SQL SP declaration:
	#CREATE procedure LinkCustToGroup @CustID integer, @GroupID integer, @SessionID integer, @Construct bit as

	#Define SQL statement
	my $SQL = "execute LinkCustToGroup $cust_id, $group_id, $session_id, $construct";
		my $sth = $myDB->prepare($SQL);
		$sth->execute();
		$sth->finish();	
		$myDB->disconnect();

}	##LinkCustToGroup

############################################################################
sub LinkGroupToGroup($$$$)		#03/26/01 1:30:PM
# Links or unlinks a Group to a Sub-Group, given group_id, sub_group_id,
# session_id and construct bit (specifies whether to link or unlink)
#
# Argument list:
# 1. group_id         int
# 2. sub_group_id     int
# 3. session_id       int
# 4. construct        bit (0 to unlink, 1 to link)
#
############################################################################
{
	my ($group_id, $sub_group_id, $session_id, $construct) = @_;
	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();
	#SQL SP declaration:
	#CREATE procedure LinkGroupToGroup @GroupID integer, @SubGroupID integer, @SessionID integer, @Construct bit as

	#Define SQL statement
	my $SQL = "execute LinkGroupToGroup $group_id, $sub_group_id, $session_id, $construct";
		my $sth = $myDB->prepare($SQL);
		$sth->execute();
		$sth->finish();	
		$myDB->disconnect();

}	##LinkGroupToGroup

############################################################################
sub EscQuote($)     #03/23/01 2:42 PM
# Escapes single quotes with two single quotes to comply with SQL syntax
############################################################################
{
    my ($delim_return) = @_;
	$delim_return =~ s/[']/''/gi;
	return $delim_return;
}   ##EscQuote($)

############################################################################
sub CreateStaffRecords($$$$$$$$)        #04/04/01 4:29:PM
# Creates a staff and associated staff_client_list record given the
# following parameters:
#
# 1. LogonID varchar(50)  -- user name
# 2. Password varchar(50) -- password
# 3. IsActive bit (1 is True, 0 is False)  --whether user is active or not
# 4. contact_info_id int  -- associated contact_info_id
# 5. client_id int        -- client_id for which staff_client_list record will be written
# 6. user_level varchar(50)  -- user's level ("CU", "MN", "AR", "Coordinator", etc.)
# 7. cu_cust_id int -- CU user's cust_id; use -1 if not applicable
# 8. session_id int -- current session_id
#
# Returns the new staff_id created.  On error:
# -1 => Logon/Password already exists
# -2 => No staff_id returned from SP
# -3 => No user_type for user_level found
############################################################################
{
	my ($LogonID, $Password, $IsActive, $contact_info_id, $client_id, $user_level, $cu_cust_id, $session_id) = @_;

	#my $myDB = new Win32::ODBC($main::DSN);
	my $myDB = DBInterface->new();
	my $myDB2 = DBInterface->new();
	my $myDB4 = DBInterface->new();

	my $LevelID;
	my $NewStaffID;
    my $SQL = "select 0 as staff_id UNION select staff_id from staff with (nolock) where LogonID = '$LogonID' and Password = '$Password' order by 1 desc";
		my $sth = $myDB->prepare($SQL);
		$sth->execute();
		my $user = $sth->fetchrow_hashref();
		$sth->finish();	


	# if (valid LogonID and Password already exist)
	if ($user->{staff_id} > 0  and $LogonID ne "<<<INVALID>>>" and $Password ne "<<<INVALID>>>"){
		# then return an error
		$myDB->disconnect();
		return -1;
	}
	else {
		# Determine user_type_id from user_level;
        my $LevelSQL = "select user_type_id from WebAccessLevel with (nolock) where name = '$user_level'";
		my $sth2 = $myDB->prepare($LevelSQL);
		$sth2->execute();

		#if ($DBLevel->FetchRow()) {
		if (my $LevelHash = $sth2->fetchrow_hashref()) {
 			$LevelID = $LevelHash->{user_type_id};
 			#Initiate call to SP

            my $StaffSQL = "execute CreateStaffRecord '$LogonID', '$Password', $IsActive, $contact_info_id, $LevelID, $session_id";
            $NewStaffID = "";

			my $sth3 = $myDB2->prepare($StaffSQL);
			$sth3->execute();

		#if ($DBLevel->FetchRow()) {
		if (my $StaffHash = $sth3->fetchrow_hashref()) {
				#New staff_id returned from SP CreateStaffRecord
 				$NewStaffID = $StaffHash->{staff_id};

				#Initiate call to SP CreateStaffClientListRecord
                my $StaffClientSQL = "execute CreateStaffClientListRecord " . $NewStaffID. " , $client_id, '$user_level',  $cu_cust_id, $session_id";
				my $sth4 = $myDB4->prepare($StaffClientSQL);
				$sth4->execute();
				$sth4->finish();	
				return $NewStaffID;
            }
            else {
                #No staff_id returned from SP CreateStaffRecord; return error.
                return -2;
            }
		}
		else {
			# No user_type_id found for $user_level provided; return error.
			return -3;
		}
	}

		$myDB->disconnect();
		$myDB2->disconnect();
		$myDB4->disconnect();

}	##CreateCUStaffRecords

return 1;



