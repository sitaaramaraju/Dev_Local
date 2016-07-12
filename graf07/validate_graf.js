// 4/25/2016
//qwest/graf/validate_graf.js
/*--------------------------------------------------------------------------------------------------------------------------*/
/* common */

function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}
//-------------------------------------------------------------------------------
function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}
//-------------------------------------------------------------------------------
function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}
//-------------------------------------------------------------------------------
function MM_swapImage() { //v3.0
  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}
//-------------------------------------------------------------------------------
function MM_openBrWindow(theURL,winName,features) { //v2.0
  window.open(theURL,winName,features);
}
//-------------------------------------------------------------------------------
function MM_goToURL() { //v3.0
  var i, args=MM_goToURL.arguments; document.MM_returnValue = false;
  for (i=0; i<(args.length-1); i+=2) eval(args[i]+".location='"+args[i+1]+"'");
}
/*--------------------------------------------------------------------------------------------------------------------------*/
/* common for enroll */
//-------------------------------------------------------------------------------
function buildDatedob() {

    // Get out if any fields are blank, date not fully entered yet
    if ( document.regi.yeardob.value  == '' ||
         document.regi.monthdob.value == '' ||
         document.regi.daydob.value   == '' ){
        return;
    }

    // multiply by 1 to force to integer
    var longyear = document.regi.yeardob.value * 1;

    // is this a leap year?
    var isleapyear = 0;
    isleapyear = (longyear % 4 == 0) && ((longyear % 100 != 0) || (longyear % 400 == 0));

    // check to see if day is valid for this month and year
    switch (document.regi.monthdob.value) {
        case "04":
        case "06":
        case "09":
        case "11":

            if (document.regi.daydob.value > 30) {

                // let the user know
                alert("Please enter a valid date");

                // set the day to the 30th (IE sets the pull down)
                document.regi.daydob.value = "30";

            }
            break;

        case "02":
            // if this isn't leap year
            if (!isleapyear) {

                // only dates below 28 are ok
                if (document.regi.daydob.value > 28)  {

                    // let the user know
                    alert("Please enter a valid date");

                    // set the day to the 27th (IE sets the pull down)
                    document.regi.daydob.value = "28";
                }
            }

            // if this is leap year
            else {

                // the 29th is OK
                if (document.regi.daydob.value > 29)  {

                    // let the user know
                    alert("Please enter a valid date");

                    // set the day to the 28th (IE sets the pull down)
                    document.regi.daydob.value = "29";
                }
            }
            break;
    }
    // the new valid date
    return (document.regi.monthdob.value + '/' + document.regi.daydob.value + '/' + document.regi.yeardob.value);
}
//-------------------------------------------------------------------------------
var isNN = (navigator.appName.indexOf("Netscape")!=-1);

function autoTab(input,len, e) {
  var keyCode = (isNN) ? e.which : e.keyCode;
  var filter = (isNN) ? [0,8,9] : [0,8,9,16,17,18,37,38,39,40,46];
  if(input.value.length >= len && !containsElement(filter,keyCode)) {
    input.value = input.value.slice(0, len);
    input.form[(getIndex(input)+1) % input.form.length].focus();
  }

  function containsElement(arr, ele) {
    var found = false, index = 0;
    while(!found && index < arr.length)
    if(arr[index] == ele)
    found = true;
    else
    index++;
    return found;
  }

  function getIndex(input) {
    var index = -1, i = 0, found = false;
    while (i < input.form.length && index == -1)
    if (input.form[i] == input)index = i;
    else i++;
    return index;
  }
  return true;
}

//-------------------------------------------------------------------------------
/*
function clean_phone( field ) {
        // We are looking for exactly 10 digits in the mess
        var val = ''; // string of digits
		var pl = -1;
		if (field == 'undefined' || !field )
		{
			pl = 0;
		}
		else {
			field.length;
		}
		if (pl > 0)
		{
			for( ii=0; ii < pl; ii++){
				var ch = field.charAt(ii);
				if (ch >= "0" && ch <= "9" ){
                val = val + ch;
            }
        }
		}
        if (val.length != 10 || pl > 0 ){
            val = ''; // invalid
        }
        //alert('phone is '+ val);
        return val;
    }
*/
//-------------------------------------------------------------------------------
// to validate email
function verifyEmail(inemail){
var status = 1;     
var emailRegEx = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
     if (inemail.search(emailRegEx) == -1) {
         status = 0;     
     }
     return status;
} 
//-------------------------------------------------------------------------------
/* enroll.cgi */

    function checkform_bau() {
        document.regi.redir.value = 1;
        // Check the phone1, it will be the password
        var myphone1 =  document.regi.phone1 + document.regi.phone2 + document.regi.phone3 ; // was using clean phone
		var validEmail = verifyEmail(document.regi.email.value);
        if ( document.regi.osr_id.value == "") {
            document.regi.redir.value = 0;
            window.alert('Please enter the Rep ID.');
        }
        else if ( document.regi.first.value == "" || document.regi.last.value == "" ) {
            document.regi.redir.value = 0;
            window.alert('Please enter your first and last name.');
        }else if (document.regi.addr1.value == "" || document.regi.city.value == "" || document.regi.state.value == "" || document.regi.zip.value == "") {
            document.regi.redir.value = 0;
            window.alert('Please enter your full address.');
        }
		else if( myphone1 == "") {
            document.regi.redir.value = 0;
            window.alert('Invalid Home Phone number.\\n Because your phone number will be your password,\\n it must include your area code, and have exactly 10 digits');
        }else if( (document.regi.ssn4.value == "" ) || (isNaN(document.regi.ssn4.value) )) {
	        document.regi.redir.value = 0;
	        window.alert('Please enter the Last Four Digits of your Social Security Number or Individual Taxpayer Identification Number');
        }else if( document.regi.yeardob.value  == '' ||
                  document.regi.monthdob.value == '' ||
                  document.regi.daydob.value   == '') {
            document.regi.redir.value = 0;
            window.alert('The Date of Birth field is invalid');
        }else if( document.regi.property_name.value == "") {
            document.regi.redir.value = 0;
            window.alert('Please enter a Property Name');
        }else if( document.regi.bus_name.value == "") {
            document.regi.redir.value = 0;
            window.alert('Please enter a Employer Name');
		}else if( (document.regi.bus_addr1.value == "") || (document.regi.bus_city.value == "")||
			(document.regi.bus_state.value == "") || (document.regi.bus_zip.value == "") ) {
            document.regi.redir.value = 0;
            window.alert('Please enter full Business Address.');
		}else if( validEmail == 0) {
            document.regi.redir.value = 0;
            window.alert('Please provide valid email.');
		} else if( !document.regi.yes_mdu[0].checked  && !document.regi.yes_mdu[1].checked) {
            document.regi.redir.value = 0;
            window.alert('Please indicate if you are employee of MDU.');
		}

        // No errors, and we already submitted once?
        if ( document.regi.redir.value == 1  ) {
            //alert("hey " + prevent_double_submits );
            document.regi.submit();
            return true;
        }
        else{
            // Nope, error, or we already submitted once
            //alert("Nope");
            return false;
        }
    }

//-------------------------------------------------------------------------------
/* quickform.cgi */
function checkContactform () {
        document.regi.redir.value = 1;
		var validEmail = verifyEmail(document.regi.email.value);
		var issueNum = 0;

		for (var d=0; d < document.regi.issue.length; d++){
			if (document.regi.issue[d].checked ){
						issueNum =  issueNum + 1;
					}
		}

		 if ( document.regi.part_name.value == ""){
            document.regi.redir.value = 0;
            window.alert('Please provide your name.');
		}else if ( document.regi.part_name.value == ""){
            document.regi.redir.value = 0;
            window.alert('Please provide your name.');
		}else if (validEmail == 0 )
		{
            document.regi.redir.value = 0;
            window.alert('Please provide valid email.');
		} else if (issueNum ==0 ) {
            document.regi.redir.value = 0;
            window.alert('Please select issue.');
		}

        if ( document.regi.redir.value == 1  ) {
            //alert("hey " + prevent_double_submits );
            document.regi.submit();
            return true;
        }
        else{
            // Nope, error, or we already submitted once
            //alert("Nope");
            return false;
        }

}
//-------------------------------------------------------------------------------
// newenroll_b2c.cgi
function checkform_b2c() {
        document.regi_b2c.redir.value = 1;
        // Check the phone1, it will be the password

		//var myphone1 = clean_phone( document.regi_b2c.phone1 + document.regi_b2c.phone2 + document.regi_b2c.phone3) ;
		var validEmail = verifyEmail(document.regi_b2c.email.value);

var team_name = '';
var team_sp = ''
for ( var i=0; i<regi_b2c.length; i++) {
	if (regi_b2c[i].checked) {
		bus_type = regi_b2c[i].value ;
		break;
	}
}


        if ( document.regi_b2c.osr_id.value == "") {
            document.regi_b2c.redir.value = 0;
            window.alert('Please enter the Rep ID.');
			document.regi_b2c.osr_id.focus();
        }
		else if ( document.regi_b2c.bus_name.value == "" ) {
            document.regi_b2c.redir.value = 0;
            window.alert('Please enter your Business name.');
			document.regi_b2c.bus_name.focus();
        }else if( (document.regi_b2c.bus_addr1.value == "") || (document.regi_b2c.bus_city.value == "")||
			(document.regi_b2c.bus_state.value == "") || (document.regi_b2c.bus_zip.value == "") ) {
            document.regi_b2c.redir.value = 0;
            window.alert('Please enter full Business Address.');
			document.regi_b2c.bus_state.focus();
		}else if( (isNaN(document.regi_b2c.bus_prim_phone1.value) ) ||(isNaN(document.regi_b2c.bus_prim_phone2.value) ) || (isNaN(document.regi_b2c.bus_prim_phone3.value) )) {
            document.regi_b2c.redir.value = 0;
            window.alert('Invalid Primary Phone number.\\n Because your phone number will be your password,\\n it must include your area code, and have exactly 10 digits');
        			document.regi_b2c.bus_prim_phone1.focus();
		}else if ( document.regi_b2c.first.value == "" || document.regi_b2c.last.value == "" ) {
            document.regi_b2c.redir.value = 0;
            window.alert('Please enter your first and last name.');
			document.regi_b2c.first.focus();
        }else if( (isNaN(document.regi_b2c.contact_phone1.value) ) ||(isNaN(document.regi_b2c.contact_phone2.value) ) || (isNaN(document.regi_b2c.contact_phone3.value) )) {
            document.regi_b2c.redir.value = 0;
            window.alert('Invalid contact Phone number.');
        	document.regi_b2c.contact_phone1.focus();
        }else if( document.regi_b2c.industry.value == "") {
            document.regi_b2c.redir.value = 0;
            window.alert('Please select the industry which most closely describes your current employer.');
            document.regi_b2c.industry.focus();
        }else if( document.regi_b2c.bus_name_w9.value == "") {
            document.regi_b2c.redir.value = 0;
            window.alert('Please enter Business Name as shown On your Income Tax return');
        	document.regi_b2c.bus_name_w9.focus();
        }else if( ((isNaN(document.regi_b2c.ssn1.value) ) ||(isNaN(document.regi_b2c.ssn2.value) ) || (isNaN(document.regi_b2c.ssn3.value) ))
			&& ((isNaN(document.regi_b2c.ein1.value) ) || (isNaN(document.regi_b2c.ein2.value) )) ){
            document.regi_b2c.redir.value = 0;
            window.alert('Please enter valid Social Security number or Employer Identification Number');
			        	document.regi_b2c.ssn1.focus();

        }else if( validEmail == 0) {
            document.regi.redir.value = 0;
            window.alert('Please provide valid email.');
		}



        // No errors, and we already submitted once?
        if ( document.regi_b2c.redir.value == 1   ) {
            //alert("hey " + prevent_double_submits );
            document.regi_b2c.submit();
            return true;
        }
        else{
            // Nope, error, or we already submitted once
            //alert("Nope");
            return false;
        }
    }
