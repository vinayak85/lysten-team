// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Secondary', {
	refresh: function(frm) {
		
		
		frm.add_custom_button(__("Recalculate Secondary"),
			function() { frm.trigger('get_items_all'); }, "fa fa-sitemap", "btn-default");
		
		frm.add_custom_button(__("test"),
			function() { frm.trigger('test'); }, "fa fa-sitemap", "btn-default");

	},
	/*onload: function(frm) {
		
		frappe.ui.form.on("Secondary", "year", function(frm, cdt, cdn) 
		{
			//alert("hello");
			//frm.set_value("sec_items_qty[0].value_tot","200");
			//frappe.model.set_value("Secondary", "sec_items_qty[0]", "value_tot", "100");
			//change_select(frm);
			var tbl1 = frm.doc.sec_items_qty || [];
			 tbl1[0].opn_tot =tbl1[0].opn_tot +2;
			frm.refresh_field('sec_items_qty');
			
		});

	},*/
	test:function (frm) {
		
		frappe.call({
			method:'team.team.doctype.secondary.secondary.get_items1',
			args:{
				
			},
			callback:function (r) {
				
			}
		});
	},
				
	
	get_items_all:function (frm) {
		var filters=[["used_for_secondary","=","1"]];
		frappe.call({
			method:'team.team.doctype.secondary.secondary.get_items',
			args:{
				year: frm.doc.year,
				month: frm.doc.month,
				stockist: frm.doc.stockist
			},
			callback:function (r) {
				//alert(r.message[1].name);
				var sec_items_qty = $.map(frm.doc.sec_items_qty, function(d) { return d.sec_item_qty });
				//alert(sec_items_qty );
				for (var i=0; i< r.message.length; i++) {
					
					if (sec_items_qty.indexOf(r.message[i].name) === -1) {
						
					        if(test(frm,r.message[i].item_name) != false)
					        {
						
						var row = frappe.model.add_child(frm.doc, frm.fields_dict.sec_items_qty.df.options, frm.fields_dict.sec_items_qty.df.fieldname);
						row.item_code2 = r.message[i].name;
						row.item_code2 = r.message[i].item_name;
						
						var avg_sell_rate=r.message[i].avg_rate
						var avg_credit_rate=r.message[i].cr_avg_rate
						if(avg_credit_rate<=0){
							row.item_rate = avg_sell_rate;
						}
						else
						{
							row.item_rate =avg_credit_rate;
						}	
						
						row.opn_tot = r.message[i].close_tot;
						row.opn_qty = r.message[i].close_qty;
						row.opn_free = r.message[i].close_free;
							
						row.rec_tot = r.message[i].tot_qty;
						row.rec_qty = r.message[i].qty;
						row.rec_free = r.message[i].f_qty;
						
						row.value_credit_note_tot = r.message[i].cr_q_amt;
						row.value_credit_note_qty = r.message[i].cr_q_amt;
						row.value_credit_note_free = r.message[i].cr_f_amt;
					
						//row.value_sale_tot = r.message[i].q_amt;
						//row.value_sale_qty = r.message[i].q_amt;
						//row.value_sale_free = r.message[i].f_amt;
						
						}
					        else
					        {
							//alert('yes:'+ r.message[i].item_name);
							var tbl1 = frm.doc.sec_items_qty || [];
							ii=test1(frm,r.message[i].item_name);
							
							var avg_sell_rate=r.message[i].avg_rate
							var avg_credit_rate=r.message[i].cr_avg_rate
							if(avg_credit_rate<=0){
							 tbl1[ii].item_rate = avg_sell_rate;
							}
							else
							{
							 tbl1[ii].item_rate =avg_credit_rate;
							}
							
		                                 	
							tbl1[ii].opn_tot = r.message[i].close_tot;
							tbl1[ii].opn_qty = r.message[i].close_qty;
							tbl1[ii].opn_free = r.message[i].close_free;
							
		  			               	tbl1[ii].rec_tot = r.message[i].tot_qty;
							tbl1[ii].rec_qty = r.message[i].qty;
							tbl1[ii].rec_free = r.message[i].f_qty;
						
							tbl1[ii].value_credit_note_tot = r.message[i].cr_q_amt;
							tbl1[ii].value_credit_note_qty = r.message[i].cr_q_amt;
							tbl1[ii].value_credit_note_free = r.message[i].cr_f_amt;
					
							//tbl1[ii].value_sale_tot = r.message[i].q_amt;
							//tbl1[ii].value_sale_qty = r.message[i].q_amt;
							//tbl1[ii].value_sale_free = r.message[i].f_amt;
							/*alert('mmm:'+ r.message[i].item_name+'nnn:'+ r.message[i].item_name);*/
								
						
					        }	
				
					}					
					
				}
				frm.refresh_field('sec_items_qty');
				
				
			}
		})
		
	}
	});

/*
	frappe.ui.form.on("Secondary", {onload: function(frm) {
		frappe.ui.form.on("Secondary", "year", function(frm, cdt, cdn) 
		{
			var tbl1 = frm.doc.sec_items_qty || [];
			tbl1[0].opn_tot = 1+tbl1[0].opn_tot;
			//frm.set_value("sec_items_qty[0].value_tot","200");
			//frappe.model.set_value("Secondary", "sec_items_qty[0]", "value_tot", "100");
			//change_select(frm);
		});
		frappe.ui.form.on("Secondary", "month", function(frm, cdt, cdn)  
		{
			
			change_select(frm);
		});        
		frappe.ui.form.on("Secondary", "stockist", function(frm, cdt, cdn)  
		{
			check_duplicate_item(frm);
            		//change_select(frm);    
        	});  
		frappe.ui.form.on("sec_item_qty", "close_tot", function(frm, cdt, cdn)  
		{
			calculate_item_row(frm);
        	});

	}});          

	change_select=function (frm)
	{
		old_name=frm.doc.name;
		new_name=frm.doc.year+"-"+frm.doc.month+"-"+frm.doc.stockist
		if(old_name!=new_name)
		{
		     frappe.call({
			method:'team.team.doctype.secondary.secondary.check_duplicate',
			args:{
				year: frm.doc.year,
				month: frm.doc.month,
				stockist: frm.doc.stockist
			},
			callback:function (r) {
				
				
				if(r.message.count==1)
				{					
				frappe.msgprint(__('Secondory Record Alredy Exist for '+ 	
                                              frm.doc.year+"-"+frm.doc.month+"-"+frm.doc.stockist));	
				}
			}
		      }); 
		}
		else
		{
			//alert("not changed");
		}
		//alert(frm.doc.year+"---"+frm.doc.month+"----"+frm.doc.stockist);
		
	 
	};



*/
	
	test= function(frm,check_item_name) {
		//alert("hii");
		//var sec_items_qty = $.map(frm.doc.sec_items_qty, function(d) { return d.sec_item_qty });
		flag=true;
		var tbl1 = frm.doc.sec_items_qty || [];
		var strr="";
		//var total_earn = 0; var total_ded = 0;
	        for(var i = 0; i < tbl1.length; i++)
		{
			if(check_item_name==tbl1[i].item_code2)
				flag=false;;
			
		  //strr=strr+" ... "+ tbl1[i].item_code;
	        }
		return flag;
		
		
	};

      test1= function(frm,check_item_name) {		
		
		var tbl1 = frm.doc.sec_items_qty || [];
		var strr="";
		//var total_earn = 0; var total_ded = 0;
	        for(var i = 0; i < tbl1.length; i++)
		{
			if(check_item_name==tbl1[i].item_code2)
				return i;
			
		  //strr=strr+" ... "+ tbl1[i].item_code;
	        }
				
		
	};

