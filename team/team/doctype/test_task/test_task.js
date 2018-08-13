// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('test_task', {
	refresh: function(frm) {

	},
	btn1: function (frm) {
		
		frappe.call({
			method:'team.team.doctype.test_task.test_task.btn_1_job',
			args:{
				
			},
			callback:function (r) {
				alert('hii');	
			}
		});
		         
	},
	btn2: function (frm) {
		
		frappe.call({
			method:'team.team.doctype.test_task.test_task.btn_2_job',
			args:{
				
			},
			callback:function (r) {
				alert(r);	
			}
		});
		         
	}

});
