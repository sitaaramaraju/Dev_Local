function   opennew() {
			var w=window.open('ycapp_email3.cgi', 'sendemail', 'height=300, width=550 left=75, top=60, toolbar=no, menubar=no, status=no, scrollbars=no');
			document.frm.action = "ycapp_email3.cgi";
			document.frm.target =  'sendemail';
			document.frm.submit();

    }
	
function check_email(e) {
ok = "1234567890qwertyuiop[]asdfghjklzxcvbnm.@-_QWERTYUIOPASDFGHJKLZXCVBNM";

for(i=0; i < e.length ;i++){
if(ok.indexOf(e.charAt(i))<0){ 
return (false);
}	
} 

if (document.images) {
re = /(@.*@)|(\.\.)|(^\.)|(^@)|(@$)|(\.$)|(@\.)/;
re_two = /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
if (!e.match(re) && e.match(re_two)) {
return (-1);		
} 

}

}


function checkstuff() {
	document.get_email.mailer.disabled = true;
	document.get_email.mailer.value = "Please wait...";

	var to = document.get_email.tomail.value;
	document.get_email.redir.value =1;

if(!check_email(to)){
		 document.get_email.redir.value = 0;
alert("Invalid send email detected.");
document.get_email.tomail.focus(); 
}
if (document.get_email.redir.value ==1 && document.get_email.mailer.value == "Please wait...") {
    document.get_email.submit();
    return true;
}

}

function gotoemail(){
	if (document.frm.show_email.value == 1){
		document.frm.action = "email_index.cgi";
	}
	else {
		document.frm.action = "email_error.cgi";
	}
			document.frm.target =  '_self';
			document.frm.submit();
}

function gotomkt(){ 
			document.frm.action = "mkt_materials.cgi";
			document.frm.target =  '_self';
			document.frm.submit();
}

/*---------------------------------------*/
/*Open large light-box style window*/


function openModalLarge(src) {
        $.modal('<iframe src="' + src + '" height="600" width="800" style="border:0">');
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


