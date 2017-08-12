// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('testing', {
	refresh: function(frm) {
		alert('ref');
	},
	btn1: function(frm) {
		alert('hi');		
	}
	
});
