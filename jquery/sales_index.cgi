use strict;
	use warnings;
	use CGI::Carp qw/ fatalsToBrowser /;
	use CGI qw(:standard);
	use Date::Calc qw(Today Add_Delta_Days);
	my $cgi = CGI->new();
    require "G:/CenturyLink/xroot/cgi-bin/delimeter.cgi";
	require "G:/CenturyLink/xroot/cgi-bin/init.cgi";
	
	my $db = Win32::ODBC->new($main::DSN);
	my (%state, $sql, $str);
	
	$sql = "select distinct state from lp_states order by state";
	$db->Sql($sql);
	while ( $db->FetchRow()) {
		%state = $db->DataHash();	
			$str .= $state{state}."," ;			
	}
	
	print "$str";
	

<!doctype html>
<html lang="us">
<head>
	<meta charset="utf-8">
	<title>jQuery UI Example Page</title>
	<link href="css/ui-lightness/jquery-ui-1.10.4.custom.css" rel="stylesheet">
	<script src="js/jquery-1.10.2.js"></script>
	<script src="js/jquery-ui-1.10.4.custom.js"></script>
	
	<script>
	
	$( function() {
		
		var availableTags = [ "ActionScript", "AppleScript", "Asp", "BASIC", "C", "C++", "Clojure", "COBOL", "ColdFusion", "Erlang", "Fortran",
			"Groovy", "Haskell", "Java", "JavaScript", "Lisp", "Perl",
			"PHP",
			"Python",
			"Ruby",
			"Scala",
			"Scheme"
		];
		$( "#autocomplete" ).autocomplete({
			source: availableTags
		});
		

	});
	</script>
	<style>
	body{
		font: 62.5% "Trebuchet MS", sans-serif;
		margin: 50px;
	}
	.demoHeaders {
		margin-top: 2em;
	}
	#dialog-link {
		padding: .4em 1em .4em 20px;
		text-decoration: none;
		position: relative;
	}
	#dialog-link span.ui-icon {
		margin: 0 5px 0 0;
		position: absolute;
		left: .2em;
		top: 50%;
		margin-top: -8px;
	}
	#icons {
		margin: 0;
		padding: 0;
	}
	#icons li {
		margin: 2px;
		position: relative;
		padding: 4px 0;
		cursor: pointer;
		float: left;
		list-style: none;
	}
	#icons span.ui-icon {
		float: left;
		margin: 0 4px;
	}
	.fakewindowcontain .ui-widget-overlay {
		position: absolute;
	}
	</style>
</head>
<body>


<!-- Autocomplete -->
<h2 class="demoHeaders">Autocomplete</h2>
<div>
	<input id="autocomplete" title="type &quot;a&quot;">
</div>

</body>
</html>
