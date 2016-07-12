use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();

require "D:/centurylinkyoucan/cgi-bin/init.cgi";

use DBInterface;
my $myDB = DBInterface->new();

my $special= $cgi->param('special');
my $specialselect = $cgi->param('specialselect') || ''; 

my $thisfile = 'newenroll.cgi';

my $PAGETITLE = 'NEW ENROLLMENT';

require "graf07/header.cgi";
print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>$PAGETITLE</title>
<script language="JavaScript" src="graf07menus.js"></script>
<link href="Style.css" rel="stylesheet" type="text/css" />
<script type="text/JavaScript">
<!--
function MM_openBrWindow(theURL,winName,features) { //v2.0
  window.open(theURL,winName,features);
}

function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}

function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}

function clean_phone(field) {
        // We are looking for exactly 10 digits in the mess
        var val = ''; // string of digits
        for( ii=0; ii < field.value.length; ii++){
            var ch = field.value.charAt(ii);
            if (ch >= "0" && ch <= "9" ){
                val = val + ch;
            }
        }
        if (val.length != 10){
            val = ''; // invalid
        }
        //alert('phone is '+ val);
        return val;
    }

    function trim_spaces(str) {
    return str.replace(/^\\s*|\\s*\$/g,"");
    }



    var prevent_double_submits = 0;
    function checkform() {
        document.newenrollment.redir.value = 1;
        // Check the phone1, it will be the password
        var myphone1 = clean_phone( document.newenrollment.phone1 );
        var myphone2 = clean_phone( document.newenrollment.phone2 );
        var myfirst = trim_spaces(document.newenrollment.first.value);
        var mylast = trim_spaces(document.newenrollment.last.value);
        var myaddr1 = trim_spaces(document.newenrollment.addr1.value);
        var myaddr2 = trim_spaces(document.newenrollment.addr2.value);
        var mycity = trim_spaces(document.newenrollment.city.value);
        var myzip = trim_spaces(document.newenrollment.zip.value);
	var myEmail = trim_spaces(document.newenrollment.email.value);
	var myspecialselect = document.newenrollment.specialselect.value ;


        if(document.newenrollment.redir.value == 1){

	    if (myspecialselect == 'Startek'
			&& !document.newenrollment.confirm.checked ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please confirm that you work for the CenturyLink vendor Startek ');
	    }
	    else if (myspecialselect  == 'Focus' && !document.newenrollment.confirm.checked ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please confirm that you work for the CenturyLink vendor Focus ');
	    }
	    else if (myspecialselect  == 'AFNI' && !document.newenrollment.confirm.checked ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please confirm that you work for the CenturyLink vendor AFNI');
	    }
	    else if (myspecialselect  == 'Allied' && !document.newenrollment.confirm.checked ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please confirm that you work for the CenturyLink vendor Allied');
	    }
	    else if (myspecialselect  == 'ER Solutions' && !document.newenrollment.confirm.checked ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please confirm that you work for the CenturyLink vendor ER Solutions');
	    }
    	    else if (myspecialselect  == 'AFNI'
			&& document.newenrollment.work_city.value == "" ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please choose appropriate work-city ');
	    }
	    else if (myspecialselect  == 'West Manage' && !document.newenrollment.confirm.checked ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please confirm that you work for the CenturyLink vendor West Manage ');
	    }
    	    else if (myspecialselect  == 'West Manage'
			&& document.newenrollment.work_city.value == "" ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please choose appropriate work-city ');
	    }
		else if (myspecialselect == 'Aspen-Mobile Marketing' ) {
	            window.alert('No more enrollments are allowed for Aspen-Mobile Marketing.'); 
				return false;
            }
	    else if (myspecialselect == 'West Manage' ) {
	          if (document.newenrollment.team_name.value == "") {
                document.newenrollment.redir.value = 0;
                window.alert('Please select your West Manage Team Name.'); }
            }
		    else if (myspecialselect == 'ER Solutions' ) {
	          if (document.newenrollment.team_name.value == "") {
                document.newenrollment.redir.value = 0;
                window.alert('Please select your ER Solutions Team Name.'); }
            }
	    else if (myspecialselect  == 'ER Solutions'
			&& document.newenrollment.work_city.value == "" ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please choose appropriate work-city ');
	    }
	    else if (myspecialselect  == 'Dex'
			&& document.newenrollment.work_city.value == "" ) {
			document.newenrollment.redir.value = 0;
			window.alert('Please choose appropriate work-city ');
	    }

            else if (myfirst == "" ) {
                document.newenrollment.redir.value = 0;
                window.alert('Please enter your first name.');
            }
            else if ( mylast == "" ) {
                document.newenrollment.redir.value = 0;
                window.alert('Please enter your last name.');
            }
	    else if (myaddr1 == "" || mycity == "" || document.newenrollment.state.value == "" || myzip == "") {
                document.newenrollment.redir.value = 0;
                window.alert('Please enter your full address.');
            }else if( myphone1 == "") {
                document.newenrollment.redir.value = 0;
                window.alert('Invalid Home Phone number.\\n Because your phone number will be your password,\\n it must include your area code, and have exactly 10 digits');
            }
	    else if ( myEmail == '') {
			if(myspecialselect  != 'ER Solutions' && myspecialselect  != 'Focus' &&
				myspecialselect  != 'CCS' && myspecialselect  != 'Oxford' && myspecialselect  != 'GCServ' && myspecialselect  != 'Alliance One') {
                document.newenrollment.redir.value = 0;
                window.alert('Please Enter your Email.');     }
            }	else if( (document.newenrollment.ssn4.value == "" ) || (isNaN(document.newenrollment.ssn4.value) )) {
                document.newenrollment.redir.value = 0;
                window.alert('Please enter the Last Four Digits of your Social Security Number or Individual Taxpayer Identification Number ');
            }else if( document.newenrollment.yeardob.value  == '' ||
                      document.newenrollment.monthdob.value == '' ||
                      document.newenrollment.daydob.value   == '') {
                document.newenrollment.redir.value = 0;
                window.alert('The Date of Birth field is invalid');

            } else if (document.newenrollment.dob.value == '') {
                document.newenrollment.redir.value = 0;
                window.alert('Please enter a valid date of birth');
	    }
        }


        // No errors, and we already submitted once?
        if ( document.newenrollment.redir.value == 1 && prevent_double_submits == 0 ) {
            //alert("hey " + prevent_double_submits );
            prevent_double_submits = 1;
            document.newenrollment.submit();
            return true;
        }
        else{
            // Nope, error, or we already submitted once
            //alert("Nope");
            return false;
        }
    }
function buildDatedob() {

    // Get out if any fields are blank, date not fully entered yet
    if ( document.newenrollment.yeardob.value  == '' ||
         document.newenrollment.monthdob.value == '' ||
         document.newenrollment.daydob.value   == '' ){
        return;
    }

    // multiply by 1 to force to integer
    var longyear = document.newenrollment.yeardob.value * 1;
    // is this a leap year?
    var isleapyear = 0;
    isleapyear = (longyear % 4 == 0) && ((longyear % 100 != 0) || (longyear % 400 == 0));
    // check to see if day is valid for this month and year
    switch (document.newenrollment.monthdob.value) {
        case "04":
        case "06":
        case "09":
        case "11":
            if (document.newenrollment.daydob.value > 30) {
                // let the user know
                alert("Please enter a valid date");
                // set the day to the 30th (IE sets the pull down)
                document.newenrollment.daydob.value = "30";
            }
            break;
        case "02":
            // if this isn't leap year
            if (!isleapyear) {
                // only dates below 28 are ok
                if (document.newenrollment.daydob.value > 28)  {
                    // let the user know
                    alert("Please enter a valid date");
                    // set the day to the 27th (IE sets the pull down)
                    document.newenrollment.daydob.value = "28";
                }
            }
            // if this is leap year
            else {

                // the 29th is OK
                if (document.newenrollment.daydob.value > 29)  {
                    // let the user know
                    alert("Please enter a valid date");
                    // set the day to the 28th (IE sets the pull down)
                    document.newenrollment.daydob.value = "29";
                }
            }
            break;
    }
    // the new valid date
    return (document.newenrollment.monthdob.value + '/' + document.newenrollment.daydob.value + '/' + document.newenrollment.yeardob.value);
}


//-->
</script>
<script language="JavaScript" src="mm_menu.js"></script>
</head>
<body onload="MM_preloadImages('images/nav_home_on.gif','images/nav_about_on.gif','images/nav_faqs_on.gif','images/nav_contact_on.gif','images/nav_Products_on.gif','images/nav_espanol_on.gif','images/nav_enrollment_on.gif','images/nav_benefits_on.gif','images/nav_products_on.gif')">
 <table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
 <tr>
<td>
<table width="954" border="0" cellspacing="0" cellpadding="0">
<tr>
<!-- <td align="center" valign="top"><img src="images/ctl_con_logo4.png" width="954" height="324"/></td> -->
</tr>
<tr>
<td></td>
</tr>
<tr>
<td width="954" height="9" align="left" valign="top"><img src="images/topBumper.gif" width="954" height="9" /></td>
</tr>
<tr>
<td background="images/background.gif">
<table width="913" border="0" align="center" cellpadding="0" cellspacing="0">
<tr>
<td align="left" valign="top"><img src="images/Sub_titleTop.gif" width="913" height="16" /></td>
</tr>
<tr>
<td background="images/Subtitle_tile.gif">
<table width="900" border="0" cellspacing="1" cellpadding="1">
<tr>
<td width="10">&nbsp;</td>
<td align="left" valign="top" class="BlueTitles">NEW ENROLLMENT PAGE&nbsp;</td>
</tr>
</table>
</td>
</tr>
<tr>
<td align="left" valign="top"><img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
</tr>
<tr>
<td align="left" valign="middle" background="images/Sub_tile.gif">
<table width="900" border="0" cellspacing="1" cellpadding="1">
<tr>
<td width="10" align="left" valign="top">&nbsp;</td>
<td align="left" valign="top">
<table width="850" border="0" align="center" cellpadding="0" cellspacing="0">
<tr>
<td>&nbsp;<table align="center" border="0" cellpadding="1" cellspacing="1" width="775">
<tr>
<td align="left" valign="top">
<form name="newenrollment" action="welcome.cgi" method="post">
<input type='hidden' name='special' value='$special' >
<input type='hidden' name='specialselect' value='$specialselect' >

<table border="0" cellpadding="1" cellspacing="1" class="Enrollcopy" width="825">
<tr>
EOF
# <!-- will need to be changed if Aspen, any vendor etc  -->
if  ($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' and $special ne 'leasing' ) {
print<<"EOF";
<td width="327" align="right" valign="top" class="FAQuestions">Confirmation</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<input type="radio" name="confirm">I confirm that I am a $specialselect
			employee  working <br> for CenturyLink Communications and am enrolling in the <br>CenturyLink Partner Referral Program on a voluntary basis
</div>
</td>
</tr>
EOF
}
# ERS 304
if(($specialselect eq 'ER Solutions') and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">$specialselect Team Name</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="team_name">
<option value="">-- Select --</option>
<option value="First Party - Consumer Treatment (Atlanta)">First Party-Consumer Treatment (Atlanta)</option>
<option value="First Party- Collections Treatment (Renton)">First Party-Collections Treatment (Renton)</option>
<option value="Third Party -  Consumer Primary">Third Party-Consumer Primary</option>
<option value="Third Party Consumer Precollect">Third Party Consumer Precollect</option>
<option value="Third Party Consumer Renton Precollect">Third Party Consumer Renton Precollect</option>
<option value="Third Party-  Consumer Secondary">Third Party-Consumer Secondary</option>
<option value="Other">Other</option>
</select>
</div>
</td>
</tr>
EOF
}
# for West Mange 302
if(($specialselect eq 'West Manage') and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">$specialselect Team Name</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="team_name">
<option value="">-- Select --</option>
<option value="First Party- Collections Texarkana">First Party- Collections Texarkana</option>
<option value="OTHER NE-Omaha">OTHER NE-Omaha</option>
<option value="Third Party- Business Commerical (Omaha)">Third Party- Business Commerical (Omaha)</option>
<option value="Third Party- Cons./Bus. Precollect">Third Party- Cons./Bus. Precollect</option>
<option value="Third Party- Consumer Precollect">Third Party- Consumer Precollect</option>
<option value="Third Party- Consumer Primary">Third Party- Consumer Primary</option>
</select>
</div>
</td>
</tr>
EOF
}
# CCS 243
if(($specialselect eq 'CCS')  and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">$specialselect Team Name</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="team_name">
<option value="">-- Select --</option>
<option value="Third Party Primary">Third Party Primary</option>
<option value="Third Party- Cons. Bus Primary">Third Party- Cons. Bus Primary</option>
</select>
</div>
</td>
</tr>
EOF
}
# Allied 305
if(($specialselect eq 'Allied')  and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">$specialselect Team Name</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="team_name">
<option value="">-- Select --</option>
<option value="Other">Other</option>
<option value="Third Party-  Consumer Secondary">Third Party-  Consumer Secondary</option>
<option value="Third Party- Consumer Primary">Third Party- Consumer Primary</option>
</select>
</div>
</td>
</tr>
EOF
}
if(($specialselect eq 'EOS' || $specialselect eq 'EOS-CCA Tertiary')  and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">$specialselect Team Name</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="team_name">
<option value="">-- Select --</option>
<option value="EOS-Early Out">EOS-Early Out</option>
<option value="EOS-3rd Party Collections">EOS-3rd Party Collections</option>
</select>
</div>
</td>
</tr>
EOF
}
if(($specialselect eq 'Arizona Public Service')  and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">$specialselect Rep ID</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left"><input type="text" name="aps_rep_id" maxlength="10" class="FAQuestions" style="width: 100px">
</div>
</td>
</tr>
EOF
}
else {
	print<<"EOF";
<input type="hidden" name="aps_rep_id" maxlength="10" class="FAQuestions" value="">
EOF
}

if(($specialselect eq 'ER Solutions') and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">ER Solutions Work-City</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="work_city">
<option value="">-- Select --</option>
<option value="AZ-Phoenix">AZ-Phoenix</option>
<option value="GA-Atlanta">GA-Atlanta</option>
<option value="WA-Renton">WA-Renton</option>
<option value="WA-Renton">TX-Houston</option>
</select>
</div>
</td>
</tr>
EOF
}
if(($specialselect eq 'West Manage' ) and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">West Manage Work-City</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="work_city">
<option value="">-- Select --</option>
<option value="AR-Texarkana">AR-Texarkana</option>
<option value="NE-Omaha">NE-Omaha</option>
</select>
</div>
</td>
</tr>
EOF
}
if(($specialselect eq 'Dex' ) and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">DEX Work-City</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="work_city">
<option value="">-- Select --</option>
<option value="AZ-Phoenix">AZ-Phoenix</option>
<option value="AZ-Mesa">AZ-Mesa</option>
<option value="CO">CO</option>
<option value="MN">MN</option>
<option value="MT">MT</option>
<option value="NE">NE</option>
<option value="OR">OR</option>
<option value="UT">UT</option>
<option value="VT">VT</option>
<option value="WA">WA</option>
</select>
</div>
</td>
</tr>
EOF
}
if(($specialselect eq 'AFNI' ) and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">AFNI Work-City</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="work_city">
<option value="">-- Select --</option>
<option value="AZ-Phoenix">IL-Bloomington</option>
<option value="WA">MO-St.Charles</option>
</select>
</div>
</td>
</tr>
EOF
}
if(($specialselect eq 'Arizona Public Service')  and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">APS Work-City
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left"><select class="FAQuestions" name="work_city">
<option value="">-- Select --</option>
<option value="Deer Valley">Deer Valley</option>
<option value="502">502</option>
<option value="Business Office">Business Office</option>
<option value="Pivotal">Pivotal</option>
</select>
</div>
</td>
</tr>
EOF
}

if (( $specialselect eq 'Focus' )and
($special ne 'customer' and $special ne 'retiree' and $special ne 'pioneer-retain' )) {
print<<"EOF";
<tr>
<td width="327" align="right" valign="top" class="FAQuestions">Focus Team Name</td>
<td width="3">&nbsp;</td>
<td width="482" colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="team_name">
<option value="">-- Select --</option>
<option value="Tampa">Tampa</option>
<option value="Albuquerque">Albuquerque</option>
<option value="Other">Other</option>
</select>
</div>
</td>
</tr>
EOF
}

print<<"EOF";
<td align="left" class="FAQuestions" valign="top">
<div align="right">First Name:</div></td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left"><input name="first" type="text" class="FAQuestions" style="width: 100px" />*</div></td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Last Name:
</div>
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="last" type="text" class="FAQuestions" style="width: 100px" />*</div>
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Home Address:
</div>
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="addr1" type="text" class="FAQuestions" style="width: 230px" />*<br />
<input name="addr2" type="text" class="FAQuestions" style="width: 229px" /></div>
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">City: </div>
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="city" type="text" class="FAQuestions" style="width: 97px" />*</div>
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">State: </div> </td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="state">
          <option value='0'>Select  --</option>
EOF
my ($sql, %state);
$sql = "select distinct state, abbreviation from lp_states with (nolock)
where program_id = ?
order by state";
my $success = eval {
	my $sth = $myDB->prepare($sql) or die $myDB->errstr;
	$sth->{PrintError} = 0;
	$sth->execute(154) or die $sth->errstr;

    while ( my $state = $sth->fetchrow_hashref) {
        print "<option  value='$state->{abbreviation}' >$state->{state}";
    }
	$sth->finish();
};
unless($success) {
		DBInterface::writelog('graf07',"$thisfile", $@ );
}	
    print<<"EOF"; 
	</select> *</div> 
</td>
</tr>
<tr>
<td class="FAQuestions"><div align="right">Zip:</div></td>
<td>&nbsp;</td>
<td colspan="2"><div align="left"><input name="zip" type="text" class="FAQuestions" style="width: 57px" />*</div>
</td> </tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Home Phone:</div> </td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="phone1" type="text" class="FAQuestions" size="10" />*</div>     
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Mobile Phone: </div>   
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="phone2" type="text" class="FAQuestions" size="10" /></div>  
</td>
</tr>
EOF
if ($specialselect eq 'Allied') { 
print<<"EOF";
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Email: </div>   
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">  <div align="left">
<input name="email" value="Vanessa.Fargie\@iqor.com" type="text" size="30" class="FAQuestions" readonly/>*</div>  
EOF
}
elsif ($specialselect eq 'ER Solutions' || $specialselect eq 'Focus' 
	|| $specialselect eq 'CCS' || $specialselect eq 'Oxford' || $specialselect eq 'GCServ' || $specialselect eq 'Alliance One') { 
print<<"EOF";
<input  name="email" value="" type="hidden"  /></div>  
EOF
}
elsif ($specialselect eq 'West Manage') { 
print<<"EOF";
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Email: </div>   
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">  <div align="left">
<input name="email" value="akent\@west.com" type="text" size="30" class="FAQuestions" readonly/>*</div>  
EOF
}
else {
print<<"EOF";
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Email: </div>   
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">  <div align="left">
<input name="email" type="text" class="FAQuestions" size="30" />*</div>  
EOF
}

print<<"EOF";
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Last 4 Digits of Social Security Number<br />
(SSN) or Individual Taxpayer Identification Number (ITIN):   
</div>        
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="ssn4" type="text" class="FAQuestions" size="4" />*</div>  
</td>
</tr>       
<tr>
<td align="left" class="FAQuestions" valign="top">


<div align="right">Date of Birth (D.O.B.)     
</div>           
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<!-- dob insert start  -->
<input type="hidden" name="dob" value=""  maxlength="8">
<select class="FAQuestions" name="monthdob"  onClick="document.newenrollment.dob.value = buildDatedob();">
<OPTION VALUE="">--</option>
            <OPTION VALUE="01">January</option>
            <OPTION VALUE="02">February</option>
            <OPTION VALUE="03">March</option>
            <OPTION VALUE="04">April</option>
            <OPTION VALUE="05">May</option>
            <OPTION VALUE="06">June</option>
            <OPTION VALUE="07">July</option>
            <OPTION VALUE="08">August</option>
            <OPTION VALUE="09">September</option>
            <OPTION VALUE="10">October</option>
            <OPTION VALUE="11">November</option>
            <OPTION VALUE="12">December</option>
    </select>
<select class="FAQuestions" name="daydob" onClick="document.newenrollment.dob.value =  buildDatedob();">
<OPTION VALUE="">--</option>
            <OPTION VALUE="01">01</option>
            <OPTION VALUE="02">02</option>
            <OPTION VALUE="03">03</option>
            <OPTION VALUE="04">04</option>
            <OPTION VALUE="05">05</option>
            <OPTION VALUE="06">06</option>
            <OPTION VALUE="07">07</option>
            <OPTION VALUE="08">08</option>
            <OPTION VALUE="09">09</option>
            <OPTION VALUE="10">10</option>
            <OPTION VALUE="11">11</option>
            <OPTION VALUE="12">12</option>
            <OPTION VALUE="13">13</option>
            <OPTION VALUE="14">14</option>
            <OPTION VALUE="15">15</option>
            <OPTION VALUE="16">16</option>
            <OPTION VALUE="17">17</option>
            <OPTION VALUE="18">18</option>
            <OPTION VALUE="19">19</option>
            <OPTION VALUE="20">20</option>
            <OPTION VALUE="21">21</option>
            <OPTION VALUE="22">22</option>
            <OPTION VALUE="23">23</option>
            <OPTION VALUE="24">24</option>
            <OPTION VALUE="25">25</option>
            <option VALUE="26">26</option>
            <OPTION VALUE="27">27</option>
            <OPTION VALUE="28">28</option>
            <OPTION VALUE="29">29</option>
            <OPTION VALUE="30">30</option>
            <OPTION VALUE="31">31</option>
</select>
<select class="FAQuestions" name="yeardob" onClick="document.newenrollment.dob.value = buildDatedob();">
<OPTION VALUE="">--
            <OPTION VALUE="1913">1913</option>
            <OPTION VALUE="1914">1914</option>
            <OPTION VALUE="1915">1915</option>
            <OPTION VALUE="1916">1916</option>
            <OPTION VALUE="1917">1917</option>
            <OPTION VALUE="1918">1918</option>
            <OPTION VALUE="1919">1919</option>
            <OPTION VALUE="1920">1920</option>
            <OPTION VALUE="1921">1921</option>
            <OPTION VALUE="1922">1922</option>
            <OPTION VALUE="1923">1923</option>
            <OPTION VALUE="1924">1924</option>
            <OPTION VALUE="1925">1925</option>
            <OPTION VALUE="1926">1926</option>
            <OPTION VALUE="1927">1927</option>
            <OPTION VALUE="1928">1928</option>
            <OPTION VALUE="1929">1929</option>
            <OPTION VALUE="1930">1930</option>
            <OPTION VALUE="1931">1931</option>
            <OPTION VALUE="1932">1932</option>
            <OPTION VALUE="1933">1933</option>
            <OPTION VALUE="1934">1934</option>
            <OPTION VALUE="1935">1935</option>
            <OPTION VALUE="1936">1936</option>
            <OPTION VALUE="1937">1937</option>
            <OPTION VALUE="1938">1938</option>
            <OPTION VALUE="1939">1939</option>
            <OPTION VALUE="1940">1940</option>
            <OPTION VALUE="1941">1941</option>
            <OPTION VALUE="1942">1942</option>
            <OPTION VALUE="1943">1943</option>
            <OPTION VALUE="1944">1944</option>
            <OPTION VALUE="1945">1945</option>
            <OPTION VALUE="1946">1946</option>
            <OPTION VALUE="1947">1947</option>
            <OPTION VALUE="1948">1948</option>
            <OPTION VALUE="1949">1949</option>
            <OPTION VALUE="1950">1950</option>
            <OPTION VALUE="1951">1951</option>
            <OPTION VALUE="1952">1952</option>
            <OPTION VALUE="1953">1953</option>
            <OPTION VALUE="1954">1954</option>
            <OPTION VALUE="1955">1955</option>
            <OPTION VALUE="1956">1956</option>
            <OPTION VALUE="1957">1957</option>
            <OPTION VALUE="1958">1958</option>
            <OPTION VALUE="1959">1959</option>
            <OPTION VALUE="1960">1960</option>
            <OPTION VALUE="1961">1961</option>
            <OPTION VALUE="1962">1962</option>
            <OPTION VALUE="1963">1963</option>
            <OPTION VALUE="1964">1964</option>
            <OPTION VALUE="1965">1965</option>
            <OPTION VALUE="1966">1966</option>
            <OPTION VALUE="1967">1967</option>
            <OPTION VALUE="1968">1968</option>
            <OPTION VALUE="1969">1969</option>
            <OPTION VALUE="1970">1970</option>
            <OPTION VALUE="1971">1971</option>
            <OPTION VALUE="1972">1972</option>
            <OPTION VALUE="1973">1973</option>
            <OPTION VALUE="1974">1974</option>
            <OPTION VALUE="1975">1975</option>
            <OPTION VALUE="1976">1976</option>
            <OPTION VALUE="1977">1977</option>
            <OPTION VALUE="1978">1978</option>
            <OPTION VALUE="1979">1979</option>
            <OPTION VALUE="1980">1980</option>
            <OPTION VALUE="1981">1981</option>
            <OPTION VALUE="1982">1982</option>
            <OPTION VALUE="1983">1983</option>
            <OPTION VALUE="1984">1984</option>
            <OPTION VALUE="1985">1985</option>
            <OPTION VALUE="1986">1986</option>
            <OPTION VALUE="1987">1987</option>
            <OPTION VALUE="1988">1988</option>
            <OPTION VALUE="1989">1989</option>
            <OPTION VALUE="1990">1990</option>
            <OPTION VALUE="1991">1991</option>
            <OPTION VALUE="1992">1992</option>
            <OPTION VALUE="1993">1993</option>
            <OPTION VALUE="1994">1994</option>
            <OPTION VALUE="1995">1995</option>
            <OPTION VALUE="1996">1996</option>
            <OPTION VALUE="1997">1997</option>
            <OPTION VALUE="1998">1998</option>
            <OPTION VALUE="1999">1999</option>
            <OPTION VALUE="2000">2000</option>
            <OPTION VALUE="2001">2001</option>
            <OPTION VALUE="2002">2002</option>
            <OPTION VALUE="2003">2003</option>
            <OPTION VALUE="2004">2004</option>
            <OPTION VALUE="2005">2005</option>
</select>
*</div>  
</td>
</tr>
EOF
if ($special eq 'leasing') {
print<<"EOF";
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Property Name:</div> </td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="bus_name" type="text" class="FAQuestions" size="50" />*</div>     
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Property Address1:</div> </td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="bus_addr1" type="text" class="FAQuestions" size="50" />*</div>     
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Property Address2:</div> </td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="bus_addr2" type="text" class="FAQuestions" size="50" /></div>     
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right">Property City: </div>
</td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top">
<div align="left">
<input name="bus_city" type="text" class="FAQuestions" style="width: 97px" />*</div>
</td>
</tr>
<tr>
<td align="left" class="FAQuestions" valign="top">
<div align="right"> Property State: </div> </td>
<td>&nbsp;</td>
<td colspan="2" align="left" valign="top" class="LEQuiz">
<div align="left">
<select class="FAQuestions" name="bus_state">
          <option value='0'>Select  --</option>
EOF
    $sql = "select distinct state, abbreviation from lp_states with (nolock)
where program_id = 154
order by state";
	my $sth = $myDB->prepare($sql);
	$sth->execute();    
    while (my $state = $sth->fetchrow_hashref()) {
        
        print "<option  value='$state->{abbreviation}' >$state->{state}";
    }
    print<<"EOF"; 
	</select> *</div> 
</td>
</tr>
<tr>
<td class="FAQuestions"><div align="right">Property Zip:</div></td>
<td>&nbsp;</td>
<td colspan="2"><div align="left"><input name="bus_zip" type="text" class="FAQuestions" style="width: 57px" />*</div>
</td> </tr>
EOF

}
print<<"EOF";
<tr>
<td align="center" class="LEQuiz" colspan="4" valign="top">
			  <input type="hidden" name="redir" value="">
            <input type="button" name="go" value="REGISTER NOW" class="btnon"
            onMouseOver="this.className='btnoff';"
            onMouseOut="this.className='btnon';" onclick="checkform();"></td>
</tr>
<tr>
<td colspan="4" align="center">*Required fields</td>
</tr>
</table>
</form>
</td>
</tr>
</table>
</td>
</tr>
<tr>                  <td colspan="2" align="center">
                                                            </td>
                                                        </tr>
                                                  </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" valign="top">
                                        <img src="images/Sub_bottom.gif" width="913" height="16" /></td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
        <td><img src="images/bottombuffer.gif" width="954" height="15" /></td>
      </tr>
      <tr>
        <td width="904" height="66" align="center" valign="middle" background="images/bottom_amex.gif"><table width="500" border="0" align="center" cellpadding="0" cellspacing="0">
EOF
require "graf07/footer.cgi";
print<<"EOF";
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>


EOF


