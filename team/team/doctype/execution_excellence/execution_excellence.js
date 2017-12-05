// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Execution Excellence', {
	refresh: function(frm) {
		frm.add_custom_button(__("Recalculate Execution Data"),
			function() { frm.trigger('get_data'); }, "fa fa-sitemap", "btn-default");
	},
	
	get_data:function (frm) {
		//alert("hiii");
		remove_child_rows(frm);
				
	}
		
});

remove_child_rows= function(frm) {
	var tbl = frm.doc.execution_excellence_table || [];
	var i = tbl.length;
	while (i--){ 
	//for (var i=0; i< 12; i++) {
	alert(	get_month(0));
	//}
        frm.get_field("execution_excellence_table").grid.grid_rows[i].remove();
	}
	 frm.refresh_field('execution_excellence_table');
};
get_month=function(i)
{
	if(i==0)
	{
		return "April";
	}
};

