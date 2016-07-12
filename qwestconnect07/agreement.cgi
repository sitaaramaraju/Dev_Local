use strict;
use CGI::Carp qw/ fatalsToBrowser /;
use cgi::cookie;
use CCICryptography;
use CGI qw(:standard);
my $cgi = CGI->new();
#print $cgi->header("text/html");
 my $cci_id = $cgi->param('cci_id')||'';

my $server ="";
my $HOST = $ENV{HTTP_HOST};
if ($ENV{HTTP_HOST} eq 'centurylinkyoucandev.com') {
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'youcanuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnectuat.ccionline.biz'){
    $server = "D:/centurylinkyoucan";
	$server = "/centurylinkyoucan";
}
elsif ($ENV{HTTP_HOST} eq 'centurylinkconnect.com'){
    $server = "D:/centurylinkyoucan";
}
else {
    $server = "D:/centurylinkyoucan";
	#$server = "/centurylinkyoucan";
}

#require "$server/cgi-bin/init.cgi";
require "$server/qwestconnect07/subs.cgi";
#my $url = "centurylinkyoucandev.com/index_lmsii07.cgi";
my $url = CCICryptography::getUrl_sites('lms');

############## validation ################
my $valid = 0;
my ($s, $e) = (0,0);
if ($cci_id ne "") {
	$valid =  CCICryptography::validate_CL_sites($cci_id,'lms');
	($s, $e) = CCICryptography::getEmpid($cci_id); 
}
else {
	$valid = 1;
}

if ($valid <= 0) {
  headernocss();
  print qq[
  <form name="lead" action="" method="post">
  <input type="hidden" name="session_id" value="0">
    <script language='javascript'>
      alert("There was an error loading the page.  Please log in and try again.");
      document.lead.action='$url';
      document.lead.submit();
    </script>
  </form>
 </body>
</html>];
exit();

}


my  $PAGETITLE = 'CenturyLink Connect';
my $css = 'style.css';
my $header = get_header(  # init.cgi new improved header
        'title' => $PAGETITLE,
        'css'   => 'style.css',
    );
#print $header;
my $special = $cgi->param('special');

#<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />


print qq[
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>$PAGETITLE</title>
<script language="JavaScript" src="qwestconnect07menus.js"></script>
<script language="JavaScript" src="validate.js"></script>
<link href="Style.css" rel="stylesheet" type="text/css" />
<script language="JavaScript" src="mm_menu.js"></script>
</head>

<body onload="MM_preloadImages('images/Sub_nav_home_on.gif','images/Sub_nav_about_on.gif','images/Sub_nav_faq_on.gif','images/Sub_nav_contact_on.gif','images/Sub_nav_Products_on.gif')">
<script language="JavaScript1.2">mmLoadMenus();</script>
<table width="954" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td>
];
getHeader($cci_id, $s, $e);

print qq[	
	</td>
      </tr>
      <tr>
        <td width="954" height="9" align="left" valign="top"><img src="images/topBumper.gif" width="954" height="9" /></td>
      </tr>
      <tr>
        <td background="images/background.gif"><table width="913" border="0" align="center" cellpadding="0" cellspacing="0">
          <tr>
            <td align="left" valign="top"><img src="images/Sub_titleTop.gif" width="913" height="16" /></td>
          </tr>
          <tr>
            <td background="images/Subtitle_tile.gif"><table width="900" border="0" cellspacing="1" cellpadding="1">
              
];


if ($special eq "BAU") {

print qq[
			
<tr>
                <td width="10">&nbsp;</td>
                <td align="left" valign="top" class="BlueTitles">CenturyLink&reg; Retail Referral Rewards Program Agreement </td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td align="left" valign="top"><img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
          </tr>
          <tr>
            <td align="left" valign="middle" background="images/Sub_tile.gif"><table width="900" border="0" cellspacing="1" cellpadding="1">
              <tr>
                <td width="10" align="left" valign="top">&nbsp;</td>
                <td><table width="650" border="0" align="center" cellpadding="1" cellspacing="1">
					<tr>
                    <td><span class="BlueTitles">CenturyLink&reg; Retail Referral Rewards Program Agreement</br> Effective May 20, 2016</span><br />
                      <br />
					
                     <table width="600" border="0" cellspacing="3" cellpadding="3">
						<tr>
                          <td align="left" valign="top" class="FAQuestions">Eligible Participants who participate in the CenturyLink Retail Referral Rewards Program (the &ldquo;Program&rdquo;) are required to read, understand and accept this Agreement supporting the Program, particularly as they relate to ethical sales practices. CenturyLink reserves the right to revise the Program, Service eligibility, Participant eligibility, rewards, or cancel the Program at any time, without notice, and without any liability or obligation to any Participant.
						 </td>
                          </tr>
						  <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">General Provisions and Definitions</span></td>
                          </tr>						  
						<tr>
                          <td align="left" valign="top" class="FAQuestions">This agreement (&ldquo;Agreement&rdquo;) is made between CenturyLink Service Group, LLC (&ldquo;CenturyLink&rdquo;) and the individual or entity (collectively, &ldquo;Participant&rdquo;, &ldquo;you&rdquo;, or &ldquo;your&rdquo;) who completes the registration process to participate in the Program. This Agreement establishes the non&ndash;exclusive terms and conditions under which you shall register as a sales lead program participant with CenturyLink for the purpose of identifying and submitting a &ldquo;Lead Referral&rdquo; (as defined hereafter) to CenturyLink for compensation. The Agreement term will begin on the date you complete the registration Process for the Program and will continue until either you or CenturyLink terminates the relationship as described in this Agreement. Participants agree that there is no employer&ndash;employee relationship, joint venture, partnership or agency created by this Agreement. You have no authority to act for, or on behalf of CenturyLink and are not authorized to bind CenturyLink in any manner whatsoever.
						 </td>
                        </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">As used herein, a &ldquo;Lead Referral&rdquo; shall refer to a sales lead provided by you to CenturyLink which you submit to CenturyLink via the website designated by CenturyLink, using a completed &ldquo;Lead Referral Form&rdquo; which identifies a prospective customer (&ldquo;Prospective Customer&rdquo;) who might be interested in receiving Services from CenturyLink. CenturyLink has no obligation to pursue or take any action on any Lead Referral submitted by you or directly to retail store.
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">As used herein, &ldquo;Services&rdquo; shall refer to those telecommunications and multimedia services and products provided pursuant to CenturyLink&rsquo;s standard service, ordering, and provisioning processes (all CenturyLink products and services shall collectively be referred to as &ldquo;Services&rdquo;). CenturyLink reserves the right to modify, add to or delete Services at its sole option without notice to Participants.
						</td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Eligible Participants</span>
						</td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions">
						 <ol>
							<li>Participants may be an individual or business who meets eligibility requirements described at www.centurylinkconnect.com and completes the enrollment process.</li>
							<li>Business Participants must provide an accurate description of the entity (sole proprietor, partnership, trust, corporation, etc.) and the name of an authorized business to which the compensation will be paid.</li>
							<li>All Participants must meet the following criteria:
								<ol STYLE="list-style-type: lower-alpha;">
								<li>Must provide accurate and complete registration information and complete form W&ndash;9, if required.</li>
								<li>To the extent that Participant is enrolled as an MDU and intends to enter referrals by virtue of its access to residents of a multiple dwelling unit property (&ldquo;MDU&rdquo;), the MDU may not be the subject of a marketing or promotional agreement with CenturyLink or any other provider of voice, video, and data services.</li>
								<li>Participant and those entering referrals on behalf of the Business will avoid any conduct or action that conflicts or appears to conflict with honest, ethical conduct and will not engage in any activity that may be detrimental to CenturyLink&rsquo;s interest, reputation, or goodwill.</li>
								<li>Participant and those entering referrals on behalf of the Business must act in accordance with and not violate this Agreement or CenturyLink policies or rules.</li>
								<li>CenturyLink may declare any individual and any Participant ineligible at any time and terminate their enrollment.</li>
								<li>Current CenturyLink employees, individuals or businesses participating in any other CenturyLink sales, marketing, or related program, including those in CenturyLink Partner programs, and those enrolled in any other CenturyLink program may not enter referrals for any Participant.</li>
								<li>Master agent, subagent, indirect sales representatives of CenturyLink are excluded.</li>
								<li>Residents of a CenturyLink employee’s household are excluded. </li>
								<li>Participants must complete the enrollment process and agree to this Agreement. </li>
							</ol>
							</li>
							</ol>
						 </td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Enrollment</span>
						</td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions">Participants must expressly agree to participate and accept and agree to this Agreement by going online to www.centurylinkconnect.com to enroll in the Program. </td>
						 </tr>
						<tr><td align="left" valign="top" class="FAQuestions">
						<ol>
							<li>Enrollment is not complete until Participant completes the registration form including: CenturyLink Reference Code, name, type of entity (Business), address, phone number, email address, Business name, Employer Name, Employer address, name of authorized individual to whom communications are to be directed.</li>
							<li>Business Participants must provide the type of entity that it is (sole proprietor, partnership, trust, corporation, etc.), and provide the name of the individual, authorized by Participant to act on its behalf in connection with the Program and to whom communications about the Program may be directed. No other individuals will be authorized to act on behalf of the Business Participant in the Program.</li>
						 <li>Business Participants must complete a W&ndash;9 form with an accurate identification number (the identification number is the Federal ID Number used to file federal income tax returns for the business. Tax id must match the Business name used to enroll. </li>
						 </ol>
						 </td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Lead Referral Process Considerations</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">
						<ol>
							<li>Participant must name an individual to whom communications about the program may be directed. That individual and others entering referrals on behalf of Participant must be over the age of 18.</li>
							<li>The prospective customer is the individual or entity responsible for the account, and/or decision maker.</li>
							<li>Participant must ensure that Services are ordered on behalf of the Prospective Customer by an individual with authority to bind the Prospective Customer to such order and that such person provides valid consent for the Participant to submit the order to CenturyLink. The authorized individual will be contacted by CenturyLink to finalize the order and sale of Services. The authorized individual must provide consent to CenturyLink for the order and agree to all terms and conditions associated with the Service, and provide all other information and approvals required by CenturyLink to complete the order and sales of Service.</li>
						 <li>Participants who create a referral are eligible for rewards when the referral closes as a valid, completed sale according to this Agreement. </li>
						 </ol>
						 </td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Products and Marketing</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">
						<ol>
						 <li>Lead Referrals will not be eligible for Program rewards if the Service is already on the Prospective Customer&rsquo;s account, or if the contact results in a decrease of the amount due on the Prospective Customer&rsquo;s monthly CenturyLink invoice. </li>
						 <li>Billing corrections, corrections to Service orders, requests for repair, or any other contact or assistance that does not involve the provision and sale of a new or added Service will not qualify as a referral.</li>
						 <li>Outbound telemarketing and door&ndash;to&ndash;door sales by Participants are strictly prohibited. CenturyLink reserves the right to add other tactics to this restricted list at any time in its sole discretion.  If CenturyLink adds other tactics, it will make reasonable efforts to notify Participants of such changes and will have no liability or obligation to provide rewards or compensation for any Lead Referrals after the effective date of such changes.</li>
						 <li>Only CenturyLink&ndash;approved promotional collateral and information (collectively, &ldquo;Approved Collateral&rdquo;) may be used in creating a referral. You shall make no representations or warranties relating to the Services except as set forth in the Approved Collateral.</li>
						<li>Participants may generally discuss Services, but may never make representations, claims, offers or otherwise characterize any Service, term, condition, tariff, price list, discounts or other matters, except as expressly described and stated in Approved Collateral.</li>
						 <li>Prospective Customers must always be advised that the actual performance, price or other matter affecting a Service, and such information must be confirmed by CenturyLink. </li>
						 <li>Lead Referrals cannot be made for the following Prospective Customers: Businesses, official company service (OCS) orders for CenturyLink owned and operated facilities, political organizations, referrals made by Participants for itself/his/herself, and CenturyLink employees or others where the Services are provided by CenturyLink under a company concession or promotional plan.</li>
						 <li>Participants may not use or have access to any non&ndash;public CenturyLink systems, databases or facilities to identify a Prospective Customer, identify the suitability of a referral, to suggest the availability of a Service, market Services, or any other use.</li>
						 </ol>
						 </td>
						 </tr>
						<tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Program Guidelines and Interpretation</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">Questions regarding this Agreement and its interpretation or any Program disputes should be directed to <a href="mailto:refer.friend\@centurylink.com" target="_top">refer.friend\@centurylink.com</a> or www.centurylinkconnect.com. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">
						<ol>
						 <li>A CenturyLink Sales Center acting on behalf of Program Management must conclude any and every sale of a Service, explaining, as appropriate, the functions, features, price, etc., to the Prospective Customer prior to issuing the order </li>
						 <li>CenturyLink reserves the right to limit the maximum award issued to any Participant in the Program. </li>
						 <li>Two open referrals for the same account or telephone number, for the same Service will be considered duplicate referrals. In the case of a duplicate referral, the first&ndash;received referral will receive the award, if applicable. </li>
						 <li>The actions, resolutions, and determinations of CenturyLink are final and cannot be appealed.</li>
						 </ol>
						 </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Rewards and Redemption</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">CenturyLink agrees to pay Participants for a Lead Referral accepted by CenturyLink after a sales agreement is made between the Prospective Customer and CenturyLink and Service(s) are installed and operational. Award amounts will be determined by CenturyLink in its sole discretion and are subject to change without notice. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">The value of an award made pursuant to the Program is subject to federal and state income tax. Participants are responsible for all applicable taxes, including those directed to an Approved Organization. Participant&rsquo;s tax ID numbers are required for tax reporting purposes and a 1099&ndash;MISC will be issued to Participants earning an annual, cumulative amount of \$600 or more through this program. CenturyLink, acting through the Program Management will make all decisions regarding reward eligibility and issuance. The Program Management is the sole judge in interpreting all provisions, rules, qualifications, awards and any disputes that may arise in the operation of the Program. All of these decisions are final and cannot be appealed. No contract rights are created by the existence of or participation in the Program. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">All Approved Collateral provided by CenturyLink, and CenturyLink&rsquo;s name, trademarks, service marks, label designs, product identifications, artwork, and other symbols and devices associated with this Agreement (collectively, the &ldquo;CenturyLink Marks&rdquo;) are and will remain the property of CenturyLink. You are authorized to use the Approved Collateral and CenturyLink Marks as described by CenturyLink and only with CenturyLink&rsquo;s prior written approval. Your use of the Approval Collateral and the CenturyLink Marks is non&ndash;exclusive, non&ndash;sublicenseable, non&ndash;assignable, and non&ndash;transferable. Your uses of the Approved Collateral and the CenturyLink Marks inure solely to the benefit of CenturyLink, and no other use is permitted. CenturyLink will have the right to use the name, marks, and trade designations for any Business Participant in the Program for the duration of that Business Participant&rsquo;s participation in the Program in order to communicate its association with the Business Participant. You shall not issue any press release or make any other public announcement regarding this Agreement or any relation between you and CenturyLink.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Limitation of Liability</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">CenturyLink shall have no liability to you for rewards, payments, or commissions that might have been earned hereunder but for the inability or failure of CenturyLink to provide Services to any Prospective Customer or in the event of discontinuation or modification of the Services. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">CENTURYLINK SHALL NOT BE LIABLE FOR ANY DIRECT, SPECIAL, PUNITIVE, INDIRECT, OR CONSEQUENTIAL DAMAGES IN ANY CAUSE OF ACTION, WHETHER IN CONTRACT OR TORT, AND WHETER OR NOT THE OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. YOUR SOLE AND EXCLUSIVE REMEDY HEREUNDER SHALL BE FOR YOU TO DISCONTINUE YOUR PARTICIPATION IN THE PROGRAM AND TERMINATE THIS AGREEMENT.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Indemnification</span>
						</td>
						</tr>
						  <tr><td align="left" valign="top" class="FAQuestions">You agree to defend, indemnify and hold harmless CenturyLink, its directors, officers, employees, agents and their successors from all third party claims, losses, liabilities, costs, or expenses, including reasonable attorneys’ fees, arising from or related to (a) this Agreement and (b) your participation in the Program.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Representations and Warranties</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">You represent and warrant to CenturyLink that: (a) you are over the age of eighteen (18) and have the power and authority to enter into and perform your obligations under this Agreement, including authority to act on behalf of a Business Participant, if applicable; (b) entering into this Agreement will not place you in breach or default of any other Agreement to which you are a party; (c) you shall comply with all terms and conditions of this Agreement; (d) you will conduct yourself in a professional manner and will not make any false, misleading or disparaging statements regarding any CenturyLink competitor or any other individual or organization as it relates to any activity associated with the Program; and (e) you have provided accurate and complete registration information, including your legal name, address and telephone number.</td>
						 </tr>
						  <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Confidentiality</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">During the term of this Agreement and after termination or expiration of this Agreement, you shall not disclose information concerning the terms of this Agreement, CenturyLink technology, business affairs, trade secrets, price lists, business plans, data, research, and marketing or sales plans, or any other information related to CenturyLink (collectively, “CenturyLink Confidential Information”). CenturyLink Confidential Information is the exclusive property of CenturyLink and may be used by you solely in the performance of your obligations under this Agreement. You agree that monetary damages for breach of this Section are not adequate, that CenturyLink shall be entitled to injunctive relief with respect to such breach, and you will not raise the defense of an adequate remedy at law. This Section and all obligations contained therein shall survive any termination of the Agreement.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Termination</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">This Agreement is effective upon your acceptance as set forth herein and shall continue in full force until terminated. CenturyLink reserves the right, in its sole discretion and without notice, at any time and for any reason, to: (a) remove or disable access to all or any portion of the Program; (b) modify or discontinue the Program; (c) suspend your access to use of all or any portion of the Program; and (d) terminate this Agreement.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Miscellaneous</span>
						</td>
						</tr>
						  <tr><td align="left" valign="top" class="FAQuestions">Neither you nor CenturyLink shall be liable for loss or damage or deemed to be in breach of this Agreement if the failure to perform an obligation results from (a) compliance with any law, ruling, order, regulation, requirement of any federal, state or municipal government or department or agency thereof or court of competent jurisdiction; (b) acts of God or any other cause beyond that party’s reasonable control; (c) acts or omissions of the other party; or (d) fires, strikes, war, terrorism, labor disputes, insurrection or riot. The terms and conditions of this Agreement are applicable to the Program only and do not supersede the terms and conditions in any Master Representative Agreement, or similar agreement between you and CenturyLink. No provision of this Agreement which may be deemed unenforceable shall in any way invalidate any other provisions of this Agreement, all of which shall remain in full force and effect. You may not assign this Agreement without the written consent of CenturyLink, and the Agreement only may be amended by a writing signed by both parties.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Dispute Resolution</span>
						</td>
						</tr>
						  <tr><td align="left" valign="top" class="FAQuestions">This Agreement shall be governed by the laws of the State of Colorado, regardless of its conflict of laws provisions, and constitutes the entire Agreement between you and CenturyLink with respect to the subject matter hereof. </td>
						 </tr>
						 </tr>
						  <tr><td align="left" valign="top" class="FAQuestions">If the parties are unable to resolve a dispute through informal means, you and CenturyLink agree to arbitrate any and all claims, controversies or disputes of any kind (collectively, “Claims”) against each other, including but not limited to Claims arising out of or relating to this Agreement. This agreement to arbitrate is intended to be broadly interpreted and applies to all Claims between the parties. The sole exception to this arbitration agreement is that either you or CenturyLink may, in the alternative, bring Claims in a small claims court having valid jurisdiction. You and CenturyLink agree, however, that neither CenturyLink nor you will join any Claim with a claim or claims of any other person(s) or entity(ies), whether in a lawsuit, arbitration, or any other proceeding. You and CenturyLink agree that no Claims will be asserted in any representative capacity on behalf of anyone else, that no Claims will be resolved on a class&ndash;wide or collective basis, that no arbitrator or arbitration forum will have jurisdiction to adjudicate or determine any Claims on a class&ndash;wide or collective basis, and that no rules for class&ndash;wide or collective arbitration will apply. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">A party who intends to seek arbitration must first send to the other, by certified mail, a written notice of dispute (&ldquo;Notice&rdquo;). The Notice address for CenturyLink is 1801 California St., Denver, CO 80202, Attn: Litigation Department; and your Notice address is the address you entered for the Program. The Notice must (a) describe the nature and basis of the Claim; and (b) set forth the specific relief sought. If you and CenturyLink do not reach an agreement to resolve the Claim within thirty (30) days after the Notice is received, you or CenturyLink may commence an arbitration proceeding. A single arbitrator engaged in the practice of law will conduct the arbitration. The arbitration will be filed with the American Arbitration Association (&ldquo;AAA&rdquo;), the arbitrator will be selected according to the AAA&rsquo;s procedures and the Federal Arbitration Act, 9 U.S.C. &sect;&sect;  1&ndash;16 (&ldquo;FAA&rdquo;), and Claims will be resolved pursuant to this dispute resolution provision and the AAA&rsquo;s rules in effect when the Claim is filed. Claims also may be referred to another arbitration organization if you and CenturyLink agree in writing or to an arbitrator appointed pursuant to section 5 of the FAA. The arbitration will be confidential. The arbitrator is bound by the terms of this Agreement, and the arbitrator’s authority is limited to Claims between you and CenturyLink alone. The arbitrator has no authority to join or consolidate Claims, or adjudicate joined or consolidated Claims, unless you and CenturyLink agree in writing. All issues are for the arbitrator to decide. The arbitrator&rsquo;s decision and award is final and binding, and judgment on the award may be entered in any court with jurisdiction. The arbitrator can award the same damages and relief that a court can award, including the award of declaratory or injunctive relief; provided, however, that any declaratory or injunctive relief may only be in favor of the individual party seeking relief and only to the extent necessary to provide relief warranted by that party&rsquo;s individual Claim. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">Each party will be responsible for paying its share of any arbitration fees (including filing, administrative, hearing or other fees). The FAA, and not state law, applies to this dispute resolution provision and governs all questions of whether a Claim is subject to arbitration. If any portion of this dispute resolution provision is determined to be invalid or unenforceable, the remainder of the provision remains in full force and effect. If for any reason, the above provisions on arbitration are held unenforceable or are found not to apply to a Claim, you and CenturyLink waive the right to a jury trial on your respective Claims, and waive any right to pursue any Claims on a class or consolidated basis or in a representative capacity.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">BY CLICKING THE ACCEPTANCE BUTTON OR PARTICIPATING IN THE PROGRAM, YOU EXPRESSLY AGREE TO AND CONSENT TO BE BOUND BY THE TERMS AND CONDITIONS IN THIS AGREEMENT, INCLUDING THE WAIVER OF TRIAL BY JURY. IF YOU DO NOT AGREE TO ALL OF THE TERMS OF THIS AGREEMENT, THE BUTTON INDICATING REJECTION MUST BE SELECTED, AND YOU WILL NOT PARTICIPATE IN THE PROGRAM. </td>
						 </tr>


<!--	ABOVE THIS	-->
                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><table width="300" border="0" align="center" cellpadding="1" cellspacing="1">
 <tr>
<form name="agree" action="newenroll.cgi" method="post">
							<input type="hidden" name="special" value="$special">
                              <td align="center" valign="top"><input name="Submit" type="submit"  value="I Agree" /></td>
</form>  
							<form name="agree" action="disagree.cgi" method="post">
							<input type="hidden" name="special" value="$special">
							  <td align="center" valign="top"><input name="Submit2" type="submit"  value="I Disagree" /></td>
</form>                           
							</tr>
	];

}
elsif ($special eq "B2C") {

	print qq[

<tr>
                <td width="10">&nbsp;</td>
                <td align="left" valign="top" class="BlueTitles">CenturyLink&reg; Retail Referral Rewards Program Agreement </td>
              </tr>
            </table></td>
          </tr>
          <tr>
            <td align="left" valign="top"><img src="images/SubTitle_bot.gif" width="913" height="9" /></td>
          </tr>
          <tr>
            <td align="left" valign="middle" background="images/Sub_tile.gif"><table width="900" border="0" cellspacing="1" cellpadding="1">
              <tr>
                <td width="10" align="left" valign="top">&nbsp;</td>
                <td><table width="650" border="0" align="center" cellpadding="1" cellspacing="1">
					<tr>
                    <td><span class="BlueTitles">CenturyLink&reg; Retail Referral Rewards Program Agreement</br> Effective May 20, 2016</span><br />
                      <br />
					
                     <table width="600" border="0" cellspacing="3" cellpadding="3">
						<tr>
                          <td align="left" valign="top" class="FAQuestions">Eligible Participants who participate in the CenturyLink Retail Referral Rewards Program (the &ldquo;Program&rdquo;) are required to read, understand and accept this Agreement supporting the Program, particularly as they relate to ethical sales practices. CenturyLink reserves the right to revise the Program, Service eligibility, Participant eligibility, rewards, or cancel the Program at any time, without notice, and without any liability or obligation to any Participant.
						 </td>
                          </tr>
						  <tr>
                          <td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">General Provisions and Definitions</span></td>
                          </tr>						  
						<tr>
                          <td align="left" valign="top" class="FAQuestions">This agreement (&ldquo;Agreement&rdquo;) is made between CenturyLink Service Group, LLC (&ldquo;CenturyLink&rdquo;) and the individual or entity (collectively, &ldquo;Participant&rdquo;, &ldquo;you&rdquo;, or &ldquo;your&rdquo;) who completes the registration process to participate in the Program. This Agreement establishes the non&ndash;exclusive terms and conditions under which you shall register as a sales lead program participant with CenturyLink for the purpose of identifying and submitting a &ldquo;Lead Referral&rdquo; (as defined hereafter) to CenturyLink for compensation. The Agreement term will begin on the date you complete the registration Process for the Program and will continue until either you or CenturyLink terminates the relationship as described in this Agreement. Participants agree that there is no employer&ndash;employee relationship, joint venture, partnership or agency created by this Agreement. You have no authority to act for, or on behalf of CenturyLink and are not authorized to bind CenturyLink in any manner whatsoever.
						 </td>
                        </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">As used herein, a &ldquo;Lead Referral&rdquo; shall refer to a sales lead provided by you to CenturyLink which you submit to CenturyLink via the website designated by CenturyLink, using a completed &ldquo;Lead Referral Form&rdquo; which identifies a prospective customer (&ldquo;Prospective Customer&rdquo;) who might be interested in receiving Services from CenturyLink. CenturyLink has no obligation to pursue or take any action on any Lead Referral submitted by you or directly to retail store.
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">As used herein, &ldquo;Services&rdquo; shall refer to those telecommunications and multimedia services and products provided pursuant to CenturyLink&rsquo;s standard service, ordering, and provisioning processes (all CenturyLink products and services shall collectively be referred to as &ldquo;Services&rdquo;). CenturyLink reserves the right to modify, add to or delete Services at its sole option without notice to Participants.
						</td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Eligible Participants</span>
						</td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions">
						 <ol>
							<li>Participants may be an individual or business who meets eligibility requirements described at www.centurylinkconnect.com and completes the enrollment process.</li>
							<li>Business Participants must provide an accurate description of the entity (sole proprietor, partnership, trust, corporation, etc.) and the name of an authorized business to which the compensation will be paid.</li>
							<li>All Participants must meet the following criteria:
								<ol STYLE="list-style-type: lower-alpha;">
								<li>Must provide accurate and complete registration information and complete form W&ndash;9, if required.</li>
								<li>To the extent that Participant is enrolled as an MDU and intends to enter referrals by virtue of its access to residents of a multiple dwelling unit property (&ldquo;MDU&rdquo;), the MDU may not be the subject of a marketing or promotional agreement with CenturyLink or any other provider of voice, video, and data services.</li>
								<li>Participant and those entering referrals on behalf of the Business will avoid any conduct or action that conflicts or appears to conflict with honest, ethical conduct and will not engage in any activity that may be detrimental to CenturyLink&rsquo;s interest, reputation, or goodwill.</li>
								<li>Participant and those entering referrals on behalf of the Business must act in accordance with and not violate this Agreement or CenturyLink policies or rules.</li>
								<li>CenturyLink may declare any individual and any Participant ineligible at any time and terminate their enrollment.</li>
								<li>Current CenturyLink employees, individuals or businesses participating in any other CenturyLink sales, marketing, or related program, including those in CenturyLink Partner programs, and those enrolled in any other CenturyLink program may not enter referrals for any Participant.</li>
								<li>Master agent, subagent, indirect sales representatives of CenturyLink are excluded.</li>
								<li>Residents of a CenturyLink employee’s household are excluded. </li>
								<li>Participants must complete the enrollment process and agree to this Agreement. </li>
							</ol>
							</li>
							</ol>
						 </td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Enrollment</span>
						</td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions">Participants must expressly agree to participate and accept and agree to this Agreement by going online to www.centurylinkconnect.com to enroll in the Program. </td>
						 </tr>
						<tr><td align="left" valign="top" class="FAQuestions">
						<ol>
							<li>Enrollment is not complete until Participant completes the registration form including: CenturyLink Reference Code, name, type of entity (Business), address, phone number, email address, Business name, Employer Name, Employer address, name of authorized individual to whom communications are to be directed.</li>
							<li>Business Participants must provide the type of entity that it is (sole proprietor, partnership, trust, corporation, etc.), and provide the name of the individual, authorized by Participant to act on its behalf in connection with the Program and to whom communications about the Program may be directed. No other individuals will be authorized to act on behalf of the Business Participant in the Program.</li>
						 <li>Business Participants must complete a W&ndash;9 form with an accurate identification number (the identification number is the Federal ID Number used to file federal income tax returns for the business. Tax id must match the Business name used to enroll. </li>
						 </ol>
						 </td>
						</tr>
						<tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Lead Referral Process Considerations</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">
						<ol>
							<li>Participant must name an individual to whom communications about the program may be directed. That individual and others entering referrals on behalf of Participant must be over the age of 18.</li>
							<li>The prospective customer is the individual or entity responsible for the account, and/or decision maker.</li>
							<li>Participant must ensure that Services are ordered on behalf of the Prospective Customer by an individual with authority to bind the Prospective Customer to such order and that such person provides valid consent for the Participant to submit the order to CenturyLink. The authorized individual will be contacted by CenturyLink to finalize the order and sale of Services. The authorized individual must provide consent to CenturyLink for the order and agree to all terms and conditions associated with the Service, and provide all other information and approvals required by CenturyLink to complete the order and sales of Service.</li>
						 <li>Participants who create a referral are eligible for rewards when the referral closes as a valid, completed sale according to this Agreement. </li>
						 </ol>
						 </td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Products and Marketing</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">
						<ol>
						 <li>Lead Referrals will not be eligible for Program rewards if the Service is already on the Prospective Customer&rsquo;s account, or if the contact results in a decrease of the amount due on the Prospective Customer&rsquo;s monthly CenturyLink invoice. </li>
						 <li>Billing corrections, corrections to Service orders, requests for repair, or any other contact or assistance that does not involve the provision and sale of a new or added Service will not qualify as a referral.</li>
						 <li>Outbound telemarketing and door&ndash;to&ndash;door sales by Participants are strictly prohibited. CenturyLink reserves the right to add other tactics to this restricted list at any time in its sole discretion.  If CenturyLink adds other tactics, it will make reasonable efforts to notify Participants of such changes and will have no liability or obligation to provide rewards or compensation for any Lead Referrals after the effective date of such changes.</li>
						 <li>Only CenturyLink&ndash;approved promotional collateral and information (collectively, &ldquo;Approved Collateral&rdquo;) may be used in creating a referral. You shall make no representations or warranties relating to the Services except as set forth in the Approved Collateral.</li>
						<li>Participants may generally discuss Services, but may never make representations, claims, offers or otherwise characterize any Service, term, condition, tariff, price list, discounts or other matters, except as expressly described and stated in Approved Collateral.</li>
						 <li>Prospective Customers must always be advised that the actual performance, price or other matter affecting a Service, and such information must be confirmed by CenturyLink. </li>
						 <li>Lead Referrals cannot be made for the following Prospective Customers: Businesses, official company service (OCS) orders for CenturyLink owned and operated facilities, political organizations, referrals made by Participants for itself/his/herself, and CenturyLink employees or others where the Services are provided by CenturyLink under a company concession or promotional plan.</li>
						 <li>Participants may not use or have access to any non&ndash;public CenturyLink systems, databases or facilities to identify a Prospective Customer, identify the suitability of a referral, to suggest the availability of a Service, market Services, or any other use.</li>
						 </ol>
						 </td>
						 </tr>
						<tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Program Guidelines and Interpretation</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">Questions regarding this Agreement and its interpretation or any Program disputes should be directed to <a href="mailto:refer.friend\@centurylink.com" target="_top">refer.friend\@centurylink.com</a> or www.centurylinkconnect.com. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">
						<ol>
						 <li>A CenturyLink Sales Center acting on behalf of Program Management must conclude any and every sale of a Service, explaining, as appropriate, the functions, features, price, etc., to the Prospective Customer prior to issuing the order </li>
						 <li>CenturyLink reserves the right to limit the maximum award issued to any Participant in the Program. </li>
						 <li>Two open referrals for the same account or telephone number, for the same Service will be considered duplicate referrals. In the case of a duplicate referral, the first&ndash;received referral will receive the award, if applicable. </li>
						 <li>The actions, resolutions, and determinations of CenturyLink are final and cannot be appealed.</li>
						 </ol>
						 </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Rewards and Redemption</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">CenturyLink agrees to pay Participants for a Lead Referral accepted by CenturyLink after a sales agreement is made between the Prospective Customer and CenturyLink and Service(s) are installed and operational. Award amounts will be determined by CenturyLink in its sole discretion and are subject to change without notice. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">The value of an award made pursuant to the Program is subject to federal and state income tax. Participants are responsible for all applicable taxes, including those directed to an Approved Organization. Participant&rsquo;s tax ID numbers are required for tax reporting purposes and a 1099&ndash;MISC will be issued to Participants earning an annual, cumulative amount of \$600 or more through this program. CenturyLink, acting through the Program Management will make all decisions regarding reward eligibility and issuance. The Program Management is the sole judge in interpreting all provisions, rules, qualifications, awards and any disputes that may arise in the operation of the Program. All of these decisions are final and cannot be appealed. No contract rights are created by the existence of or participation in the Program. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">All Approved Collateral provided by CenturyLink, and CenturyLink&rsquo;s name, trademarks, service marks, label designs, product identifications, artwork, and other symbols and devices associated with this Agreement (collectively, the &ldquo;CenturyLink Marks&rdquo;) are and will remain the property of CenturyLink. You are authorized to use the Approved Collateral and CenturyLink Marks as described by CenturyLink and only with CenturyLink&rsquo;s prior written approval. Your use of the Approval Collateral and the CenturyLink Marks is non&ndash;exclusive, non&ndash;sublicenseable, non&ndash;assignable, and non&ndash;transferable. Your uses of the Approved Collateral and the CenturyLink Marks inure solely to the benefit of CenturyLink, and no other use is permitted. CenturyLink will have the right to use the name, marks, and trade designations for any Business Participant in the Program for the duration of that Business Participant&rsquo;s participation in the Program in order to communicate its association with the Business Participant. You shall not issue any press release or make any other public announcement regarding this Agreement or any relation between you and CenturyLink.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Limitation of Liability</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">CenturyLink shall have no liability to you for rewards, payments, or commissions that might have been earned hereunder but for the inability or failure of CenturyLink to provide Services to any Prospective Customer or in the event of discontinuation or modification of the Services. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">CENTURYLINK SHALL NOT BE LIABLE FOR ANY DIRECT, SPECIAL, PUNITIVE, INDIRECT, OR CONSEQUENTIAL DAMAGES IN ANY CAUSE OF ACTION, WHETHER IN CONTRACT OR TORT, AND WHETER OR NOT THE OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. YOUR SOLE AND EXCLUSIVE REMEDY HEREUNDER SHALL BE FOR YOU TO DISCONTINUE YOUR PARTICIPATION IN THE PROGRAM AND TERMINATE THIS AGREEMENT.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Indemnification</span>
						</td>
						</tr>
						  <tr><td align="left" valign="top" class="FAQuestions">You agree to defend, indemnify and hold harmless CenturyLink, its directors, officers, employees, agents and their successors from all third party claims, losses, liabilities, costs, or expenses, including reasonable attorneys’ fees, arising from or related to (a) this Agreement and (b) your participation in the Program.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Representations and Warranties</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">You represent and warrant to CenturyLink that: (a) you are over the age of eighteen (18) and have the power and authority to enter into and perform your obligations under this Agreement, including authority to act on behalf of a Business Participant, if applicable; (b) entering into this Agreement will not place you in breach or default of any other Agreement to which you are a party; (c) you shall comply with all terms and conditions of this Agreement; (d) you will conduct yourself in a professional manner and will not make any false, misleading or disparaging statements regarding any CenturyLink competitor or any other individual or organization as it relates to any activity associated with the Program; and (e) you have provided accurate and complete registration information, including your legal name, address and telephone number.</td>
						 </tr>
						  <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Confidentiality</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">During the term of this Agreement and after termination or expiration of this Agreement, you shall not disclose information concerning the terms of this Agreement, CenturyLink technology, business affairs, trade secrets, price lists, business plans, data, research, and marketing or sales plans, or any other information related to CenturyLink (collectively, “CenturyLink Confidential Information”). CenturyLink Confidential Information is the exclusive property of CenturyLink and may be used by you solely in the performance of your obligations under this Agreement. You agree that monetary damages for breach of this Section are not adequate, that CenturyLink shall be entitled to injunctive relief with respect to such breach, and you will not raise the defense of an adequate remedy at law. This Section and all obligations contained therein shall survive any termination of the Agreement.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Termination</span>
						</td>
						</tr>
						 <tr><td align="left" valign="top" class="FAQuestions">This Agreement is effective upon your acceptance as set forth herein and shall continue in full force until terminated. CenturyLink reserves the right, in its sole discretion and without notice, at any time and for any reason, to: (a) remove or disable access to all or any portion of the Program; (b) modify or discontinue the Program; (c) suspend your access to use of all or any portion of the Program; and (d) terminate this Agreement.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Miscellaneous</span>
						</td>
						</tr>
						  <tr><td align="left" valign="top" class="FAQuestions">Neither you nor CenturyLink shall be liable for loss or damage or deemed to be in breach of this Agreement if the failure to perform an obligation results from (a) compliance with any law, ruling, order, regulation, requirement of any federal, state or municipal government or department or agency thereof or court of competent jurisdiction; (b) acts of God or any other cause beyond that party’s reasonable control; (c) acts or omissions of the other party; or (d) fires, strikes, war, terrorism, labor disputes, insurrection or riot. The terms and conditions of this Agreement are applicable to the Program only and do not supersede the terms and conditions in any Master Representative Agreement, or similar agreement between you and CenturyLink. No provision of this Agreement which may be deemed unenforceable shall in any way invalidate any other provisions of this Agreement, all of which shall remain in full force and effect. You may not assign this Agreement without the written consent of CenturyLink, and the Agreement only may be amended by a writing signed by both parties.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions"><span class="Enrollcopy">Dispute Resolution</span>
						</td>
						</tr>
						  <tr><td align="left" valign="top" class="FAQuestions">This Agreement shall be governed by the laws of the State of Colorado, regardless of its conflict of laws provisions, and constitutes the entire Agreement between you and CenturyLink with respect to the subject matter hereof. </td>
						 </tr>
						 </tr>
						  <tr><td align="left" valign="top" class="FAQuestions">If the parties are unable to resolve a dispute through informal means, you and CenturyLink agree to arbitrate any and all claims, controversies or disputes of any kind (collectively, “Claims”) against each other, including but not limited to Claims arising out of or relating to this Agreement. This agreement to arbitrate is intended to be broadly interpreted and applies to all Claims between the parties. The sole exception to this arbitration agreement is that either you or CenturyLink may, in the alternative, bring Claims in a small claims court having valid jurisdiction. You and CenturyLink agree, however, that neither CenturyLink nor you will join any Claim with a claim or claims of any other person(s) or entity(ies), whether in a lawsuit, arbitration, or any other proceeding. You and CenturyLink agree that no Claims will be asserted in any representative capacity on behalf of anyone else, that no Claims will be resolved on a class&ndash;wide or collective basis, that no arbitrator or arbitration forum will have jurisdiction to adjudicate or determine any Claims on a class&ndash;wide or collective basis, and that no rules for class&ndash;wide or collective arbitration will apply. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">A party who intends to seek arbitration must first send to the other, by certified mail, a written notice of dispute (&ldquo;Notice&rdquo;). The Notice address for CenturyLink is 1801 California St., Denver, CO 80202, Attn: Litigation Department; and your Notice address is the address you entered for the Program. The Notice must (a) describe the nature and basis of the Claim; and (b) set forth the specific relief sought. If you and CenturyLink do not reach an agreement to resolve the Claim within thirty (30) days after the Notice is received, you or CenturyLink may commence an arbitration proceeding. A single arbitrator engaged in the practice of law will conduct the arbitration. The arbitration will be filed with the American Arbitration Association (&ldquo;AAA&rdquo;), the arbitrator will be selected according to the AAA&rsquo;s procedures and the Federal Arbitration Act, 9 U.S.C. &sect;&sect;  1&ndash;16 (&ldquo;FAA&rdquo;), and Claims will be resolved pursuant to this dispute resolution provision and the AAA&rsquo;s rules in effect when the Claim is filed. Claims also may be referred to another arbitration organization if you and CenturyLink agree in writing or to an arbitrator appointed pursuant to section 5 of the FAA. The arbitration will be confidential. The arbitrator is bound by the terms of this Agreement, and the arbitrator’s authority is limited to Claims between you and CenturyLink alone. The arbitrator has no authority to join or consolidate Claims, or adjudicate joined or consolidated Claims, unless you and CenturyLink agree in writing. All issues are for the arbitrator to decide. The arbitrator&rsquo;s decision and award is final and binding, and judgment on the award may be entered in any court with jurisdiction. The arbitrator can award the same damages and relief that a court can award, including the award of declaratory or injunctive relief; provided, however, that any declaratory or injunctive relief may only be in favor of the individual party seeking relief and only to the extent necessary to provide relief warranted by that party&rsquo;s individual Claim. </td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">Each party will be responsible for paying its share of any arbitration fees (including filing, administrative, hearing or other fees). The FAA, and not state law, applies to this dispute resolution provision and governs all questions of whether a Claim is subject to arbitration. If any portion of this dispute resolution provision is determined to be invalid or unenforceable, the remainder of the provision remains in full force and effect. If for any reason, the above provisions on arbitration are held unenforceable or are found not to apply to a Claim, you and CenturyLink waive the right to a jury trial on your respective Claims, and waive any right to pursue any Claims on a class or consolidated basis or in a representative capacity.</td>
						 </tr>
						 <tr><td align="left" valign="top" class="FAQuestions">BY CLICKING THE ACCEPTANCE BUTTON OR PARTICIPATING IN THE PROGRAM, YOU EXPRESSLY AGREE TO AND CONSENT TO BE BOUND BY THE TERMS AND CONDITIONS IN THIS AGREEMENT, INCLUDING THE WAIVER OF TRIAL BY JURY. IF YOU DO NOT AGREE TO ALL OF THE TERMS OF THIS AGREEMENT, THE BUTTON INDICATING REJECTION MUST BE SELECTED, AND YOU WILL NOT PARTICIPATE IN THE PROGRAM. </td>
						 </tr>


<!--	ABOVE THIS	-->
<!--	DO NOT TOUCH BELOW THIS	-->

                        <tr>
                          <td align="left" valign="top" class="FAQuestions"><table width="300" border="0" align="center" cellpadding="1" cellspacing="1">

 <tr>
<form name="agree" action="newenroll_b2c.cgi" method="post">
	 <input type="hidden" name="special" value="$special">
                              <td align="center" valign="top"><input name="Submit" type="submit"  value="I Agree" /></td>
</form>
	 <form name="agree" action="disagree.cgi" method="post">
	 <input type="hidden" name="special" value="$special">
							  <td align="center" valign="top"><input name="Submit2" type="submit"  value="I Disagree" /></td>
</form>                           
							</tr>
		];
}
else {
  headernocss();
  print qq[
  <form name="lead" action="" method="post">
     <script language='javascript'>
      alert("There was an error loading the page. Please start over again.");
      document.lead.action='$url';
      document.lead.submit();
    </script>
  </form>
 </body>
</html>];
exit();
}
print qq[


                          </table></td>
                        </tr>
                      </table></td>
                  </tr>
                </table></td>
              </tr>
            </table></td>
          </tr>
         ];
getFooter($cci_id);
print qq[
        </table></td>
      </tr>
    </table></td>
  </tr>
</table>
</body>
</html>
]
#------------------------------------------------------


