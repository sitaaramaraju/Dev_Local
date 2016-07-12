	

    function checkform(){
    var temp1 = document.frm.acct.value ;
    var temp2 = document.frm.acct2.value ;
    var how = document.frm.how_did_you_hear.value ;

    document.frm.redir.value = 1;
		if (temp1 =="" || temp2 == "" || how == "")
		{
                    document.frm.redir.value = 0;
                    window.alert('Account Number and How you heard about us is required.');
					document.frm.acct.focus();

		}
                if(temp1 != temp2 ) {
                    document.frm.redir.value = 0;
                    window.alert('Please confirm valid Account Number.');
					document.frm.acct.focus();
		    }
                if ( document.frm.redir.value == 0 ) {
                    return false;
                }
                else  {
					document.frm.submit();
                    return true;
                }
    }


    function getcoupon(){
    document.frm.redir.value = 3;
    document.frm.submit();
    return true;
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

function sendemail(){
	document.frm.sender.disabled = true;
	document.frm.sender.value = "Please wait...";

    var to = document.frm.tomail.value ;
	var toname =  document.frm.to_name.value ;
	var fromname =  document.frm.from_name.value ;
	var nodouble = 0;
    document.frm.action.value = 1;

if (toname == "")
{
document.frm.action.value = 0;
alert("Please provide Recipient's First Name.");
document.frm.to_name.focus(); 
document.frm.sender.disabled = false;
document.frm.sender.value = "Submit";
}
if (fromname == "")
{
document.frm.action.value = 0;
alert("Please provide your First Name.");
document.frm.from_name.focus(); 
document.frm.sender.disabled = false;
document.frm.sender.value = "Submit";
}

if(!check_email(to)){
document.frm.action.value = 0;
alert("Invalid send email detected.");
document.frm.tomail.focus(); 
document.frm.sender.disabled = false;
document.frm.sender.value = "Submit";
}

if (!check_email(email1)) {
	document.frm.redir.value = 0;
	alert("Invalid email detected.");
	document.frm.from_email.focus(); 
document.frm.sender.disabled = false;
document.frm.sender.value = "Submit";
}


                if ( document.frm.action.value == 1  && nodouble == 0 && document.frm.sender.value == "Please wait...") {
					document.frm.submit();
                    return true;

                }
                else  { 
					nodouble =1;
					return false;

                }

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


    function openCoupon() {
			var w=window.open('http://www.qwestreferafriend.com/qwest/graf07/coupon_reprint_q-cl.html', 'coupon', 'width=550, left=75, top=60, toolbar=no, menubar=no, status=no, scrollbars=no');
			document.frm.action = "http://www.qwestreferafriend.com/qwest/graf07/coupon_reprint_q-cl.html";
			document.frm.target =  'coupon';
			document.frm.submit();

    }
