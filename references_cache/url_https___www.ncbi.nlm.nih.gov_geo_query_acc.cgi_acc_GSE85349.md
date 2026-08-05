---
reference_id: url:https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE85349
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
<meta name="ncbi_phid" content="0C428148A5F389310000000000000001">
<meta name="ncbi_sessionid" content="0C428148A5F38931_0000SID">

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
<td align="right">Not logged in | <a href="/geo/submitter?ix=1JQQJrwhqlw1s7tpcpIEYBkfvZVpFvuWEKbKXu5GB56Zc4LjjZP3OiLwN6psnQx3lJZyu1otSU9F7X-acXy">Login</a><a href="javascript:RPopUpWindow_Set(geologinbar_login,260,200,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
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
&nbsp;<label for="geo_acc">GEO accession: </label><input id="geo_acc" name="acc" onkeydown="ViewOptionsFormKeyDown(event)" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_acc)" style="font-size: 10px" type="text" value="GSE85349">&nbsp;&nbsp;</td>
<td valign="middle"><img alt="Go" border="0" onclick="SubmitViewOptionsForm()" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_go)" src="/geo/img/buttons/go_button.gif"></td>
</tr></table></td></tr></table></td>
</tr></table></form>
    <table><tr><td><table cellpadding="2" cellspacing="0" width="600"><tr bgcolor="#cccccc" valign="top"><td colspan="2"><table width="600"><tr><td><strong class="acc" id="GSE85349"><a href="/geo/query/acc.cgi?acc=GSE85349" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">Series GSE85349</a></strong></td>
<td></td>
<td align="right" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_gds)"><a href="/gds/?term=GSE85349[Accession]">Query DataSets for GSE85349</a></td>
</tr></table></td></tr>
<tr valign="top"><td>Status</td>
<td>Public on Nov 08, 2016</td>
</tr>
<tr valign="top"><td nowrap>Title</td>
<td style="text-align: justify">Vulnerability of Purkinje cells induced from spinocerebellar ataxia type 6 patient-derived iPS cells</td>
</tr>
<tr valign="top"><td nowrap>Organism</td>
<td><a href="/Taxonomy/Browser/wwwtax.cgi?mode=Info&amp;id=9606" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_organismus)">Homo sapiens</a></td>
</tr>
<tr valign="top"><td nowrap>Experiment type</td>
<td>Expression profiling by array<br></td>
</tr>
<tr valign="top"><td nowrap>Summary</td>
<td style="text-align: justify">This SuperSeries is composed of the SubSeries listed below.<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Overall design</td>
<td style="text-align: justify">Refer to individual Series<br></td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td nowrap>Citation(s)</td>
<td><span class="pubmed_id" id="27806289"><a href="/pubmed/27806289">27806289</a></span></td>
</tr>
<tr valign="top"><td colspan="2"><span id="geo2r"></span> <span id="rnaseq_counts"></span></td></tr>
<tr bgcolor="#eeeeee" valign="top"><td>Submission date</td>
<td>Aug 09, 2016</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Last update date</td>
<td>Jul 02, 2018</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td>Contact name</td>
<td>Keiko Muguruma</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>E-mail(s)</td>
<td><a href="mailto:muguruke@hirakata.kmu.ac.jp">muguruke@hirakata.kmu.ac.jp</a><br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Organization name</td>
<td style="text-align: justify">Kansai Medical University<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Department</td>
<td style="text-align: justify">Graduate School of Medicine<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Lab</td>
<td style="text-align: justify">iPS Cell Applied Medicine<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Street address</td>
<td style="text-align: justify">2-5-1 Shinmachi<br></td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>City</td>
<td style="text-align: justify">Hirakata</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>ZIP/Postal code</td>
<td style="text-align: justify">5731010</td>
</tr>
<tr bgcolor="#eeeeee" valign="top"><td nowrap>Country</td>
<td style="text-align: justify">Japan</td>
</tr>
<tr valign="top"><td nowrap>&nbsp;</td>
<td></td>
</tr>
<tr valign="top"><td>Platforms (2)</td>
<td onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GPL20844" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GPL20844</a></td>
<td valign="top">Agilent-072363 SurePrint G3 Human GE v3 8x60K Microarray 039494 [Feature Number Version]</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GPL21185" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GPL21185</a></td>
<td valign="top">Agilent-072363 SurePrint G3 Human GE v3 8x60K Microarray 039494 [Probe Name Version]</td>
</tr>
</table></td>
</tr>
<tr valign="top"><td>Samples (21)<div id="L1662681711divshown" name="L1662681711divshown" style="display: none"><a href="javascript:HandleVisibilityChangeL1662681711()"><img alt="Less..." border="0" src="/geo/img/minus_close.gif">&nbsp;Less...</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
<div id="L1662681711divhidden" name="L1662681711divhidden" style="display: block"><a href="javascript:HandleVisibilityChangeL1662681711()"><img alt="More..." border="0" src="/geo/img/plus_small.gif">&nbsp;More...</a></div>
</td>
<td onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265462" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265462</a></td>
<td valign="top">SAMPLE 1_Embryonic stem cells</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265463" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265463</a></td>
<td valign="top">SAMPLE 2_Embryonic stem cells</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265464" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265464</a></td>
<td valign="top">SAMPLE 3_Healthy control-derived iPS cells (HC-4)_1</td>
</tr>
</table>
<script language="Javascript" type="text/javascript">
<!--
function HandleVisibilityChangeL1662681711(){if(document.getElementById("L1662681711div").style.display == "block"){document.getElementById("L1662681711div").style.display = "none";document.getElementById("L1662681711divhidden").style.display = "block";document.getElementById("L1662681711divshown").style.display = "none";}else{document.getElementById("L1662681711div").style.display = "block";document.getElementById("L1662681711divhidden").style.display = "none";document.getElementById("L1662681711divshown").style.display = "block";}}
-->
</script>
<div id="L1662681711div" name="L1662681711div" style="display: none"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265465" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265465</a></td>
<td valign="top">SAMPLE 4_Healthy control-derived iPS cells (HC-4)_2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265466" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265466</a></td>
<td valign="top">SAMPLE 5_SCD162-17-2-derived iPS cells_1</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265467" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265467</a></td>
<td valign="top">SAMPLE 6_SCD162-17-2-derived iPS cells_2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265468" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265468</a></td>
<td valign="top">SAMPLE 7_SCD16-2E-derived iPS cells_1</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265469" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265469</a></td>
<td valign="top">SAMPLE 8_SCD16-2E-derived iPS cells_2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265470" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265470</a></td>
<td valign="top">SAMPLE 9_Healthy control-derived iPS cells (201B7)_1</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265471" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265471</a></td>
<td valign="top">SAMPLE 10_Healthy control-derived iPS cells (201B7)_2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265472" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265472</a></td>
<td valign="top">SAMPLE 11_SCD166-2-14-derived iPS cells_1</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265473" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265473</a></td>
<td valign="top">SAMPLE 12_SCD166-2-14-derived iPS cells_2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265474" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265474</a></td>
<td valign="top">SAMPLE 13_Normal human dermal fibroblasts</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265475" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265475</a></td>
<td valign="top">Day35 Control-derived neural progenitor cells 1</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265476" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265476</a></td>
<td valign="top">Day35 Control-derived neural progenitor cells 2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265477" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265477</a></td>
<td valign="top">Day35 Control-derived neural progenitor cells 3</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265478" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265478</a></td>
<td valign="top">Day35 Control-derived neural progenitor cells 4</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265479" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265479</a></td>
<td valign="top">Day35 Case-derived neural progenitor cells 1</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265480" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265480</a></td>
<td valign="top">Day35 Case-derived neural progenitor cells 2</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265481" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265481</a></td>
<td valign="top">Day35 Case-derived neural progenitor cells 3</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSM2265482" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSM2265482</a></td>
<td valign="top">Day35 Case-derived neural progenitor cells 4</td>
</tr>
</table></div>
</td>
</tr>
<tr valign="top"><td colspan="2">This SuperSeries is composed of the following SubSeries:</td></tr>
<tr valign="top"><td colspan="2" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)"><table cellpadding="3" style="position:relative;top:-5px;left:-5px"><tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSE85347" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSE85347</a></td>
<td valign="top">Vulnerability of Purkinje cells induced from spinocerebellar ataxia type 6 patient-derived iPS cells [1]</td>
</tr>
<tr><td valign="top"><a href="/geo/query/acc.cgi?acc=GSE85348" onmouseout="onLinkOut('HelpMessage' , geo_empty_help)" onmouseover="onLinkOver('HelpMessage' , geoaxema_recenter)">GSE85348</a></td>
<td valign="top">Vulnerability of Purkinje cells induced from spinocerebellar ataxia type 6 patient-derived iPS cells [2]</td>
</tr>
</table></td></tr>
<tr valign="top"><td colspan="2"><strong>Relations</strong></td></tr>
<tr valign="top"><td>BioProject</td>
<td><a href="https://www.ncbi.nlm.nih.gov/bioproject/PRJNA338237">PRJNA338237</a></td>
</tr>
</table>
<br><span id="gdv"></span><table cellspacing="3" width="600"><tr bgcolor="#eeeeee"><td><strong>Download family</strong></td>
<td><strong>Format</strong></td>
</tr>
<tr><td><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE85nnn/GSE85349/soft/" target="_blank">SOFT formatted family file(s)</a></td>
<td>SOFT<a href="javascript:RPopUpWindow_Set(geoaxema_famsoft,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
</tr>
<tr><td><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE85nnn/GSE85349/miniml/" target="_blank">MINiML formatted family file(s)</a></td>
<td>MINiML<a href="javascript:RPopUpWindow_Set(geoaxema_famminiml,260,120,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
</tr>
<tr><td><a href="ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE85nnn/GSE85349/matrix/" target="_blank">Series Matrix File(s)</a></td>
<td>TXT<a href="javascript:RPopUpWindow_Set(geoaxema_fammatrix,260,210,'','','#E1EAE6','','#538AA9','MessageBox2');" onmouseout="RPopUpWindow_Stop()"><img alt="Help" height="11" src="/coreweb/images/long_help4.gif" style="border: none" width="19"></a></td>
</tr>
</table>
<br><table cellpadding="2" cellspacing="2" width="600"><tr bgcolor="#eeeeee" valign="top"><td align="middle" bgcolor="#CCCCCC"><strong>Supplementary file</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Size</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>Download</strong></td>
<td align="middle" bgcolor="#CCCCCC"><strong>File type/resource</strong></td>
</tr>
<tr valign="top"><td bgcolor="#DEEBDC">GSE85349_RAW.tar</td>
<td bgcolor="#DEEBDC" title="79185920">75.5 Mb</td>
<td bgcolor="#DEEBDC"><a href="/geo/download/?acc=GSE85349&amp;format=file">(http)</a><a id="customDl" href="">(custom)</a></td>
<td bgcolor="#DEEBDC">TAR (of TXT)</td>
</tr>
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


