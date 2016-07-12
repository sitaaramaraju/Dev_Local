# Filename: /cgi-bin/email
# Last Revised 10/29/2001 RF

# Generalized e-mail function
use strict;
use DBInterface;
my $myDB = DBInterface->new();

############################################################################
sub SendEmail($$$$$$)		# 10/29/01 14:23
							# Sends an e-mail given the following parameters:
							# 1. To (e-mail address(es))
							# 2. CC (e-mail address(es))
							# 3. BCC (e-mail address(es))
							# 4. From (e-mail address usually 'postmaster@coopcom.com')
							# 5. Subject
							# 6. Body
							#
							# Returns 0 on success, 1 on error
############################################################################
{
	my ($to, $cc, $bcc, $from, $subject, $body) = @_;
	use Mail::Sender;

	#Replace all semicolons with commas in address vars
	$to =~ s/;/,/g;
	$cc =~ s/;/,/g;
	$bcc =~ s/;/,/g;

#    my $sender = new Mail::Sender({from=>"$from",
#                    smtp => 'mail.ccionline.biz'});

#                    if (!(ref $sender) =~ /Sender/i){
#                        print "ERROR:  $Mail::Sender::Error\n";
#                        return 1;
#                    }

#    $sender->OpenMultipart({to=>"$to", bcc=>"$bcc", cc=>"$cc",
#        subject=>"$subject"});

#    $sender->Body;
#    $sender->SendLine("$body\n");
#    $sender->Close;

#    if ( ($sender->{'error'}) < 0 ) {
#        print "ERROR:  $Mail::Sender::Error\n";
#        return 1;
#    }
#    else {
#        return 0;
#    }

    #my $db = new Win32::ODBC($main::DSN);
    my $sql = "insert into ccimail (tofield, ccfield, bccfield, fromfield, subject,longbody) values
        ('" . EscQuote($to) . "','" . EscQuote($cc) . "','" . EscQuote($bcc) . "','" . EscQuote($from). "','" .EscQuote($subject). "','')";
		my $sth = $myDB->prepare($sql);
   if ( ! $sth->execute() ) {
       my $thisfile = "email.cgi";
       my $err = "Unable to insert into ccimail";
       my $msg = $myDB->Error();
       dienicely($err, $sql, $msg, $thisfile, \%main::session,0,0,0,\%main::postInputs);
   }else{
    $sth->execute();
	my $email = $sth->fetchrow_hashref();
	$sth->finish();
    #my %email = $db->DataHash();
    $sql = "exec spUpdateCCIMail " . $email->{ccimail_id} . ",'" . EscQuote($body) . "'";
	my $sth = $myDB->prepare($sql);
	
    if ( ! $sth->execute() ) {
       my $thisfile = "email.cgi";
       my $err = "Unable to insert TEXT field into ccimail";
       my $msg = $myDB->Error();
       dienicely($err, $sql, $msg, $thisfile, \%main::session,0,0,0,\%main::postInputs);
   }
   }

	return 0;

}	##SendEmail($$$$$$)

############################################################################
sub SendEmailNoDB($$$$$$)		# 10/15/2003 09:10AM
								# Sends an e-mail, without writing to ccimail, given the following parameters:
								# 1. To (e-mail address(es))
								# 2. CC (e-mail address(es))
								# 3. BCC (e-mail address(es))
								# 4. From (e-mail address usually 'postmaster@coopcom.com')
								# 5. Subject
								# 6. Body
								#
							# Returns 0 on success, 1 on error
############################################################################
{
	my ($to, $cc, $bcc, $from, $subject, $body) = @_;
	use Mail::Sender;

	#Replace all semicolons with commas in address vars
	$to =~ s/;/,/g;
	$cc =~ s/;/,/g;
	$bcc =~ s/;/,/g;

    my $sender = new Mail::Sender({from=>"$from",
                    smtp => 'mail.ccionline.biz'});

                    if (!(ref $sender) =~ /Sender/i){
                        print "ERROR:  $Mail::Sender::Error\n";
                        return 1;
                    }

    $sender->OpenMultipart({to=>"$to", bcc=>"$bcc", cc=>"$cc",
        subject=>"$subject"});

    $sender->Body;
    $sender->SendLine("$body\n");
    $sender->Close;

    if ( ($sender->{'error'}) < 0 ) {
        print "ERROR:  $Mail::Sender::Error\n";
        return 1;
    }
    else {
        return 0;
    }
}	##SendEmailNoDB($$$$$$)

############################################################################
sub TransactionEmails($$)		# 10/20/03 4:32:PM
								# Perl wrapper function for SP spTransactionEmails that
								# returns a transaction's pertinent e-mail addresses and names
								# given:
								# 	transaction_type_id int => 1 for pre_pa's  (later on I can add pre_claim (2) and problem (3))
								#   id int => pre_pa_id for pre_pa's
############################################################################
{
	my ($transaction_type_id, $id) = @_;

    my $db = new Win32::ODBC($main::DSN);
	my $emailSQL = "execute spTransactionEmails $transaction_type_id, $id";
	$db->Sql($emailSQL);
	my %emails;
	if ( $db->FetchRow() ) {
		%emails = $db->DataHash();
	}
	$db->Close();
	return (%emails);
}	##TransactionEmails($$)
#--------------------------------------------------------------------
sub SendEmailWithAttachment{
    my ($sendto, $subject, $body, $filename, $filedescr) = @_;
    use Mail::Sender;
    use Mozilla::CA; 
    IO::Socket::SSL::set_ctx_defaults( SSL_ca_file => Mozilla::CA::SSL_ca_file(), );
    $sendto =~ s/\s//g;  # Eat spaces


    # Don't bother if nobody to mailto
    return unless $sendto;


    my $sender = new Mail::Sender({from => 'do_not_reply@CCIonline.biz',
                                   smtp => 'mail.ccionline.biz'});

    if (!(ref $sender) =~ /Sender/i){
        return $Mail::Sender::Error;
    }

    $sender->OpenMultipart({to=>$sendto, subject=>$subject});
    $sender->Body;
    $sender->SendLine($body);

    my $pathdis =         "/tmp/$filename";
    my $pathway = "G:/CenturyLink/xroot/tmp/$filename"; # normal case, file in tmp
    if ($filename =~ /\// ){                # like logs/test.txt
        $pathdis =         '/'.$filename;
        $pathway = "d:/xroot/$filename"; # some other place under xroot
    }

    my $temp_dis = "attachment\; filename=$pathdis\; type=image";
    $sender->SendFile(  {description => $filedescr,
                         ctype       => 'Image',
                         encoding    => 'Base64',
                         disposition => $temp_dis,
                         file        => $pathway} );
    $sender->Close;


    if ( ($sender->{'error'}) < 0 ) {
        return $Mail::Sender::Error;
    }
    return '';
}
#from Common154
################################################################

return 1;
