// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Call Summary Report', {
	refresh: function(frm) {

	}
});

/************* Code Added On 21/02/2018 **************/

var str_minutes=0;

frappe.ui.form.on("Call Summary Report", {
    refresh: function(frm) {
       frm.add_custom_button(__("Print"),
			function() { frm.trigger('print_form'); }, "fa fa-sitemap", "btn-default");
    },
print_form:function (frm) {

/************ Append Code For Chart Printing Correctly START*************/

var nodeList = document.getElementById('chart1').querySelector('svg').querySelectorAll('.c3-chart path');
    var nodeList2 = document.getElementById('chart1').querySelector('svg').querySelectorAll('.c3-axis path');
    var nodeList3 = document.getElementById('chart1').querySelector('svg').querySelectorAll('.c3 line');
    var line_graph = Array.from(nodeList);
    var x_and_y = Array.from(nodeList2).concat(Array.from(nodeList3));
    line_graph.forEach(function(element){
        element.style.fill = "none";
    })
    x_and_y.forEach(function(element){
        element.style.fill = "none";
        element.style.stroke = "black";
    })

/************ Append Code For Chart Printing Correctly END*************/

 printDiv("abc") 
}
});

function printDiv(divName) {
     //var printContents = document.getElementById('chart').innerHTML;
     var originalContents = document.body.innerHTML;
/*---*/
var printContents = document.getElementById('chart1').innerHTML ;
		    /*+ "<br/>" +document.getElementById('chart2').innerHTML
		    + "<br/>" +document.getElementById('chart3').innerHTML
		    + "<br/>" +document.getElementById('chart4').innerHTML;*/		   

/*----*/
	var pop = window.open();
	pop.document.body.innerHTML = printContents;

     //document.body.innerHTML = printContents;
     //window.print();
     //document.body.innerHTML = originalContents;
}

frappe.ui.form.on("Call Summary Report", "btn_show", function (frm) {
	get_minutes(frm);
	var x = new Date(frm.doc.from);
	var y = new Date(frm.doc.to);
	if(y>=x)
	{

		var timeDiff = Math.abs(y.getTime() - x.getTime());
		var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24)); 
		//alert(diffDays);
		if(diffDays <=10)
		{
			//msgprint(__("Date Okk"));	
			if(str_minutes>0)
			{
				call_report(frm);
			}	
			else
			{
				msgprint(__("MUST BE SELECT ATLEAST 1 TIME INTERVAL"));
			}
		}
		else
		{
			msgprint(__("MUST BE CHOOSE FROM-TO DATE LESS THAN 10 DAYS"));
		}
	}
	else
	{
		msgprint(__("MUST BE TO DATE GREATER THAN FROM DATE"));
	}	
});

function get_minutes(frm)
{
	if(frm.doc.half_hour==1)
	{
		str_minutes=30;
	}
	else if(frm.doc.one_hour==1)
	{
		str_minutes=60;
	}
	else if(frm.doc.two_hour==1)
	{
		str_minutes=120;
	}

}

frappe.ui.form.on("Call Summary Report", "half_hour", function (frm) {
	if(frm.doc.half_hour==1)
	{
		frm.set_value("one_hour", 0)
		frm.set_value("two_hour", 0)
		str_minutes=30;
	}
	else
	{
		str_minutes=0;
	}
	
});

frappe.ui.form.on("Call Summary Report", "one_hour", function (frm) {
	if(frm.doc.one_hour==1)
	{
		frm.set_value("half_hour", 0)
		frm.set_value("two_hour", 0)
		str_minutes=60;
	}
	else
	{
		str_minutes=0;
	}
	
});

frappe.ui.form.on("Call Summary Report", "two_hour", function (frm) {
	if(frm.doc.two_hour==1)
	{
		frm.set_value("half_hour", 0)
		frm.set_value("one_hour", 0)
		str_minutes=120;
	}
	else
	{
		str_minutes=0;
	}
	
});

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
        //text += "<td class='name'><span style='background-color:" + bgcolor + "'></span>" + name + "</td>";
        text += "<td class='value'>" + value + "</td>";
        text += "</tr>";
    }
    return text + "</table>";   
}


/*########################################*/


function initialize(frm,dataset){

var myarray = dataset.shift();;  

//alert(myarray);
//alert(JSON.stringify(dataset));
//alert(JSON.stringify(dataset));bindto: '#chart1',

var chart = c3.generate({
bindto: '#chart1',
    data: {
        columns: dataset,
    },
    axis: {
        x: {
            type: 'category',
            categories: myarray	  
        }
    }
});


}


function call_report(frm){  
/*
frmdt:'2018-01-04',
todt:'2018-01-06',
inttime:'60',
wrkstrttime:'08:00:00',
wrkendtime:'21:00:00'

var x = new Date(frm.doc.from);
var y = new Date(frm.doc.to);
method:'team.chart_report_employee_calls.get_call_summary',*/

		frappe.call({
			method:'team.team.doctype.call_summary_report.call_summary_report.get_call_summary',			
			args:{
				frmdt:frm.doc.from,
				todt:frm.doc.to,
				inttime:str_minutes,
				wrkstrttime:'08:00:00',
				wrkendtime:'21:00:00'
			},
			callback:function (r) {				
				initialize(frm,r.message);//getproductwise
			}
		      }); 
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
