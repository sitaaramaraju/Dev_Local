#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use DBInterface;
use CGI qw(:standard);
my $cgi = CGI->new();

my $server;
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
#else{
#    $server = "d:/xroot";
#}

#require "$server/cgi-bin/init.cgi";
require "$server/cgi-bin/delimeter.cgi";
require "$server/cgi-bin/html2pdf.pm";

my $db = DBInterface->new();
my $db2 = DBInterface->new();
my $myDB2 = DBInterface->new();

#my ( $db, $db2, $myDB2);
	my $thisfile = "sbgemail_subs.cgi";
    my $url_prefix="";
# Lines 788 & 1420 to fix emails
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getEmpID_SourceID {
	my ($cci_id ) = @_;

	my ($session_id,$e) = CCICryptography::getEmpid($cci_id); #(1,1);

	return ($e);

}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub dropProposal {
	my ($proposalID ) = @_;

	my $str = '<br>Your Proposal was not sent.<br>';

	my $sql = "update ctl_sbg_PreProposal set processed = 0 where pre_id = ?";
	my $sth = $db->prepare($sql);
	$sth->execute($proposalID);
	$sth->finish();
	return $str;

}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub printQtyBar {
	my ($prodID, $tab, $db ) = @_;

	my $ret = qq[<table width="100%" border="2" class="email-content" >]; #style="border-color:yellow;"
	my ($qty_name,$term_name,$nrc_name,$mrc_name,$ship_name ,$speed_name, $nrcError, $mrcError);
	my $tabover_td ='';
	my $tdwidth ='16.5%'; 
	if ($tab == 1) {
		$tabover_td = '<td width="5%">&nbsp;</td>';
		$tdwidth = '15.8%';

	}

	my $query = " select --RTRIM(prod_sub_selection) as subsel , productID, 
				ISNULL(is_LQ,0) as is_LQ, ISNULL(is_LCTL,0) as is_LCTL,
				ISNULL(show_nrc,0) as show_nrc, ISNULL(show_mrc,0) as show_mrc,
				ISNULL(show_term,0) as show_term, ISNULL(show_qty,0) as show_qty,isnull(show_speed,0) as show_speed,
				ISNULL(show_shipping,0) as show_shipping,
				case when (ISNULL(show_nrc,0) =0 and ISNULL(show_mrc,0) =0 and
				ISNULL(show_shipping,0) =0 and ISNULL(show_term,0) =0 and ISNULL(show_qty,0) =0 and isnull(show_speed,0) = 0 ) then 0 else 1 end as flag
			from ctl_sbgProposal_product with (nolock) where is_active = 1
			and productId  = $prodID";


	my $sth = $db->prepare($query);
	$sth->execute();
	my $qty_dt = $sth->fetchrow_hashref();
	$sth->finish();
	$qty_name = 'qty_'.$prodID ;
	$term_name = 'term_'.$prodID ;
	$nrc_name = 'nrc_'.$prodID ;
	$mrc_name = 'mrc_'.$prodID ;
	$ship_name = 'ship_'.$prodID ;
	$speed_name = 'speed_'.$prodID ;
# 
			#QTY
			#---------------------
			if ($qty_dt->{show_qty} == 1) {
				$ret .= qq[$tabover_td<td width="$tdwidth" align="center">
							<input type="text"  name="$qty_name"  id="$qty_name" class="prop-field" size="10" maxlength="7"
							onblur="if(value=='' || value==' ' || value==' '){ this.value='QTY' }" onclick="if(value=='QTY'){ this.value='' }"
							value="QTY" onkeyup="isNumberKey(event);"></td>	];
			}
			else {
				$ret .= qq[$tabover_td<td width="$tdwidth" align="center">&nbsp;<input type="hidden" name="$qty_name" id="$qty_name" value="-1"> </td> ];
			}
			#----------------------
			#Term
			if ($qty_dt->{show_term} == 1) {
				$ret .= qq[<td width="$tdwidth" align="center"><select name="$term_name" id="$term_name" size="1" >
						  <option value="-Select Term-" selected="selected">-Select Term-</option>
						  <option value="MTM">MTM</option>
						  <option value="12 Months">12 Months</option>
						  <option value="24 Months">24 Months</option>
						  <option value="36 Months">36 Months</option></select> </td>];
			}
			else {
				$ret .= qq[<td width="$tdwidth" align="center">&nbsp;<input type="hidden" name="$term_name" id="$term_name" value="-1"> </td>];
			}
			#----------------------
			#NRC
			if ($qty_dt->{show_nrc} == 1) {
				$ret .= qq[<td width="$tdwidth" align="center" nowrap><p3>\$</p3>
							<input type="text" name="$nrc_name" id="$nrc_name" size="10" maxlength="7" class="prop-field" 
							onblur="if(value=='' || value==' ' || value==' '){ this.value='NRC' }" onclick="if(value=='NRC'){ this.value='' }" 
							value="NRC" > </td>];
			}
			else {
				$ret .= qq[<td width="$tdwidth" align="center">&nbsp;<input type="hidden" name="$nrc_name" id="$nrc_name" value="-1"> </td>];
			}
			#----------------------
			#MRC
			if ($qty_dt->{show_mrc} == 1) {
				$ret .= qq[<td width="$tdwidth" align="center" nowrap><p3>\$</p3><input type="text" name="$mrc_name" id="$mrc_name" size="10" maxlength="7" class="prop-field" onblur="if(value=='' || value==' ' || value==' '){ this.value='MRC' }" onclick="if(value=='MRC'){ this.value='' }" value="MRC" > </td>];
			}
			else {
				$ret .= qq[<td width="$tdwidth" align="center">&nbsp;<input type="hidden" name="$mrc_name" id="$mrc_name" value="-1"> </td>];
			}
			#----------------------
			#SHIP Other
			if ($qty_dt->{show_shipping} == 1) {
				$ret .= qq[<td width="$tdwidth" align="center" nowrap><p3>\$</p3>
					<input type="text" name="$ship_name"  id="$ship_name" size="10" maxlength="7" class="prop-field" onblur="if(value=='' || value==' ' || value==' '){ this.value='Shipping' }" onclick="if(value=='Shipping'){ this.value='' }" value="Shipping"> </td>];
			}
			else {
				$ret .= qq[<td width="$tdwidth" align="center"> &nbsp;<input type="hidden" name="$ship_name" id="$ship_name" value="-1"> </td>];
			}
			#----------------------
			#Speed 

			if ($qty_dt->{show_speed} == 1) {
				if ($qty_dt->{is_LQ} == 1) {
					$ret .= qq[<td width="$tdwidth" align="center"><select name="$speed_name" id="$speed_name" size="1">
						  <option value="0" selected="selected">-Select Speed-</option>
						  <option value="1.5Mbps">1.5Mbps</option>
						  <option value="7Mbps">7Mbps</option>
						  <option value="12Mbps">12Mbps</option>
						  <option value="20Mbps">20Mbps</option>
						  <option value="40Mbps">40Mbps</option>
						  <option value="60Mbps">60Mbps</option>
						  <option value="80Mbps">80Mbps</option>
						  <option value="100Mbps">100Mbps</option>
						  </select>	</td> ];
				}
				else {
					$ret .= qq[<td width="$tdwidth" align="center"><select name="$speed_name" id="$speed_name" size="1">
						  <option value="0" selected="selected">-Select Speed-</option>
						  <option value="1.5Mbps">1.5Mbps</option>
						  <option value="3Mbps">3Mbps</option>
						  <option value="5Mbps">5Mbps</option>
						  <option value="10Mbps">10Mbps</option>
						  <option value="15Mbps">15Mbps</option>
						  <option value="20Mbps">20Mbps</option>
						  <option value="25Mbps">25Mbps</option>
						  <option value="30Mbps">30Mbps</option>
						  <option value="40Mbps">40Mbps</option>
						  <option value="45Mbps">45Mbps</option>
						  <option value="50Mbps">50Mbps</option>
						  </select>	</td> ];
				}
			}
			else {
				$ret .= qq[<td width="$tdwidth" align="center">&nbsp;<input type="hidden" name="$speed_name" id="$speed_name" value="-1"> </td> ];
			}



	return $ret;

}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getPromos { # for Proposal Builder
	my ($heading,$headerID, $language_id, $legacy) = @_;

	my ($pvc, $promo_name);
	my $legacy_clause = "and ISNULL(is_LCTL,0)= 1";
	if ($legacy == 1) {
		$legacy_clause = "and ISNULL(is_LQ,0)= 1";
	}


	my $ret = '';

	my $query = "select 0 as cnt union 
			select count(promoId)  as cnt from ctl_sbgProposal_promotions with (nolock) 
			where is_active = 1 
			and ISNULL(header_id,0) = $headerID 
			and GETDATE() between ISNULL(promo_start,'01/01/1900') and promo_end $legacy_clause  order by 1 desc";
	#$ret .= qq[<tr><td> $query </td></tr>];
	my $sth = $db->prepare($query);
	$sth->execute();
	my $pro_dt2 = $sth->fetchrow_hashref();
	$sth->finish();
if ($pro_dt2->{cnt} == 0){
	$ret .= qq[<table width="100%" border="2" class="email-content" >
				<tr><td> No promotions are available at this time </td></tr>
				</table>];
}
else {
	$query = "select distinct  header_id, promo_name, isnull((
			select count(promoId) from ctl_sbgProposal_promotions b with (nolock)
			where b.header_id = ctl_sbgProposal_promotions.header_id and b.is_active = 1 and b.promo_name = ctl_sbgProposal_promotions.promo_name 
			 $legacy_clause ),0) as pvc , item_order
			from ctl_sbgProposal_promotions with (nolock) 
			where is_active = 1 
			and ISNULL(header_id,0) = $headerID 
			and GETDATE() between ISNULL(promo_start,'01/01/1900') and promo_end
			$legacy_clause order by item_order";
	#	$ret .= qq[ <tr><td>179 $query </td></tr>];

	$sth = $db->prepare($query);
	$sth->execute();

	while (my $pro_dt = $sth->fetchrow_hashref) {
			$pvc = $pro_dt->{pvc};
			$headerID = $pro_dt->{header_id};
			$promo_name = $pro_dt->{promo_name};
			$ret .= get_promo_details ($promo_name,$pvc,  $headerID, $legacy);

	}
}
	$sth->finish();
$ret .= qq[</table>];
return $ret;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub get_sub_products {

	my ($heading, $selection, $legacy, $language_id, $header_id, $db, $db2) = @_;
	my ($sql, %subdt, $productID, $nrc_name, $mrc_name,$term_name , $speed_name, $id, $qty_name, $ship_name, $detaildiv);
	my ($req_qty,$req_term,$req_nrc,$req_mrc,$req_ship,$req_speed, $nrcError, $mrcError );
    my ( $qtyclause, $termclause, $nrcclause ,$mrcclause, $shipclause, $speedclause, $addNote);
	my $ret = '';
	my $tab = 1;
	my $legacy_clause = "and ISNULL(is_LCTL,0)= 1";
	if ($legacy == 1) {
		$legacy_clause = "and ISNULL(is_LQ,0)= 1";
	}
	$sql="	select RTRIM(prod_sub_selection) as subsel , productID, isnull(prod_note_line,'') as prod_note_line,
	ISNULL(show_nrc,0) as show_nrc, ISNULL(show_mrc,0) as show_mrc,
				ISNULL(show_term,0) as show_term, ISNULL(show_qty,0) as show_qty,isnull(show_speed,0) as show_speed,
				ISNULL(show_shipping,0) as show_shipping,
				ISNULL(is_LCTL,0) as is_LCTL, ISNULL(is_LQ,0) as is_LQ,
				case when (ISNULL(show_nrc,0) =0 and ISNULL(show_mrc,0) =0 and
				ISNULL(show_shipping,0) =0 and ISNULL(show_term,0) =0 and ISNULL(show_qty,0) =0 and isnull(show_speed,0) = 0 ) then 0 else 1 end as flag
			from ctl_sbgProposal_product with (nolock) where is_active = 1 and ISNULL(prod_sub_selection,'') <> 'Main Prod'
			and prod_heading = '$heading' and prod_selection = '$selection' $legacy_clause order by item_order";

	$ret .= qq[<table width="100%" border="2" class="email-content" >];
	#$ret .= qq[<tr><td> call this 763<pre> $sql</pre> </td></tr></table><table width="100%" border="2" class="email-content" >];

	my $sth = $db2->prepare($sql);
	$sth->execute();

	while (my $subdt = $sth->fetchrow_hashref) {
		$productID = $subdt{productID};
		$req_qty = "req_qty_".$productID;
		$req_term = "req_term_".$productID;
		$req_nrc = "req_nrc_".$productID;
		$req_mrc = "req_mrc_".$productID;
		$req_ship = "req_ship_".$productID;
		$req_speed = "req_speed_".$productID;
		$nrcError = "nrcRrror_".$productID;
		$mrcError = "mrcError_".$productID;

		( $qtyclause, $termclause, $nrcclause ,$mrcclause, $shipclause, $speedclause, $addNote)=('','','','','','','');
		if ($subdt->{show_qty} == 1) { $qtyclause = "<span id='".$req_qty."'></span>"; }
		if ($subdt->{show_term} == 1) { $termclause = "<span id='".$req_term."'></span>"; }
		if ($subdt->{show_nrc} == 1) { $nrcclause = "<span id='".$req_nrc."'></span>"; }
		if ($subdt->{show_mrc} == 1) { $mrcclause = "<span id='".$req_mrc."'></span>"; }
		if ($subdt->{show_shipping} == 1) { $shipclause = "<span id='".$req_ship."'></span>"; }
		if ($subdt->{show_speed} == 1) { $speedclause = "<span id='".$req_speed."'></span>"; }
		if ($subdt->{prod_note_line} ne "") {	$addNote = "<small class=\"orange\"><em>$subdt{prod_note_line}</em></small>";	}

			$detaildiv = 'detaildiv_'.$productID;
			$ret .= qq [<tr><td width="5%">&nbsp;</td><td> <input name="productID" id="$productID" type="checkbox" value="$productID" onClick="toggleVisibility('$detaildiv');"/> 
								$subdt->{subsel} $addNote $qtyclause $termclause $nrcclause $mrcclause $shipclause $speedclause</td></tr>];
		if ($subdt{flag} >0) {
			$ret .= qq[<tr><td colspan="2"><!-- div to hide qty fields open	-->
								<div id="$detaildiv" name="$detaildiv" style="display: none;">
								<table width="100%" border="2" class="email-content" style="border-color:blue;" ><tr>];
			$ret .= printQtyBar ($productID, $tab, $db);
		$ret .= qq[</tr></table></div>	<!-- div to hide qty fields close	--></td></tr> ];
	}

	}
	$sth->finish();
	$ret .= qq[</table>];
	return $ret;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub get_promo_details {
	my ($promo_name, $pvc, $headerID, $legacy) = @_;
	my $sth2;

	my $ret =  qq[<table width="100%" border="0" class="email-content" >]; #style="border-color:yellow;"
	my ($sql2, $promoID, $promoFieldID);
	my $legacy_clause = "and isnull(is_LCTL,0) = 1";
	if ($legacy == 1) {
		$legacy_clause = "and isnull(is_LQ,0) = 1 ";
	}

	if ($pvc == 1) {
		$sql2 = "select promoID, promo_name, promo_descr 
						from ctl_sbgProposal_promotions with (nolock) 
						where is_active = 1  and isnull(header_id,0) = $headerID
						and promo_name = '$promo_name' $legacy_clause ";
	#	$ret .= qq[ <pre>405 $sql2 </pre>];
	# this was after promo_name <br><extrasmall>$pr_dt{promo_descr}</extrasmall>
		my $sth = $myDB2->prepare($sql2);
		$sth->execute();
		my $pr_dt = $sth->fetchrow_hashref();
		$sth->finish();

		$promoID = $pr_dt->{promoID};
		$promoFieldID = 'promoID_'.$promoID;
			$ret .= qq[ <tr><td width="10%" align="center"><input name="promoID" id="promoID" type="checkbox" value="$promoID" ></td>
						<td width="90%"> $pr_dt->{promo_name} </td></tr> ];
	}
	else {
	$ret .= qq[ <tr><td width="10%">&nbsp;</td><td colspan="2"width="90%"> $promo_name </td></tr> ];
		$sql2 = "select promoID, promo_name, promo_version, promo_descr 
						from ctl_sbgProposal_promotions with (nolock) 
						where is_active = 1  and isnull(header_id,0) = $headerID
						and promo_name = '$promo_name' $legacy_clause ";
	#	$ret .= qq[ <pre>421 $sql2 </pre>];
		$sth2 = $myDB2->prepare($sql2);
		$sth2->execute();

		while (my $pr_dt = $sth2->fetchrow_hashref) {
			$promoID = $pr_dt->{promoID};
			$promoFieldID = 'promo_'.$promoID ;
			$ret .= qq[ <tr><td width="10%">&nbsp;</td><td width="10%"  align="center">
						<input name="$promoFieldID" id="$promoFieldID" type="checkbox" value="$promoID" ></td>
						<td width="80%">$pr_dt->{promo_version}<br><extrasmall>$pr_dt->{promo_descr}</extrasmall></td></tr> ];

		}
		$sth2->finish();
	}
	$ret .= qq[</table>];
	return $ret;
	
}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getHdrProdDisclaimer {
	my ($hdr_id ) = @_;
	my $q = "select isnull(rtrim(hdr_disclaimer),'') as hdr_disclaimer  from ctl_sbgProposal_header with (nolock) where header_id = $hdr_id";
	my $sth = $db->prepare($q);
	$sth->execute();
	my $hdr_dt = $sth->fetchrow_hashref();
	$sth->finish();

	my $hd = $hdr_dt->{hdr_disclaimer};
	if ($hd ne "") { $hd.='<br>'; 	}

	return $hd;

}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub process_email {
#my ($db, $db2) = @_;

my $str = '';
my $str2 = '';
my ($s,$emplid) = CCICryptography::getEmpid($cgi->param('cci_id')); #(1,1);
my $source_id = $cgi->param('source_id')|| 2 ;
my $company_name = delim_return($cgi->param('company_name')) ;  
my $first_name = ucfirst( delim_return($cgi->param('first_name')));    
my $last_name = ucfirst( delim_return($cgi->param('last_name')));      
my $email = delim_return($cgi->param('email')) ;
my $address = '';#delim_return($main::cgi{address}) ;
my $city = '';#delim_return($main::cgi{city}) ;
my $state = '';#delim_return($main::cgi{state}) ;
my $zip = '';#delim_return($main::cgi{zip}) ;
my $note = delim_return($cgi->param('note')) ;
#my $opportunitytype = $main::cgi{opportunitytype} ;
my $theme = $cgi->param('theme') ;
my $language_id = $cgi->param('language_id')||1 ;
my $legacy =  $cgi->param('legacy') || 1;
my $lang = 'English';
if ($language_id == 2) {
	$lang = 'Spanish';
}
my $leg = 'Qwest';
if ($legacy == 2) {
	$leg = 'CenturyLink';
}
#---- for topic ID
#my @topics = $main::cgi{topic_name} ;
my @topics = $cgi->param('topic_name');
my $topic_list = "(";

foreach my $tid (@topics) {
	if ($topic_list eq "(") {
		$topic_list .= $tid ;
	}
	else {
       $topic_list = $topic_list . ", " . $tid;
	}
}
$topic_list .=")";

#----
# for sell_sheets
#my @ss = $main::cgi{ss_id} ;
my @ss = $cgi->param('ss_id');

my $ss_list = '(';

foreach my $sid (@ss) {
	if ($ss_list eq "(") {
		$ss_list .= $sid ;
	}
	else {
       $ss_list .=  ', ' . $sid;
	}
}
$ss_list .=')';
#----
my $email_purpose_id ;
if ($language_id == 1 && $theme == 1 ) {
	$email_purpose_id = 13;
}
elsif ($language_id == 1 && $theme != 1) {
	$email_purpose_id = 14;
}
elsif ($language_id == 2 && $theme== 1 ) {
	$email_purpose_id = 15;
}
elsif ($language_id == 2 && $theme != 1 ) {
	$email_purpose_id = 16;
}

#email purpose id
#13	50	SBG-General Product Info
#14	50	SBG-Topic Info
#15	50	SBG-General Product Info-Spanish
#16	50	SBG-Topic Info-Spanish
my ($sql,$sbg_id);
my ($subject, $bcc,$cc, $from, $body);

#get theme name
$sql = "select  RTRIM(description) as themename from ctl_sbgEmail_theme with (nolock) where is_active = 1 and theme_id = ?";
	my $sth = $db->prepare($sql);
	$sth->execute($theme);
	my $data2 = $sth->fetchrow_hashref();
	$sth->finish();
my $themename = $data2->{themename};

#$str2 .= $sql.'<br>';
# get employee info
if ($source_id == 2) {
	$sql = "select emplid, rtrim(cuid) as cuid, RTRIM(email) as emp_email, RTRIM(first_name)+' '+RTRIM(last_name) as emp_name, 2 as source_id, 
 SUBSTRING ( work_phone ,1 , 3 )+'-'+SUBSTRING ( work_phone ,4 , 3 )+'-'+SUBSTRING ( work_phone ,7 , 4 ) as work_phone
 from qwesthr with (nolock) where convert( int, emplid ) =  ? ";

}
else {
	$sql = "select floater_id as emplid, rtrim(cuid) as cuid, RTRIM(email) as emp_email, RTRIM(first_name)+' '+RTRIM(last_name) as emp_name, 8 as source_id,
	 '' as work_phone
	from ctl_floaters with (nolock) where floater_id = ? ";
}

#$str .= $sql;
	$sth = $db->prepare($sql);
	$sth->execute($emplid);
	$data2 = $sth->fetchrow_hashref();
	$sth->finish();

my $emp_name = $data2->{emp_name};
my $emp_email = lc($data2->{emp_email});
my $cuid = $data2->{cuid};
#$source_id = $data2->{source_id};
$cc =  $emp_email;
# get pdf's
my $pdf_list = "";
my ($t,$d, $sql2,$pdf_url, $pdf_name, $sth3);

$sql = "select description, theme_id from ctl_sbgEmail_topic with (nolock) where topic_id in $topic_list";

#$str2 .= $sql.'<br>';

my $sth2 = $db->prepare($sql);
	$sth2->execute();

	while (my $data = $sth2->fetchrow_hashref) {

$t = $data->{theme_id};
$d = $data->{description};

$sql2 = " select pdf_name, pdf_url 
from ctl_sbgEmail_topic with (nolock) where description = '$d'
 and theme_id = $t
	 ";
#$str2 .= $sql2.'<br>';

	$sth3 = $db2->prepare($sql2);
	$sth3->execute();

	while (my $data3 = $sth3->fetchrow_hashref) {
		$pdf_name = $data3->{pdf_name};
		if ($language_id == 2) {
    
		if($data3->{pdf_url_spanish} !~ /^http/) { #NOTE: CL made a change. They are hosting some documents another web site, so in those cases where we have an http address, don't
                                             # add the smallbiz prefix, as we do when the document is local to our server.
        
			$url_prefix= 'http://'.$HOST.'/sbgemailbuilder/';        
		}else {
			$url_prefix='';    
		}  
    
		$pdf_url =  $url_prefix .$data3->{pdf_url_spanish};
		$pdf_url =  $url_prefix .$data3->{pdf_url};
	}
	else {
    
    if($data3->{pdf_url} !~ /^http/) {
        
        $url_prefix= 'http://'.$HOST.'/sbgemailbuilder/';        #'http://www.smallbizmailtool.com/';        
    }else {
         $url_prefix='';    
    }  
    
	$pdf_url = $url_prefix .$data3->{pdf_url};
}

	$pdf_list .= "<br><a href=\"$pdf_url\" target=\"_blank\">$pdf_name</a>";
#$str .= $pdf_list.'<br>';
}


	}
	$sth->finish();

 # get sell sheets
my $sell_sheet = "";
$sql2 = "select description, heading , pdf_url ,pdf_LCL , pdf_url_spanish , pdf_LCL_spanish 
from ctl_sbgEmail_sellsheets with (nolock) where ss_id in $ss_list";


 #$str2 .= $sql2.'<br>';

	$sth3 = $db2->prepare($sql2);
	$sth3->execute();
	while (my $data2 = $sth3->fetchrow_hashref) {


    if($data2->{pdf_url} !~ /^http/) {
        
        $url_prefix= 'http://'.$HOST.'/sbgemailbuilder/';         #'http://www.smallbizmailtool.com/';   
    }else {
         $url_prefix='';    
    }

$pdf_url = $url_prefix . $data2->{pdf_url};

if ($legacy == 2) { # and language_id = 1

    if($data2->{pdf_LCL} !~ /^http/) {
        
        $url_prefix= 'http://'.$HOST.'/sbgemailbuilder/';        ;#'http://www.smallbizmailtool.com/';   
    }else {
         $url_prefix='';    
    }
        
    $pdf_url = $url_prefix . $data2->{pdf_LCL};
}
if ($language_id == 2) {
    
	if ($legacy == 1) {
	    
	    if($data2->{pdf_url_spanish} !~ /^http/) {
        
            $url_prefix= 'http://'.$HOST.'/sbgemailbuilder/';        ;#'http://www.smallbizmailtool.com/';        
        }else {
             $url_prefix='';    
        }  
        
	#	$pdf_url = 'http://staging.ccionline.biz/qwest/sbgemailbuilder/'.$data2{pdf_url_spanish};
		$pdf_url = $url_prefix . $data2->{pdf_url_spanish};
	}
	else {
	    
	    if($data2->{pdf_LCL_spanish} !~ /^http/) {
        
            $url_prefix= 'http://'.$HOST.'/sbgemailbuilder/';        #'http://www.smallbizmailtool.com/';        
        }else {
             $url_prefix='';    
        }  
        
		#$pdf_url = 'http://staging.ccionline.biz/qwest/sbgemailbuilder/'.$data2{pdf_LCL_spanish};
		$pdf_url = $url_prefix . $data2->{pdf_LCL_spanish};
	}
}

if ( $data2->{heading} eq "Other Sell Sheets") {
	$sell_sheet .= "<br><a href=\"$pdf_url\" target=\"_blank\">$data2->{description}</a>";
}
else {
	$sell_sheet .= "<br><a href=\"$pdf_url\" target=\"_blank\">$data2->{heading}</a>";
}

$str .= $sell_sheet.'<br>';

}
if ($sell_sheet ne "") {
	if ($language_id == 2) {
		$sell_sheet = '<font face="Arial, Helvetica, sans-serif">A usted podría interesarle:'.$sell_sheet;
	}
	else {
		$sell_sheet = '<font face="Arial, Helvetica, sans-serif">You may be interested in:'.$sell_sheet;
	}
}
# get db fields
$sql = "select email_subject, ltrim(rtrim(email_header)) as email_header, ltrim(rtrim(email_body)) as email_body,
ltrim(RTRIM(email_footer))  as email_footer, email_from_address
from email_templates with (nolock) where is_active = 1 and email_purpose_id = ? ";

	my $sth4 = $db->prepare($sql);
	$sth4->execute($email_purpose_id);
	my $data = $sth4->fetchrow_hashref();
	$sth4->finish();
$from = lc($emp_email);#$data{email_from_address};
$subject = $data->{email_subject};
$subject = EscQuote($subject);
  $body = $data->{email_body};
  $body =~ s/\$email_header/$data->{email_header}/gi;
  $body =~ s/\$email_footer/$data->{email_footer}/gi;
  $body =~ s/\$themename/$themename/gi;
  $body =~ s/\$first_name/$first_name/gi;
  $body =~ s/\$last_name/$last_name/gi;
  $body =~ s/\$emp_name/$emp_name/gi;
  $body =~ s/\$emp_email/$emp_email/gi;
  $body =~ s/\$note/$note/gi;
  $body =~ s/\$sell_sheet/$sell_sheet/gi;
  $body =~ s/\$pdf_list/$pdf_list/gi;
  
  
  $body =EscQuote($body);

# insert into sbg email table
$sql = "insert into ctl_sbgemail (createdby_cuid, createdby_emplid, date_created,  theme_id, email_status_id,
email_status_chng_dt, company_name, first_name, last_name, address, city,	state, zip, subject,
tofield, ccfield, bccfield,  fromfield, longbody, ctype, source_id, language_id, legacy)
values ('$cuid','$emplid', GETDATE(), $theme, 1,
getdate(), '$company_name','$first_name','$last_name','$address','$city','$state','$zip','$subject',
'$email','$cc','$bcc','$from','$body','text/html', $source_id, $language_id,$legacy ) ";

	my $sth5 = $db->prepare($sql);
	$sth5->execute();
	$data= $sth5->fetchrow_hashref();
	$sth5->finish();
    $sbg_id = $data->{mail_id};


#$str .= $sql.'<br>';

#  $email = 'james.miroslaw@centurylink.com,scotts@ccionline.biz,brianf@channelmanagement.com,archanak@ccionline.biz'; # scotts@ccionline.biz,
 #   $email = 'james.miroslaw@centurylink.com,janet.brodsky@centurylink.com'; # scotts@ccionline.biz,
	$bcc = '';#'james.miroslaw@centurylink.com,janet.brodsky@centurylink.com,archanak@ccionline.biz';
# insert into ccimail table
#$body .= $str;
#$body = 'After testing this email will go to: '.$email.'<br>'.$body;

$body = EscQuote($body);

#$email = 'james.miroslaw@centurylink.com,janet.brodsky@centurylink.com,maryann.domsch@centurylink.com,scotts@channelmanagement.com,archanak@channelmanagement.com';
#$email = 'scotts@channelmanagement.com,archanak@channelmanagement.com';
$sql = "insert into ccimail (client_id, program_id,date_created, subject, tofield, bccfield, ccfield,fromfield, longbody, ctype)
		values(50, 447,GETDATE(), '$subject', '$email', '$bcc','$cc', '$from', '$body','text/html')";
#$sql = "insert into ccimail (client_id, date_created, subject, tofield, bccfield, ccfield,fromfield, longbody, ctype)
#		values(50, GETDATE(), '$subject', '$email', '$bcc','', '$from', '$body','text/html')";

	$sth = $db->prepare($sql);
	$sth->execute();
	$data = $sth->fetchrow_hashref();
	$sth->finish();
my	$ccimail_id = $data->{ccimail_id};

#$str .= $sql.'<br>';
# update sbgemail table with ccimail_id
$sql = "update ctl_sbgemail set ccimail_id = $ccimail_id where mail_id = $sbg_id ";
	$sth = $db->prepare($sql);
	$sth->execute();

if ($ccimail_id > 0 && $sbg_id  > 0) {
	$str = '<br>Email sent to '.$email ;
}
else {
	$str .= '<br>There was error in processing the previous email.' ;
}
return ($str, $str2);

}
#-------------------------------------------------------------------------------------------------------
sub createOCemail {
#	my ($myDB, $myDB2) = @_;
	my ($str, $insert, $sql,  $pre_oc_id) ;
#$str .= "calling ";
my ($s,$emplid) = CCICryptography::getEmpid($cgi->param('cci_id')); #(1,1);
my $source_id = $cgi->param('source_id') ;
my $company_name = delim_return($cgi->param('company_name')) ;
my $first_name = ucfirst( delim_return($cgi->param('first_name'))) ;
my $last_name = ucfirst(delim_return($cgi->param('last_name'))) ;
my $email = delim_return($cgi->param('email')) ;
my $noteOC = delim_return($cgi->param('noteOC')) ;
my $language_id = $cgi->param('language_id')||1 ;
my $legacy =  $cgi->param('legacy') || 1;
my $btn = EscQuote($cgi->param('btn1')).EscQuote($cgi->param('btn2')).EscQuote($cgi->param('btn3'));
my $install_date = $cgi->param('install_date');
my $order_number = delim_return($cgi->param('order_number'));

if ( $source_id == 2) {
	$sql = "select emplid, rtrim(cuid) as cuid, RTRIM(email) as emp_email, RTRIM(first_name)+' '+RTRIM(last_name) as emp_name, 2 as source_id
 from qwesthr with (nolock) where emplid = ? ";

}
else {
$sql = " select floater_id as emplid, rtrim(cuid) as cuid, RTRIM(email) as emp_email, RTRIM(first_name)+' '+RTRIM(last_name) as emp_name, 8 as source_id
 from ctl_floaters with (nolock) where floater_id = ? ";

}
#$str .= $sql;

my $sth = $db->prepare($sql);
	$sth->execute($emplid);
my	$data = $sth->fetchrow_hashref();
	$sth->finish();
my $emp_name = $data->{emp_name};
my $emp_email = lc($data->{emp_email});
my $cuid = $data->{cuid};

$insert = "insert into ctl_sbg_PreOC with (rowlock) (createdby_cuid, createdby_emplid, date_created, company_name, first_name, last_name, 
			tofield, subject, fromfield, source_id, language_id, legacy, personal_note, btn, install_date, order_number)
			values (?,?, getdate(), ? ,	? ,? ,	
			?,'CenturyLink Order Confirmation', ? , ? , ? ,  ? , ? ,?,?,? )";
$insert = "insert into ctl_sbg_PreOC with (rowlock) (createdby_cuid, createdby_emplid, date_created, company_name, first_name, last_name, 
			tofield, subject, fromfield, source_id, language_id, legacy, personal_note, btn, install_date, order_number)
			values ('$cuid',$emplid, getdate(), '$company_name' ,'$first_name' ,' $last_name' ,	
			'$email','CenturyLink Order Confirmation', '$emp_email' , $source_id ,  $language_id , $legacy , '$noteOC' ,'$btn','$install_date','$order_number' )";
	$sth = $db->prepare($insert);
	#$sth->execute($cuid, $emplid, $company_name, $first_name, $last_name, $email , $emp_email , $source_id, $language_id, $legacy, $noteOC,$btn,$install_date,$order_number);
	$sth->execute();
	$data = $sth->fetchrow_hashref();
	$sth->finish();
#$str .= '1763 '.$install_date.' <br>'.$insert.'<br>';
#$str .= $insert;
	$pre_oc_id = $data->{pre_oc_id};

	my @pl = $cgi->param('productID');
	foreach my $pid (@pl) {

		$insert = "insert into ctl_sbg_OC_prod_interest (oc_id, productID, last_modified_by, last_modified)
					values ($pre_oc_id,$pid, $emplid, getdate() )";
		$sth = $db->prepare($insert);
		$sth->execute();
		$sth->finish();
		#$str .= '731 '.$insert.'<br>';
	}
	$str .= "Review OC Email";
	return ($str, $pre_oc_id) ;

}
# -------------------------------------------------------------------
sub createProposal {

	my ($str, $ProposalD, $insert, $sql,  $str2) ;

my ($s,$emplid) = CCICryptography::getEmpid($cgi->param('cci_id')); #(1,1);
my $source_id = $cgi->param('source_id')|| 2 ;

my $company_name = delim_return($cgi->param('company_name')) ;
my $first_name = ucfirst( delim_return($cgi->param('first_name'))) ;
my $last_name = ucfirst(delim_return($cgi->param('last_name'))) ;
my $email = delim_return($cgi->param('email')) ;
my $proposal_note = '';#delim_return($main::cgi{proposal_note}) ;
my $personal_note = delim_return($cgi->param('personal_note')) ;
my $language_id = $cgi->param('language_id')||1 ;
my $legacy =  $cgi->param('legacy') || 1;

if ( $source_id == 2) {
	$sql = "select emplid, rtrim(cuid) as cuid, RTRIM(email) as emp_email, RTRIM(first_name)+' '+RTRIM(last_name) as emp_name, 2 as source_id
 from qwesthr with (nolock) where emplid = ? ";

}
else {
$sql = " select floater_id as emplid, rtrim(cuid) as cuid, RTRIM(email) as emp_email, RTRIM(first_name)+' '+RTRIM(last_name) as emp_name, 25 as source_id
 from ctl_floaters with (nolock) where floater_id = ? ";

}
#$str .= $sql;
my $sth = $db->prepare($sql);
	$sth->execute($emplid);
my	$data = $sth->fetchrow_hashref();
	$sth->finish();

my $emp_name = $data->{emp_name};
my $emp_email = lc($data->{emp_email});
my $cuid = $data->{cuid};


			$insert = 	"insert into ctl_sbg_PreProposal (createdby_cuid, createdby_emplid, date_created, 
						company_name, first_name, last_name, 
						tofield, subject, fromfield, 
						source_id, language_id, legacy, 
						proposal_note, personal_note)
				values ('$cuid', $emplid, getdate(), 
						'$company_name', '$first_name','$last_name',
						'$email','CenturyLink Proposal','$emp_email',
						 $source_id , $language_id , $legacy,
						'$proposal_note','$personal_note')";

	$sth = $db->prepare($insert);
	$sth->execute();
	$data = $sth->fetchrow_hashref();
	$sth->finish();

	#$str .= '860 '.$insert.'<br>';

	my $pre_id = $data->{pre_id};


my @pl = $cgi->param('productID');
my ($nrc_name, $mrc_name,$term_name,$speed_name, $ship_name, $qty_name)  ;
my ($nrc, $mrc, $term, $speed, $ship, $prod_note, $qty);
	foreach my $pid (@pl) {
		$nrc_name =  'nrc_'.$pid ; 
		$mrc_name = 'mrc_'.$pid ;
		$term_name =  'term_'.$pid ;
		$speed_name = 'speed_'.$pid ;
		$ship_name = 'ship_'.$pid;
		$qty_name = 'qty_'.$pid;
		
		if ($cgi->param($nrc_name) eq "NRC" || $cgi->param($nrc_name) eq "-1") {
			$nrc = 0;
		}
		else {
			$nrc = $cgi->param($nrc_name);
		}
		if ($cgi->param($mrc_name) eq "MRC" || $cgi->param($mrc_name) eq "-1") {
			$mrc = 0;
		}
		else {
			$mrc = $cgi->param($mrc_name);
		}
		if ($cgi->param($qty_name) eq "QTY" || $cgi->param($qty_name) eq "-1") {
			$qty = 0;
		}
		else {
			$qty = $cgi->param($qty_name);
		}
		if ($cgi->param($ship_name) eq "Shipping" || $cgi->param($ship_name) eq "-1") {
			$ship = 0;
		}
		else {
			$ship = $cgi->param($ship_name);
		}
		#term
		if ($cgi->param($term_name) eq "-Select Term-" || $cgi->param($term_name) eq "-1") {
			$term = 0;
		}
		else {
			$term = $cgi->param($term_name);
		}
		#speed
		if ($cgi->param($speed_name) eq "-Select Speed-" || $cgi->param($speed_name) eq "-1") {
			$speed = "";
		}
		else {
			$speed = $cgi->param($speed_name);
		}
		$prod_note =  '';

		$insert = "insert into ctl_sbg_Proposal_prod_interest 
					(pre_id, productID,  mrc, 
					nrc, speed, term, prod_note, last_modified_by, last_modified, shipping, qty)
					values ($pre_id, $pid,  $mrc, $nrc, '$speed',
							'$term', '$prod_note',$emplid, getdate(),$ship, $qty )";
		$sth = $db->prepare($insert);
		$sth->execute();
		#$str .= '923 '.$insert.'<br>';
	}

 my $promoFieldID = '';

 @pl = $cgi->param('promoID');
	foreach my $promo_id (@pl) {
		$insert = "insert into ctl_sbgProposal_promo_interest 
					(pre_id, promoID, last_modified_by, last_modified)
					values ($pre_id, $promo_id,$emplid, getdate())";
		$sth = $db->prepare($insert);
		$sth->execute();
		#$str .= '934 '.$insert.'<br>';
	}

	$str .= "Review Proposal";
	return ($str, $pre_id) ;
	
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub showSelectedProducts {
	my ($pre_id) = @_;
	my ($sql,$mrc, $nrc, $ship, $term, $qty,$speed,$hdr_id, $prod_heading, $str,$prop_hdr_desc,$prod_selection);
	my ($sql2,$promo_cnt ,$sth2, $sth3 , $prom_dt, $prom_dt2);
#	$str = qq[<table width="100%" border="2" class="email-content" style="border-color:yellow;">];
		#shortcut - show Products selected and then just drop down
	my $hdr_sql = "select  distinct header_id, prod_heading , hdr.hdr_order
				from ctl_sbg_Proposal_prod_interest pint with (nolock)
				inner join ctl_sbgProposal_product prod with (nolock) on prod.productId = pint.productID
				inner join ctl_sbgProposal_header hdr with (nolock)on hdr.description = prod.prod_heading
				where pre_id = $pre_id
				and isnull(hdr.is_LQ,0) = isnull(prod.is_LQ,0)
				and isnull(hdr.is_LCTL,0) = isnull(prod.is_LCTL,0)
				order by hdr.hdr_order";
	#$str .= qq[$hdr_sql];
	my $sth = $db->prepare($hdr_sql);
	$sth->execute();

	while (my $dt = $sth->fetchrow_hashref) {
		$hdr_id = $dt->{header_id};
		$sql = "select pint.productID, prod_notes, header_id, rtrim(proposal_note) as proposal_note, 
				prod_heading, prod_selection, 
				case when prod_sub_selection = 'Main Prod' then prod_selection else prod_sub_selection end as prod_sub_selection,
				prod.description, prop_hdr_desc,
				isnull(show_mrc,0) as show_mrc, isnull(show_nrc,0) as show_nrc,isnull(show_shipping,0) as show_shipping,
				ISNULL(show_qty,0) as show_qty, ISNULL(show_term,0) as show_term, ISNULL(show_speed,0) as show_speed,
				case when (isnull(show_mrc,0)= 1) then isnull(pint.mrc,0) else -1 end as mrc,
				case when (isnull(show_nrc,0)=1) then isnull(pint.nrc,0) else -1 end  as nrc,
				case when (isnull(show_shipping,0)=1) then isnull(pint.shipping,0) else 0 end  as shipping,
				case when (isnull(show_term,0)=1) then isnull(pint.term,0) else 'Not Selected' end  as term,
				case when (isnull(show_qty,0)=1) then isnull(pint.qty,0) else 0 end  as qty,
				case when (isnull(show_speed,0)=1) then isnull(pint.speed,'') else '' end  as speed
				from ctl_sbg_Proposal_prod_interest pint with (nolock)
				inner join ctl_sbgProposal_product prod with (nolock) on prod.productId = pint.productID
				inner join ctl_sbgProposal_header hdr with (nolock)on hdr.description = prod.prod_heading
				where pre_id = $pre_id
				and hdr.header_id = $hdr_id
				and isnull(hdr.is_LQ,0) = isnull(prod.is_LQ,0)
				and isnull(hdr.is_LCTL,0) = isnull(prod.is_LCTL,0)
				order by prod_heading, prod_selection ";
			#$str .= qq[<tr><td>302<pre>$sql</pre></td></tr>];
			$sth2 = $db2->prepare($sql);
			$sth2->execute();

			while (my $prod_dt = $sth2->fetchrow_hashref) {
				($term, $qty, $nrc, $mrc, $ship, $speed) = ('&nbsp;','&nbsp;','&nbsp;','&nbsp;','&nbsp;','&nbsp;');
				if ($prod_heading ne $prod_dt->{prod_heading}) {
					$str .= qq [<h4>$prod_dt->{prod_heading} </h4>];
					#if ($prop_hdr_desc ne $prod_dt{prop_hdr_desc} ) {
					#	$str .= qq[<tr><td>$prod_dt{prop_hdr_desc} </td></tr>];
					#}
				}
				if ($prod_selection ne $prod_dt->{prod_selection}) {
				$str .= qq[<tr><td> $prod_dt->{prod_selection}</td></tr>];
				}
				if ($prod_dt->{prod_sub_selection} ne "") {
					$str .= qq[<tr><td>$prod_dt->{prod_sub_selection} <td></tr> ];
				}
			#	if ($prod_dt{description} ne "") {
			#		$str .= $prod_dt{description};
			#	}
				# add details:
				$str .= qq[</table>];
				# add qty bar
				if ($prod_dt->{show_term} > 0) {
					$term = "<small><em>Term=</em></small>".$prod_dt->{term};
				} 
				if ($prod_dt->{show_qty} > 0) {
					$qty = "<small><em>QTY=</em></small>".$prod_dt->{qty};
				}
				if ($prod_dt->{show_shipping} > 0) {
					$ship = "<small><em>Shipping=</em></small>\$".$prod_dt->{shipping}; 	
				}
				if ($prod_dt->{show_nrc} > 0) { 
					$nrc = "<small><em>NRC=</em></small>\$".$prod_dt->{nrc}; 
				}
				if ($prod_dt->{show_mrc} > 0) { 
					$mrc = "<small><em>MRC=</em></small>\$".$prod_dt->{mrc}; 	
				}
				if ($prod_dt->{show_speed} > 0) { 
					$speed = "<small><em>Speed=</em></small>".$prod_dt->{speed}; 	
				}
				#style="border-color:yellow;"
				$str.= qq[ <table width="100%" border="0" class="email-content" >
							<tr><td width="16.5%" align="center">$qty</td><td width="16.5%" align="center">$term</td><td width="16.5%" align="center">$nrc</td>
							<td width="16.5%" align="center">$mrc</td><td width="16.5%" align="center">$ship</td><td width="16.5%" align="center">$speed</td></tr>
							</table>];

				$prod_heading = $prod_dt->{prod_heading};
				$prop_hdr_desc = $prod_dt->{prop_hdr_desc};
				$prod_selection = $prod_dt->{prod_selection};

		} # finished adding products now add promos for this header
		$sth2->finish();
		#--- add promos
					$sql2 = "select 0 as promo_cnt union
					select count(promoInt_iD) as promo_cnt
					from ctl_sbgProposal_promo_interest pint with (nolock)
					inner join ctl_sbgProposal_promotions pros with (nolock) on pros.promoId = pint.promoID
					where pint.pre_id = $pre_id
					and pros.header_id = $hdr_id
					order by 1 desc";
	# $str .= qq[ 732<pre> $sql2 </pre><br>];
			$sth3 = $myDB2->prepare($sql2);
			$sth3->execute();
			$prom_dt = $sth3->fetchrow_hashref();
			$sth->finish();

			$promo_cnt= $prom_dt->{promo_cnt};
			if ($promo_cnt > 0) {
				$str .= qq[<table width="100%" border="0" class="email-content" >
								<tr><td>Limited Time Offers for $prom_dt->{prod_heading}; $prom_dt->{prod_selection}:</td></tr>];
				$sql2 = "select rtrim(pros.promo_name) as promo_name, rtrim(pros.promo_proposal_note) as promo_proposal_note,
					rtrim(pros.promo_disclaimer) as promo_disclaimer
					from ctl_sbgProposal_promo_interest pint with (nolock)
					inner join ctl_sbgProposal_promotions pros with (nolock) on pros.promoId = pint.promoID
					where pint.pre_id = $pre_id
					and pros.header_id = $hdr_id";
	# $str .= qq[ 375<pre> $sql2 </pre><br>];
		$sth3 = $myDB2->prepare($sql2);
		$sth3->execute();
		while ($prom_dt2 = $sth3->fetchrow_hashref) {

				$str .= qq[<tr><td>$prom_dt2->{promo_name} </td></tr>];
				}
				$str.= qq[</table>];
			}

		# done adding promos
		$sth3->finish();
	}
	$sth->finish();
	$str .=qq[</table>];
	return $str;
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub UpdateOCemail (){
	my ($pre_id) = @_;
	my ($str, $insert, $sql ) ;

my $company_name = delim_return($cgi->param('company_name')) ;
my $first_name = ucfirst( delim_return($cgi->param('first_name'))) ;
my $last_name = ucfirst(delim_return($cgi->param('last_name'))) ;
my $email = delim_return($cgi->param('email')) ;
my $noteOC = delim_return($cgi->param('noteOC')) ;
my $btn = EscQuote($cgi->param('btn1')).EscQuote($cgi->param('btn2')).EscQuote($cgi->param('btn3'));
my $install_date = $cgi->param('install_date'); #$main::cgi{install_date};
my $order_number = delim_return($cgi->param('order_number'));

$str = "Updating Information.";

	$sql =  "select createdby_emplid from  ctl_sbg_PreOC with (nolock) where pre_oc_id = $pre_id";
	my $sth = $db->prepare($sql);
	$sth->execute();
	my $data = $sth->fetchrow_hashref();
	$sth->finish();
	my $emplid = $data->{createdby_emplid};
	# update contact info
	$sql =  "update ctl_sbg_PreOC set company_name = '$company_name',
			first_name = '$first_name', last_name = '$last_name', tofield = '$email', personal_note = '$noteOC',
			btn = '$btn', order_number = '$order_number', install_date = CONVERT(datetime, '$install_date')
			where pre_oc_id = $pre_id";
	$sth = $db->prepare($sql);
	$sth->execute();
	$sth->finish();
	#	$str .= '1700 '.$sql.'<br>';

	# update product
	$sql = "delete from ctl_sbg_OC_prod_interest where oc_id = $pre_id";
	#	$str .= '1704 '.$sql.'<br>';
	$sth = $db->prepare($sql);
	$sth->execute();
	$sth->finish();

	my @pl = $cgi->param('productID');
	foreach my $pid (@pl) {

		$sql = "insert into ctl_sbg_OC_prod_interest with (rowlock)(oc_id, productID, last_modified_by, last_modified)
					values ($pre_id,$pid, $emplid, getdate() )";
		$sth = $db->prepare($sql);
		$sth->execute();
		$sth->finish();
		#$str .= '921 '.$sql.'<br>';
	}

return $str;

}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub sendOrderConfirmation {
	
	my ($pre_oc_id) = @_;

	my ($string ,$prodlist, $noteList, $ret );

	my $sql = " select prod.description --, rtrim(ISNULL(email_note,'')) as email_note
				from ctl_sbg_OC_prod_interest oc_int with (nolock)
				inner join ctl_sbgOrderConfirm_product prod with (nolock) on prod.productID = oc_int.productID
				where oc_int.oc_id = $pre_oc_id
				order by prod.item_order";
	my $sth = $db->prepare($sql);
	$sth->execute();

	while (my $dt = $sth->fetchrow_hashref) { 
		if ($dt->{description} ne "") {
			$prodlist .= qq[ <tr><td>&bull;$dt->{description}</td></tr>];
		}
	}

	$sql = "select distinct rtrim(ISNULL(email_note,'')) as email_note
				from ctl_sbg_OC_prod_interest oc_int with (nolock)
				inner join ctl_sbgOrderConfirm_product prod with (nolock) on prod.productID = oc_int.productID
				where oc_int.oc_id = $pre_oc_id";
	$sth = $db->prepare($sql);
	$sth->execute();

	while (my $dt2 = $sth->fetchrow_hashref) { 
		if ($dt2->{email_note} ne "") {
			$noteList .= qq[ <tr><td>$dt2->{email_note}</td></tr>];
		}
	}
	my $sql2 = "select convert(varchar, date_created,101) as dt ,datepart(yyyy,getdate()) as year , rtrim(first_name) as first_name, rtrim(btn) as btn,legacy,
				rtrim(last_name) as last_name,	rtrim(company_name) as company_name, RTRIM(tofield) as tofield, createdby_emplid as emplid,source_id,
					rtrim(order_number) as order_number, convert(varchar,install_date, 101) as install_date,  rtrim(personal_note) as personal_note
				from ctl_sbg_PreOC with (nolock)
				where pre_oc_id =  $pre_oc_id";

	$sth = $db->prepare($sql2);
	$sth->execute();
	my $dt3 = $sth->fetchrow_hashref();
	$sth->finish();

	my $year = $dt3->{year};
	my $company_name = $dt3->{company_name};
	my $first_name = $dt3->{first_name};
	my $last_name = $dt3->{last_name};
	my $tofield = $dt3->{tofield};
	my $source_id = $dt3->{source_id};
	my $btn = $dt3->{btn};
	my $order_number = $dt3->{order_number};
	my $install_date = $dt3->{install_date};
	my $emplid = $dt3->{emplid};
	my $legacy = $dt3->{legacy};
	my $personal_note = $dt3->{personal_note};
	my $cdate =  $dt3->{dt};

	my $sql3 = "";
	if ($source_id == 2) {
		$sql3 = " select 2 as source_id, cuid as cuid, SAP_ID as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail , 
					case when isnull(work_phone,'') = '' then ''
						when isnull(work_phone,'') = '0000000000' then ''
						else SUBSTRING ( work_phone ,1 , 3 )+'-'+SUBSTRING ( work_phone ,4 , 3 )+'-'+SUBSTRING ( work_phone ,7 , 4 )end  as work_phone
				from qwesthr with (nolock) where convert( int, emplid ) = $emplid";
	}
	else {
			$sql3 = " select 0 as source_id, cuid as cuid, '' as sap_id, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail,
						'' as work_phone
						from ctl_floaters with (nolock) where floater_id = $emplid ";
	}

	$sth = $db->prepare($sql3);
	$sth->execute();
	my $emp_dt = $sth->fetchrow_hashref();
	$sth->finish();

	my $emp_email = $emp_dt->{empEmail};
	my $SAP_ID = $emp_dt->{SAP_ID};
	my $cuid = $emp_dt->{cuid};
	my $wk_phone = $emp_dt->{work_phone};
	if ($wk_phone eq "") {
		$wk_phone = $emp_email;
	}


	$string = qq[ <html><link type="text/css" href="../assets/css/style.css" rel="stylesheet" title="print" media="screen" />
		<head></head> <body > <div id="layout"> <div id="layout-header">
		<img src="../assets/img/logo-centurylink.png" width="242px">
		</div><!--END LAYOUT-HEADER-->
		<table width="90%" border="0" class="form-table" align="right">
	<tr> <td align="left">$cdate</td> </tr>
	<tr> <td align="left"><b> $first_name $last_name </b></td> </tr>
	<tr> <td align="left"><b> $company_name  </b></td> </tr>
	<tr> <td align="left"><b>  $tofield </b></td> </tr>
	<tr> <td align="left">Dear<b> $first_name $last_name</b>,</td> </tr>
	<tr> <td align="left">Thank you for choosing CenturyLink for your business services.</td></tr>
	<tr><td>Your order is being processed.  Please review a summary of your order below.</td></tr>
	<tr><td>Billing Telephone Number:  $btn<br><small><em>(Phone numbers are not guaranteed until installation is completed.)</td></tr>
	<tr><td>Order Number:  $order_number </td></tr>
	<tr><td> Installation Date:  $install_date</td></tr>
	<tr><td>Order:  $order_number</td></tr>
		$prodlist];
	if ($noteList ne "") {
		$string .= $noteList ;
	}
	$string .= qq[<tr><td>$personal_note</td></tr><tr><td>Thank you for choosing CenturyLink.</td></tr></table>
					</div>
					</body>
					</html>];


	$sql = "insert into ctl_sbgOrderConfirmEmail (createdby_cuid, createdby_emplid, createdby_source_id, date_created, company_name,
			first_name, last_name, subject, tofield, ccfield, fromfield, longbody, ctype, language_id, legacy)
			values ('$cuid', $emplid, $source_id, getdate(),'$company_name', '$first_name', '$last_name','CenturyLink Order Confirmation','$tofield',
			'$emp_email', '$emp_email','$string','text/html',1, $legacy	)";

	$sth = $db->prepare($sql);
	$sth->execute();
	my $dt5 = $sth->fetchrow_hashref();
	$sth->finish();
	my $oc_id = $dt5->{oc_id};
	#		$ret .= '1887 '.$sql;

	$sql = "update ctl_sbg_PreOC set processed = 1 where pre_oc_id = $pre_oc_id";
	$sth = $db->prepare($sql);
	$sth->execute();
	$sth->finish();

	$sql = "insert into ccimail (client_id, program_id,date_created, subject, tofield, ccfield, fromfield, longbody, ctype)
					values (50,447, getdate(), 'CenturyLink Order Confirmation','$tofield','$emp_email','$emp_email','$string','text/html')";
	$sth = $db->prepare($sql);
	$sth->execute();
	$dt5 = $sth->fetchrow_hashref();
	$sth->finish();
	my $ccimail_id = $dt5->{ccimail_id};
		#$ret .= $sql3;
	$sql = "update ctl_sbgOrderConfirmEmail set ccimail_id = $ccimail_id ,processed = 1 where oc_id = $oc_id";
	$sth = $db->prepare($sql);
	$sth->execute();
	$sth->finish();
		$ret  .= '<br>Your Order Confirmation Email was sent successfully.<br>';
	

		return $ret;


}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub UpdateContactForProposal {
	
	my ($preProposal_id) = @_;

my $company_name = delim_return($cgi->param('company_name')) ;
my $first_name = ucfirst( delim_return($cgi->param('first_name'))) ;
my $last_name = ucfirst(delim_return($cgi->param('last_name'))) ;
my $email = delim_return($cgi->param('email')) ;
#my $proposal_note = delim_return($main::cgi{proposal_note}) ;
my $edit_personal_note = delim_return($cgi->param('edit_personal_note')) ;

	my $str = 'Fields Updated.';

	my $sql = "	update ctl_sbg_PreProposal set
		company_name =  '$company_name',
		first_name = '$first_name',
		last_name = '$last_name',
		tofield = '$email',
		personal_note = '$edit_personal_note'
		where pre_id = $preProposal_id ";
	my $sth = $db->prepare($sql);
	$sth->execute();
	$sth->finish();
	
	$str.= $sql ;
	return $str;

}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub  getProposalbody {
	my ($preProposal_id) = @_;
	my $promo_disclaimer = '';
	my $prod_disclaimer = '';
	my $hdr_prod_disclaimer = '';

	my ($mrc, $nrc, $ship, $term, $qty,$speed, $hdr_id, $sql2, $promo_cnt, $mn_sql, $sql, $pdf_link, $productID, $sth2) ;
	my ($prod_heading,  $prop_hdr_desc, $prod_selection, $addNote, $activation)=('','','','','');

	my $propbody ='';
	#my $propbody = qq[ <table width="100%" border="2" class="form-table" style="border-color:blue;padding:5px;" >];

	$sql = "select language_id, legacy  from ctl_sbg_PreProposal with (nolock) where pre_id = $preProposal_id";
	my $sth = $db->prepare($sql);
	$sth->execute();
	my $hdr_dt = $sth->fetchrow_hashref();
	$sth->finish();

	my $language_id = $hdr_dt->{language_id};
	my $legacy = $hdr_dt->{legacy};
	my $clause = "";
if ($language_id == 2) { #spanish
	if ($legacy == 1) {  #qwest
		$clause = "and LQ_spanish = 1 ";
	}
	elsif ($legacy == 2) {
		$clause = "and LCTL_spanish = 1 ";
	}
}
else { #language is english
	if ($legacy == 1) {  #qwest
		$clause = "and LQ_english = 1 ";
	}
	elsif ($legacy == 2) {
		$clause = "and LCTL_english = 1 ";
	}
}

	$mn_sql = "select  distinct header_id, prod_heading , hdr.hdr_order ,
				case when ISNULL(hdr_disclaimer,'')='' then 0 else 1 end as hasHdrDis
				from ctl_sbg_Proposal_prod_interest pint with (nolock)
				inner join ctl_sbgProposal_product prod with (nolock) on prod.productId = pint.productID
				inner join ctl_sbgProposal_header hdr with (nolock)on hdr.description = prod.prod_heading
				where pre_id = $preProposal_id
				and isnull(hdr.is_LQ,0) = isnull(prod.is_LQ,0)
				and isnull(hdr.is_LCTL,0) = isnull(prod.is_LCTL,0)
				order by hdr.hdr_order";
#		$propbody .= qq[<tr><td>993<pre> $mn_sql </pre></td></tr>];

	$sth = $db->prepare($mn_sql);
	$sth->execute();

	while (my $hdr_dt = $sth->fetchrow_hashref) {
		$hdr_id = $hdr_dt->{header_id};
		# set to blanks
			($prod_heading ,$prop_hdr_desc ,$prod_selection, $addNote)=('','','','');
			if ( $hdr_dt->{hasHdrDis} > 0) {
					$hdr_prod_disclaimer .= getHdrProdDisclaimer ($hdr_id);
					#$hdr_prod_disclaimer .= '<br>';
				}

		$sql = "select pint.productID, prod_notes, header_id, ltrim(rtrim(proposal_note)) as prod_proposal_note, 
				prod_heading, prod_selection, 
				case when prod_sub_selection = 'Main Prod' then prod_selection else prod_sub_selection end as prod_sub_selection,
				prod.description, ltrim(rtrim(prop_hdr_desc)) as prop_hdr_desc,isnull(prod_note_line,'') as prod_note_line,
				isnull(show_mrc,0) as show_mrc, isnull(show_nrc,0) as show_nrc,isnull(show_shipping,0) as show_shipping,
				ISNULL(show_qty,0) as show_qty, ISNULL(show_term,0) as show_term,ISNULL(show_speed,0) as show_speed,
				case when (isnull(show_mrc,0)= 1) then isnull(pint.mrc,0) else -1 end as mrc,
				case when (isnull(show_nrc,0)=1) then isnull(pint.nrc,0) else -1 end  as nrc,
				case when (isnull(show_shipping,0)=1) then isnull(pint.shipping,0) else 0 end  as shipping,
				case when (isnull(show_term,0)=1) then isnull(pint.term,0) else 'Not Selected' end  as term,
				case when (isnull(show_qty,0)=1) then isnull(pint.qty,0) else 0 end  as qty,
				case when (isnull(show_speed,0)=1) then isnull(pint.speed,'') else '' end  as speed
				from ctl_sbg_Proposal_prod_interest pint with (nolock)
				inner join ctl_sbgProposal_product prod with (nolock) on prod.productId = pint.productID
				inner join ctl_sbgProposal_header hdr with (nolock)on hdr.description = prod.prod_heading
				where pre_id = $preProposal_id
				and hdr.header_id = $hdr_id
				and isnull(hdr.is_LQ,0) = isnull(prod.is_LQ,0)
				and isnull(hdr.is_LCTL,0) = isnull(prod.is_LCTL,0)
				order by item_order ";

#		$propbody .= qq[<tr><td>1028<pre> $sql </pre></td></tr>];
		$sth2 = $myDB2->prepare($sql);
		$sth2->execute();

		while (my $prop_dt = $sth2->fetchrow_hashref) {
			($mrc, $nrc, $ship, $term, $qty,$speed) = (0,0,0,'',0,'');
			$productID = $prop_dt->{productID};
			if ($prod_heading ne $prop_dt->{prod_heading}) {
				$propbody .=  qq[ <tr><td style="height:5px;" ><hr></td></tr>
									<tr><td><h4> $prop_dt->{prod_heading} </h4>];
				if ($prop_hdr_desc ne $prop_dt->{prop_hdr_desc} ) {
					#$propbody .= '<p>'.$prop_dt{prop_hdr_desc}.'</p>';
					$propbody .= qq[$prop_dt->{prop_hdr_desc}];
				}
				$propbody .= qq[ </td></tr>];
			}
$propbody .= qq[<tr><td valign="top" align="left" >];
# style="border-color:blue;"
$propbody .= qq[ <table width="80%" border="0" >]; # class="form-table"
#		$propbody .= qq[<br> 1043 set val of prod_selection = $prod_selection ; incoming val of prod_selection = $prop_dt{prod_selection} <br>];
			if ($prod_selection ne $prop_dt->{prod_selection}) {
			# taking this off per CL-1135
			#$propbody .= qq[<tr><td colspan="4"> $prop_dt{prod_selection}</td></tr>];
			$propbody .= qq[<tr><td colspan="4"> $prop_dt->{prod_proposal_note} </td></tr>];
			}
			if ($prop_dt->{prod_sub_selection} ne "") {
				$propbody .= qq[<tr><td colspan="4">&nbsp;$prop_dt->{prod_sub_selection}:</td></tr> ];
			}
			if ($prop_dt->{description} ne "") {
				if ($prop_dt->{prod_note_line} ne "") {
					$addNote = "<small class=\"orange\"><em>Priced below per line or service</em></small>";
				}
				$propbody .= qq[<tr><td colspan="4">&nbsp; $prop_dt->{description}];
				if ($prop_dt->{show_speed} > 0 && $prop_dt->{speed} ne "" ) {
					$propbody .= qq[ $prop_dt->{speed}];
				}
				$propbody .= qq[ $addNote </td></tr>];
			}
		#	$propbody .= '<tr><td width="50%"><table width="100%" border="1" class="form-table" style="border-color:red;">';
			# add details:
			#$propbody .= '<br>&nbsp;&nbsp;Order Details:<br> ';
			if ($prop_dt->{prod_selection} eq "Modem Purchase Option") { $activation = "Purchase"; }
			elsif ($prop_dt->{prod_sub_selection} eq "Modem Purchase Option") {$activation = "Purchase"; }
			else {$activation = "Activation Charge";}
		#	if ($prop_dt{show_speed} > 0) 
		#		{ $propbody .= '<tr><td width="25%">&nbsp;</td><td width="25%" align="left">&bull;'.$prop_dt{speed}.'</td><td width="50%" align="left">Speed</td></tr>'; 	}
			if ($prop_dt->{show_term} > 0) 
				{ $propbody .= qq[ <tr><td width="15%">&nbsp;</td><td width="15%"align="left">&bull; $prop_dt->{term} </td><td width="30%" align="left">Term Commitment</td><td width="40%">&nbsp;</td></tr>]; }
			if ($prop_dt->{show_qty} > 0 && $prop_dt->{qty} > 0) 
				{ $propbody .= qq[<tr><td width="15%">&nbsp;</td><td width="15%"align="left">&bull; $prop_dt->{qty} </td><td width="30%" align="left">Quantity (priced per unit)</td><td width="40%">&nbsp;</td></tr>]; }
			if ($prop_dt->{show_shipping} > 0) 
				{ $propbody .= qq[<tr><td width="15%">&nbsp;</td><td width="15%"align="left">&bull; \$$prop_dt->{shipping} </td><td width="30%" align="left">Shipping Charge</td><td width="40%">&nbsp;</td></tr>]; }
			if ($prop_dt->{show_nrc} > 0 && $prop_dt->{nrc}> 0 ) 
				{ $propbody .= qq[<tr><td width="15%">&nbsp;</td><td width="15%"align="left">&bull; \$$prop_dt->{nrc}</td><td width="30%" align="left">$activation</td><td width="40%">&nbsp;</td></tr>]; }
			if ($prop_dt->{show_mrc} > 0) 
				{ $propbody .= qq[<tr><td width="15%">&nbsp;</td><td width="15%"align="left">&bull; \$$prop_dt->{mrc}</td><td width="30%" align="left">Monthly Recurring Charge</td><td width="40%">&nbsp;</td></tr>]; }


			$prod_heading = $prop_dt->{prod_heading};
			$prop_hdr_desc = $prop_dt->{prop_hdr_desc};
			$prod_selection = $prop_dt->{prod_selection};
			#$prod_disclaimer .= $prop_dt{prod_disclaimer};
			
	#			$sql2 = "select ";

			#	$propbody .= '</table></td><td width="50%">&nbsp;</td></tr></table>';
			$propbody .= qq[</table></td></tr>];

		} # finished adding products now add promos for this header
			$sth2->finish();

		# add disclaimers for the prods
		#		$propbody .= qq[<tr><td>1095 calling prod disc  $preProposal_id, $hdr_id </td></tr>];

		
			$sql2 = "select 0 as promo_cnt union
					select count(promoInt_iD) as promo_cnt
					from ctl_sbgProposal_promo_interest pint with (nolock)
					inner join ctl_sbgProposal_promotions pros with (nolock) on pros.promoId = pint.promoID
					where pint.pre_id = $preProposal_id
					and pros.header_id = $hdr_id
					order by 1 desc";
#	 $propbody .= qq[<tr><td> 1103<pre> $sql2 </pre></td></tr> ];
			$sth = $db->prepare($sql2);
			$sth->execute();
			my $prom_dt = $sth->fetchrow_hashref();
			$sth->finish();

			$promo_cnt= $prom_dt->{promo_cnt};
			if ($promo_cnt > 0) {
				$propbody .= qq[ <tr><td><p><b>Limited Time Offers for $prom_dt->{prod_heading}</p></b></td></tr>];
				#					<tr><td><p>$prop_dt{prod_selection}:</p></td></tr>];
				$sql2 = "select rtrim(pros.promo_name) as promo_name, rtrim(pros.promo_proposal_note) as promo_proposal_note,
					rtrim(pros.promo_disclaimer) as promo_disclaimer
					from ctl_sbgProposal_promo_interest pint with (nolock)
					inner join ctl_sbgProposal_promotions pros with (nolock) on pros.promoId = pint.promoID
					where pint.pre_id = $preProposal_id
					and pros.header_id = $hdr_id";
#	 $propbody .= qq[<tr><td> 1117<pre> $sql2 </pre></td></tr>];
				$sth2 = $myDB2->prepare($sql);
				$sth2->execute();

				while ($prom_dt = $sth2->fetchrow_hashref) {
				#$propbody .= '<br><b>'.$prom_dt{promo_name}.'</b>';
				$propbody .= qq[ <tr><td>$prom_dt->{promo_proposal_note}</td></tr>];
				if ($prom_dt->{promo_disclaimer} ne "") {
					$propbody .='<br><small><font color="black">Disclaimer:'.$prom_dt->{promo_disclaimer}.'</font></small>';
				}
			#	$disclaimer = '<br>'.$prom_dt{promo_disclaimer};
				}
				$sth2->finish();
			}
			#finished adding promos add sell sheets
	#----
	#----
	} 
	$sth->finish();

	# add universal promos
#-------------------------------------
		$propbody .= qq[<tr><td style="height:5px;" ><hr></td></tr>]; #</td></tr>
		#$prod_disclaimer .= getProdDisclaimer ( $preProposal_id, $productID, $myDB2);
		$prod_disclaimer .= getProdDisclaimer ( $preProposal_id );
		return ($propbody , $promo_disclaimer, $prod_disclaimer, $hdr_prod_disclaimer) ;

}
#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub getProdDisclaimer {
	#my ( $preProposal_id, $productID, $dbh) = @_;
	my ( $preProposal_id ) = @_;
	my ( $pd );
my $q = "select distinct ISNULL(RTRIM(prod_disclaimer),'') as prod_disclaimer
				from ctl_sbg_Proposal_prod_interest pint with (nolock)
				inner join ctl_sbgProposal_product prod with (nolock) on prod.productId = pint.productID
				inner join ctl_sbgProposal_header hdr with (nolock)on hdr.description = prod.prod_heading
				where pre_id = $preProposal_id
				and isnull(hdr.is_LQ,0) = isnull(prod.is_LQ,0)
				and isnull(hdr.is_LCTL,0) = isnull(prod.is_LCTL,0)
				and  ISNULL(prod_disclaimer,'')<>''";
#	my $q ="select ISNULL(RTRIM(prod_disclaimer),'') as prod_disclaimer from  ctl_sbgProposal_product prod with (nolock) where productId = $productID";
	my $sth = $db->prepare($q);
	$sth->execute();
	while (my $hdr_dt = $sth->fetchrow_hashref) {
		$pd = $hdr_dt->{prod_disclaimer};
		if ($pd ne "") { $pd.='<br>'; 	}
	}
	$sth->finish();

	return $pd;
	
}

#------------------------------------------------------------------------------------------------------------------------------------------------------------
sub sendFinalProposal {
	
	my ($pre_id) = @_;

	my $str = '';
	my $errorFlag = 0;

my ($proposal_body, $promo_disclaimer, $prod_disclaimer, $hdr_prod_disclaimer) = getProposalbody ($pre_id);

if ($promo_disclaimer ne "") {
	$promo_disclaimer = '<b>Promotion Disclaimers:</b><br>'.$promo_disclaimer;
}
if ($hdr_prod_disclaimer ne "") {
	$hdr_prod_disclaimer = '<br><b>Product Disclaimers:</b><br>'.$hdr_prod_disclaimer;
}
elsif ($prod_disclaimer ne "") {
	$prod_disclaimer = '<br><b>Product Disclaimers:</b><br>'.$prod_disclaimer;
}

=head
	if ($hdr_prod_disclaimer ne "") {
		$hdr_prod_disclaimer = '<tr><td>'. $hdr_prod_disclaimer.'</td></tr>';
	}
	if ($prod_disclaimer ne "") {
		$prod_disclaimer = '<tr><td>'. $prod_disclaimer.'</td></tr>';
	}
	if ($promo_disclaimer ne "") {
		$promo_disclaimer = '<tr><td>'. $promo_disclaimer.'</td></tr>';
	}
=cut
#$promo_disclaimer = $prod_disclaimer.'<br>'.$promo_disclaimer;

#	$hdr_prod_disclaimer .= '<br>'.$promo_disclaimer;

	my $sql = "select convert(varchar, date_created,101) as dt ,datepart(yyyy, getdate()) as year, first_name, last_name,
			convert(varchar,(LTRIM(RTRIM(replace(first_name,char(32),'')))+'_'+LTRIM(RTRIM(replace(last_name,char(32),''))))) as filenm,
			rtrim(company_name) as company_name, tofield, personal_note, 
			rtrim(proposal_note) as proposal_note, createdby_emplid as emplid, language_id, legacy, source_id
			from ctl_sbg_PreProposal pre with (nolock) where pre_id = ?";

	my $sth = $db->prepare($sql);
	$sth->execute($pre_id);
	my $dt = $sth->fetchrow_hashref();
	$sth->finish();

my $prop_date = $dt->{dt};
my $company_name = $dt->{company_name};
my $first_name =$dt->{first_name};
my $last_name = $dt->{last_name};
my $tofield = $dt->{tofield};
my $personal_note = $dt->{personal_note};
my $filenm = $dt->{filenm};
my $language_id = $dt->{language_id};
my $leg = $dt->{legacy};
my $emplid = $dt->{emplid};
my $source_id = $dt->{source_id};
my $year = $dt->{year};
my $intro_body = getIntro($company_name);

#$str .= qq[1163<br> $sql2];
my $sql3 = "";
if ($source_id == 2) {
	$sql3 = " select 2 as source_id, SAP_ID as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail , 
			 case when isnull(work_phone,'') = '' then ''
 when isnull(work_phone,'') = '0000000000' then ''
 else SUBSTRING ( work_phone ,1 , 3 )+'-'+SUBSTRING ( work_phone ,4 , 3 )+'-'+SUBSTRING ( work_phone ,7 , 4 )end  as work_phone
 from qwesthr with (nolock) where convert( int, emplid ) = $dt->{emplid}";
}
else {
	$sql3 = "select 8 as source_id, cuid as SAP_ID, RTRIM(first_name)+' '+rtrim(last_name) as empName, RTRIM(email) as empEmail,
				'' as work_phone
			from ctl_floaters with (nolock) where floater_id = $dt->{emplid}";
}
#$str .= qq[1192<br> $sql3 ];
$sth = $db->prepare($sql3);
$sth->execute();
my $emp_dt = $sth->fetchrow_hashref();
$sth->finish();

my $empEmail = $emp_dt->{empEmail};
my $SAP_ID = $emp_dt->{SAP_ID};
my $empName = $emp_dt->{empName};
my $empPhone = $emp_dt->{work_phone};
if ($empPhone eq "") {
	$empPhone = $empEmail;
}

my $end_body = getEnd ( $empName, $empPhone);

my $generalTandC = '<br><b>Terms and Conditions '. $year.' </b>:';
$generalTandC .=getGeneralTandC();
	
	$generalTandC .= $year;
	$generalTandC .= " CenturyLink.  All Rights Reserved. ";


my $actual_email =  qq [ <html><link type="text/css" href="../assets/css/style.css" rel="stylesheet" title="print" media="screen" />
<head></head> <body > <div id="layout"> <div id="layout-header">
<img src="../assets/img/logo-centurylink.png" width="242px">
</div><!--END LAYOUT-HEADER-->
<table width="90%" border="0" class="form-table" align="right">
	<tr> <td align="left">$prop_date</td> </tr>
	<tr> <td align="left"><b> $first_name $last_name </b></td> </tr>
	<tr> <td align="left"><b> $company_name  </b></td> </tr>
	<tr> <td align="left"><b>  $tofield </b></td> </tr>
	<tr> <td align="left">Dear<b> $first_name $last_name</b>,</td> </tr>
	<tr> <td align="left"> $intro_body </td> </tr> $proposal_body <tr> <td align="left"> $end_body </td></tr>
	$hdr_prod_disclaimer
	$prod_disclaimer
	$promo_disclaimer 
	<tr><td>$generalTandC</td></tr>
</table>
</div>
</body>
</html>];

$actual_email = EscQuote($actual_email);


$actual_email =~s/^\s*(\S*)\s*$/$1/;

$hdr_prod_disclaimer =~s/^\s*(\S*)\s*$/$1/;
$prod_disclaimer =~s/^\s*(\S*)\s*$/$1/;
$promo_disclaimer =~s/^\s*(\S*)\s*$/$1/;


$company_name = EscQuote( $company_name);
$first_name = EscQuote( $first_name);
$last_name = EscQuote( $last_name);

my $insert_sql = "insert into ctl_sbgProposal (createdby_cuid, createdby_emplid, date_created, proposal_status_id,
					proposal_status_chng_dt, company_name, first_name, last_name, 
					subject, tofield, ccfield, bccfield, 
					fromfield, longbody, ctype, source_id, 
					language_id, legacy, pre_id)
				values ('$SAP_ID',$emplid, getdate(), 1,
						getdate(), '$company_name','$first_name','$last_name',
						'CenturyLink Small Business Proposal','$tofield','$empEmail','',
						'$empEmail','$actual_email','text/html',$source_id,
						$language_id, $leg, $pre_id )";
# $str .= qq[1237 <pre> $insert_sql </pre>];
$sth = $db->prepare($insert_sql);
$sth->execute();
my $prop_dt = $sth->fetchrow_hashref();
$sth->finish();
my $pro_id = $prop_dt->{proposalID};

#my $html_pdf_name2 = $company_name.'_'.$pro_id.'.html';
#my $link = 'http://smallbizmailtool.perl.ccionline.biz/FinalProposal.cgi?pro_id='.$pro_id ;
#my $htmllink2 = 'http://smallbizmailtool.perl.ccionline.biz'.$html_pdf_name2 ;

#my $htmlFile2 = $html_pdf_name2 ; #'/tmp/'.

#open (PDATA, ">", $htmllink) || die "Could not open file $htmllink"; 

$sql = "select longbody as stuffd from ctl_sbgProposal with (nolock) where proposalID = $pro_id";

$sth = $db->prepare($sql);
$sth->execute();
$dt = $sth->fetchrow_hashref();
$sth->finish();

my $stuffd = $dt->{stuffd};
#$str .= qq[1281<br> $sql2];

#my $html_pdf_name = $first_name.'_'.$last_name.'_'.$pro_id.'.html';
#my $htmllink = 'http://smallbizmailtool.perl.ccionline.biz/tm'.$html_pdf_name ;
#----------------------------
my $filesize = 0;
my $htmlFile = $filenm."_".$pro_id.".html";
#my $fullFile = "$server/sbgemailbuilder/tmp/".$htmlFile;
#my $fullFile ='http://'.$HOST.'/sbgemailbuilder/tmp/'.$htmlFile;
#my $fullFile ='tmp/'.$htmlFile;
my $fullFile ='D:/centurylinkyoucan/sbgemailbuilder/tmp/'.$htmlFile;

# Use the open() function to create the file.
unless(open( FILE, '>>'.$fullFile)){
	# Die with error message 
	# if we can't open it.
	$str .= "Could not open file $fullFile";
}

# Write some text to the file.
#print FILE $stuffd;
my $newP = qq[<html><link type="text/css" href="../assets/css/style.css" rel="stylesheet" title="print" media="screen" />
<head></head> <body > <div id="layout"> <div id="layout-header">
<img src="../assets/img/logo-centurylink.png" width="242px">
</div><!--END LAYOUT-HEADER-->
<table width="90%" border="0" class="form-table" align="right">
	<tr> <td align="left">$pro_id</td> </tr>
	<tr> <td align="left"><b> $first_name $last_name </b></td> </tr>
	<tr> <td align="left"><b> $company_name  </b></td> </tr>
	<tr> <td align="left"><b>  $tofield </b></td> </tr>
	<tr> <td align="left">Dear<b> $first_name $last_name</b>,</td> </tr>
	<tr> <td align="left"> $intro_body </td> </tr>];
my $lastP = qq[<tr><td> $end_body <br><br>$hdr_prod_disclaimer $prod_disclaimer $promo_disclaimer</td></tr>
	<tr><td>$generalTandC</td></tr>
</table>
</div>
</body>
</html>];
$newP =~s/^\s*(\S*)\s*$/$1/;
$proposal_body =~s/^\s*(\S*)\s*$/$1/;
$lastP =~s/^\s*(\S*)\s*$/$1/;

#print FILE $newP.$proposal_body.$lastP;

print FILE $newP;
print FILE $proposal_body;
print FILE qq[<tr><td> $end_body <br><br>$hdr_prod_disclaimer $prod_disclaimer $promo_disclaimer</td></tr>
	<tr><td>$generalTandC</td></tr>
</table>
</div>
</body>
</html>];

#print FILE "start";
#print FILE $proposal_body;
#print FILE "end";

# close the file.
close FILE;
if ((-s $fullFile)+0 == 0) {
	$errorFlag++;
}

$filesize = (-s $fullFile)+0;
my $filesize2 = (-s $htmlFile)+0;
#$str .= '<br> Filesize ='. $filesize.'<br>'; 

#--------------------------------
my $pdf_file  = HTML2PDF($htmlFile);
#UPDATE BELOW for staging to live
#my $pdflink = "$HOST/tmp/".$pdf_file ;
my $pdflink ='http://'.$HOST.'/sbgemailbuilder/tmp/'.$pdf_file;

#my $pdflink = 'http://smallbizmailtool.com/tmp/'.$pdf_file ;
#my $pdf_file2  = HTML2PDF($htmlFile2);
#my $pdflink2 = 'http://smallbizmailtool.perl.ccionline.biz/tmp/'.$pdf_file2 ;
#get email stuff
#-------------------------------------------------
my $sell_sheet_link = '';
my %prop_dt;
my $sell_sheet_url = '';

if ($language_id == 2) { # need spanish pdf
$sql = "	select distinct rtrim(pdf_name) as ps, ISNULL(pdf_spanish,'') as pdflink 
				from ctl_sbgProposal_pdf sbpdf with (nolock) 
				inner join ctl_sbg_Proposal_prod_interest pint with (nolock) on pint.productID = sbpdf.prop_prod_id
				and pint.pre_id  = $pre_id
				where ISNULL(pdf_spanish,'')<>'' ";	
}
else { # need english
$sql = "select distinct rtrim(pdf_name) as ps, ISNULL(pdf_english,'') as pdflink 
				from ctl_sbgProposal_pdf sbpdf with (nolock) 
				inner join ctl_sbg_Proposal_prod_interest pint with (nolock) on pint.productID = sbpdf.prop_prod_id
				and pint.pre_id = $pre_id
				where ISNULL(pdf_english,'')<>'' ";
}

	$sth = $db->prepare($sql);
	$sth->execute();

	while (my $prop_dt = $sth->fetchrow_hashref) {

	#UPDATE BELOW for staging to live
	$sell_sheet_url = 'http://'.$HOST.'/sbgemailbuilder/pdf/'.$prop_dt->{pdflink};
	#$sell_sheet_url = 'http://smallbizmailtool.com/'.$prop_dt{pdflink};
	$sell_sheet_link .= '<br><a href="'.$sell_sheet_url.'">'.$prop_dt->{ps}.'</a>.<br>';
}


 $sql = "select email_subject, email_header, email_body , email_footer
			from email_templates with (nolock)
			where email_purpose_id = 18 and is_active = 1 and client_id = 50";
$sth = $db->prepare($sql);
$sth->execute();
$prop_dt = $sth->fetchrow_hashref();
$sth->finish();
my $emailS = $prop_dt->{email_subject};

#$personal_note .= '<a href="'.$htmllink.'">Click here</a> to read your HTML.<br>';
#$personal_note .= '<a href="'.$htmllink2.'">Click here</a> to read your HTML2.<br>';
$personal_note .= '<br><br>Please <a href="'.$pdflink.'">Click here</a> to read your Proposal.<br>';
#$personal_note .= '<a href="'.$pdflink2.'">Click here</a> to read your PDF2.<br>';
$personal_note .= '<br><br>Learn more about the products offered in your proposal through the links below:<br>'.$sell_sheet_link.'<br><br>';

my $emailB = $prop_dt->{email_header}.$prop_dt->{email_body}. $prop_dt->{email_footer};
	$emailB  =~ s/\$first_name/$first_name/gi;
	$emailB  =~ s/\$last_name/$last_name/gi;
	$emailB  =~ s/\$personal_note/$personal_note/gi;
	$emailB  =~ s/\$empName/$empName/gi;
	$emailB  =~ s/\$empEmail/$empEmail/gi;
	$emailB  =~ s/\$empPhone/$empPhone/gi;
	$emailB  =~ s/\$year/$year/gi;
#	$emailB  =~ s/\$prolink/$link/gi;
	$emailB = EscQuote($emailB);

#$emailB = 'After testing this email will go to: '.$tofield.'<br>'.$emailB;

$emailB = EscQuote($emailB);
my $cc = '';
$cc = $empEmail;
my $cciamildt;
#$tofield = 'james.miroslaw@centurylink.com,janet.brodsky@centurylink.com,maryann.domsch@centurylink.com,scotts@channelmanagement.com,archanak@channelmanagement.com';
#$tofield = 'scotts@channelmanagement.com,archanak@channelmanagement.com';
#--------------------------------------------------------------
	if ( $filesize > 0 ) {
			$sql = "insert into ccimail (client_id, program_id,date_created, subject, tofield, ccfield, fromfield, longbody, ctype)
					values (50, 447,getdate(), '$emailS','$tofield','$cc','$empEmail','$emailB','text/html')";
	#		$sql = "insert into ccimail (client_id, date_created, subject, tofield, ccfield, fromfield, longbody, ctype)
	#				values (50, getdate(), '$emailS','$tofield','$tofield','$empEmail','$emailB','text/html')";
			$sth = $db->prepare($sql);
			$sth->execute();
			$cciamildt = $sth->fetchrow_hashref();
			$sth->finish();

		$str .= '<br>Your Proposal was sent successfully.<br>';
	}
	else {
		$str .= '<br><font color="red">There was error creating and emailing your Proposal.<br>We apologize for the inconvenience, please create a new proposal.</font><br>';
	}

	return $str;
	
}

###################################################################################################################################
#-------------------------------------------------------------------------------------------------------
sub UpdateProductsForProposal {
	my ($pre_id, $emplid) = @_;
my ($nrc_name, $mrc_name,$term_name,$speed_name, $ship_name, $qty_name)  ;
my ($nrc, $mrc, $term, $speed, $ship, $prod_note, $qty, $insert, $str);
	my $sql = "delete from ctl_sbg_Proposal_prod_interest where pre_id = $pre_id";
	my $sth = $db->prepare($sql);
	$sth->execute();
	$sth->finish();

	#$str.=$sql.'<br>';
	$sql = "delete from ctl_sbgProposal_promo_interest where pre_id = $pre_id";
	$sth = $db->prepare($sql);
	$sth->execute();
	$sth->finish();
	#$str.=$sql.'<br>';

#products 
my @pl = $cgi->param('productID');
	foreach my $pid (@pl) {
		$nrc_name =  'nrc_'.$pid ; 
		$mrc_name = 'mrc_'.$pid ;
		$term_name =  'term_'.$pid ;
		$speed_name = 'speed_'.$pid ;
		$ship_name = 'ship_'.$pid;
		$qty_name = 'qty_'.$pid;
		
		if ($cgi->param($nrc_name) eq "NRC" || $cgi->param($nrc_name) eq "-1") {
			$nrc = 0;
		}
		else {
			$nrc = $cgi->param($nrc_name);
		}
		if ($cgi->param($mrc_name) eq "MRC" || $cgi->param($mrc_name) eq "-1") {
			$mrc = 0;
		}
		else {
			$mrc = $cgi->param($mrc_name);
		}
		if ($cgi->param($qty_name) eq "QTY" || $cgi->param($qty_name) eq "-1") {
			$qty = 0;
		}
		else {
			$qty = $cgi->param($qty_name);
		}
		if ($cgi->param($ship_name) eq "Shipping" || $cgi->param($ship_name) eq "-1") {
			$ship = 0;
		}
		else {
			$ship = $cgi->param($ship_name);
		}
		#term
		if ($cgi->param($term_name) eq "-Select Term-" || $cgi->param($term_name) eq "-1") {
			$term = 0;
		}
		else {
			$term = $cgi->param($term_name);
		}
		#speed
		if ($cgi->param($speed_name) eq "-Select Speed-" || $cgi->param($speed_name) eq "-1") {
			$speed = "";
		}
		else {
			$speed = $cgi->param($speed_name);
		}

		$insert = "insert into ctl_sbg_Proposal_prod_interest 
					(pre_id, productID,  mrc, 
					nrc, speed, term, prod_note, last_modified_by, last_modified, shipping, qty)
					values ($pre_id, $pid,  $mrc, $nrc, '$speed',
							'$term', '$prod_note',$emplid, getdate(),$ship, $qty )";
		$sth = $db->prepare($sql);
		$sth->execute();
		$sth->finish();

		#$str .= $insert.'<br>';
	}

 @pl = $cgi->param('promoID');
	foreach my $promo_id (@pl) {
		$insert = "insert into ctl_sbgProposal_promo_interest 
					(pre_id, promoID, last_modified_by, last_modified)
					values ($pre_id, $promo_id,$emplid, getdate())";
		$sth = $db->prepare($sql);
		$sth->execute();
		$sth->finish();
		#$str .= $insert.'<br>';
	}
	
	return $str;
}

#-------------------------------------------------------------------------------------------------------
sub getIntro {
	my ($comp_name) = @_;
	my $str = "More than 500,000 companies rely on CenturyLink to help their business thrive. Our best&ndash;in&ndash;class network allows us to offer a broad range of communication solutions designed with the needs of a wide variety of small businesses in mind. We&rsquo;re confident our solutions will meet your business&rsquo;s unique needs. 
	<br>The following proposal has been created exclusively for <b>$comp_name</b>.";

	return $str;
}
#-------------------------------------------------------------------------------------------------------
sub getEnd {
	my ($empName, $wp, $disclaimer) = @_;
	my $str = "Thank you for taking the time to tell us more about your business. 
	We appreciate the opportunity to present this proposal. Please do not hesitate to contact us with any questions.<br><br>
	Best regards,<br> <b>$empName <br> $wp </b><br>";

	return $str;
}
#-------------------------------------------------------------------------------------------------------
sub getGeneralTandC {
	my $str = " Rates and offers expire 1/31/2015, unless otherwise noted. This proposal contains CenturyLink proprietary and confidential information. It is not to be disclosed outside of your employees, nor is it to be duplicated, used, or disclosed, in whole or in part, for any purpose other than to evaluate this proposal. Any changes to the service offerings will result in changes to the rates offered. Offers may not be combined.
<b>General</b> &ndash; Services not available everywhere. Business customers only. CenturyLink may change or cancel services or substitute similar services at its sole discretion without notice. 
	Offer, plans and stated rates are subject to change and may vary by service area. Requires credit approval and deposit may be required. 
	<b>Taxes, Fees and Surcharges</b> &ndash; All prices exclude taxes, fees and surcharges, which apply to all services, and include federal and state-mandated and permitted charges, cost recovery charges, state and local fees that vary by area, and certain in-state surcharges. 
	Cost recovery fees are not taxes or government-required charges for use. 
	Additional charges apply depending on services selected, including a carrier Universal Service charge, a federal regulatory recovery fee and property tax fee, a one-time High-Speed Internet activation fee, a one-time voice service activation fee, extended area service charges, monthly zone increment charges, and connection fees. 
	Taxes, fees, and surcharges apply based on standard monthly, not promotional, rates. 
	<b>Terms and Conditions</b> &ndash; All products and services are governed by tariffs, terms of service, or terms and conditions posted at http://www.centurylink.com/Pages/AboutUs/Legal/. 
	Products and services are provided by the CenturyLink operating company serving your service location. 
	<b>Monthly Rate</b> &ndash; Monthly rate applies while customer subscribes to all qualifying services. 
	If one or more services are cancelled, the standard monthly rate or rate defined in the tariffs/terms and conditions will apply to each remaining service. 
	<b>Discounts and Credits</b> &ndash; All applicable discounts and credits will be applied beginning in the first or second full month of billing.<br> 
	&reg; ";
	

	return $str;
}
#-------------------------------------------------------------------------------------------------------
sub dropOrderConfirmation {
	
	my ($pre_oc_id) = @_;

	my $str = '<br>Your Order Confirmation was not sent.<br>';

	my $sql = "update ctl_sbg_PreOC set processed = 0 where pre_oc_id = $pre_oc_id";
	my $sth = $db->prepare($sql);
	$sth->execute();
	$sth->finish();

	return $str;


}
#-------------------------------------------------------------------------------------------------------
sub get_header
{

	my %hash  = @_;
	my $title = $hash{title} || '';
	my $css   = $hash{css} || '';
	my $more  = $hash{more} || '';

	$css = "<link rel=\"stylesheet\" href=\"$css\" type=\"text/css\">\n" if $css;

	#my $str = "Content-type: text/html\n\n";
	my $str .= <<EOF;
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

EOF
	return $str;
}

1;

=head
=cut