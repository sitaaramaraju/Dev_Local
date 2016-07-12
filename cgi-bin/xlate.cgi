############################################################################
#my $db_xlate = new Win32::ODBC("DSN=xlate;UID=fm;PWD=sep49sling");
#my $db_xlate = new Win32::ODBC("driver={SQL Server};Server=1.1.1.2;database=coop;uid=fm;pwd=sep49sling;");
#my $db_xlate = new Win32::ODBC("driver={SQL Server};Server=galaxynew.cciprod.local;database=coop;uid=fm;pwd=sep49sling;");
use DBInterface;
my $db_xlate = DBInterface->new();
sub xlate($)
# Use this sub to translate terms from the language_translate table.
# Pass it a key and it will return a word or phrase from the table
############################################################################
{
        my $xlation = "";
        my $searchfor = uc(@_[0]);
        my $language_id;
        if ( $main::session{language} ) {
            $language_id = $main::session{language};
        }else{
            $language_id = 1;
        }

       my $xlate = "execute sp_xlate ?, ?";
            #$db_xlate->Sql($xlate);
            #$db_xlate->FetchRow();
            #%xlHash = $db_xlate->DataHash();
			
			my $sth = $db_xlate->prepare($xlate);
			$sth->execute($language_id,$searchfor);
			
			my $xlHash = $sth->fetchrow_hashref();
			$sth->finish();
			
			$xlation = $xlHash->{language_translation};            

    return $xlation;
}   ##xlate($)
############################################################################
sub closexlate      #07/25/01 4:24:PM
############################################################################
 {
    $db_xlate->Close();
}   ##closexlate
return 1;
