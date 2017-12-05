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
		add_child_rows(frm);
				
	}
		
});

add_child_rows= function(frm) {
	var tbl = frm.doc.execution_excellence_table || [];
	var i = tbl.length;
	while (i--){ 
	for (var i=0; i< 12; i++) {
		var row = frappe.model.add_child(frm.doc, frm.fields_dict.execution_excellence_table.df.options,
						 frm.fields_dict.execution_excellence_table.df.fieldname);
		
		row.month = get_month(i);
		row.total_days_month = "30";
		row.holidays = "5";
		row.working = "25";

		
	}
       
	}
	 frm.refresh_field('execution_excellence_table');
};

remove_child_rows= function(frm) {
	var tbl = frm.doc.execution_excellence_table || [];
	var i = tbl.length;
	while (i--){ 
	
          frm.get_field("execution_excellence_table").grid.grid_rows[i].remove();
	}
	 frm.refresh_field('execution_excellence_table');
};
get_month=function(i)
{
	if(i==0)
	{
		return "April";
	}else if(i==1)
	{
		return "May";
	}else if(i==2)
	{
		return "June";
	}else if(i==3)
	{
		return "July";
	}
	else if(i==4)
	{
		return "Aug";
	}
	else if(i==5)
	{
		return "Sept";
	}
	else if(i==6)
	{
		return "Oct";
	}
	else if(i==7)
	{
		return "Nov";
	}
	else if(i==8)
	{
		return "Dec";
	}
	else if(i==9)
	{
		return "Jan";
	}
	else if(i==10)
	{
		return "Feb";
	}else if(i==11)
	{
		return "Mar";
	}
};

