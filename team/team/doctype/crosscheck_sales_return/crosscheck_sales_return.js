// Copyright (c) 2019, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('CrossCheck Sales Return', {
	refresh: function(frm) {

	},
	onload: function(frm) {
	frappe.ui.form.on("CrossCheck Sales Return", "crosscheck", function(frm, cdt, cdn) 
		{
		//get_crosscheck_data
		alert("ttt");
		frappe.call({
			method:'team.team.doctype.crosscheck_sales_return.crosscheck_sales_return.get_crosscheck_data',
			args:{
				sr:frm.doc.enter_sales_return				
			},
			callback:function (r) {	
				//alert(JSON.stringify(r.message));
				frm.doc.sr_amount=r.message.sum_rounded_total;
				
			}
		      }); 
			
			
		});
	}
});

