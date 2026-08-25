---
reference_id: url:https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE89420
title: GEO Accession viewer
content_type: url
---

# GEO Accession viewer

## Content

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<HTML>
  <HEAD>
    
    <style type="text/css">
      a { text-decoration: none; }
	.bordergc {background-color: #6699CC;}
	.bordergd {background-color: #B6C7E5;}
	.borderge {background-color: #EEF3FB;}
	.bordergf {background-color: #FFFFFF;}
	.bordergg {background-color: #CCCCCC;}
      .small8b { font-size:8pt;
                font-family: ariel,helvetica,sans-serif;
                color:#6633cc;
              }
      .small8db { font-size:8pt;
                font-family: ariel,helvetica,sans-serif;
                color:#4411aa;
              }

    </style>
    <META http-equiv="Content-Type"
      content="text/html; charset=UTF-8">
    <META name="keywords"
      CONTENT="NCBI GEO Gene Expression Omnibus microarray oligonucleotide array SAGE">
    <META name="description"
      content="NCBI's Gene Expression Omnibus (GEO) is a public archive and resource for gene expression data.">

<meta name="ncbi_app" content="geo">
<meta name="ncbi_pdid" content="full">
<meta name="ncbi_phid" content="0C42990FA83886D10000000000000001">
<meta name="ncbi_sessionid" content="0C42990FA83886D1_0000SID">

    <TITLE>
    GEO Accession viewer
    </TITLE>
    <link rel="stylesheet"
      href="/corehtml/ncbi.css">
    <!-- GEO_SCRIPT -->

<SCRIPT LANGUAGE="JavaScript1.2"
SRC="/coreweb/javascript/imagemouseover.js"></SCRIPT>

<SCRIPT LANGUAGE="JavaScript1.2"
SRC="/coreweb/javascript/show_message.js"></SCRIPT>

<script type="text/javascript" src="/corehtml/jsutils/utils.1.js"></script>

<script type="text/javascript" src="/corehtml/jsutils/remote_data_provider.1.js"></script>

<SCRIPT LANGUAGE="JavaScript1.2"
SRC="/geo/js/help_def_messages.js"></SCRIPT>

<script type="text/javascript">
    window.onload = function () {
        jQuery.getScript("/core/alerts/alerts.js", function () {
            galert(['#galerts_table','body > *:nth-child(1)'])
        });
    }
</script>



<LINK  rel = STYLESHEET href = "../info/geo_style.css" Type  = "text/css" >
<link rel="stylesheet" type="text/css" href="acc.css" />
  <script language="Javascript">

  function OnFormFieldChange()
  {
    var view = document.getElementById("view");

    if(document.getElementById("ViewOptions").form.value == 'html')
    {
        view.remove(3);
        view.remove(2);
    }
    else
    {
        var NewOption = document.createElement("OPTION");

        NewOption.text = "Full";
        NewOption.value = "full";

        try
        {
            view.add(NewOption, null);
        }
        catch(ex)
        {
            view.add(NewOption);
        }

        NewOption = document.createElement("OPTION");

        NewOption.text = "Data";
        NewOption.value = "data";

        try
        {
            view.add(NewOption, null);
        }
        catch(ex)
        {
            view.add(NewOption);
        }
    }
  }

  function SubmitViewOptionsForm()
  {
	var form = document.forms.ViewOptions;
    if(form.form.value == 'html')
    {
		form.form.setAttribute('disabled','disabled');
		if (form.view.value == 'quick') {
			form.view.setAttribute('disabled','disabled');
		}
		if (form.targ.value == 'self') {
			form.targ.setAttribute('disabled','disabled');
		}
        var token = document.getElementById("token_input");
        if (token) {
            form.token.value = token.value;
        } else {
            form.token.setAttribute('disabled','disabled');
        }
        form.submit();
    }
    else
    {
        window.open("acc.cgi?acc=" + form.acc.value + "&targ=" + form.targ.value +
                  "&form=" + form.form.value + "&view=" + form.view.value, "_self");
    }

    return false;
  }
  
  function ViewOptionsFormKeyDown(event)
  {
	if (event == undefined)
	{    
		event = window.event;
	}
	if (event.keyCode == 13)
	{
		SubmitViewOptionsForm();
		return false;
	}
  };

  function OpenFTP(url)
  {
    window.open(url.replace('ftp://', 'https://'), '_blank');
  }

  function OpenLink(url, where)
  {
    window.open(url, where);
  }

  utils.addEvent(window, "load", OnFormFieldChange)
  </script>

</head>
<body background="/coreweb/template1/pix/bg_main3.gif" topmargin="20" marginheight="20">


<script type="text/javascript" src="/core/jig/1.15.10/js/jig.min.js"></script>
<script type="text/javascript" src="/corehtml/pmc/granthub/v1/granthubsearch.min.js"></script>
<script type="text/javascript" src="/geo/js/dd_menu.js"></script>
	<table width="740" border="0" cellspacing="0" cellpadding="0" align="center" >
			<tr>
				<td>
					<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
						<tr>
							<td><a href="/"><img src="/geo/img/ncbi_logo.gif" alt="NCBI Logo" width="145" height="66" border="0"></a></td>
							<td width="100%" align="center" valign="middle" nowrap background="/coreweb/template1/pix/top_bg_white.gif"><img src="/coreweb/template1/pix/pixel.gif" width="550" height="1" alt="" border="0"><br>
								<a href="/geo/"><img src="/geo/img/geo_main.gif" alt="GEO Logo" border="0"></a>
							</td>
							<td align="right" background="/coreweb/template1/pix/top_bg_white.gif"><img src="/coreweb/template1/pix/top_right.gif" alt="" width="5" height="66" border="0"></td>
						</tr>
					</table>
					<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
						<tr>
							<td><img src="/coreweb/template1/pix/top2_left.gif" width="601" height="2" alt="" border="0"></td>
							<td width="100%" background="/coreweb/template1/pix/top2_mid_bg.gif"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td>
							<td align="right"><img src="/coreweb/template1/pix/top2_right.gif" alt="" width="14" height="2" border="0"></td>
						</tr>
					</table>
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" id="galerts_table"/>
					<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
						<tr>
							<td><img src="/coreweb/template1/pix/top3_ulm_no_a.gif" width="145" height="16" alt="" border="0" usemap="#unlmenu" name="unl_menu_pix"></td>
							<td background="/coreweb/template1/pix/top3_mainmenu_mid_bg.gif"><img src="/coreweb/template1/pix/top3_mainmenu_left.gif" width="3" height="16" alt="" border="0"></td>
							<td width="100%" valign="middle" nowrap background="/coreweb/template1/pix/top3_mainmenu_mid_bg.gif">

					<!-- GEO Navigation -->
			<ul id="geo_nav_bar">
				<li><a href="#">GEO Publications</a>
					<ul class="sublist">
						<li><a href="/geo/info/GEOHandoutFinal.pdf">Handout</a></li>
                        <li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10767856/">NAR 2024 (latest)</a></li>
						<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC99122/">NAR 2002 (original)</a></li>
						<li><a href="https://pmc.ncbi.nlm.nih.gov/search/?term=10767856,4944384,3531084,3341798,3013736,2686538,2270403,1669752,1619900,1619899,539976,99122[UID]">All publications</a></li>
					</ul>
				</li>
				<li><a href="/geo/info/faq.html">FAQ</a></li>
				<li><a href="/geo/info/MIAME.html" title="Minimum Information About a Microarray Experiment">MIAME</a></li>
				<li><a href="mailto:geo@ncbi.nlm.nih.gov">Email GEO</a></li>
			</ul>
			<!-- END GEO Navigation -->

                    </td>
                    <td background="/coreweb/template1/pix/top3_mainmenu_mid_bg.gif" align="right"><img src="/coreweb/template1/pix/top3_mainmenu_right.gif" width="5" height="16" alt="" border="0"></td>
                </tr>
            </table>
            
            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr>
                    <td><img src="/coreweb/template1/pix/top4_ulm_left.gif" width="145" height="4" alt="" border="0"></td>
                    <td width="100%" background="/coreweb/template1/pix/top4_mid_bg.gif"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td>
                    <td align="right" background="/coreweb/template1/pix/top4_mid_bg.gif"><img src="/coreweb/template1/pix/top4_ulm_right.gif" width="5" height="4" alt="" border="0"></td>
                </tr>
            </table>
    
            <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
                <tr>
                    <td width=1 background="/coreweb/template1/pix/main_left_bg.gif"><img src="/coreweb/template1/pix/main_left_bg.gif" alt="" width="4" height="3" border="0"></td>
                    <td width="10000" bgcolor="#F0F8FF">
                        <table cellpadding="0" cellspacing="0" width="100%"><tr><td><font class="Top_Navigation_text" color="#2F6E87" face="Verdana" size="+1">&nbsp;&nbsp;&nbsp;<a href="/">NCBI</a> &gt; <a href="/geo"><font color="">GEO</font></a> &gt; <a href="acc.cgi"><b>Accession Display</b></a><a href="javascript:RPopUpWindow_Set(geologinbar_location,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></font></td>
<td align="right">Not logged in | <a href="/geo/submitter?ix=1fignWK-EMArx_1XiITtZF45LuBxeteqXCEAjqLIkTuJPPFQWz1oOYsOK7zsabz1rC8VzrN2QAiQF2ohYf5">Login</a><a href="javascript:RPopUpWindow_Set(geologinbar_login,260,200,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
</tr></table>
                    </td>
                    <td width=1 background="/coreweb/template1/pix/main_right_bg.gif"><img src="/coreweb/template1/pix/main_right_bg.gif" width="4" height="3" alt="" border="0"></td>
                </tr>
                <tr>
                    <td background="/coreweb/template1/pix/main_left_bg.gif"><img src="/coreweb/template1/pix/main_left_bg.gif" width="4" height="1" alt="" border="0"></td>
                    <td width="10000" bgcolor="#E0EEEE"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td>
                    <td align="right" background="/coreweb/template1/pix/main_right_bg.gif"><img src="/coreweb/template1/pix/main_right_bg.gif" alt="" width="4" height="1" border="0"></td>
                </tr>

                <tr>
                    <td background="/coreweb/template1/pix/main_left_bg.gif"><img src="/coreweb/template1/pix/main_left_bg.gif" width="4" height="3" alt="" border="0"></td>
                    <td width="100%" bgcolor="White">
                        <table width="98%" border="0" align="center">
                            <tr>
                                <td>
                                    <table border="0" cellspacing="0" cellpadding="0" align="right" width="100%">
                                        <tr>
                                            <td>

 <script type="text/javascript" src="acc.js"></script>
 <span id="msg_err" style="color:red"></span>
 <span id="msg_info" style="color:blue"></span>
<table cellpadding="0" cellspacing="0" style="border: 1px solid #C0F8FF"><tr><td><img alt=" " height="35" src="/coreweb/template1/pix/pixel.gif" width="1"></td>
<td bgcolor="#F0F8FF" width="100%"><font color="#0066CC" face="Arial" size="1"><div id="HelpMessage" style="font: 11px/11px arial, sans-serif"><strong>GEO help:</strong> Mouse over screen elements for information.</div></font></td>
</tr></table>
<form action="acc.cgi" enctype="application/x-www-form-urlencoded" id="ViewOptions" method="POST" name="ViewOptions" target="_self"><table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td></td>
<td bgcolor="#CCCCCC" nowrap valign="middle" width="100%"><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td nowrap><table border="0" cellpadding="0" cellspacing="0"><tr><td valign="middle"><input id="token" name="token" type="hidden" value=""><label for="scope">Scope: </label><select id="scope" name="targ" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_scope)" style="font-size: 10px"><option selected value="self">Self</option>
<option value="gpl">Platform</option>
<option value="gsm">Samples</option>
<option value="gse">Series</option>
<option value="all">Family</option>
</select>
&nbsp;&nbsp;<label for="form">Format: </label><select id="form" name="form" onchange="OnFormFieldChange()" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_format)" style="font-size: 10px"><option value="html">HTML</option>
<option value="text">SOFT</option>
<option value="xml">MINiML</option>
</select>
&nbsp;&nbsp;<label for="view">Amount: </label><select id="view" name="view" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_amount)" style="font-size: 10px"><option value="brief">Brief</option>
<option selected value="quick">Quick</option>
</select>
&nbsp;<label for="geo_acc">GEO accession: </label><input id="geo_acc" name="acc" onkeydown="ViewOptionsFormKeyDown(event)" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_acc)" style="font-size: 10px" type="text" value="GSE89420">&nbsp;&nbsp;</td>
<td valign="middle"><img alt="Go" border="0" onclick="SubmitViewOptionsForm()" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_go)" src="/geo/img/buttons/go_button.gif"></td>
</tr></table></td></tr></table></td>
</tr></table></form>
    <table><tr><td><table cellpadding="2" cellspacing="0" width="600"><tr bgcolor="#cccccc" valign="top"><td colspan="2"><table width="600"><tr><td><strong class="acc" id="GSE89420"><a href="/geo/query/acc.cgi?acc=GSE89420" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">Series GSE89420</a></strong></td>
<td></td>
<td align="right" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_gds)"><a href="/gds/?term=GSE89420[Accession]">Query DataSets for GSE89420</a></td>
</tr></table></td></tr>
<tr valign="top"><td>Status</td>
<td>Public on Feb 01, 2018</td>
</tr>
<tr valign="top"><td nowrap>Title</td>
<td style="text-align: justify">Surveillance of rRNA synthesis by an RNA helicase mediates tissue-specific developmental disorders</td>
</tr>
<tr valign="top"><td nowrap>Organism</td>
<td><a href="/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=9606" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_organismus)">Homo sapiens</a></td>
</tr>
<tr valign="top"><td nowrap>Experiment type</td>
<td>Genome binding/occupancy profiling by high throughput sequencing<br>Expression profiling by high throughput sequencing<br></td>
</tr>
<tr valign="top"><td nowrap>Summary</td>
<td style="text-align: justify">Myriad of craniofacial disorders are caused by heterozygous mutations in general regulators of housekeeping cellular functions such as ribosome biogenesis. While it is understood that many of these highly tissue-specific malformations are a consequence of defects in cranial neural crest cells (cNCCs), an embryonic cell group that gives rise to most of the facial structures during embryogenesis, the mechanism underlying cell type-selectivity of these effects remains largely unknown. Here we show that DDX21, a DEAD-box RNA helicase involved in control of both RNA polymerase (Pol) I and Pol II dependent transcriptional arms of ribosome biogenesis, is a key mediator of the nucleolar stress response. Using an in vitro model of Treacher Collins Syndrome (TCS), a craniofacial disorder caused by heterozygous mutations in components of the Pol I transcriptional machinery, we demonstrate that perturbations in ribosomal RNA (rRNA) transcription induce DDX21-mediated surveillance mechanism in cNCCs, leading to DDX21 relocalization from the nucleolus to the nucleoplasm, its eviction from Pol I and Pol II chromatin targets and inhibition of rRNA processing. Importantly, these effects are cell type-selective, cell-autonomous and involve activation of the p53 pathway. We further show that cNCCs are characterized by the inherently high reservoir of p53 mRNA and sensitivity to p53-mediated apoptosis. Remarkably, preventing the loss of DDX21 from nucleolus and chromatin can rescue both the sensitivity to apoptosis and TCS-associated craniofacial phenotypes in vivo. This mechanism is not restricted to TCS, as gene function perturbations linked to other ribosomopathies with craniofacial manifestations also lead to the activation of DDX21 surveillance. Lastly, we provide evidence that inhibition of rRNA synthesis leads to rDNA damage, and furthermore, that rDNA damage is sufficient to activate DDX21 surveillance and elicits tissue-selective and dosage-dependent effects on craniofacial development in vivo.<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Overall design</td>
<td style="text-align: justify">Examination of DDX21 and TCOF1 binding to chromatin<br><br>Examination of DDX21 irCLIP from HeLa with DMSO or ActD treatments<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td>Contributor(s)</td>
<td><a href="/pubmed/?term=Calo E[Author]">Calo E</a>, <a href="/pubmed/?term=Wysocka J[Author]">Wysocka J</a></td>
</tr>
<tr valign="top"><td nowrap>Citation(s)</td>
<td><span class="pubmed_id" id="29364875"><a href="/pubmed/29364875">29364875</a></span></td>
</tr>
<tr valign="top"><td colspan="2"><span id="geo2r"></span> <span id="rnaseq_counts"></span></td></tr>
<tr bgcolor="#eeeeee" valign="top"><td>Submission date</td>
<td>Nov 02, 2016</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Last update date</td>
<td>Jul 25, 2021</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Contact name</td>
<td>Eliezer Calo</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>E-mail(s)</td>
<td><a href="mailto:ecalolab@gmail.com">ecalolab@gmail.com</a><br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Organization name</td>
<td style="text-align: justify">Massachusetts Institute of Technology<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Department</td>
<td style="text-align: justify">Biology<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Lab</td>
<td style="text-align: justify">calo<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Street address</td>
<td style="text-align: justify">31 Ames St, 68-270A<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>City</td>
<td style="text-align: justify">Cambridge</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>State/province</td>
<td style="text-align: justify">MASSACHUSETTS</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>ZIP/Postal code</td>
<td style="text-align: justify">02139</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Country</td>
<td style="text-align: justify">USA</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td>Platforms (2)</td>
<td onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GPL16791" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GPL16791</a></td>
<td valign="top">Illumina HiSeq 2500 (Homo sapiens)</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GPL18573" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GPL18573</a></td>
<td valign="top">Illumina NextSeq 500 (Homo sapiens)</td>
</tr>
</table></td>
</tr>
<tr valign="top"><td>Samples (10)<div id="L996243195divshown" name="L996243195divshown" style="display: none"><a href="javascript:HandleVisibilityChangeL996243195()"><img alt="Less..." border="0" src="/geo/img/minus_close.gif">&nbsp;Less...</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
<div id="L996243195divhidden" name="L996243195divhidden" style="display: block"><a href="javascript:HandleVisibilityChangeL996243195()"><img alt="More..." border="0" src="/geo/img/plus_small.gif">&nbsp;More...</a></div>
</td>
<td onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2371331" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2371331</a></td>
<td valign="top">HeLa DDX21 ChIP-seq</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2371332" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2371332</a></td>
<td valign="top">HeLa DDX21 ChIP-seq in iPol I treated cells</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2371333" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2371333</a></td>
<td valign="top">HeLa DDX21 ChIP-seq in siTCOF1</td>
</tr>
</table>
<script language="Javascript" type="text/javascript">
<!--
function HandleVisibilityChangeL996243195(){if(document.getElementById("L996243195div").style.display == "block"){document.getElementById("L996243195div").style.display = "none";document.getElementById("L996243195divhidden").style.display = "block";document.getElementById("L996243195divshown").style.display = "none";}else{document.getElementById("L996243195div").style.display = "block";document.getElementById("L996243195divhidden").style.display = "none";document.getElementById("L996243195divshown").style.display = "block";}}
-->
</script>
<div id="L996243195div" name="L996243195div" style="display: none"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2371334" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2371334</a></td>
<td valign="top">HeLa TCOF1 ChIP-seq</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2371335" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2371335</a></td>
<td valign="top">HeLa Input</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2371336" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2371336</a></td>
<td valign="top">HeLa Input iPOL2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2741615" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2741615</a></td>
<td valign="top">DDX21 irCLIP from HeLa with DMSO Biological replicate 1</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2741616" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2741616</a></td>
<td valign="top">DDX21 irCLIP from HeLa with DMSO Biological replicate 2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2741617" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2741617</a></td>
<td valign="top">DDX21 irCLIP from HeLa with ActD Biological replicate 1</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2741618" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2741618</a></td>
<td valign="top">DDX21 irCLIP from HeLa with ActD Biological replicate 2</td>
</tr>
</table></div>
</td>
</tr>
<tr valign="top"><td colspan="2"><strong>Relations</strong></td></tr>
<tr valign="top"><td>BioProject</td>
<td><a href="https://www.ncbi.nlm.nih.gov/bioproject/PRJNA352129">PRJNA352129</a></td>
</tr>
<tr valign="top"><td>SRA</td>
<td><a href="https://www.ncbi.nlm.nih.gov/sra?term=SRP092428">SRP092428</a></td>
</tr>
</table>
<br><span id="gdv"></span><table cellspacing="3" width="600"><tr bgcolor="#eeeeee"><td><strong>Download family</strong></td>
<td><strong>Format</strong></td>
</tr>
<tr><td><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89420/soft/" target="_blank">SOFT formatted family file(s)</a></td>
<td>SOFT<a href="javascript:RPopUpWindow_Set(geoaxema_famsoft,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
</tr>
<tr><td><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89420/miniml/" target="_blank">MINiML formatted family file(s)</a></td>
<td>MINiML<a href="javascript:RPopUpWindow_Set(geoaxema_famminiml,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
</tr>
<tr><td><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89420/matrix/" target="_blank">Series Matrix File(s)</a></td>
<td>TXT<a href="javascript:RPopUpWindow_Set(geoaxema_fammatrix,260,210,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
</tr>
</table>
<br><table cellpadding="2" cellspacing="2" width="600"><tr bgcolor="#eeeeee" valign="top"><td align="middle" bgcolor="#CCCCCC"><strong>Supplementary file</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Size</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Download</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>File type/resource</strong></td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSE89420_HS_HeLa_irCLIP_DDX21_ActD_minus.bw</td>
<td bgcolor="#DEEBDC" title="1377124">1.3 Mb</td>
<td bgcolor="#DEEBDC"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89420/suppl/GSE89420%5FHS%5FHeLa%5FirCLIP%5FDDX21%5FActD%5Fminus%2Ebw">(ftp)</a><a href="/geo/download/?acc=GSE89420&amp;format=file&amp;file=GSE89420%5FHS%5FHeLa%5FirCLIP%5FDDX21%5FActD%5Fminus%2Ebw">(http)</a></td>
<td bgcolor="#DEEBDC">BW</td>
</tr>
<tr valign="top"><td bgcolor="#EEEEEE">GSE89420_HS_HeLa_irCLIP_DDX21_ActD_plus.bw</td>
<td bgcolor="#EEEEEE" title="1482732">1.4 Mb</td>
<td bgcolor="#EEEEEE"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89420/suppl/GSE89420%5FHS%5FHeLa%5FirCLIP%5FDDX21%5FActD%5Fplus%2Ebw">(ftp)</a><a href="/geo/download/?acc=GSE89420&amp;format=file&amp;file=GSE89420%5FHS%5FHeLa%5FirCLIP%5FDDX21%5FActD%5Fplus%2Ebw">(http)</a></td>
<td bgcolor="#EEEEEE">BW</td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSE89420_HS_HeLa_irCLIP_DDX21_DMSO_minus.bw</td>
<td bgcolor="#DEEBDC" title="1292279">1.2 Mb</td>
<td bgcolor="#DEEBDC"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89420/suppl/GSE89420%5FHS%5FHeLa%5FirCLIP%5FDDX21%5FDMSO%5Fminus%2Ebw">(ftp)</a><a href="/geo/download/?acc=GSE89420&amp;format=file&amp;file=GSE89420%5FHS%5FHeLa%5FirCLIP%5FDDX21%5FDMSO%5Fminus%2Ebw">(http)</a></td>
<td bgcolor="#DEEBDC">BW</td>
</tr>
<tr valign="top"><td bgcolor="#EEEEEE">GSE89420_HS_HeLa_irCLIP_DDX21_DMSO_plus.bw</td>
<td bgcolor="#EEEEEE" title="1391544">1.3 Mb</td>
<td bgcolor="#EEEEEE"><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE89nnn/GSE89420/suppl/GSE89420%5FHS%5FHeLa%5FirCLIP%5FDDX21%5FDMSO%5Fplus%2Ebw">(ftp)</a><a href="/geo/download/?acc=GSE89420&amp;format=file&amp;file=GSE89420%5FHS%5FHeLa%5FirCLIP%5FDDX21%5FDMSO%5Fplus%2Ebw">(http)</a></td>
<td bgcolor="#EEEEEE">BW</td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSE89420_RAW.tar</td>
<td bgcolor="#DEEBDC" title="43960320">41.9 Mb</td>
<td bgcolor="#DEEBDC"><a href="/geo/download/?acc=GSE89420&amp;format=file">(http)</a><a id="customDl" href="">(custom)</a></td>
<td bgcolor="#DEEBDC">TAR (of WIG)</td>
</tr>
<tr><td><a href="/Traces/study/?acc=PRJNA352129">SRA Run Selector</a><a href="javascript:RPopUpWindow_Set(geoaxema_srarun,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td></tr>
<tr><td class="message">Raw data are available in SRA</td></tr>
<tr><td class="message">Processed data provided as supplementary file</td></tr>
</table>
<span id="customDlArea"></span><br></td></tr></table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
        <td background="/coreweb/template1/pix/main_right_bg.gif"><img src="/coreweb/template1/pix/main_right_bg.gif" width="4" height="3" alt="" border="0"></td>
    </tr>
    <tr>
        <td background="/coreweb/template1/pix/but_left.gif"><img src="/coreweb/template1/pix/but_left.gif" width="4" height="4" alt="" border="0"></td>
        <td width="10000" bgcolor="#FFFFFF" background="/coreweb/template1/pix/but_mid_bg.gif"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td>
        <td align="right" background="/coreweb/template1/pix/but_right.gif"><img src="/coreweb/template1/pix/but_right.gif" alt="" width="4" height="4" border="0"></td>
    </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
	<tr>
        <td width="99%"><img src="/coreweb/template1/pix/pixel.gif" width="1" height="1" alt="" border="0"></td><td valign="top" align="right"  nowrap>
	        <span class="HELPBAR">|<A HREF="https://www.nlm.nih.gov"> NLM </A>|<A HREF="https://www.nih.gov" CLASS="HELPBAR"> NIH </A>|<A HREF="mailto:geo@ncbi.nlm.nih.gov" CLASS="HELPBAR"> GEO Help </A>|<A HREF="/geo/info/disclaimer.html" CLASS="HELPBAR"> Disclaimer </A>|<a href="https://www.nlm.nih.gov/accessibility.html" class="HELPBAR"> Accessibility </a>|</span><br>
        </td>
	</tr>
</table>


<map name="unlmenu">
<area alt="NCBI Home" coords="2,0,39,15" href="/" onMouseOver="changpics(unl_menu_pix, unl_menu_home_a)" onMouseOut="changpics(unl_menu_pix, unl_menu_noa)">
<area alt="NCBI Search" coords="40,0,91,15" href="/ncbisearch/" onMouseOver="changpics(unl_menu_pix, unl_menu_search_a)" onMouseOut="changpics(unl_menu_pix, unl_menu_noa)">
<area alt="NCBI SiteMap" coords="92,0,143,15" href="/Sitemap/" onMouseOver="changpics(unl_menu_pix, unl_menu_sitemap_a)" onMouseOut="changpics(unl_menu_pix, unl_menu_noa)">
</map>

<script type="text/javascript" 
  src="/portal/portal3rc.fcgi/rlib/js/InstrumentNCBIBaseJS/InstrumentPageStarterJS.js"> </script>
</body>
</html>


