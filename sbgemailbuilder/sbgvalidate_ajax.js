// 10/30/2013
//qwest/sbgemailbuilder/assets/js/sbgvalidate_ajax.js
/*---------------------------------------*/

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------ mail_id,cci_id
function updatestatus (mailid ) {
		$.ajax({
			url: "sbgemail_ajax.cgi",
			data: "markSold=1&mailid="+mailid,
			cache: false,
			success: function(html){
					if (html) {	
							alert('Status updated');
							showTrack ();
					}else{	
						alert('Status could not be updated');
						showTrack ();
					}
				},	
				error: function() {alert('Connection Issue. Please Try Again.');
									showTrack ();}
				});}
//------------------------------------------------------------------------------ mail_id,cci_id
function updatestatus_proposal (propid) {
		$.ajax({
			url: "sbgemail_ajax.cgi",
			data: "markSold_prop=1&propid="+propid,
			cache: false,
			success: function(html){
					if (html) {	
							alert('Status updated');
							showTrack ();
					}else{	
						alert('Status could not be updated');
						showTrack ();
					}
				},	
				error: function() {alert('Connection Issue. Please Try Again.');
									showTrack ();}
				});}
//------------------------------------------------------------------------------ cci_id
function showTrack (source_id) {
//	window.alert ('in');
		$.ajax({
			url: "sbgemail_ajax.cgi",
			data: "getTrack=1&source_id="+source_id,
			cache: false,
			success: function(html){
					if (html) {
						$("#trackdiv").html('');
						$("#trackdiv").append(html);
						$("#trackdiv").show();

					}else{
						alert('No Old Emails');
					}
				},
				error: function() {alert('58 Connection Issue. Please Try Again.');}
				});}
//-------------------------------------------------------------------------------
// remove if this does not work

function getTopic(){
	var legacy_id = 0
	// get value for legacy
		for (var i=0; i < document.frm.legacy.length; i++){
			if (document.frm.legacy[i].checked){
					legacy_id = document.frm.legacy[i].value;
				}
			}
	var lang_id = 0 ;
	// get value for language
	for (var i=0; i < document.frm.language_id.length; i++){
			if (document.frm.language_id[i].checked){
					lang_id = document.frm.language_id[i].value;
				}
			}

	var theme_id = 0 ;
	// get value for theme
	for (var i=0; i < document.frm.theme.length; i++){
			if (document.frm.theme[i].checked){
					theme_id = document.frm.theme[i].value;
				}
			}

				 $.ajax({
			url: "sbgemail_ajax.cgi",
			data: "getTopicList=1&theme_id="+theme_id+"&language_id="+lang_id+"&legacy="+legacy_id,
			cache: false,
			success: function(html){
					if (html) {
						$("#themediv").html('');
						$("#themediv").append(html);
						$("#themediv").show();

					}else{
						alert('No Topics for selected Theme');
					}
				},
				error: function() {alert('Connection Issue. Please Try Again.');}
				});

}
//-------------------------------------------------------------------------------
// to display topic based on theme_id selected

	function showTopic (themeID) {
	
	var lang_id = 0 ;
	
	// get value for language
	//for (var i=0; i < 2; i++){ //document.frm.language_id.length
	//		if (document.frm.language_id[i].checked){
	//				lang_id = document.frm.language_id[i].value;
	//			}
	//		}
	var lang2 = document.getElementsByName("language_id")		;
		for (var i=0; i < lang2.length; i++){
			if (lang2[i].checked){
					lang_id =lang2[i].value;
					//break;
				}
			}	
	var legacy_id = 0;
	// get value for legacy
	//	for (var i=0; i < 2; i++){ //document.frm.legacy.length
	//		if (document.frm.legacy[i].checked){
	//				legacy_id = document.frm.legacy[i].value;
	//			}
	//		}
			
	var leg2 = document.getElementsByName("legacy")	;
		for (var i2=0; i2 < leg2.length; i2++){
			if (leg2[i2].checked){
					legacy_id =leg2[i2].value;
					break;
				}
			}


		if (themeID < 1){
			$("#themediv").html('');
			$("#themediv").html('<span class="font1">Select Theme </span>');
			return false;
		}
		 $.ajax({
			url: "sbgemail_ajax.cgi",
			data: "getTopicList=1&theme_id="+themeID+"&language_id="+lang_id+"&legacy="+legacy_id,
			cache: false,
			success: function(html){
					if (html) {
						$("#themediv").html('');
						$("#themediv").append(html);
						$("#themediv").show();

					}else{
						alert('No Topics for selected Theme');
					}
				},
				error: function() {alert('Connection Issue. Please Try Again.');}
				});
	}//#end div region get.
//-------------------------------------------------------------------
	function checkFlow_lang (langID) {
	var legacy_id = 0
	// get value for legacy
		for (var i=0; i < document.frm.legacy.length; i++){
			if (document.frm.legacy[i].checked){
					legacy_id = document.frm.legacy[i].value;
				}
			}

	var flowID = 0 ;
	// get value for bau or PB
	for (var i=0; i < document.frm.bau.length; i++){
			if (document.frm.bau[i].checked){
					flowID = document.frm.bau[i].value;
				}
			}

		if (flowID < 1){
			$("#flowdiv").html('');
			$("#flowdiv").html('<span class="font1">Select Flow</span>');
			return false;
		}
		 $.ajax({
			url: "sbgemail_ajax.cgi",
			data: "getform=1&flowID="+flowID+"&language_id="+langID+"&legacy="+legacy_id,
			cache: false,
			success: function(html){
					if (html) {
						$("#flowdiv").html('');
						$("#flowdiv").append(html);
						$("#flowdiv").show();

					}else{
						alert('No Topics selected.');
					}
				},
				error: function() {alert('Connection Issue. Please Try Again.');}
				});

	}
//-------------------------------------------------------------------
	function checkFlow_legacy (legacyID) {
	var lang_id = 0 ;
	// get value for language
	for (var i=0; i < document.frm.language_id.length; i++){
			if (document.frm.language_id[i].checked){
					lang_id = document.frm.language_id[i].value;
				}
			}

	var flowID = 0 ;
	// get value for bau or PB
	for (var i=0; i < document.frm.bau.length; i++){
			if (document.frm.bau[i].checked){
					flowID = document.frm.bau[i].value;
				}
			}

		if (flowID < 1){
			$("#flowdiv").html('');
			$("#flowdiv").html('<span class="font1">Select Flow</span>');
			return false;
		}
		 $.ajax({
			url: "sbgemail_ajax.cgi",
			data: "getform=1&flowID="+flowID+"&language_id="+lang_id+"&legacy="+legacyID,
			cache: false,
			success: function(html){
					if (html) {
						$("#flowdiv").html('');
						$("#flowdiv").append(html);
						$("#flowdiv").show();

					}else{
						alert('No Topics selected.');
					}
				},
				error: function() {alert('Connection Issue. Please Try Again.');}
				});

	}

//-------------------------------------------------------------------
	function showFlow (flowID) {
		
	var legacy_id = 0
	// get value for legacy
//		for (var i=0; i < document.frm.legacy.length; i++){
//			if (document.frm.legacy[i].checked){
//					legacy_id = document.frm.legacy[i].value;
//				}
//			}

var LegacyRadios = document.getElementsByName('legacy');

for (var i = 0, length = LegacyRadios.length; i < length; i++) {
    if (LegacyRadios[i].checked) {
        // do whatever you want with the checked radio
        legacy_id= (LegacyRadios[i].value);

        // only one radio can be logically checked, don't check the rest
        break;
    }
}



	var lang_id = 0 ;
	// get value for language
var Lang_Radios = document.getElementsByName('language_id');

for (var i = 0, length = Lang_Radios.length; i < length; i++) {
    if (Lang_Radios[i].checked) {
        // do whatever you want with the checked radio
        lang_id= (Lang_Radios[i].value);

        // only one radio can be logically checked, don't check the rest
        break;
    }
}
//window.alert(lang_id);


		if (flowID < 1){
			$("#flowdiv").html('');
			$("#flowdiv").html('<span class="font1">Select Flow</span>');
			return false;
		}

		 $.ajax({
			url: "sbgemail_ajax.cgi",
			data: "getform=1&flowID="+flowID+"&language_id="+lang_id+"&legacy="+legacy_id,
			cache: true,
			success: function(html){
					if (html) {
						$("#flowdiv").html('');
						$("#flowdiv").append(html);
						$("#flowdiv").show();

					}else{
						alert('No Topics selected.');
					}
				},
				error: function() {alert('Connection Issue. Please Try Again.');}
				});
	}//#end div region get.

//-------------------------------------------------------------------

// to display promotions based on header and actual product

function showPromo ( headerID, prodID) {
			var divName = "promodiv_"+ headerID ;
			if (headerID < 1){
			$("#"+divName).html('');
			$("#"+divName).html('<span class="font1">Select Theme </span>');
			return false;
		}
		 $.ajax({
			url: "sbgemail_ajax.cgi",
			data: "getPromo=1&headerID="+headerID+"&prodID="+prodID,
			cache: false,
			success: function(html){
					if (html) {
						$("#"+divName).html('');
						$("#"+divName).append(html);
						$("#"+divName).show();

					}else{
						alert('No Topics for selected Theme');
					}
				},
				error: function() {alert('Connection Issue. Please Try Again.');}
				});

}

//-------------------------------------------------------------------



// to edit proposal onload in sbgProposalReview.cgi
	//whatpart = 1 => contactinfo
	//whatpart = 2 => Products :(

function EditProp ( whatpart, preProposalID) {
// window.alert (whatpart);
// window.alert (preProposalID);
			if (whatpart < 1){
			$("#editdiv").html('');
			$("#editdiv").html('<span class="font1">Select Info to edit</span>');
			return false;
		}
		 $.ajax({
			url: "sbgemail_ajax.cgi",
			data: "editPart="+whatpart+"&preProposalID="+preProposalID,
			cache: false,
			success: function(html){
					if (html) {
						$("#editdiv").html('');
						$("#editdiv").append(html);
						$("#editdiv").show();

					}else{
						alert('No Part selected.');
					}
				},
				error: function() {alert('356 Connection Issue. Please Try Again.');}
				});

}

//-------------------------------------------------------------------

function EditOCemail ( dowhat , pre_oc_ID) {

//window.alert(dowhat);
			if (dowhat < 1){
			$("#editOCemaildiv").html('');
			$("#editOCemaildiv").html('<span class="font1">Select Info to edit</span>');
			return false;
		}
		 $.ajax({
			url: "sbgemail_ajax.cgi",
			data: "dowhat="+dowhat+"&pre_oc_ID="+pre_oc_ID,
			cache: false,
			success: function(html){
					if (html) {
						$("#editOCemaildiv").html('');
						$("#editOCemaildiv").append(html);
						$("#editOCemaildiv").show();

					}else{
						alert('What Part of Confirmation you want to  edit?');
					}
				},
				error: function() {alert('384 Connection Issue. Please Try Again.');}
				});


}

