// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Secondary report', {
	refresh: function(frm) {

	}
});
frappe.ui.form.on("Secondary report", "btn_show", function (frm) {
//datasetreturn();
initialize(frm);
});

function initialize(frm){
   if (document.getElementById('chart'))
	{
	
	 let data = {
 	 labels: [ "July", "Aug", "Sept",
           "Oct", "Nov", "Dec", "Jan-2018"],
	datasets: []

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

 //datasets:datasetreturn();
};

alert(JSON.stringify(datasetreturn()));
//data.datasets.push(ee[0]);
//alert(JSON.stringify(data));



let chart = new Chart({
  parent: "#chart", // or a DOM element
  title: "Secondary Report",
  data: data,
  type: 'bar', // or 'line', 'scatter', 'pie', 'percentage'
  height: 250,

  colors: ['#7cd6fd', 'violet', 'blue'],

  format_tooltip_x: d => (d + '').toUpperCase(),
  format_tooltip_y: d => d + ' Qty'
});
	}
}

function datasetreturn()
{
//alert("sdff");
        
		frappe.call({
			method:'team.chart_secondary.get_date_and_app_support',
			
			callback:function (r) {
				//return r;
				//return r.message;
				//test= JSON.stringify(r.message]);
				//return datasets;
				//return r.message;
				//alert(JSON.stringify(r.message[0]["values"]));
				//return 	(JSON.stringify(r.message[0]["values"]));
				 				
				return r.message;			
				
				
				
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
