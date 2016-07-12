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
            window.alert('here');
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
                document.login.source_id.value=2;
                document.login.submit();
                return true;
        }else{
                return false;
        }

}


function showTopic (topic_num) {
document.getElementById('gpi').style.display="none";
document.getElementById('mbe').style.display="none";
document.getElementById('pyb').style.display="none";
document.getElementById('ibo').style.display="none";

if (topic_num == 1)
{
	topic_name = 'gpi';
}
else if (topic_num == 2)
{
	topic_name = 'mbe';

}
else if (topic_num == 3)
{
		topic_name = 'pyb';

}
else {
	topic_name = 'ibo';

}
document.getElementById(topic_name).style.display="block";

}

//-------------------------------------------------------------------------------

function checkform () {
			var valid = 1;

			if (document.frm.company_name.value == '')
			{
				document.getElementById('req_company_name').innerHTML='<font color=red>* Required </font>';
				document.frm.company_name.focus();
				valid = 0;
			}
			else if (document.frm.first_name.value == '')
			{
				document.getElementById('req_first_name').innerHTML='<font color=red>* Required </font>';
				document.frm.first_name.focus();
				valid = 0;
			}
			else if (document.frm.last_name.value == '')
			{
				document.getElementById('req_last_name').innerHTML='<font color=red>* Required </font>';
				document.frm.last_name.focus();
				valid = 0;
			}
			else if (document.frm.email.value == '')
			{
				document.getElementById('req_email').innerHTML='<font color=red>* Required </font>';
				document.frm.email.focus();
				valid = 0;
			}

	        if (valid == 1){
				document.frm.action = "landing.cgi"
		   document.frm.redir.value = 1;
           document.frm.submit();
      //        return valid;
        }


}




	function showTopic_notworking (themeID, session) {
		if (themeID < 1){
			$("#themediv").html('');
			$("#themediv").html('<span class="font1">Select Area First</span>');
			return false;
		}
		 $.ajax({
			url: "sbgemail_subs.cgi",
			data: "getTopicList=1&theme_id="+themeID+"&session_id="+session,
			cache: false,
			success: function(html){
					if (html != 1) {
						$("#themediv").html('');
						$("#themediv").append(html);
					}else{
						alert('No Topics for selected Theme');
					}
				},
				error: function() {alert('Connection Issue.  Please Try Again.');}
				});
	}//#end div region get.

//	---------------------------
//
//		function showRegionDiv(area, program, session) {
//		if (area == -1){
//			$("#regiondiv").html('');
//			$("#regiondiv").html('<span class="font1">Select Area First</span>');
//			return false;
//		}
//		 $.ajax({
//			url: "/leadpro/400-ajax.cgi",
//			data: "getRegionsByArea=1&program_id="+program+"&session_id="+session+"&area="+area,
//			cache: false,
//			success: function(html){
//					if (html != 1) {
//						$("#regiondiv").html('');
//						$("#regiondiv").append(html);
//					}else{
//						alert('No Regions Found for selected area');
//					}
//				},
//				error: function() {alert('Connection Issue.  Please Try Again.');}
//				});
//	}//#end div region get.