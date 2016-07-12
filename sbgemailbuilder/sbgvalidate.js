// 01/30/2012
//qwest/sbgemailbuilder/assets/js/sbgvalidate.js
/*---------------------------------------*/
/*Logon Page Submit*/
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
/*Logon Page Submit*/
function checkLogin(){
        var valid = 1;
        if ( document.login.userid.length = 0) {
            document.getElementById('reqUser').innerHTML='<font color=red><-- Required field</font>';
            document.login.userid.focus();
            valid = 0;
        }else{
            document.getElementById('reqUser').innerHTML='&nbsp;';
        }

        if ( document.login.password.length = 0) {
            document.getElementById('reqPass').innerHTML='<font color=red><-- Required field</font>';
            document.login.password.focus();
            valid = 0;
        }else{
            document.getElementById('reqPass').innerHTML='&nbsp;';
        }

        if (valid == 1){
                document.login.submit();
                return true;
        }else{
                return false;
        }

}

//-------------------------------------------------------------------------------
function isNumberKey(evt)
      {
         var charCode = (evt.which) ? evt.which : event.keyCode
         if (charCode > 31 && (charCode < 48 || charCode > 57))
            return false;
 
         return true;
      }
//-------------------------------------------------------------------------------
/*
function acceptDigits(objtextbox)
	{	var exp = /[^\\d]/g;
		objtextbox.value = objtextbox.value.replace(exp,'');
	}

//-------------------------------------------------------------------------------
function acceptCurr(objtextbox)
	{
		var pattern = ^(0|0?[1-9]\d*)\.\d\d$ ;
		objtextbox.value = objtextbox.value.replace(pattern,'');
	}
*/
//-------------------------------------------------------------------------------


function proposalCheck() {
	var valid = 1;
	var emailstatus = verifyEmail(document.frm.email.value);

	var prodcnt = 0;
	var qtyName = '';
	var termName = '';
	var nrcName = '';
	var mrcName = '';
	var speedName = '';
	var shipName = '';

	var qtySpanName = '';
	var termSpanName = '';
	var nrcSpanName = '';
	var mrcSpanName = '';
	var speedSpanName = '';
	var shipSpanName = '';

	var prodID = 0;


	document.frm.redir.value = 0;

				for (var d=0; d < document.frm.productID.length; d++){
					if (document.frm.productID[d].checked ){
						prodcnt =  prodcnt + 1;
					}
				}


//	window.alert (document.frm.redir.value);
			if (document.frm.company_name.value == "")
			{
				document.getElementById('req_company_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('company_name').style.backgroundColor = '#F5BCA9';
				document.frm.company_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_company_name').innerHTML='';
				document.getElementById('company_name').style.backgroundColor = '';
			}
			if (document.frm.first_name.value == "")
			{
				document.getElementById('req_first_name').innerHTML='<font color=red>* Required </font>';
				document.frm.first_name.focus();
				document.getElementById('first_name').style.backgroundColor = '#F5BCA9';
				valid = 0;
			}
			else {
				document.getElementById('req_first_name').innerHTML='';
				document.getElementById('first_name').style.backgroundColor = '';
			}
			if (document.frm.last_name.value == "")
			{
				document.getElementById('req_last_name').innerHTML='<font color=red>* Required </font>';
				document.frm.last_name.focus();
				document.getElementById('last_name').style.backgroundColor = '#F5BCA9';
				valid = 0;
			}
			else {
				document.getElementById('req_last_name').innerHTML='';
				document.getElementById('last_name').style.backgroundColor = '';
			}
			if (document.frm.email.value == "")
			{
				document.getElementById('req_email').innerHTML='<font color=red>* Required </font>';
				document.frm.email.focus();
				document.getElementById('email').style.backgroundColor = '#F5BCA9';
				valid = 0;
			}
			else {
				document.getElementById('req_email').innerHTML='';
				document.getElementById('email').style.backgroundColor = '';
			}
			if (emailstatus == 0)
			{
				document.getElementById('req_email').innerHTML='<br><font color=red>*Valid Email Required </font>';
				document.frm.email.focus();
				document.getElementById('email').style.backgroundColor = '#F5BCA9';
				valid = 0;
			}
			else {
				document.getElementById('req_email').innerHTML='';
				document.getElementById('email').style.backgroundColor = '';
			}
			if (prodcnt == 0)
			{
				document.getElementById('req_prod').innerHTML='<font color=red>*Select a product </font>';
				document.frm.legacy[0].focus();
				valid = 0;
			}
			else {
				document.getElementById('req_prod').innerHTML='';
			}
/*
							// NRC
							if (document.getElementById(nrcName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(nrcName).value == "NRC" || document.getElementById(nrcName).value == 0)
							{	
								document.getElementById(nrcSpanName).innerHTML='<font color=red>* NRC Required </font>';
								document.getElementById(nrcName).focus();
								document.getElementById(nrcName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(nrcSpanName).innerHTML='';
								document.getElementById(nrcName).style.backgroundColor = '';
							}
*/
// chk prod fields
for (var d=0; d < document.frm.productID.length; d++){
		//				window.alert (document.frm.productID[d].value);
					if (document.frm.productID[d].checked ){
						prodID = document.frm.productID[d].value;
						qtyName = "qty_"+  prodID ;
						qtySpanName = "req_qty_"+prodID ;
						termName = "term_"+ prodID ;
						termSpanName = "req_term_"+prodID ;
						nrcName = "nrc_"+ prodID ;
						nrcSpanName = "req_nrc_"+prodID ;
						mrcName = "mrc_"+ prodID ;
						mrcSpanName = "req_mrc_"+prodID ;
						shipName = "ship_"+ prodID ;
						shipSpanName = "req_ship_"+prodID ;
						speedName = "speed_"+ prodID ;
						speedSpanName = "req_speed_"+prodID ;
						//	QTY
							if (document.getElementById(qtyName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(qtyName).value == "QTY" || document.getElementById(qtyName).value == "0" || document.getElementById(qtyName).value > 9)
							{	
								document.getElementById(qtySpanName).innerHTML='<font color=red>* QTY Required </font>';
								document.getElementById(qtyName).focus();
								document.getElementById(qtyName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(qtySpanName).innerHTML='';
								document.getElementById(qtyName).style.backgroundColor = '';
							}
						// Term
							if (document.getElementById(termName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(termName).value =="-Select Term-")
							{
								document.getElementById(termSpanName).innerHTML='<font color=red>* Term Required </font>';
								document.getElementById(termName).focus();
								document.getElementById(termName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(termSpanName).innerHTML='';
								document.getElementById(termName).style.backgroundColor = '';
							}
							// MRC
							if (document.getElementById(mrcName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(mrcName).value == "MRC" || document.getElementById(mrcName).value == 0)
							{	
								document.getElementById(mrcSpanName).innerHTML='<font color=red>* MRC Required </font>';
								document.getElementById(mrcName).focus();
								document.getElementById(mrcName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(mrcSpanName).innerHTML='';
								document.getElementById(mrcName).style.backgroundColor = '';
							}
							// ship
							if (document.getElementById(shipName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(shipName).value == "Shipping" )
							{	
								document.getElementById(shipSpanName).innerHTML='<font color=red>* Shipping Required </font>';
								document.getElementById(shipName).focus();
								document.getElementById(shipName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(shipSpanName).innerHTML='';
								document.getElementById(shipName).style.backgroundColor = '';
							}
							//speed
							if (document.getElementById(speedName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(speedName).value == "0"  )
							{	
								document.getElementById(speedSpanName).innerHTML='<font color=red>* Speed Required </font>';
								document.getElementById(speedName).focus();
								document.getElementById(speedName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(speedSpanName).innerHTML='';
								document.getElementById(speedName).style.backgroundColor = '';
							}
				}
}

		//	valid = 0;
			if (valid == 1)
			{
					document.frm.action = "sbgProposalReview.cgi";
					document.frm.redir.value =0;
					document.frm.submit();

			}
			

}
//-------------------------------------------------------------------------------
function reviewProposal( ProposalD) {
				$.modal('<iframe src="sbgProposalReview.cgi?preProposal_id='+ProposalD+'&redir=0" height="600" width="900" style="border:0">');
                $.modal({
                        autoResize: true
                });




}
//-------------------------------------------------------------------------------
function updateProposal(){
					document.frm.action = "sbgProposalEdit.cgi";
					document.frm.redir.value =2;
					document.frm.submit();
}

//-------------------------------------------------------------------------------
function editProposal(){
					document.frm.action = "sbgProposalEdit.cgi";
					document.frm.redir.value =1;
					document.frm.submit();
}
//-------------------------------------------------------------------------------

function sendProposal (){
					document.frm.action = "landing.cgi";
					document.frm.redir.value =2;
					document.frm.submit();
}
//-------------------------------------------------------------------------------
function cancelProposal() {
					document.frm.action = "landing.cgi";
					document.frm.redir.value =3;
					document.frm.submit();
}
//-------------------------------------------------------------------------------
function backToReview(){
					document.frm.action = "sbgProposalReview.cgi";
					document.frm.submit();
}
//-------------------------------------------------------------------------------
function checkform () {
			var valid = 1;
var emailstatus = verifyEmail(document.frm.email.value);
var themeid = 0;
var  topicid ="";
var ssid_theme = "";
//var sid  = document.frm.session_id.value;

				for (var j=0; j < document.frm.theme.length; j++){
					if (document.frm.theme[j].checked){
					themeid = document.frm.theme[j].value;
					}
				}
			if ( themeid > 1)
			{
				for (var d=0; d < document.frm.topic_name.length; d++){
					if (document.frm.topic_name[d].checked ){
						topicid =  topicid + document.frm.topic_name[d].value;
					}
				}
			}
			if (themeid == 1)
			{
				for (var d=0; d < document.frm.ss_id.length; d++){
					if (document.frm.ss_id[d].checked ){
						ssid_theme =  ssid_theme + document.frm.ss_id[d].value;
					}
				}
			}
			if (document.frm.company_name.value == '')
			{
				document.getElementById('req_company_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('company_name').style.backgroundColor = '#F5BCA9';
				document.frm.company_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_company_name').innerHTML='';
				document.getElementById('company_name').style.backgroundColor = '';
			}
			if (document.frm.first_name.value == '')
			{
				document.getElementById('req_first_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('first_name').style.backgroundColor = '#F5BCA9';
				document.frm.first_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_first_name').innerHTML='';
				document.getElementById('first_name').style.backgroundColor = '';
			}
			if (document.frm.last_name.value == '')
			{
				document.getElementById('req_last_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('last_name').style.backgroundColor = '#F5BCA9';
				document.frm.last_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_last_name').innerHTML='';
				document.getElementById('last_name').style.backgroundColor = '';
			}
			if (document.frm.email.value == '')
			{
				document.getElementById('req_email').innerHTML='<font color=red>* Required </font>';
				document.getElementById('email').style.backgroundColor = '#F5BCA9';
				document.frm.email.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_email').innerHTML='';
				document.getElementById('email').style.backgroundColor = '';
			}
			if (emailstatus == 0)
			{
				document.getElementById('req_email').innerHTML='<font color=red>*Valid Email Required </font>';
				document.getElementById('email').style.backgroundColor = '#F5BCA9';
				document.frm.email.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_email').innerHTML='';
				document.getElementById('email').style.backgroundColor = '';
			}
			if (themeid == 0)
			{
				document.getElementById('req_theme').innerHTML='<font color=red>*Theme Required </font>';
				document.frm.theme[0].focus();
				valid = 0;
			} 
			if ( themeid > 1 && (topicid == 0 || topicid ==""))
			{
				document.getElementById('req_topic').innerHTML='<font color=red>*Topic Required </font>';
				document.frm.topic_name[0].focus();
				valid = 0;
			}	        
			if (themeid == 1 && (ssid_theme == 0 || ssid_theme ==""))
			{
				document.getElementById('req_topic').innerHTML='<font color=red>*Topic Required </font>';
				document.frm.ss_id[0].focus();
				valid = 0;
			}

			return valid ;	       	       

}
//------------------------------------------------------------------------------
function getconfirm() {

	var isvalid = checkform();


	var lang = '';
	var lang_id = 0 ;
	// get value for language
	for (var i=0; i < document.frm.language_id.length; i++){
			if (document.frm.language_id[i].checked){
					lang_id = document.frm.language_id[i].value;
				}
			}

	if (lang_id == 1)
	{
		lang = 'English';
	}
	else {
		lang = 'Spanish';
	}

	var legacy = '';
	var legacy_id = 0
	// get value for legacy
		for (var i=0; i < document.frm.legacy.length; i++){
			if (document.frm.legacy[i].checked){
					legacy_id = document.frm.legacy[i].value;
				}
			}

	if (legacy_id == 1)
	{
		legacy = 'Qwest';
	}
	if (legacy_id == 2)
	{
		legacy = 'CenturyLink';
	}

var thechoice = 'You chose to send email in '+ lang +' for Legacy '+ legacy +' system.' ;
var r=confirm(thechoice);
if (r==true && isvalid == 1)
  {
	sendemail();
  }

}
//------------------------------------------------------------------------------
function sendemail(){
	document.frm.redir.value =1;
	document.frm.submit();
}
//------------------------------------------------------------------------------
function clearField(target){
        target.value= "";
    }
//------------------------------------------------------------------------------
    function toggleDiv(item, a){

	if (document.getElementById(item).style.display=='none'){
        document.getElementById(item).style.display='';
		a.innerHTML='Hide Product List';
		
    }
    else{
         document.getElementById(item).style.display='none';
		a.innerHTML='Show Product List';
    }


    }
//------------------------------------------------------------------------------
function toggleVisibility(item){
    if (document.getElementById(item).style.display=='none'){
        document.getElementById(item).style.display='';
    }
    else{
         document.getElementById(item).style.display='none';
    }
}


//------------------------------------------------------------------------------
function editContactCheck() {

	var valid = 1;
	var emailstatus = verifyEmail(document.frm.email.value);
	
	document.frm.redir.value = 0;


//	window.alert ('in edit contact');
//	window.alert (document.frm.redir.value);
			if (document.frm.company_name.value == '')
			{
				document.getElementById('req_company_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('company_name').style.backgroundColor = '#F5BCA9';
				document.frm.company_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_company_name').innerHTML='';
				document.getElementById('company_name').style.backgroundColor = '';
			}
				
			if (document.frm.first_name.value == '')
			{
				document.getElementById('req_first_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('first_name').style.backgroundColor = '#F5BCA9';
				document.frm.first_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_first_name').innerHTML='';
				document.getElementById('first_name').style.backgroundColor = '';
			}
				
			if (document.frm.last_name.value == '')
			{
				document.getElementById('req_last_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('last_name').style.backgroundColor = '#F5BCA9';
				document.frm.last_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_last_name').innerHTML='';
				document.getElementById('last_name').style.backgroundColor = '';
			}
				
			if (document.frm.email.value == '' || emailstatus == 0)
			{
				document.getElementById('req_email').innerHTML='<font color=red>* Required </font>';
				document.getElementById('email').style.backgroundColor = '#F5BCA9';
				document.frm.email.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_email').innerHTML='';
				document.getElementById('email').style.backgroundColor = '';
			}
				

			//return valid;
			if (valid == 1)
			{
					document.frm.redir.value =1;
					document.frm.submit();

			}


}
//------------------------------------------------------------------------------ mail_id,
function editProductCheck (){
	var valid = 1;
	
	var prodcnt = 0;
	var qtyName = '';
	var termName = '';
	var nrcName = '';
	var mrcName = '';
	var speedName = '';
	var shipName = '';

	var qtySpanName = '';
	var termSpanName = '';
	var nrcSpanName = '';
	var mrcSpanName = '';
	var speedSpanName = '';
	var shipSpanName = '';

	var prodID = 0;

/*							// NRC
							if (document.getElementById(nrcName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(nrcName).value == "NRC" || document.getElementById(nrcName).value == 0)
							{	
								document.getElementById(nrcSpanName).innerHTML='<font color=red>* NRC Required </font>';
								document.getElementById(nrcName).focus();
								document.getElementById(nrcName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(nrcSpanName).innerHTML='';
								document.getElementById(nrcName).style.backgroundColor = '';
							}
*/

	document.frm.redir.value = 0;

				for (var d=0; d < document.frm.productID.length; d++){
					if (document.frm.productID[d].checked ){
						prodcnt =  prodcnt + 1;
					}
				}

if (document.frm.needNewProd.value == "yes")
{
			if (prodcnt == 0)
			{
				document.getElementById('req_prod').innerHTML='<font color=red>*Select a product </font>';
				valid = 0;
			}
			else {
				document.getElementById('req_prod').innerHTML='';
			}

			for (var d=0; d < document.frm.productID.length; d++){
		//				window.alert (document.frm.productID[d].value);
					if (document.frm.productID[d].checked ){
						prodID = document.frm.productID[d].value;
						qtyName = "qty_"+  prodID ;
						qtySpanName = "req_qty_"+prodID ;
						termName = "term_"+ prodID ;
						termSpanName = "req_term_"+prodID ;
						nrcName = "nrc_"+ prodID ;
						nrcSpanName = "req_nrc_"+prodID ;
						mrcName = "mrc_"+ prodID ;
						mrcSpanName = "req_mrc_"+prodID ;
						shipName = "ship_"+ prodID ;
						shipSpanName = "req_ship_"+prodID ;
						speedName = "speed_"+ prodID ;
						speedSpanName = "req_speed_"+prodID ;
						//	QTY
							if (document.getElementById(qtyName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(qtyName).value == "QTY" || document.getElementById(qtyName).value == "0" || document.getElementById(qtyName).value > 9)
							{	
								document.getElementById(qtySpanName).innerHTML='<font color=red>* QTY Required </font>';
								document.getElementById(qtyName).focus();
								document.getElementById(qtyName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(qtySpanName).innerHTML='';
								document.getElementById(qtyName).style.backgroundColor = '';
							}
						// Term
							if (document.getElementById(termName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(termName).value =="-Select Term-")
							{
								document.getElementById(termSpanName).innerHTML='<font color=red>* Term Required </font>';
								document.getElementById(termName).focus();
								document.getElementById(termName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(termSpanName).innerHTML='';
								document.getElementById(termName).style.backgroundColor = '';
							}
							// MRC
							if (document.getElementById(mrcName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(mrcName).value == "MRC" || document.getElementById(mrcName).value == 0)
							{	
								document.getElementById(mrcSpanName).innerHTML='<font color=red>* MRC Required </font>';
								document.getElementById(mrcName).focus();
								document.getElementById(mrcName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(mrcSpanName).innerHTML='';
								document.getElementById(mrcName).style.backgroundColor = '';
							}
							// ship
							if (document.getElementById(shipName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(shipName).value == "Shipping" || document.getElementById(shipName).value == 0)
							{	
								document.getElementById(shipSpanName).innerHTML='<font color=red>* Shipping Required </font>';
								document.getElementById(shipName).focus();
								document.getElementById(shipName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(shipSpanName).innerHTML='';
								document.getElementById(shipName).style.backgroundColor = '';
							}
							//speed
							if (document.getElementById(speedName).value == "-1")
							{
								//ignore
							}
							else if (document.getElementById(speedName).value == "-Select Speed-"  )
							{	
								document.getElementById(speedSpanName).innerHTML='<font color=red>* Speed Required </font>';
								document.getElementById(speedName).focus();
								document.getElementById(speedName).style.backgroundColor = '#F5BCA9';
								valid = 0;
							}
							else {
								document.getElementById(speedSpanName).innerHTML='';
								document.getElementById(speedName).style.backgroundColor = '';
							}
				}
}

				}

				if (valid == 1)
				{
					document.frm.redir.value =2;
					document.frm.submit();
				}
			
}
//------------------------------------------------------------------------------
function getProdEmailConfirm () {
	var valid = 1;
	
	var id = document.frm.install_date.value;

	var emailstatus = verifyEmail(document.frm.email.value);
	var prodcnt = 0;

 
 var objCBarray = document.getElementsByName('productID');
  for (i = 0; i < objCBarray.length; i++) {
    if (objCBarray[i].checked) {
			prodcnt =  prodcnt + 1;
    }
  }


				if (document.frm.company_name.value == '')
			{
				document.getElementById('req_company_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('company_name').style.backgroundColor = '#F5BCA9';
				document.frm.company_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_company_name').innerHTML='';
				document.getElementById('company_name').style.backgroundColor = '';
			}
			if (document.frm.first_name.value == '')
			{
				document.getElementById('req_first_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('first_name').style.backgroundColor = '#F5BCA9';
				document.frm.first_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_first_name').innerHTML='';
				document.getElementById('first_name').style.backgroundColor = '';
			}
			if (document.frm.last_name.value == '')
			{
				document.getElementById('req_last_name').innerHTML='<font color=red>* Required </font>';
				document.getElementById('last_name').style.backgroundColor = '#F5BCA9';
				document.frm.last_name.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_last_name').innerHTML='';
				document.getElementById('last_name').style.backgroundColor = '';
			}
			if (document.frm.email.value == '')
			{
				document.getElementById('req_email').innerHTML='<font color=red>* Required </font>';
				document.getElementById('email').style.backgroundColor = '#F5BCA9';
				document.frm.email.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_email').innerHTML='';
				document.getElementById('email').style.backgroundColor = '';
			}
			if (emailstatus == 0)
			{
				document.getElementById('req_email').innerHTML='<font color=red>*Valid Email Required </font>';
				document.getElementById('email').style.backgroundColor = '#F5BCA9';
				document.frm.email.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_email').innerHTML='';
				document.getElementById('email').style.backgroundColor = '';
			}
			if (prodcnt == 0)
			{
				document.getElementById('req_prod').innerHTML='<font color=red>*Select a product </font>';
				valid = 0;
			}
			else {
				document.getElementById('req_prod').innerHTML='';
			}
			if (document.frm.install_date.value == '')
			{
				document.getElementById('req_install_date').innerHTML='<font color=red>*Valid Install Date Required 3</font>';
				document.getElementById('install_date').style.backgroundColor = '#F5BCA9';
				document.frm.email.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_install_date').innerHTML='';
				document.getElementById('install_date').style.backgroundColor = '';
			}
			if (document.frm.btn1.value == '' ||document.frm.btn2.value == '' || document.frm.btn2.value == '' )
			{
				document.getElementById('req_btn').innerHTML='<font color=red>*BTN required</font>';
				document.getElementById('btn1').style.backgroundColor = '#F5BCA9';
				document.getElementById('btn2').style.backgroundColor = '#F5BCA9';
				document.getElementById('btn3').style.backgroundColor = '#F5BCA9';
				document.frm.btn1.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_btn').innerHTML='';
				document.getElementById('btn1').style.backgroundColor = '';
				document.getElementById('btn2').style.backgroundColor = '';
				document.getElementById('btn3').style.backgroundColor = '';
			}
			if (document.frm.order_number.value == '')
			{
				document.getElementById('req_order_number').innerHTML='<font color=red>*Order Number Required </font>';
				document.getElementById('order_number').style.backgroundColor = '#F5BCA9';
				document.frm.order_number.focus();
				valid = 0;
			}
			else {
				document.getElementById('req_order_number').innerHTML='';
				document.getElementById('order_number').style.backgroundColor = '';
			}

	if (valid == 1 && document.frm.goWhere.value == 0)
				{
					document.frm.action = "sbgOrderConfirmReview.cgi";
					document.frm.redir.value =0;
					document.frm.submit();
				}
				else if (valid == 1 && document.frm.goWhere.value == 1)
				{
					document.frm.action = "sbgOrderConfirmReview.cgi";
					document.frm.redir.value =1;
					document.frm.submit();
				}

}
//------------------------------------------------------------------------------ mail_id,

function sendOCemail (){
					document.frm.action = "landing.cgi";
					document.frm.redir.value =4;
					document.frm.submit();
}
//-------------------------------------------------------------------------------
function cancelOCemail() {
					document.frm.action = "landing.cgi";
					document.frm.redir.value =5;
					document.frm.submit();
}

//------------------------------------------------------------------------------ mail_id,
function editProposal(pre_id) {
//	document.frm.redir = 4;
	document.frm.action = "sbgProposalEdit.cgi";
	document.frm.submit();

}

//-------------------------------------------------------------------
// to make sure personalised note is not longer than 300 characters.
function CheckFieldLength(fn,wn,rn,mc) {
  var len = fn.value.length;
  if (len > mc) {
    fn.value = fn.value.substring(0,mc);
    len = mc;
  }
  document.getElementById(wn).innerHTML = len;
  document.getElementById(rn).innerHTML = mc - len;
}
//-------------------------------------------------------------------
// to validate email

function verifyEmail(inemail){
var status = 1;     
var emailRegEx = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
     if (inemail.search(emailRegEx) == -1) {
         status = 0;     
     }
     return status;
} 
//------------------------------------------------------------------
function getpwd(){

var isvalid = 1;
			if (document.fpwd.loginid.value=="")
			{
				document.getElementById('req_someID').innerHTML='<font color=red>* Required </font>';
				document.fpwd.loginid.focus();
				isvalid = 0;
			}

        if (isvalid == 1){
				document.fpwd.redir.value=1;
                document.fpwd.submit();
                return true;
        }else{
                return false;
        }

}
//------------------------------------------------------------------
//------------------------------------------------------------------
// open new window for content map
		function openWin(URL) {
			aWindow = window.open(URL, 'content', 'width=750, height=700, left=75, top=60, toolbar=yes, location=yes,directories=yes,status=yes,menubar=yes,scrollbars=yes,copyhistory=yes,resizable=yes');
		 }

//------------------------------------------------------------------
/*Open large light-box style window*/
function openModalLarge(src) {
        $.modal('<iframe src="' + src + '" height="600" width="800" style="border:0">');
                $.modal({
                        autoResize: true
                });
 }
function openModalAST(src) {
        $.modal('<iframe src="' + src + '" height="700" width="900" style="border:0">');
                $.modal({
                        autoResize: true
                });
 }
function openModalmedium(src) {
        $.modal('<iframe src="' + src + '" height="400" width="600" style="border:0">');
                $.modal({
                        autoResize: true
                });
 }

//------------------------------------------------------------------
function getFullYear() {
	var d = new Date();
    var y = d.getYear();
    if (y < 1000) {y += 1900};
    return y;
}

//------------------------------------------------------------------
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
/**--------------------------
//* Validate Date Field script- By JavaScriptKit.com
//* For this script and 100s more, visit http://www.javascriptkit.com
//* This notice must stay intact for usage
---------------------------**/
/*
function checkdate(input){
var validformat=/^\d{2}\/\d{2}\/\d{2}$/ //Basic check for format validity
var returnval=false
if (!validformat.test(input.value))
alert("Invalid Date Format. Please correct and submit again.")
else{ //Detailed check for valid date ranges
var monthfield=input.value.split("/")[0]
var dayfield=input.value.split("/")[1]
var yearfield=input.value.split("/")[2]
var dayobj = new Date(yearfield, monthfield-1, dayfield)
if ((dayobj.getMonth()+1!=monthfield)||(dayobj.getDate()!=dayfield)||(dayobj.getFullYear()!=yearfield))
alert("Invalid Day, Month, or Year range detected. Please correct and submit again.")
else
returnval=true
}
if (returnval==false) input.select()
return returnval
}

*/