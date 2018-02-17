// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Standard Tour Plan', {
	refresh: function(frm) {

	}	
});

frappe.ui.form.on("Standard Tour Plan", "onload", function(frm) {
    cur_frm.set_query("stp_user", function() {
        return {
            filters: [
		    ['user', 'type', '=', 'Employee']
	    ]
        };
    });
});
