// 4/25/2016
//qwest/centurylinkconnect07/validate.js
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
			document.getElementById('req_osr').innerHTML='<font color=red>*OSR ID Required </font>';
			document.contact.osr_id.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_osr').innerHTML='';
		}

		if ( document.regi.first.value.trim() == "" || document.regi.last.value.trim() == "" ) { 
			document.getElementById('req_name').innerHTML='<font color=red>*First and Last Name are required.</font>';
			document.contact.first.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_name').innerHTML='';
		}
		
		if (document.regi.addr1.value == "" || document.regi.city.value == "" || document.regi.state.value == "" || document.regi.zip.value == "") {
     		document.getElementById('req_addr').innerHTML='<font color=red>*Complete address required.</font>';
			document.contact.addr1.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_addr').innerHTML='';
		}

		if( myphone1 == "") {
     		document.getElementById('req_p1').innerHTML='<font color=red>*Your Phone number could be your password, enter valid phone number.</font>';
			document.contact.phone1.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_p1').innerHTML='';
		}
		if (document.regi.email.value == "")
		{
			document.getElementById('req_email').innerHTML='<font color=red>*Email is required.</font>';
			document.contact.email.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_email').innerHTML='';
		}


		if( (document.regi.ssn4.value == "" ) || (isNaN(document.regi.ssn4.value) )) { 
			document.getElementById('req_last4').innerHTML='<font color=red>*Last 4 SSN required.</font>';
			document.contact.ssn4.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_last4').innerHTML='';
		}
		
		if( document.regi.yeardob.value  == '' || document.regi.monthdob.value == '' || document.regi.daydob.value   == '') {
			document.getElementById('req_dob').innerHTML='<font color=red>*Date of Birth required</font>';
			document.contact.yeardob.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_dob').innerHTML='';
		}
		if( document.regi.property_name.value == "") {
            document.getElementById('req_propname').innerHTML='<font color=red>*Property Name required</font>';
			document.contact.property_name.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_propname').innerHTML='';
		} 

		if( document.regi.bus_name.value == "") {
            document.getElementById('req_bossname').innerHTML='<font color=red>*Employer Name required</font>';
			document.contact.bus_name.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_bossname').innerHTML='';
		} 
			
		if( (document.regi.bus_addr1.value == "") || (document.regi.bus_city.value == "")||
			(document.regi.bus_state.value == "") || (document.regi.bus_zip.value == "") ) {
            document.getElementById('req_bizaddr').innerHTML='<font color=red>*Business Address required</font>';
			document.contact.bus_addr1.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_bizaddr').innerHTML='';
		} 
		
		if( !document.regi.yes_mdu[0].checked  && !document.regi.yes_mdu[1].checked) { 
            document.getElementById('req_mdu').innerHTML='<font color=red>*Please indicate if you are employee of MDU.</font>';
			document.contact.bus_phone.focus();
            document.contact.redir.value = 0;
        }
		else {
			document.getElementById('req_mdu').innerHTML='';
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

        document.contact.redir.value = 1;
		 
		var validEmail = verifyEmail(document.contact.email.value);
		var issueNum = 0;

		for (var d=0; d < document.contact.issue.length; d++){
			if (document.contact.issue[d].checked ){
						issueNum =  issueNum + 1;
					}
		}

		if ( document.contact.part_name.value == ""){
					document.getElementById('req_name').innerHTML='<font color=red>*Name Required </font>';
					document.contact.part_name.focus();
                    document.contact.redir.value = 0;
        }
		else {
					document.getElementById('req_name').innerHTML='';
		}
		
		if (validEmail == 0 ){
					document.getElementById('req_email').innerHTML='<font color=red>*Valid Email Required </font>';
					document.contact.email.focus();
                    document.contact.redir.value = 0;
        }
		else {
					document.getElementById('req_email').innerHTML='';
		}
		
		if (issueNum ==0 ) {
					document.getElementById('req_helpTopic').innerHTML='<font color=red>*Help Topic Required </font>';
                    document.contact.redir.value = 0;
        }
		else {
					document.getElementById('req_helpTopic').innerHTML='';
		}

        if ( document.contact.redir.value == 1  ) {
            //alert("hey " + prevent_double_submits );
            document.contact.submit();
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
					document.getElementById('req_osr').innerHTML='<font color=red><--OSR Required </font>';
					document.regi_b2c.osr_id.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_osr').innerHTML='';
		}
		 if ( document.regi_b2c.bus_name.value == "" ) { 
					document.getElementById('req_bus_name').innerHTML='<font color=red><--Business Name Required </font>';
					document.regi_b2c.bus_name.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_bus_name').innerHTML='';
		}
		if( (document.regi_b2c.bus_addr1.value == "") || (document.regi_b2c.bus_city.value == "")||
			(document.regi_b2c.bus_state.value == "") || (document.regi_b2c.bus_zip.value == "") ) { 
					document.getElementById('req_bus_addr').innerHTML='<font color=red><--Complete address Required </font>';
					document.regi_b2c.bus_addr1.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_bus_addr').innerHTML='';
		}
		if( (isNaN(document.regi_b2c.bus_prim_phone1.value) ) ||(isNaN(document.regi_b2c.bus_prim_phone2.value) ) || (isNaN(document.regi_b2c.bus_prim_phone3.value) )) {
					document.getElementById('req_p1').innerHTML='<font color=red><--Primary Business Phone Required </font>';
					document.regi_b2c.bus_prim_phone1.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_p1').innerHTML='';
		}
		if ( document.regi_b2c.first.value == "" || document.regi_b2c.last.value == "" ) {
					document.getElementById('req_cont_name').innerHTML='<font color=red><--First and Last Name for Contact Required </font>';
					document.regi_b2c.first.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_cont_name').innerHTML='';
		}
		if( (isNaN(document.regi_b2c.contact_phone1.value) ) ||(isNaN(document.regi_b2c.contact_phone2.value) ) || (isNaN(document.regi_b2c.contact_phone3.value) )) {
					document.getElementById('req_contact_phone').innerHTML='<font color=red><--Valid Phone number for Contact Required </font>';
					document.regi_b2c.contact_phone1.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_contact_phone').innerHTML='';
		}
		if( document.regi_b2c.industry.value == "") { 
					document.getElementById('req_indus').innerHTML='<font color=red><--Industry Required </font>';
					document.regi_b2c.industry.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_indus').innerHTML='';
		}
		if( document.regi_b2c.bus_name_w9.value == "") {
					document.getElementById('req_w9name').innerHTML='<font color=red><--Business Name as on Income Tax return Required </font>';
					document.regi_b2c.industry.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_w9name').innerHTML='';
		}
		if( ((isNaN(document.regi_b2c.ssn1.value) ) ||(isNaN(document.regi_b2c.ssn2.value) ) || (isNaN(document.regi_b2c.ssn3.value) ))
			&& ((isNaN(document.regi_b2c.ein1.value) ) || (isNaN(document.regi_b2c.ein2.value) )) ){ 
					document.getElementById('req_ssn').innerHTML='<font color=red><--Valid SSN OR EIN Required </font>';
					document.regi_b2c.ssn1.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_ssn').innerHTML='';
		}
		if( validEmail == 0) { 
					document.getElementById('req_email').innerHTML='<font color=red><--Valid Email Required </font>';
					document.regi_b2c.email.focus();
                    document.regi_b2c.redir.value = 0;
        }
		else {
					document.getElementById('req_email').innerHTML='';
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
 /*---------------------------------------*/
    function toggleMsg(item){

	if (document.getElementById(item).style.display=='none'){
        document.getElementById(item).style.display='';
   }
    else{
         document.getElementById(item).style.display='none';
		
    }
    }
 /*---------------------------------------*/
function OnSubmitForm() {
var team_name = '';
var team_sp = ''
//window.alert("here");

for ( var i=0; i<myform.length; i++) {
	if (myform[i].checked) {
		team_name = myform[i].value ;
//		window.alert("here2");

		break;
	}
}

if (team_name==''){
window.alert("Please select");

}
else {
document.myform.action ="newenroll.cgi";
//		window.alert("enroll b2c");
		myform.submit();
}

}
/*-------------------------------------------*/
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
/*-------------------------------------------*/
    function isNumeric(e) {
		return !String.fromCharCode(window.event ? e.keyCode : e.which).search(/\\d/);
	}
/*-------------------------------------------*/
    function trim_spaces(str) {
    return str.replace(/^\\s*|\\s*\$/g,"");
    }

/*-------------------------------------------*/
function showHide2() {     
    if (document.getElementById('crisChk').checked) {      
        document.getElementById('banDiv').style.display = 'none';
    } 
    else if(document.getElementById('ensChk').checked) {    
        document.getElementById('banDiv').style.display = 'block';
   }
}
/*-------------------------------------------*/
function openModalLarge(src) {
        $.modal('<iframe src="' + src + '" height="650" width="1000" style="border:0">');
                $.modal({
                        autoResize: true
                });
 }
/*-------------------------------------------*/
    function checkLeadform() {
        document.lead_lmsii.redir.value = 1;

        var cust_phone1 = clean_phone( document.lead_lmsii.phone1 );
        var cust_phone2 = clean_phone( document.lead_lmsii.phone2 );
		var leg = 0;

	var cust_name2 = trim_spaces(document.lead_lmsii.cust_name.value);

		if (document.lead_lmsii.legacy[0].checked == true  )
			{
				leg = 1;
			}
		else if (document.lead_lmsii.legacy[1].checked == true)
			{
				leg = 2;
			}

			


           if (!document.lead_lmsii.prod_int[0].checked
               && !document.lead_lmsii.prod_int[1].checked
	       && !document.lead_lmsii.prod_int[2].checked
	       && !document.lead_lmsii.prod_int[3].checked
	       && !document.lead_lmsii.prod_int[4].checked) {
					document.getElementById('req_prod').innerHTML='<font color=red>At least one product is required </font>';
					document.lead_lmsii.cust_name.focus();
                    document.lead_lmsii.redir.value = 0;
        }
		else {
					document.getElementById('req_prod').innerHTML='';
		}
		if (cust_name2 == "" ) { 
					document.getElementById('req_name').innerHTML='<font color=red>Name is required </font>';
					document.lead_lmsii.cust_name.focus();
                    document.lead_lmsii.redir.value = 0;
        }
		else {
					document.getElementById('req_name').innerHTML='';
		}
		if (document.lead_lmsii.lead_state.value == "" ) { 
					document.getElementById('req_st').innerHTML='<font color=red>Lead State required </font>';
					document.lead_lmsii.lead_state.focus();
                    document.lead_lmsii.redir.value = 0;
        }
		else {
					document.getElementById('req_st').innerHTML='';
		}
		if (document.lead_lmsii.prop_name.value == "" ) { 
					document.getElementById('req_prop').innerHTML='<font color=red>Property Name required </font>';
					document.lead_lmsii.lead_state.focus();
                    document.lead_lmsii.redir.value = 0;
        }
		else {
					document.getElementById('req_prop').innerHTML='';
		}
		if( cust_phone1 == "") { 
					document.getElementById('req_ph1').innerHTML='<font color=red>Phone Number required </font>';
					document.lead_lmsii.lead_state.focus();
                    document.lead_lmsii.redir.value = 0;
        }
		else {
					document.getElementById('req_ph1').innerHTML='';
		}
		if (document.lead_lmsii.time_to_call.value == "") { 
           			document.getElementById('req_ttc').innerHTML='<font color=red>Time to call required </font>';
					document.lead_lmsii.lead_state.focus();
                    document.lead_lmsii.redir.value = 0;
        }
		else {
					document.getElementById('req_ttc').innerHTML='';
		}
		if (leg == 2) {
				if (document.lead_lmsii.ban.value == "") { 
           			document.getElementById('req_ban').innerHTML='<font color=red>BAN Number required </font>';
					document.lead_lmsii.lead_state.focus();
                    document.lead_lmsii.redir.value = 0;
				}
				else {
					document.getElementById('req_ban').innerHTML='';
				}
		}

        // No errors, and we already submitted once?
        if ( document.lead_lmsii.redir.value == 1  ) {
            //alert("hey " + prevent_double_submits );
			document.lead_lmsii.action = "lmsii_submitreferral.cgi";
			//document.lead_lmsii.action = "lmsii_lead_thnx.cgi";
            document.lead_lmsii.submit();
            return true;
        }
        else{
            // Nope, error, or we already submitted once
            //alert("Nope");
            return false;
        }
    }

//#######################################//	
/* checkform called from graf_mypref.cgi */
//#######################################//		
var prevent_double_submits = 0;
    function checkform() {
        document.my_pref.redir.value = 1;

        if(document.my_pref.redir.value == 1){
           if (!document.my_pref.paper[0].checked && !document.my_pref.paper[1].checked ) {
                document.my_pref.redir.value = 0;
                window.alert('Please select the appropriate choice for receiving VISA Statements.');
		   } 
		   else if (!document.my_pref.offers[0].checked && !document.my_pref.offers[1].checked ) {
                document.my_pref.redir.value = 0;
                window.alert('Please select the appropriate choice for receiving E-mail Offers.');
            }
	
        }
                if ( document.my_pref.redir.value == 0 ) {
                    return false;
                }
                else  {
                    document.my_pref.submit();
                    return true;
                }

        // No errors, and we already submitted once?
    }	

/*------------------------------------------- "Are you sure you want to logout?"*/

function logoutUser( session_id, staff_id) {
		var answer = confirm("Are you sure you want to logout?")
		if (answer){ 
			 $.ajax({
				url: "graf_subs.cgi",
				data: "logout=1&staff_id="+staff_id+"&session_id="+session_id,
				cache: false,
				success: function(data){
						window.location="../index_raf.cgi";},
				error: function() {alert('Connection Issue.  Please Try Again.');}
				});
		}else{
			return false;
		}
	 }



