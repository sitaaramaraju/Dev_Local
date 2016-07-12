print<<"EOF";

<script language="JavaScript" src="/cgi-bin/date-picker.js"></script>

<script language="JavaScript">
function opencal(formname, element){
    var field = formname+'.'+element;
    show_calendar(field);
}

</script>
EOF

return 1;
