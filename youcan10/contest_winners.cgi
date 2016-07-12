use strict;       # Require all variables to be scoped explicitly
use Win32::ODBC;  # Perl's ODBC Library for Win 9x/NT
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CGI qw(:standard);
my $cgi = CGI->new();
print $cgi->header('text/html');
my $emplid = $cgi->param('emplid')||0;
my $session_id = $cgi->param('session_id')||0;

my $leadlink=0;
if ( $emplid == 0 ) {
require "G:/CenturyLinkTest/xroot/cgi-bin/init.cgi";
}else{
require "G:/CenturyLinkTest/xroot/cgi-bin/lp-init.pm";
$leadlink = 1;
}
my $myDB = Win32::ODBC->new($main::DSN);


my  $PAGETITLE = "YOUCAN | Deliver the VIP Experience ";
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
print $header;
# below to be checked


print<<"EOF";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>YOUCAN | Deliver the VIP Experience</title>

<!--FAVICON-->
<link href="/favicon.ico" rel="shortcut icon" type="image/x-icon" />

<!--CSS-->
<link type="text/css" href="assets/css/style.css" rel="stylesheet" />
<link href="assets/css/iefix.css" type="text/css" rel="stylesheet" />
<!--JAVASCRIPT-->
<script type="text/javascript" src="assets/js/jquery.js"></script>
<script type="text/javascript" src="assets/js/functions.js"></script>
<script type="text/javascript">
	animatedcollapse.addDiv('nav-sec-1', 'fade=0,speed=500,group=nav,hide=1,height=22px,persist=1')
	animatedcollapse.addDiv('nav-sec-2', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-3', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-4', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-5', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	animatedcollapse.addDiv('nav-sec-6', 'fade=0,speed=500,group=nav,hide=1,height=22px')
	
	animatedcollapse.init()
</script>
<!--[if lt IE 8]> <script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE8.js"></script> <![endif]-->
</head>

<body>
<div id="layout">

	<div id="layout-header">
EOF
require "G:/CenturyLinkTest/xroot/qwest/youcan10/youcan_header.cgi";
showhdr ($PAGETITLE, $session_id, $emplid);
print<<"EOF";
</div><!--END LAYOUT-HEADER-->
    
<div id="layout-body">
  <div id="body-left-sec">
   	<div class="capsule-710">
      <!--	commented out 02-11-2013
      <div class="capsule-710-header">
        <h2>Current Contests</h2>
      </div>
				<p> Contest Dates 12.03.12 through 12.28.12</p>
        <p><a href="pdf/YC_HSI_Dec2012_SW.pdf" target="_blank" >December Southwest Region HSI Contest</a></p>
      -->
      <div class="capsule-710-header">
        <h2>4Q Regional HSI Promotion iPad-Mini Winners</h2>
      </div>
      <div class="capsule-content">

      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/4Q_ipad_mini_bellena.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Northwest<br />Jason Ballena</h4>
          <h5>Seattle, Washington</h5><br />
          <p>Pictured with Seattle VP/GM Susan Anderson</p>
        <hr class="brk-grey clear" />
      <!--	end	-->	

      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/no_photo.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Northwest<br />Stanley Baker</h4>
          <h5>Hermiston, Oregon</h5><br />
          <p></p>
        <hr class="brk-grey clear" />
      <!--	end	-->	      

      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/4Q_ipad_mini_pacheco.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Southwest<br />Joey Pacheco</h4>
          <h5>Tucson, Arizona</h5><br />
          <p>Pictured with AOM Curtis Guyer</p>
        <hr class="brk-grey clear" />
      <!--	end	-->	
      
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/no_photo.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Southwest<br />Jimmy Morris</h4>
          <h5>Las Vegas, Nevada</h5><br />
          <p></p>
        <hr class="brk-grey clear" />
      <!--	end	-->	
      
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/4Q_ipad_mini_wright.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Mountain<br />Keith Wright</h4>
          <h5>Colorado Springs, Colorado</h5><br />
          <p>Pictured with S/W Colorado VP/GM Penny Larson</p>
        <hr class="brk-grey clear" />
      <!--	end	-->	 
            
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/4Q_ipad_mini_gallagher.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Mountain<br />Vaughn Gallagher</h4>
          <h5>Evergreen, Colorado</h5><br />
          <p></p>
        <hr class="brk-grey clear" />
      <!--	end	-->	 
      
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/4Q_ipad_mini_w_phillips.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Eastern<br />William M. Phillips</h4>
          <h5>Southern Pines, North Carolina</h5><br />
          <p></p>
        <hr class="brk-grey clear" />
      <!--	end	-->	 
            
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/no_photo.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Eastern<br />Christopher Sessoms</h4>
          <h5>Troy, North Carolina</h5><br />
          <p></p>
        <hr class="brk-grey clear" />
      <!--	end	-->	     
      
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/4Q_ipad_mini_phillips.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Southern<br />Debbie Phillips</h4>
          <h5>Ozark, Alabama</h5><br />
          <p>Pictured with APS Jeff Adams</p>
        <hr class="brk-grey clear" />
      <!--	end	-->	 
            
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/4Q_ipad_mini_jermark.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Southern<br />David Jermark</h4>
          <h5>Junction City, Kansas</h5><br />
          <p>Pictured with APS Liz Erichsen</p>
        <hr class="brk-grey clear" />
      <!--	end	-->	     
      
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/no_photo.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Midwest<br />Lowell Hanson</h4>
          <h5>Hill City, Minnesota</h5><br />
          <p></p>
        <hr class="brk-grey clear" />
      <!--	end	-->	 
            
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/4Q_ipad_mini_smith.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Midwest<br />Walter Smith</h4>
          <h5>Minneapolis, Minnesota</h5><br />
          <p></p>
        <hr class="brk-grey clear" />
      <!--	end	-->	         
      </div>
      
			<div class="capsule-710-header">
        <h2>4Q Prism TV Winners</h2>
      </div>
      <div class="capsule-content">
      
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/no_photo.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Prism<br />Anthony Boone</h4>
          <h5>Wilson, North Carolina</h5><br />
          <p> </p>
        <hr class="brk-grey clear" />
      <!--	end	-->	
      <!--	start 	-->				
        <div class="contest-winner">
          <img src="assets/img/winners/no_photo.jpg" alt="Contest Winner" />
          <small>&nbsp;</small>
        </div>   
          <h4>Prism<br />Eric Lewis</h4>
          <h5>Rocky Mountain, North Carolina</h5><br />
          <p> </p>
        <hr class="brk-grey clear" />
      <!--	end	-->	

      </div><!--END CONTEST-WINNERS-->
       <br class="clear" />
    </div>
  </div><!--END CAPSULE-->	
</div><!--END BODY-LEFT-SEC-->
<div id="body-right-sec">
EOF
if ($session_id > 0 && $emplid > 0) {
    print<<"EOF";        
        	<div class="capsule-230">
            	<div class="capsule-230-header">
                	<h3>Referrals</h3>
                </div>
                <div class="capsule-content">
                	<!-- <p><a href="welcome.cgi?session_id=$session_id&emplid=$emplid">Start a New Referral.</a></p> -->
					<p><a href="#" onClick="document.lead.action='welcome.cgi';document.lead.submit();">Start a New Referral.</a></p>
                    <hr class="brk-grey" />
                    <!-- <p><a href="ref_hist.cgi?session_id=$session_id&emplid=$emplid">View Referral History.</a></p>  -->
					<p><a href="#" onClick="document.lead.action='ref_hist.cgi';document.lead.submit();">View Referral History.</a></p>
                    <hr class="brk-grey" />
                    <!-- <p><a href="referral_report.cgi?session_id=$session_id&emplid=$emplid">Generate Referral Report.</a></p> -->
					<p><a href="#" onClick="document.lead.action='referral_report.cgi';document.lead.submit();">Generate Referral Report.</a></p>
                </div>
            </div><!--END CAPSULE-->
EOF
		}
    print<<"EOF";        
            
            
        </div><!--END BODY-RIGHT-SEC-->
        <br class="clear" />
    </div><!--END LAYOUT-BODY-->
EOF
#require "G:/CenturyLink/xroot/qwest/youcan10/youcan_footer.cgi";
showftr ($session_id, $emplid);
print<<"EOF";
</div><!--END LAYOUT-->

</body>
</html>
EOF
$myDB ->Close();
undef &get_header;

# -------------------------------------------------------------------

############################################################################
# -------------------------------------------------------------------
sub get_header
{

	my %hash  = @_;
	my $title = $hash{title} || '';
	my $css   = $hash{css} || '';
	my $more  = $hash{more} || '';

	$css = "<link rel=\"stylesheet\" href=\"$css\" type=\"text/css\">\n" if $css;

	my $str = "$ENV{SERVER_PROTOCOL} 200 OK\nContent-type: text/html\n\n";
	$str .= <<EOF;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>$title</title>
$css$more
<meta name=robots content=noindex>
<meta name="MSSmartTagsPreventParsing" content="TRUE">
<meta http-equiv="pragma" content="no-cache">
<script language="javascript">
  function openwindow(URL) {
    win = window.open(URL, "pop", "width=800, height=550, left=50, top=50, scrollbars=yes, toolbar=yes, menubar=yes, status=yes");
  }
</script>

</head>
EOF
	return $str;
}

############################################################################
