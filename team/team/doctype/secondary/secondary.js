// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Secondary', {
	refresh: function(frm) {
		
		frm.add_custom_button(__("Recalculate Secondary"),
			function() { frm.trigger('get_items_all'); }, "fa fa-sitemap", "btn-default");

	},
	
	get_items_all:function (frm) {
		var filters = "";
		frappe.call({
			method:'team.team.doctype.secondary.secondary.get_items',
			args:{
				
			},
			callback:function (r) {
				var sec_item_qty = $.map(frm.doc.sec_item_qty, function(d) { return d.item });
				for (var i=0; i< r.message.length; i++) {
					if (sec_item_qty.indexOf(r.message[i].name) === -1) {
						var row = frappe.model.add_child(frm.doc, frm.fields_dict.sec_item_qty.df.options, frm.fields_dict.sec_item_qty.df.fieldname);
						row.employee = r.message[i].name;
						row.item_code = r.message[i].item_code;
						
					}
				}
				frm.refresh_field('sec_item_qty');
				
			}
		})
		
	},
});
