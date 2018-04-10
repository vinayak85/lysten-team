// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Standard Tour Plan', {
	refresh: function(frm) {

	}
	setup: function(frm) {
		frm.set_query("user", function() {		

			return {
				filters: {
					
					"enabled": 1,
					"company": frm.doc.company
				}
			}
		});
});


