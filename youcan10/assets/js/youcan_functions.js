// 11/30/2012
//centurylink/youcan10/assets/js/youcan_functions.js
/*---------------------------------------*/
function catchEnter(e) {
if (!e) var e = window.event;
if (e.keyCode) code = e.keyCode;
else if (e.which) code = e.which;

var cuid = document.logon.userid.value ;
var pwd = document.logon.password.value ;
var wrn;
var valident = 0;
if (cuid.length==0 || pwd.length==0)
{
	valident = 0;
}
else {
valident = 1;
}
if (code==13 && valident==1) {
document.logon.submit();
//submit the form, do your validation, or whatever
}
}
/*---------------------------------------*/
function checkform() {
document.logon.redir.value = 1;
//	window.alert('what');
//	window.alert(document.logon.userid.value);
//	window.alert(document.logon.password.value);


	if ( document.logon.userid.value == ""  || document.logon.password.value == "")
	{
//		window.alert('what2');

		document.getElementById('reqd_login').innerHTML='<font color=red>*Logon and Password Required </font>';
		document.logon.redir.value = 0;
	}
	else {
		document.getElementById('reqd_login').innerHTML='';
	}
	
	if (	document.logon.redir.value == 1)
	{
		        //   document.logon.action="/cgi-bin/lp-validate.cgi";
                    document.logon.submit();
                    return true;
	}
	else {
                    return false;
	}
}
/*---------------------------------------*/
/* added for CL-864		5/29/2014 */
function checkPwdForm() {
document.frm.redir.value = 1;
var pwd1 = document.frm.password1.value;
var pwd2 = document.frm.password2.value;

pwd1 = pwd1.toString();
pwd2 = pwd2.toString();
var plen = pwd1.length;

	//	window.alert('inPwd');
	if (pwd1 == "" || pwd2 == ""  )
	{
		document.getElementById('reqd_new_pwds').innerHTML='<font color=red>*Password Required </font>';
		document.frm.redir.value = 0;
	}
	else {
		document.getElementById('reqd_new_pwds').innerHTML='';
	}
	if (pwd1 != pwd2 )
	{
		document.getElementById('reqd_new_pwds2').innerHTML='<font color=red>*Passwords do not match.</font>';
		document.frm.redir.value = 0;
	}
	else {
		document.getElementById('reqd_new_pwds2').innerHTML='';
	}
	if (plen < 5)
	{
		document.getElementById('reqd_new_pwds3').innerHTML='<font color=red>*Password should be minimum 5 characters in length.</font>';
		document.frm.redir.value = 0;
	}
	else {
		document.getElementById('reqd_new_pwds3').innerHTML='';
	}
	if (	document.frm.redir.value == 1)
	{
		        //   document.logon.action="/cgi-bin/lp-validate.cgi";
                    document.frm.submit();
                    return true;
	}
	else {
                    return false;
	}

}
/*---------------------------------------*/
/* added for CL-864		5/29/2014 */
function checkEmailForm() {
document.frm.redir.value = 2;
	//	window.alert('inEmail');
	if (document.frm.new_email.value == "" )
	{
		document.getElementById('reqd_new_email').innerHTML='<font color=red>*Email Required </font>';
		document.frm.redir.value = 0;
	}
	else {
		document.getElementById('reqd_new_email').innerHTML='';
	}
	if (	document.frm.redir.value == 2)
	{
		        //   document.logon.action="/cgi-bin/lp-validate.cgi";
                    document.frm.submit();
                    return true;
	}
	else {
                    return false;
	}
}
/*---------------------------------------*/
function onPageLoaded() {
	document.getElementById('password').style.display = "none";
	document.getElementById('pwdPlain').style.display = "inline";
	document.getElementById('userid').style.display = "none";
	document.getElementById('logid').style.display = "inline";
}
/*---------------------------------------*/
function swapPasswordBoxes(funcType) {
	if(funcType == "click") {	
		document.getElementById('pwdPlain').style.display = "none";
		document.getElementById('password').style.display = "inline";
		document.getElementById('password').focus();
	} else {
		if(document.getElementById('password').value.length == 0) {
			document.getElementById('pwdPlain').style.display = "inline";
			document.getElementById('password').style.display = "none";
		}
	}
}
/*---------------------------------------*/
function swapLoginBoxes(funcType) {
	if(funcType == "click") {	
		document.getElementById('logid').style.display = "none";
		document.getElementById('userid').style.display = "inline";
		document.getElementById('userid').focus();
	} else {
		if(document.getElementById('userid').value.length == 0) {
			document.getElementById('logid').style.display = "inline";
			document.getElementById('userid').style.display = "none";
		}
	}
}

/*--------------ABOVE AE FUNCTIONS FOR LOGIN PAGE-------------------------*/

function updateprods(objectname, prod_id){
        if ( objectname.checked == true ) {
            document.frm.prodvalidate.value = (document.frm.prodvalidate.value)*1 + 1;
        }else {
            document.frm.prodvalidate.value = (document.frm.prodvalidate.value)*1 - 1;
        }
    }
/*---------------------------------------*/
 function enablefields() {
        document.frm.lead_name.disabled = false;
        document.frm.main_btn1.disabled = false;
        document.frm.main_btn2.disabled = false;
        document.frm.main_btn3.disabled = false;
        document.frm.lead_phone1.disabled = false;
        document.frm.lead_phone2.disabled = false;
        document.frm.lead_phone3.disabled = false;
    }
/*---------------------------------------*/
 function disablefields() {
        document.frm.lead_name.disabled = true;
        document.frm.main_btn1.disabled = true;
        document.frm.main_btn2.disabled = true;
        document.frm.main_btn3.disabled = true;
        document.frm.lead_phone1.disabled = true;
        document.frm.lead_phone2.disabled = true;
        document.frm.lead_phone3.disabled = true;
    }

/*---------------------------------------*/
function showTopic (custType, session) {
	

		if (custType < 1){
			$("#themediv").html('');
			$("#themediv").html('<span class="font1">Must Select Referral type</span>');
			return false;
		}
		 $.ajax({
			//url: "D:/centurylinkyoucan/youcan10/youcan_subs.cgi",
			url: "youcan_subs.cgi",
			data: "getform=1&lead_group="+custType+"&session_id="+session,
			cache: false,
			success: function(html){
					if (html) {
						$("#themediv").html('');
						$("#themediv").append(html);
						$("#themediv").show();

					}else{
						alert('Select Referral Type');
					}
				},
				error: function() {alert('Connection Issue.  Please Try Again.');}
				});
}

/*---------------------------------------*/

function checkLegacy (val, session ) {

		if (val == ""){
			$("#showLegacyRadio").html('');
			$("#showLegacyRadio").html('<span class="font1">Must Select State</span>');
			return false;
		}
		 $.ajax({
			url: "youcan_subs.cgi",
			data: "getLegacy=1&val="+val+"&session_id="+session,
			cache: false,
			success: function(html){
					if (html) {
						$("#showLegacyRadio").html('');
						$("#showLegacyRadio").append(html);
						$("#showLegacyRadio").show();

					}else{
						alert('Select State');
					}
				},
				error: function() {alert('Connection Issue. Please Try Again.');}
				});
}
 /*---------------------------------------*/
  
	function checkformRes(){
	
	
    document.lead.redir.value = 1;
			var prevent_double_submits = 0;
			var prod = "";
			var leg = 0;
				
				



				for (var d=0; d < document.lead.product.length; d++){
					if (document.lead.product[d].checked ){
						prod =  prod + document.lead.product[d].value;
					}
				}

				
                 if ( document.lead.lead_name.value == "" ) {
					document.getElementById('req_leadname').innerHTML='<font color=red>*Name Required </font>';
					document.lead.lead_name.focus();
                    document.lead.redir.value = 0;
                }
				else {
					document.getElementById('req_leadname').innerHTML='';
				}
				if (document.lead.lead_state.value == "")
				{
					document.getElementById('req_state').innerHTML='<font color=red>*State Required </font>';
                    document.lead.redir.value = 0;
				}
				else {
					document.getElementById('req_state').innerHTML='';
				}
				
				if (document.lead.ctl_radio.value == 0)
				{ 
					leg = document.lead.ctl_legacy.value;
				}
				else if (document.lead.ctl_radio.value == 1)
				{
					if (document.lead.ctl_legacy_radio[0].checked == true  )
					{
						leg = 1;
					}
					else if (document.lead.ctl_legacy_radio[1].checked == true)
					{
						leg = 2;
					}
				}
				
				if (leg == 0)
				{
					//document.getElementById('req_legacy').innerHTML='<font color=red>*Select Legacy </font>';
                    //document.frm.redir.value = 0;
				}
				else {
					document.getElementById('req_legacy').innerHTML='';
				}
				if (document.lead.main_btn1.value == "" || document.lead.main_btn2.value == "" || document.lead.main_btn3.value == ""){
					document.getElementById('req_phone').innerHTML='<font color=red>*Complete Phone Number Required </font>';
					document.lead.main_btn1.focus();
                    document.lead.redir.value = 0;
                }else {
					document.getElementById('req_phone').innerHTML='';
				}
				
				
					
			   if (document.lead.contact_permission[0].checked == false)
			   {
					document.getElementById('req_permission').innerHTML='<font color=red>*Need Customer permission to call</font>';
                    document.lead.redir.value = 0;
			   }
			   else {
					document.getElementById('req_permission').innerHTML='';
			   }
			   if (prod == "") {
					document.getElementById('req_prod').innerHTML='<font color=red>*Select at least one product</font>';
                    document.lead.redir.value = 0;
			   }
			   else {
					document.getElementById('req_prod').innerHTML='';
			   }
                if ( document.lead.redir.value == 1 && prevent_double_submits==0) {
				
					document.lead.submitbtn.disabled = true;
					document.lead.submitbtn.value = "Please wait...";
					prevent_double_submits=1;
		           //document.lead.action="G:/CenturyLinkTest/xroot/qwest/youcan10/welcome.cgi";
                    document.lead.submit();
                    return true;
                }
				else{
                    return false;
				}
               
    }
	 /*---------------------------------------*/
/* coop 88725, 88726, 88727, 88728	*/
/* staging 	88581, 88582, 88583, 88584  */

	function checkformBiz(){
	
    document.lead.redir.value = 1;
			var prevent_double_submits = 0;
			var prod = "";
			var flag = 0;
			var med_lg_button = -1;
			var leg = 0;
			var savvis_prod_flag = 0;
			var medLg_prod_flag = 0;

/*
				if (document.frm.medLg[0].checked == true  )
					{
						med_lg_button =  1;
					}

				if (document.frm.medLg[1].checked == true)
				{
						med_lg_button =  0;
				}
*/								
								
				for (var d=0; d < document.lead.product.length; d++){
					if (document.lead.product[d].checked ){
						prod =  prod + document.lead.product[d].value;
					}
				}

/*
savvis products taken off
				if (document.frm.product[0].checked)
				{
					if (document.frm.product[0].value == "savvisdirect")
					{
						savvis_prod_flag = 1;
					}
				}
*/
				if (document.lead.lead_state.value == "")
				{
					document.getElementById('req_state').innerHTML='<font color=red>*State Required </font>';
					document.lead.lead_company_name.focus();
                    document.lead.redir.value = 0;
				}
				else {
					document.getElementById('req_state').innerHTML='';
				}
				if (document.lead.ctl_radio.value == 0)
				{
					leg = document.lead.ctl_legacy.value;
				}
				else if (document.lead.ctl_radio.value == 1)
				{
					if (document.lead.ctl_legacy_radio[0].checked == true  )
					{
						leg = 1;
					}
					else if (document.lead.ctl_legacy_radio[1].checked == true)
					{
						leg = 2;
					}
				}



				
                 if ( document.lead.lead_company_name.value == "" ) {
					document.getElementById('req_bizname').innerHTML='<font color=red>*Name Required </font>';
					document.lead.lead_company_name.focus();
                    document.lead.redir.value = 0;
                }
				else {
					document.getElementById('req_bizname').innerHTML='';
				}
                 if ( document.lead.lead_name.value == "" ) {
					document.getElementById('req_leadname').innerHTML='<font color=red>*Contact Name Required </font>';
					document.lead.lead_name.focus();
                    document.lead.redir.value = 0;
                }
				else {
					document.getElementById('req_leadname').innerHTML='';
				}

				if (leg == 0)
				{
					document.getElementById('req_legacy').innerHTML='<font color=red>*Select Legacy </font>';
					document.lead.lead_company_name.focus();
                    document.lead.redir.value = 0;
				}
				else {
					document.getElementById('req_legacy').innerHTML='';
				}

				if (document.lead.main_btn1.value == "" || document.lead.main_btn2.value == "" || document.lead.main_btn3.value == ""){
					document.getElementById('req_phone').innerHTML='<font color=red>*Complete Phone Number Required </font>';
					document.lead.main_btn1.focus();
                    document.lead.redir.value = 0;
                }else {
					document.getElementById('req_phone').innerHTML='';
				}
				if (document.lead.lead_address.value == "")
				{
					document.getElementById('req_addr').innerHTML='<font color=red>*Address Required </font>';
					document.lead.lead_address.focus();
                    document.lead.redir.value = 0;
				}
				else {
					document.getElementById('req_addr').innerHTML='';
				}
				if (document.lead.lead_city.value == "")
				{
					document.getElementById('req_city').innerHTML='<font color=red>*City Required </font>';
					document.lead.lead_city.focus();
                    document.lead.redir.value = 0;
				}
				else {
					document.getElementById('req_city').innerHTML='';
				}
				if (document.lead.lead_zip.value == "")
				{
					document.getElementById('req_zip').innerHTML='<font color=red>*Zip Required </font>';
					document.lead.lead_zip.focus();
                    document.lead.redir.value = 0;
				}
				else {
					document.getElementById('req_zip').innerHTML='';
				}
					
			   if (prod == "") {
					document.getElementById('req_prod').innerHTML='<font color=red>*Select at least one product</font>';
                    document.lead.redir.value = 0;
			   }
			   else {
					document.getElementById('req_prod').innerHTML='';
			   }
/*			   if ( med_lg_button == -1)
			   {
					document.getElementById('req_medLg').innerHTML='<font color=red>*Please select if Business is Medium/Large</font>';
                    document.frm.redir.value = 0;
			   }
			   else {
						document.getElementById('req_medLg').innerHTML='';
			   }

			   if (savvis_prod_flag > 0 && med_lg_button > 0)
			   {
					document.getElementById('req_medLg2').innerHTML='<font color=red>*Please select Savvis OR Medium/Large</font>';
                    document.frm.redir.value = 0;
			   }
			   else {
					document.getElementById('req_medLg2').innerHTML='';
			   }
			   if (medLg_prod_flag > 0 && savvis_prod_flag > 0)
			   {
					document.getElementById('req_medLg3').innerHTML='<font color=red>*Please select Savvis product OR qualifying Medium Large Product.</font>';
                    document.frm.redir.value = 0;
			   }
			   else {
					document.getElementById('req_medLg3').innerHTML='';
			   }
*/

			   if (document.lead.contact_permission[0].checked == false)
			   {
					document.getElementById('req_permission').innerHTML='<font color=red>*Need Customer permission to call</font>';
                    document.lead.redir.value = 0;
			   }
			   else {
					document.getElementById('req_permission').innerHTML='';
			   }
                if ( document.lead.redir.value == 1 && prevent_double_submits==0) {
					document.lead.submitbtn.disabled = true;
					document.lead.submitbtn.value = "Please wait...";
					prevent_double_submits=1;
		           //document.lead.action="G:/CenturyLinkTest/xroot/qwest/youcan10/welcome.cgi";
                    document.lead.submit();
                    return true;
                }
				else{
                    return false;
				}
               
    }

 /*---------------------------------------*/
    function toggleDiv(item, a){

	if (document.getElementById(item).style.display=='none'){
        document.getElementById(item).style.display='';
		a.innerHTML='Hide Lead List';
		
    }
    else{
         document.getElementById(item).style.display='none';
		a.innerHTML='Show Lead List';
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
    function hideShow(item1, item2){
    document.getElementById(item1).style.display='block';
	document.getElementById(item2).style.display = 'none';
    }

 /*---------------------------------------*/
function openModalmedium(src) {
        $.modal('<iframe src="' + src + '" height="250" width="740" style="border:0">');
                $.modal({
                        autoResize: true
                });
 }

/*--------------------------------------------------------------------------------------------------------------------------*/
function openModalLarge(src) {
        $.modal('<iframe src="' + src + '" height="650" width="750" style="border:0">');
                $.modal({
                        autoResize: true
                });
 }

/*--------------------------------------------------------------------------------------------------------------------------*/

function logoutUser(emp_id, session_id) {
		var answer = confirm("Are you sure you want to logout?")
		if (answer){
			 $.ajax({
				url: "youcan_subs.cgi",
				data: "logout=1&staff_id="+emp_id+"&session_id="+session_id,
				cache: false,
				success: function(html){
						window.location='https://centurylinkyoucan.com/';},
				error: function() {alert('Connection Issue.  Please Try Again.');}
				});
		}else{
			return false;
		}
	 }