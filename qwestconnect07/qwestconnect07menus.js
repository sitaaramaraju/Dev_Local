function mmLoadMenus() {
  if (window.mm_menu_0221111945_0) return;
  window.mm_menu_0221111945_0 = new Menu("root",200,17,"Arial, Helvetica, sans-serif",11,"#003366","#003366","#FFFFFF","#C1D72E","left","middle",3,0,1000,-5,7,true,true,true,1,true,true);
  mm_menu_0221111945_0.addMenuItem("Program Infomation","location='programinfo.cgi'");
  mm_menu_0221111945_0.addMenuItem("Terms & Conditions","location='terms.cgi'");
  
  mm_menu_0221111945_0.fontWeight="bold";
  mm_menu_0221111945_0.hideOnMouseOut=true;
  mm_menu_0221111945_0.bgColor='#555555';
  mm_menu_0221111945_0.menuBorder=1;
  mm_menu_0221111945_0.menuLiteBgColor='#FFFFFF';
  mm_menu_0221111945_0.menuBorderBgColor='#003366';
  mm_menu_0221111945_0.writeMenus();
} // mmLoadMenus()