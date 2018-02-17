// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Standard Tour Plan', {
	refresh: function(frm) {

	}	
});

frappe.ui.form.on("Standard Tour Plan", "onload", function(frm) {
    cur_frm.fields_dict['stp_user'].get_query = function(doc) {
	return {
		filters: {
			"email": 'vinupatil9@gmail.com'
		}
	}
   }
});
