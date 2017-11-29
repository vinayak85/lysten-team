// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Secondary', {
	refresh: function(frm) {
		
		frm.add_custom_button(__("Recalculate Secondary"),
			function() { frm.trigger('get_items_all'); }, "fa fa-sitemap", "btn-default");
		
		frm.add_custom_button(__("test"),
			function() { frm.trigger('test'); }, "fa fa-sitemap", "btn-default");

	},
	
	get_items_all:function (frm) {
		var filters=[["used_for_secondary","=","1"]];
		frappe.call({
			method:'team.team.doctype.secondary.secondary.get_items',
			args:{
				filters: filters
			},
			callback:function (r) {
				//alert(r.message[1].name);
				var sec_items_qty = $.map(frm.doc.sec_items_qty, function(d) { return d.sec_item_qty });
				//alert(sec_items_qty );
				for (var i=0; i< r.message.length; i++) {
					if (sec_items_qty.indexOf(r.message[i].name) === -1) {
						var row = frappe.model.add_child(frm.doc, frm.fields_dict.sec_items_qty.df.options, frm.fields_dict.sec_items_qty.df.fieldname);
						row.item_code = r.message[i].name;
						row.item_code = r.message[i].item_name;
						
					}
				}
				frm.refresh_field('sec_items_qty');
				
				
			}
		})
		
	},
	
	test:function (frm,check_item_name) {
		//alert("hii");
		//var sec_items_qty = $.map(frm.doc.sec_items_qty, function(d) { return d.sec_item_qty });
		var tbl1 = frm.doc.sec_items_qty || [];
		var strr="";
		//var total_earn = 0; var total_ded = 0;
	        for(var i = 0; i < 3; i++)
		{
		  strr=strr+" ... "+ tbl1[i].item_code;
	        }
		alert(strr);
		
		
	},
});
