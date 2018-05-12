// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('TP Months for App', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		frappe.ui.form.on("TP Months for App", "add_users", function(frm, cdt, cdn) 
		{
			if(frm.doc.active==true){
			add_user(frm,cdt,cdn);
			}
			
				
		});
		frappe.ui.form.on("TP Months for App", "temp_btn", function(frm, cdt, cdn) 
		{
			
			test(frm,cdt,cdn);
			
			
				
		});
	}
});
add_user= function(frm,cdt,cdn) {
		frappe.call({
			method:'team.team.doctype.tp_months_for_app.tp_months_for_app.get_user',
			args:{
				branch: frm.doc.branch,
				
			},
			callback:function (r) {
				
				var active_users = $.map(frm.doc.active_users, function(d) { return d.active_users });
				//alert(sec_items_qty );
				for (var i=0; i< r.message.length; i++) {
					
					if (active_users.indexOf(r.message[i].name) === -1) {
						
						
					        if(check_duplicate(frm,r.message[i].name) != false)
					        {
							var row = frappe.model.add_child(frm.doc, frm.fields_dict.active_users.df.options, frm.fields_dict.active_users.df.fieldname);
							row.user_id = r.message[i].name;
							row.user_name = r.message[i].full_name ;
						}
						else
						{
							
						}
					}
				}
						
				frm.refresh_field('active_users');
			}
		});
		
		
};
			    
			
check_duplicate= function(frm,check_user_id) {
		//alert("hii");
		//var sec_items_qty = $.map(frm.doc.sec_items_qty, function(d) { return d.sec_item_qty });
		flag=true;
		var tbl1 = frm.doc.active_users || [];
		var strr="";
		//var total_earn = 0; var total_ded = 0;
	        for(var i = 0; i < tbl1.length; i++)
		{
			if(check_user_id==tbl1[i].user_id)
				flag=false;;
			
		  //strr=strr+" ... "+ tbl1[i].item_code;
	        }
		return flag;
		
		
	};
			
	
test= function(frm,cdt,cdn) {
		frappe.call({
			method:'team.team.doctype.tp_months_for_app.tp_months_for_app.test',
			args:{
				test_email: frm.doc.test_email,
				
			},
			callback:function (r) {
				
				frappe.msgprint(__(r));	
			}
		});
		
		
};

