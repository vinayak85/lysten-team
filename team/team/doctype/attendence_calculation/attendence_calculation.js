// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt
//get_calculations

frappe.ui.form.on('Attendence Calculation', {
	refresh: function(frm) {
		frm.add_custom_button(__("Recalculate Attendence"),
			function() { frm.trigger('get_attendence'); }, "fa fa-sitemap", "btn-default");
	},
	get_attendence:function (frm) {
		
		frappe.call({
			method:'team.team.doctype.attendence_calculation.attendence_calculation.get_calculations',			
			args:{
				fromdate:"2017/11/01",
				todate: "2017/11/05"
				
			},
			callback:function (r) 
			{
				
				
			}
		})
		
	}
	});
	

