// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Secondary', {
	refresh: function(frm) {
		
		frm.add_custom_button(__("Recalculate Secondary"),
			function() { frm.trigger('get_items_all'); }, "fa fa-sitemap", "btn-default");

	},
	
	get_items_all:function (frm) {
		var filters ;
		frappe.call({
			method:'team.team.doctype.secondary.secondary.get_items',
			args:{
				
			},
			callback:function (r) {
				alert("hello");
				
			}
		})
		
	},
});
