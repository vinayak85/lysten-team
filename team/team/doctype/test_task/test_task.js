// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('test_task', {
	refresh: function(frm) {

	},
	btn1: function (frm) {
		
		frappe.call({
			method:'team.team.doctype.test_task.test_task.test_start',
			args:{
				
			},
			callback:function (r) {
				alert('hii');	
			});
		         
	}

});
