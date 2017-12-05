// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Execution Excellence', {
	refresh: function(frm) {
		frm.add_custom_button(__("Recalculate Execution Data"),
			function() { frm.trigger('get_data'); }, "fa fa-sitemap", "btn-default");
	},
	
	get_data:function (frm) {
		//alert("hiii");
		remove_child_rows();
				
	}
		
});

remove_child_rows= function(frm) {
var tbl = doc.child_table || [];
var i = tbl.length;
while (i--)
{
    if(tbl[i].field_name == '')
    {
        frm.get_field("execution_excellence_table").grid.grid_rows[i].remove();
    }
}
frm.refresh();
};
