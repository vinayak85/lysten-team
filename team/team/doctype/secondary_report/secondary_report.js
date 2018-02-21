// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Secondary report', {
	refresh: function(frm) {

	}
});

/**************** Code Added 21/02/2018 **************/


var string_stockist="",code="",string_month="";

frappe.ui.form.on("Secondary report", {
    refresh: function(frm) {
       frm.add_custom_button(__("Print"),
			function() { frm.trigger('print_form'); }, "fa fa-sitemap", "btn-default");
    },
print_form:function (frm) {
 printDiv("abc")
}
});




frappe.ui.form.on("Secondary report", "btn_show", function (frm) {

	get_stockist(frm);
	get_product_value(frm);
	get_month_value(frm);
	//alert(string_stockist);
	//alert(code);
	//alert(string_month);&&string_stockist!=undefined
	if(string_stockist!="")
	{
		if(code!="")
		{
			if(string_month!="")
			{
				////alert(string_stockist);
				//alert("["+code+"]");
				///alert("["+string_month+"]");
				////string_stockist="";//code="";//string_month="";
				//string_stockist;
				//code="["+code+"]";
				////string_month="["+string_month+"]";
				string_month=string_month;				
				//alert(string_stockist);
				//alert(code);
				//alert(string_month);
			}
			else
			{
				 msgprint(__("MUST BE SELECT ATLEAST 1 MONTH"));
			}
		}
		else
		{
			 msgprint(__("MUST BE SELECT ATLEAST 1 PRODUCT"));
		}
	}
	else
	{
		 msgprint(__("MUST BE SELECT STOCKIST"));
	}

	datasetreturn(frm);
	datasetreturn_2(frm);
	datasetreturn_3(frm);	
	datasetreturn_4(frm);
	//initialize(frm);

	
	
});


function printDiv(divName) {
     //var printContents = document.getElementById('chart').innerHTML;
     var originalContents = document.body.innerHTML;
/*---*/
var printContents = document.getElementById('chart').innerHTML 
		    + "<br/>" +document.getElementById('chart2').innerHTML
		    + "<br/>" +document.getElementById('chart3').innerHTML
		    + "<br/>" +document.getElementById('chart4').innerHTML;

//var printContents = document.getElementById('chart3').innerHTML ;
		   

/*----*/
	var pop = window.open();
	pop.document.body.innerHTML = printContents;

     //document.body.innerHTML = printContents;
     //window.print();
     //document.body.innerHTML = originalContents;
}

/*---------------Select All Products START---------------------*/
var a=0;
frappe.ui.form.on("Secondary report", "select_all", function (frm) {
	if(frm.doc.select_all==1)
	{
		select_all_product(frm);
		a=0;
	}
	else
	{
		//alert('yyy');
		if(a==0)
		{
			unselect_all_product(frm);
		}
		//alert(frm.doc.actirab_tab);
	}
	
});


function select_all_product(frm)
{
	frm.set_value("actirab_tab", 1)
	frm.set_value("glucolyst_g1_tab", 1)		
	frm.set_value("regain_xt_tab", 1)
	frm.set_value("ten_on_30_ml_syrup", 1)
	frm.set_value("actirab_d_cap", 1)
	frm.set_value("lycolic_10ml_drop", 1)
	frm.set_value("stand_mf_60ml_susp", 1)
	frm.set_value("trygesic_tab", 1)
	frm.set_value("actirab_dv_cap", 1) 
	frm.set_value("lycorest_60ml_susp", 1)
	frm.set_value("stand_sp_tab", 1)
	frm.set_value("wego_gel_20mg", 1)
	frm.set_value("actirab_l_cap", 1)
	frm.set_value("lycorest_tab", 1)
	frm.set_value("stand_mf_plus", 1) 
	frm.set_value("wego_gel_30mg", 1)
	frm.set_value("empower_od_tab", 1)
	frm.set_value("lycort_1_ml_inj", 1)
	frm.set_value("star_t_tab", 1) 

}

function unselect_all_product(frm)
{
	frm.set_value("actirab_tab", 0)
	frm.set_value("glucolyst_g1_tab", 0)		
	frm.set_value("regain_xt_tab", 0)
	frm.set_value("ten_on_30_ml_syrup", 0)
	frm.set_value("actirab_d_cap", 0)
	frm.set_value("lycolic_10ml_drop", 0)
	frm.set_value("stand_mf_60ml_susp", 0)
	frm.set_value("trygesic_tab", 0)
	frm.set_value("actirab_dv_cap", 0) 
	frm.set_value("lycorest_60ml_susp", 0)
	frm.set_value("stand_sp_tab", 0)
	frm.set_value("wego_gel_20mg", 0)
	frm.set_value("actirab_l_cap", 0)
	frm.set_value("lycorest_tab", 0)
	frm.set_value("stand_mf_plus", 0) 
	frm.set_value("wego_gel_30mg", 0)
	frm.set_value("empower_od_tab", 0)
	frm.set_value("lycort_1_ml_inj", 0)
	frm.set_value("star_t_tab", 0)
}

/*---------------Select All Products END---------------------*/

/*---------------Products START---------------------*/

frappe.ui.form.on("Secondary report", "actirab_tab", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "glucolyst_g1_tab", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "regain_xt_tab", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "ten_on_30_ml_syrup", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "actirab_d_cap", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "lycolic_10ml_drop", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "stand_mf_60ml_susp", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "trygesic_tab", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "actirab_dv_cap", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "lycorest_60ml_susp", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "stand_sp_tab", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "wego_gel_20mg", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "actirab_l_cap", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "lycorest_tab", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "stand_mf_plus", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "wego_gel_30mg", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "empower_od_tab", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "lycort_1_ml_inj", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});
frappe.ui.form.on("Secondary report", "star_t_tab", function (frm) {
	//if(frm.doc.select_all==1)
	//{
		checked_select_all(frm);
	//}
	//else
	//{
		//unchecked_select_all(frm);
	//}	
});


function checked_select_all(frm)
{
	
	if(frm.doc.actirab_tab==1&&frm.doc.glucolyst_g1_tab==1&&frm.doc.regain_xt_tab==1&&frm.doc.ten_on_30_ml_syrup==1&&frm.doc.actirab_d_cap==1&&frm.doc.lycolic_10ml_drop==1&&frm.doc.stand_mf_60ml_susp==1&&frm.doc.trygesic_tab==1&&frm.doc.actirab_dv_cap==1&&frm.doc.lycorest_60ml_susp==1&&frm.doc.stand_sp_tab==1&&frm.doc.wego_gel_20mg==1&&frm.doc.actirab_l_cap==1&&frm.doc.lycorest_tab==1&&frm.doc.stand_mf_plus==1&&frm.doc.wego_gel_30mg==1&&frm.doc.empower_od_tab==1&&frm.doc.lycort_1_ml_inj==1&&frm.doc.star_t_tab==1)
	{
		frm.set_value("select_all", 1);
	}
	else
	{
		a=1;
		frm.set_value("select_all", 0);
	} 
}

function unselect_all_product1(frm)
{

	if(frm.doc.actirab_tab==0||frm.doc.glucolyst_g1_tab==0||frm.doc.regain_xt_tab==0||frm.doc.ten_on_30_ml_syrup==0&&frm.doc.actirab_d_cap==0&&frm.doc.lycolic_10ml_drop==0&&frm.doc.stand_mf_60ml_susp==0&&frm.doc.trygesic_tab==0&&frm.doc.actirab_dv_cap==0&&frm.doc.lycorest_60ml_susp==0&&frm.doc.stand_sp_tab==0&&frm.doc.wego_gel_20mg==0&&frm.doc.actirab_l_cap==0&&frm.doc.lycorest_tab==0&&frm.doc.stand_mf_plus==0&&frm.doc.wego_gel_30mg==0&&frm.doc.empower_od_tab==0&&frm.doc.lycort_1_ml_inj==0&&frm.doc.star_t_tab==0)
	{
		frm.set_value("select_all", 0);
	} 

}

/*---------------Products END---------------------*/

/*---------------Select Year 2017 START---------------------*/
var a2=0;
frappe.ui.form.on("Secondary report", "year_2017", function (frm) {
	if(frm.doc.year_2017==1)
	{
		//alert('hi');
		if(a2==0)
		{
			select_month_2017(frm);
		}
		////a2=0;
	}
	else
	{
		unselect_month_2017(frm);
		a2=0;
		//alert('yyy');
		////if(a2==0)
		////{
			//unselect_month_2017(frm);
		////}
		////alert(frm.doc.jan_2017);
	}	
});


function select_month_2017(frm)
{
	frm.set_value("jan_2017", 1)
	frm.set_value("feb_2017", 1)		
	frm.set_value("march_2017", 1)
	frm.set_value("apr_2017", 1)
	frm.set_value("may_2017", 1)
	frm.set_value("june_2017", 1)
	frm.set_value("july_2017", 1)
	frm.set_value("aug_2017", 1)
	frm.set_value("sept_2017", 1) 
	frm.set_value("oct_2017", 1)
	frm.set_value("nov_2017", 1)
	frm.set_value("dec_2017", 1)
}

function unselect_month_2017(frm)
{
	frm.set_value("jan_2017", 0)
	frm.set_value("feb_2017", 0)		
	frm.set_value("march_2017", 0)
	frm.set_value("apr_2017", 0)
	frm.set_value("may_2017", 0)
	frm.set_value("june_2017", 0)
	frm.set_value("july_2017", 0)
	frm.set_value("aug_2017", 0)
	frm.set_value("sept_2017", 0) 
	frm.set_value("oct_2017", 0)
	frm.set_value("nov_2017", 0)
	frm.set_value("dec_2017", 0)
}

/*---------------Select Year 2017 END---------------------*/

/*---------------Select Year 2017 Month START---------------------*/
frappe.ui.form.on("Secondary report", "jan_2017", function (frm) {
		checked_year_2017(frm);
});
frappe.ui.form.on("Secondary report", "july_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "feb_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "aug_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "march_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "sept_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "apr_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "oct_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "may_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "nov_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "june_2017", function (frm) {
		checked_year_2017(frm);	
});
frappe.ui.form.on("Secondary report", "dec_2017", function (frm) {
		checked_year_2017(frm);	
});


function checked_year_2017(frm)
{	
	if(frm.doc.jan_2017==1||frm.doc.july_2017==1||frm.doc.feb_2017==1||frm.doc.aug_2017==1||frm.doc.march_2017==1||frm.doc.sept_2017==1||frm.doc.apr_2017==1||frm.doc.oct_2017==1||frm.doc.may_2017==1||frm.doc.nov_2017==1||frm.doc.june_2017==1||frm.doc.dec_2017==1)
	{
		a2=1;
		frm.set_value("year_2017", 1);
	}
	else
	{
		//a2=1;
		frm.set_value("year_2017", 0);
	} 
}

/*---------------Select Year 2017 Month END---------------------*/

/*---------------Select Year 2018 START---------------------*/
var a3=0;
frappe.ui.form.on("Secondary report", "year_2018", function (frm) {
	if(frm.doc.year_2018==1)
	{
		//alert('hi');
		if(a3==0)
		{
			select_month_2018(frm);
		}
		////a3=0;
	}
	else
	{
		unselect_month_2018(frm);
		a3=0;
		//alert('yyy');
		////if(a3==0)
		////{
			//unselect_month_2018(frm);
		////}
		////alert(frm.doc.jan_2018);
	}		
});


function select_month_2018(frm)
{
	frm.set_value("jan_2018", 1)
	frm.set_value("feb_2018", 1)		
	frm.set_value("march_2018", 1)
	frm.set_value("apr_2018", 1)
	frm.set_value("may_2018", 1)
	frm.set_value("june_2018", 1)
	frm.set_value("july_2018", 1)
	frm.set_value("aug_2018", 1)
	frm.set_value("sept_2018", 1) 
	frm.set_value("oct_2018", 1)
	frm.set_value("nov_2018", 1)
	frm.set_value("dec_2018", 1)
}

function unselect_month_2018(frm)
{
	frm.set_value("jan_2018", 0)
	frm.set_value("feb_2018", 0)		
	frm.set_value("march_2018", 0)
	frm.set_value("apr_2018", 0)
	frm.set_value("may_2018", 0)
	frm.set_value("june_2018", 0)
	frm.set_value("july_2018", 0)
	frm.set_value("aug_2018", 0)
	frm.set_value("sept_2018", 0) 
	frm.set_value("oct_2018", 0)
	frm.set_value("nov_2018", 0)
	frm.set_value("dec_2018", 0)
}
/*---------------Select Year 2018 END---------------------*/

/*---------------Select Year 2018 Month START---------------------*/
frappe.ui.form.on("Secondary report", "jan_2018", function (frm) {
		checked_year_2018(frm);
});
frappe.ui.form.on("Secondary report", "july_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "feb_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "aug_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "march_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "sept_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "apr_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "oct_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "may_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "nov_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "june_2018", function (frm) {
		checked_year_2018(frm);	
});
frappe.ui.form.on("Secondary report", "dec_2018", function (frm) {
		checked_year_2018(frm);	
});


function checked_year_2018(frm)
{	
	if(frm.doc.jan_2018==1||frm.doc.july_2018==1||frm.doc.feb_2018==1||frm.doc.aug_2018==1||frm.doc.march_2018==1||frm.doc.sept_2018==1||frm.doc.apr_2018==1||frm.doc.oct_2018==1||frm.doc.may_2018==1||frm.doc.nov_2018==1||frm.doc.june_2018==1||frm.doc.dec_2018==1)
	{
		a3=1;
		frm.set_value("year_2018", 1);
	}
	else
	{
		//a3=1;
		frm.set_value("year_2018", 0);
	} 
}

/*---------------Select Year 2018 Month END---------------------*/

function get_stockist(frm)
{
	if(frm.doc.stockist==undefined||frm.doc.stockist=="")
	{
		//alert(frm.doc.stockist);
		string_stockist="";
		//alert('Select Stockist');
	}
	else
	{
		string_stockist=frm.doc.stockist;
	}
}

function get_product_value(frm)
{
    code="";
    if(frm.doc.actirab_d_cap==1)
    {
        code+="'ACTIRAB - D CAP',";
    }
    if(frm.doc.actirab_l_cap==1)
    {
        code+="'ACTIRAB - L CAP',";
    }
    if(frm.doc.actirab_dv_cap==1)
    {
        code+="'ACTIRAB -DV Cap',";
    }
    if(frm.doc.actirab_tab==1)
    {
        code+="'ACTIRAB TAB',";
    }
    if(frm.doc.empower_od_tab==1)
    {
        code+="'EMPOWER - OD TAB',";
    }
    if(frm.doc.glucolyst_g1_tab==1)
    {
        code+="'GLUCOLYST -G1 TAB',";
    }
    if(frm.doc.lycolic_10ml_drop==1)
    {
        code+="'LYCOLIC 10ml DROP',";
    }
    if(frm.doc.lycorest_60ml_susp==1)
    {
        code+="'LYCOREST 60ml SUSP',";
    }
    if(frm.doc.lycorest_tab==1)
    {
        code+="'LYCOREST TAB',";
    }
    if(frm.doc.lycort_1_ml_inj==1)
    {
        code+="'LYCORT 1 ml INJ',";
    }
    if(frm.doc.regain_xt_tab==1)
    {
        code+="'REGAIN - XT TAB',";
    }
    if(frm.doc.stand_mf_60ml_susp==1)
    {
        code+="'STAND - MF 60ml SUSP',";
    }
    if(frm.doc.stand_mf_plus==1)
    {
        code+="'STAND MF +',";
    }
    if(frm.doc.stand_sp_tab==1)
    {
        code+="'STAND -SP TAB',";
    }
    if(frm.doc.star_t_tab==1)
    {
        code+="'STAR T TAB',";
    }
    if(frm.doc.ten_on_30_ml_syrup==1)
    {
        code+="'TEN-ON 30 ml SYRUP',";
    }
    if(frm.doc.trygesic_tab==1)
    {
        code+="'TRYGESIC TAB',";
    }
    if(frm.doc.wego_gel_20mg==1)
    {
        code+="'WEGO GEL 20mg',";
    }
    if(frm.doc.wego_gel_30mg==1)
    {
        code+="'WEGO GEL 30mg',";
    }
    code=code==""?"":code.substr(0, code.length - 1);
}

function get_month_value(frm)
{
    string_month="";    

    /*------------------Year 2017----------------*/
    if(frm.doc.jan_2017==1)
    {
        string_month+="2017-Jan,";
    }
    if(frm.doc.feb_2017==1)
    {
        string_month+="2017-Feb,";
    }
    if(frm.doc.march_2017==1)
    {
        string_month+="2017-March,";
    }
    if(frm.doc.apr_2017==1)
    {
        string_month+="2017-Apr,";
    }
    if(frm.doc.may_2017==1)
    {
        string_month+="2017-May,";
    }
    if(frm.doc.june_2017==1)
    {
        string_month+="2017-June,";
    }
    if(frm.doc.july_2017==1)
    {
        string_month+="2017-July,";
    }
    if(frm.doc.aug_2017==1)
    {
        string_month+="2017-Aug,";
    }
    if(frm.doc.sept_2017==1)
    {
        string_month+="2017-Sept,";
    }
    if(frm.doc.oct_2017==1)
    {
        string_month+="2017-Oct,";
    }
    if(frm.doc.nov_2017==1)
    {
        string_month+="2017-Nov,";
    }
    if(frm.doc.dec_2017==1)
    {
        string_month+="2017-Dec,";
    }
    /*------------------Year 2018----------------*/
    if(frm.doc.jan_2018==1)
    {
        string_month+="2018-Jan,";
    }
    if(frm.doc.feb_2018==1)
    {
        string_month+="2018-Feb,";
    }
    if(frm.doc.march_2018==1)
    {
        string_month+="2018-March,";
    }
    if(frm.doc.apr_2018==1)
    {
        string_month+="2018-Apr,";
    }
    if(frm.doc.may_2018==1)
    {
        string_month+="2018-May,";
    }
    if(frm.doc.june_2018==1)
    {
        string_month+="2018-June,";
    }
    if(frm.doc.july_2018==1)
    {
        string_month+="2018-July,";
    }
    if(frm.doc.aug_2018==1)
    {
        string_month+="2017-Aug,";
    }
    if(frm.doc.sept_2018==1)
    {
        string_month+="2018-Sept,";
    }
    if(frm.doc.oct_2018==1)
    {
        string_month+="2018-Oct,";
    }
    if(frm.doc.nov_2018==1)
    {
        string_month+="2018-Nov,";
    }
    if(frm.doc.dec_2018==1)
    {
        string_month+="2018-Dec,";
    }

    string_month=string_month==""?"":string_month.substr(0, string_month.length - 1);
}


/*
function validation1(frm)
{
alert(frm.doc.stockist);

}*/

/*-------------Vin Sir Code----------------*/
function initialize1(frm,dataset){
alert(JSON.stringify(dataset));
   if (document.getElementById('chart'))
	{
	
	 let data = {
 	 labels: [ "Opening", "Primary/Received", "Closing", "Credit Note",
           "Sale"],
	datasets:dataset

/*  datasets: [
    {
       'values': [25, 50, 10, 15, 18, 32, 27],
      'title': "Opening"
     
    }
     ,
    {
      title: "Primary",
      values: [25, 50, 10, 15, 18, 32, 27]
    },
    {
      title: "Closing",
      values: [15, 20, 3, 15, 58, 12, 17]
    },
    {
      title: "Sale",
      values: [15, 66, 44, 15, 99, 12, 22]
    }
  ]
*/

 //datasets:dataset;
};

//alert(dataset.length);
//for(var i=0;i< dataset.length;i++)
//{
//data.datasets.push(dataset[0]);
//}
//
//alert(JSON.stringify(data));



let chart = new Chart({
  parent: "#chart", // or a DOM element
  title: "Secondary Summary Report(Fig In Bar)",
  data: data,
  type: 'bar', // or 'line', 'scatter', 'pie', 'percentage'
  height: 250,

  colors: ['#7cd6fd', 'violet', 'blue'],

  format_tooltip_x: d => (d + '').toUpperCase(),
  format_tooltip_y: d => d + ' Rs'
});
/*
let chart33 = new Chart({
  parent: "#chart3", // or a DOM element
  title: "Secondary Report(Fig In Pie)",
  data: data,
  type: 'pie', // or 'line', 'scatter', 'pie', 'percentage'
  height: 250,

  colors: ['#7cd6fd', 'violet', 'blue'],

  format_tooltip_x: d => (d + '').toUpperCase(),
  format_tooltip_y: d => d + ' Rs'
});
*/
	}
}

/*---  ;[ "July", "Aug", "Sept", "Oct","Nov","Dec","jan-2018"] string_month_lbl ['2017-Aug','2017-Sept','2017-Oct'],_lbl---*/
/*########################################*/

function tooltip_contents(d, defaultTitleFormat, defaultValueFormat, color) {
    var $$ = this, config = $$.config, CLASS = $$.CLASS,
        titleFormat = config.tooltip_format_title || defaultTitleFormat,
        nameFormat = config.tooltip_format_name || function (name) { return name; },
        valueFormat = config.tooltip_format_value || defaultValueFormat,
        text, i, title, value, name, bgcolor;
    
    // You can access all of data like this:
    console.log($$.data.targets);
    
    for (i = 0; i < d.length; i++) {
        if (! (d[i] && (d[i].value || d[i].value === 0))) { continue; }

        // ADD
        if (d[i].name === 'data2') { continue; }
        
        if (! text) {
            title = 'Secondary Details(In Rupees)'
            text = "<table class='" + CLASS.tooltip + "'>" + (title || title === 0 ? "<tr><th colspan='2'>" + title + "</th></tr>" : "");
        }

        name = nameFormat(d[i].name);
        value = valueFormat(d[i].value, d[i].ratio, d[i].id, d[i].index);
        bgcolor = $$.levelColor ? $$.levelColor(d[i].value) : color(d[i].id);

        text += "<tr class='" + CLASS.tooltipName + "-" + d[i].id + "'>";
        text += "<td class='name'><span style='background-color:" + bgcolor + "'></span>" + name + "</td>";
        text += "<td class='value'>" + value + "</td>";
        text += "</tr>";
    }
    return text + "</table>";   
}


/*########################################*/

function initialize(frm,dataset){

var array = ['x','Opening','Primary','Closing','Credit','Secondary'];
dataset.unshift(array);
//alert(JSON.stringify(dataset));

var chart = c3.generate({
    bindto: '#chart',
    data: {
	x : 'x',
        columns: dataset,
        type: 'bar'
    },
    bar: {
        width: {
            ratio: 0.5 
        }
        
    },
    axis: {
        x: {
            type: 'category',
            tick: {
                rotate: 0,
                multiline: false
            },
            height: 130
        }
    },
   tooltip: {
        contents: tooltip_contents
    }
});
}

function initialize2(frm,dataset){

//alert(JSON.stringify(dataset));

var array = string_month.split(",");
array.unshift("X");
//alert(JSON.stringify(array));
//alert("arr: "+array[0]);
dataset.unshift(array);
//alert(JSON.stringify(dataset));

var chart = c3.generate({
    bindto: '#chart2',
    data: {
        x : 'X',
        columns:dataset,
        type: 'bar',
        colors: {
            primary: '#ff7f0e',
            sale: '#ff0000',
            opening: '#00ff00',
            closing: '#0000ff',
            credit: '#9467bd',            
        },
        order: 'asc'
    },
    axis: {
        x: {
            type: 'category',
            tick: {
                rotate: 0,
                multiline: false
            },
            height: 130
        }
    },
    tooltip: {
        contents: tooltip_contents
    }
    
});   
 chart.title('Chart Details');
}

/*-----Arj code start-----*/

function initialize3(frm,dataset){
//alert(JSON.stringify(dataset));
var chart = c3.generate({
    bindto: '#chart4',
    data: {
        columns: dataset,
        type: 'bar'
    },
    tooltip: {
        contents: tooltip_contents
    }
});
}

function initialize4(frm,dataset){

//alert(JSON.stringify(dataset));

/*var chart = c3.generate({
    bindto: '#chart3',
    data: {
        // iris data from R
        columns: dataset,
        type : 'pie',
    }
});*/

var chart = c3.generate({
    bindto: '#chart3',
    exportEnabled :"1",
    data: {
        // iris data from R
        columns: dataset,
        type : 'donut'
    },
    donut: {
        title: "Secondary Details"
    }
});
}

/*-----Arj code end-----*/


function datasetreturn(frm){
//alert(string_stockist+"  "+code+"  "+string_month);
        
		frappe.call({
			method:'team.chart_secondary.get_date_and_app_support',
			args:{
				stockist_name:string_stockist,
				products:code,
				months:string_month
			},
			callback:function (r) {				
				initialize(frm,r.message);//getproductwise
			}
		      }); 
}

function datasetreturn_2(frm){    
		frappe.call({
			method:'team.chart_secondary.getmonthly',
			args:{
				stockist_name:string_stockist,
				products:code,
				months:string_month
			},
			callback:function (r) {
				//return r;
				//return r.message;
				//test= JSON.stringify(r.message]);
				//return datasets;
				//return r.message;
				//alert(JSON.stringify(r.message[0]["values"]));
				//return 	(JSON.stringify(r.message[0]["values"]));			
				initialize2(frm,r.message);				
				//return r.message;			
				//printDiv('chart');
				
				
			}
		      }); 
}

function datasetreturn_3(frm){   
		frappe.call({
			method:'team.chart_secondary.getproductwise',
			args:{
				stockist_name:string_stockist,
				products:code,
				months:string_month
			},
			callback:function (r) {	
				//alert(JSON.stringify(r.message[0]["values"]));		
				initialize3(frm,r.message);
			}
		      }); 
}

function datasetreturn_4(frm){   
		frappe.call({
			method:'team.chart_secondary.get_sec_details_for_pie',
			args:{
				stockist_name:string_stockist,
				products:code,
				months:string_month
			},
			callback:function (r) {	
				//alert(JSON.stringify(r.message[0]["values"]));		
				initialize4(frm,r.message);
			}
		      }); 
}


function objToString (obj) {
    var str = '';
    for (var p in obj) {
        if (obj.hasOwnProperty(p)) {
            str += p + '::' + obj[p] + '\n';
        }
    }
    alert(str.toString());
}
function loadjscssfile(filename, filetype) {
    if (filetype == "js") { //if filename is a external JavaScript file
        var fileref = document.createElement('script')
        fileref.setAttribute("type", "text/javascript")
        fileref.setAttribute("src", filename)
    } else if (filetype == "css") { //if filename is an external CSS file
        var fileref = document.createElement("link")
        fileref.setAttribute("rel", "stylesheet")
        fileref.setAttribute("type", "text/css")
        fileref.setAttribute("href", filename)
    }
    if (typeof fileref != "undefined")
        document.getElementsByTagName("head")[0].appendChild(fileref)
}

loadjscssfile("https://unpkg.com/frappe-charts@0.0.8/dist/frappe-charts.min.iife.js", "js");


