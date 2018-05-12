// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('TP Months for App', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		frappe.ui.form.on("TP Months for App", "active", function(frm, cdt, cdn) 
		{
			
			test(frm,cdt,cdn);
			
				
		});
	}
});
test= function(frm,cdt,cdn) {
		alert("hii");
		
		
};

