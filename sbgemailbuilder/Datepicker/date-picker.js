var a,weekend=[0,6],weekendColor="#e0e0e0",fontface="Verdana",fontsize=2,gNow=new Date,ggWinCal;isNav=navigator.appName.indexOf("Netscape")!=-1?true:false;isIE=navigator.appName.indexOf("Microsoft")!=-1?true:false;Calendar.Months=["January","February","March","April","May","June","July","August","September","October","November","December"];Calendar.DOMonth=[31,28,31,30,31,30,31,31,30,31,30,31];Calendar.lDOMonth=[31,29,31,30,31,30,31,31,30,31,30,31]; function Calendar(c,b,d,e,f){if(!(d==null&&e==null)){this.gWinCal=b==null?ggWinCal:b;if(d==null){this.gMonth=this.gMonthName=null;this.gYearly=true}else{this.gMonthName=Calendar.get_month(d);this.gMonth=new Number(d);this.gYearly=false}this.gYear=e;this.gFormat=f;this.gBGColor="white";this.gHeaderColor=this.gTextColor=this.gFGColor="black";this.gReturnItem=c}}Calendar.get_month=Calendar_get_month;Calendar.get_daysofmonth=Calendar_get_daysofmonth;Calendar.calc_month_year=Calendar_calc_month_year; Calendar.print=Calendar_print;function Calendar_get_month(c){return Calendar.Months[c]}function Calendar_get_daysofmonth(c,b){if(b%4==0){if(b%100==0&&b%400!=0)return Calendar.DOMonth[c];return Calendar.lDOMonth[c]}else return Calendar.DOMonth[c]}function Calendar_calc_month_year(c,b,d){var e=[];if(d==-1)if(c==0){e[0]=11;e[1]=parseInt(b)-1}else{e[0]=parseInt(c)-1;e[1]=parseInt(b)}else if(d==1)if(c==11){e[0]=0;e[1]=parseInt(b)+1}else{e[0]=parseInt(c)+1;e[1]=parseInt(b)}return e} function Calendar_print(){ggWinCal.print()}function Calendar_calc_month_year(c,b,d){var e=[];if(d==-1)if(c==0){e[0]=11;e[1]=parseInt(b)-1}else{e[0]=parseInt(c)-1;e[1]=parseInt(b)}else if(d==1)if(c==11){e[0]=0;e[1]=parseInt(b)+1}else{e[0]=parseInt(c)+1;e[1]=parseInt(b)}return e}new Calendar;a=Calendar.prototype;a.getMonthlyCalendarCode=function(){var c="",b="",d="";c=c+'<TABLE BORDER=1 BGCOLOR="'+this.gBGColor+'">';b=this.cal_header();d=this.cal_data();c=c+b+d;c+="</TABLE>";return c}; a.show=function(){var c="";this.gWinCal.document.open();this.wwrite("<html>");this.wwrite("<head><title>Calendar</title>");this.wwrite("</head>");this.wwrite('<body link="'+this.gLinkColor+'" vlink="'+this.gLinkColor+'" alink="'+this.gLinkColor+'" text="'+this.gTextColor+'">');this.wwriteA("<FONT FACE='"+fontface+"' SIZE=2><B>");this.wwriteA(this.gMonthName+" "+this.gYear);this.wwriteA("</B><BR>");var b=Calendar.calc_month_year(this.gMonth,this.gYear,-1);c=b[0];b=b[1];var d=Calendar.calc_month_year(this.gMonth, this.gYear,1),e=d[0];d=d[1];this.wwrite("<TABLE WIDTH='100%' BORDER=1 CELLSPACING=0 CELLPADDING=0 BGCOLOR='#e0e0e0'><TR><TD ALIGN=center>");this.wwrite("[<A HREF=\"javascript:window.opener.Build('"+this.gReturnItem+"', '"+this.gMonth+"', '"+(parseInt(this.gYear)-1)+"', '"+this.gFormat+"');\"><<</A>]</TD><TD ALIGN=center>");this.wwrite("[<A HREF=\"javascript:window.opener.Build('"+this.gReturnItem+"', '"+c+"', '"+b+"', '"+this.gFormat+"');\"><</A>]</TD><TD ALIGN=center>");this.wwrite('[<A HREF="javascript:window.print();">Print</A>]</TD><TD ALIGN=center>'); this.wwrite("[<A HREF=\"javascript:window.opener.Build('"+this.gReturnItem+"', '"+e+"', '"+d+"', '"+this.gFormat+"');\">></A>]</TD><TD ALIGN=center>");this.wwrite("[<A HREF=\"javascript:window.opener.Build('"+this.gReturnItem+"', '"+this.gMonth+"', '"+(parseInt(this.gYear)+1)+"', '"+this.gFormat+"');\">>></A>]</TD></TR></TABLE><BR>");c=this.getMonthlyCalendarCode();this.wwrite(c);this.wwrite("</font></body></html>");this.gWinCal.document.close()}; a.showY=function(){var c="",b,d,e,f;if(isIE)f=75;else if(isNav)f=25;this.gWinCal.document.open();this.wwrite("<html>");this.wwrite("<head><title>Calendar</title>");this.wwrite("<style type='text/css'>\n<!--");for(b=0;b<12;b++){c=b%3;if(b>=0&&b<=2)d=0;if(b>=3&&b<=5)d=1;if(b>=6&&b<=8)d=2;if(b>=9&&b<=11)d=3;c=parseInt(285*c)+10;e=parseInt(200*d)+f;this.wwrite(".lclass"+b+" {position:absolute;top:"+e+";left:"+c+";}")}this.wwrite("--\>\n</style>");this.wwrite("</head>");this.wwrite('<body link="'+this.gLinkColor+ '" vlink="'+this.gLinkColor+'" alink="'+this.gLinkColor+'" text="'+this.gTextColor+'">');this.wwrite("<FONT FACE='"+fontface+"' SIZE=2><B>");this.wwrite("Year : "+this.gYear);this.wwrite("</B><BR>");b=parseInt(this.gYear)-1;d=parseInt(this.gYear)+1;this.wwrite("<TABLE WIDTH='100%' BORDER=1 CELLSPACING=0 CELLPADDING=0 BGCOLOR='#e0e0e0'><TR><TD ALIGN=center>");this.wwrite("[<A HREF=\"javascript:window.opener.Build('"+this.gReturnItem+"', null, '"+b+"', '"+this.gFormat+"');\" alt='Prev Year'><<</A>]</TD><TD ALIGN=center>"); this.wwrite('[<A HREF="javascript:window.print();">Print</A>]</TD><TD ALIGN=center>');this.wwrite("[<A HREF=\"javascript:window.opener.Build('"+this.gReturnItem+"', null, '"+d+"', '"+this.gFormat+"');\">>></A>]</TD></TR></TABLE><BR>");for(b=11;b>=0;b--){if(isIE)this.wwrite('<DIV ID="layer'+b+'" CLASS="lclass'+b+'">');else isNav&&this.wwrite('<LAYER ID="layer'+b+'" CLASS="lclass'+b+'">');this.gMonth=b;this.gMonthName=Calendar.get_month(this.gMonth);c=this.getMonthlyCalendarCode();this.wwrite(this.gMonthName+ "/"+this.gYear+"<BR>");this.wwrite(c);if(isIE)this.wwrite("</DIV>");else isNav&&this.wwrite("</LAYER>")}this.wwrite("</font><BR></body></html>");this.gWinCal.document.close()};a.wwrite=function(c){this.gWinCal.document.writeln(c)};a.wwriteA=function(c){this.gWinCal.document.write(c)}; a.cal_header=function(){var c="";c+="<TR>";c=c+"<TD WIDTH='14%'><FONT SIZE='2' FACE='"+fontface+"' COLOR='"+this.gHeaderColor+"'><B>Sun</B></FONT></TD>";c=c+"<TD WIDTH='14%'><FONT SIZE='2' FACE='"+fontface+"' COLOR='"+this.gHeaderColor+"'><B>Mon</B></FONT></TD>";c=c+"<TD WIDTH='14%'><FONT SIZE='2' FACE='"+fontface+"' COLOR='"+this.gHeaderColor+"'><B>Tue</B></FONT></TD>";c=c+"<TD WIDTH='14%'><FONT SIZE='2' FACE='"+fontface+"' COLOR='"+this.gHeaderColor+"'><B>Wed</B></FONT></TD>";c=c+"<TD WIDTH='14%'><FONT SIZE='2' FACE='"+ fontface+"' COLOR='"+this.gHeaderColor+"'><B>Thu</B></FONT></TD>";c=c+"<TD WIDTH='14%'><FONT SIZE='2' FACE='"+fontface+"' COLOR='"+this.gHeaderColor+"'><B>Fri</B></FONT></TD>";c=c+"<TD WIDTH='16%'><FONT SIZE='2' FACE='"+fontface+"' COLOR='"+this.gHeaderColor+"'><B>Sat</B></FONT></TD>";c+="</TR>";return c}; a.cal_data=function(){var c=new Date;c.setDate(1);c.setMonth(this.gMonth);c.setFullYear(this.gYear);c=c.getDay();var b=1,d=Calendar.get_daysofmonth(this.gMonth,this.gYear),e=0,f="";f+="<TR>";for(i=0;i<c;i++)f=f+"<TD WIDTH='14%'"+this.write_weekend_string(i)+"><FONT SIZE='2' FACE='"+fontface+"'> </FONT></TD>";for(j=c;j<7;j++){f=f+"<TD WIDTH='14%'"+this.write_weekend_string(j)+"><FONT SIZE='2' FACE='"+fontface+"'><A HREF='#' onClick=\"self.opener.document."+this.gReturnItem+".value='"+this.format_data(b)+ "';window.close();\">"+this.format_day(b)+"</A></FONT></TD>";b+=1}f+="</TR>";for(k=2;k<7;k++){f+="<TR>";for(j=0;j<7;j++){f=f+"<TD WIDTH='14%'"+this.write_weekend_string(j)+"><FONT SIZE='2' FACE='"+fontface+"'><A HREF='#' onClick=\"self.opener.document."+this.gReturnItem+".value='"+this.format_data(b)+"';window.close();\">"+this.format_day(b)+"</A></FONT></TD>";b+=1;if(b>d){e=1;break}}if(j==6)f+="</TR>";if(e==1)break}for(m=1;m<7-j;m++)f=this.gYearly?f+"<TD WIDTH='14%'"+this.write_weekend_string(j+ m)+"><FONT SIZE='2' FACE='"+fontface+"' COLOR='gray'> </FONT></TD>":f+"<TD WIDTH='14%'"+this.write_weekend_string(j+m)+"><FONT SIZE='2' FACE='"+fontface+"' COLOR='gray'>"+m+"</FONT></TD>";return f};a.format_day=function(c){var b=gNow.getDate(),d=gNow.getMonth(),e=gNow.getFullYear();return c==b&&this.gMonth==d&&this.gYear==e?'<FONT COLOR="RED"><B>'+c+"</B></FONT>":c};a.write_weekend_string=function(c){var b;for(b=0;b<weekend.length;b++)if(c==weekend[b])return' BGCOLOR="'+weekendColor+'"';return""}; a.format_data=function(c){var b;b=1+this.gMonth;b=b.toString().length<2?"0"+b:b;var d=Calendar.get_month(this.gMonth).substr(0,3).toUpperCase(),e=Calendar.get_month(this.gMonth).toUpperCase(),f=new String(this.gYear),g=new String(this.gYear.substr(2,2));c=c.toString().length<2?"0"+c:c;switch(this.gFormat){case "MM/DD/YYYY":b=b+"/"+c+"/"+f;break;case "MM/DD/YY":b=b+"/"+c+"/"+g;break;case "MM-DD-YYYY":b=b+"-"+c+"-"+f;break;case "MM-DD-YY":b=b+"-"+c+"-"+g;break;case "DD/MON/YYYY":b=c+"/"+d+"/"+f;break; case "DD/MON/YY":b=c+"/"+d+"/"+g;break;case "DD-MON-YYYY":b=c+"-"+d+"-"+f;break;case "DD-MON-YY":b=c+"-"+d+"-"+g;break;case "DD/MONTH/YYYY":b=c+"/"+e+"/"+f;break;case "DD/MONTH/YY":b=c+"/"+e+"/"+g;break;case "DD-MONTH-YYYY":b=c+"-"+e+"-"+f;break;case "DD-MONTH-YY":b=c+"-"+e+"-"+g;break;case "DD/MM/YYYY":b=c+"/"+b+"/"+f;break;case "DD/MM/YY":b=c+"/"+b+"/"+g;break;case "DD-MM-YYYY":b=c+"-"+b+"-"+f;break;case "DD-MM-YY":b=c+"-"+b+"-"+g;break;default:b=b+"/"+c+"/"+f}return b}; function Build(c,b,d,e){gCal=new Calendar(c,ggWinCal,b,d,e);gCal.gBGColor="white";gCal.gLinkColor="black";gCal.gTextColor="black";gCal.gHeaderColor="darkgreen";gCal.gYearly?gCal.showY():gCal.show()} function show_calendar(c,b,d,e){p_item=c;p_month=b==null?new String(gNow.getMonth()):b;p_year=d==""||d==null?new String(gNow.getFullYear().toString()):d;p_format=e==null?"MM/DD/YYYY":e;vWinCal=window.open("","Calendar","width=250,height=300,status=no,resizable=no,top=200,left=200");vWinCal.opener=self;ggWinCal=vWinCal;Build(p_item,p_month,p_year,p_format)} function show_yearly_calendar(c,b,d){if(b==null||b=="")b=new String(gNow.getFullYear().toString());if(d==null||d=="")d="MM/DD/YYYY";var e=window.open("","Calendar","scrollbars=yes");e.opener=self;ggWinCal=e;Build(c,null,b,d)};