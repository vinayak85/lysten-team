// Copyright (c) 2019, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('CrossCheck Sales Return', {
	refresh: function(frm) {

	},
	onload: function(frm) {
	frappe.ui.form.on("CrossCheck Sales Return", "crosscheck", function(frm, cdt, cdn) 
		{
		//get_crosscheck_data
		//alert("ttt");
		frappe.call({
			method:'team.team.doctype.crosscheck_sales_return.crosscheck_sales_return.get_crosscheck_data',
			args:{
				sr:frm.doc.enter_sales_return				
			},
			callback:function (r) {	
				//alert(JSON.stringify(r.message));
				frm.doc.sr_amount=r.message.sr_amount;				
				frm.refresh_field('sr_amount');
				frm.doc.credit_notes_sum_amount=r.message.sum_rounded_total;				
				frm.refresh_field('credit_notes_sum_amount');
				frm.doc.match=r.message.match;				
				frm.refresh_field('match');
				frm.refresh_field('br');
				frm.reload_doc();
				test(frm,r.message.details);
				
			}
		      }); 
			
			
		});
	}
});

test= function(frm,dt) {
		//var tbl1 = frm.doc.table_4 || [];
	      
		//tbl1.splice(0,tbl1.length);
	        //frm.refresh_field('table_4');
	      var test = '<table style="width:600px" border="1px"><thead><tr><th style="width:35%">Against Invoice </th> <th style="width:5%">Items</th> <th style="width:35%">Credit Note</th> <th style="width:5%">Items</th> <th style="width:20%">Match</th> <tr></thead><tbody>';
    var tr='';
    for(var i=0;i<dt.length;i++){
        tr += '<tr>';
        for(var j=0;j<5;j++){
            tr += '<td>'+dt[i][j]+'</td>';
            }
        }
        tr +='</tr>';
    test += tr;
	
	     
	$(frm.fields_dict.tm.wrapper).html(test)
	//frm.refresh_field('tm');
	//frm.reload_doc();
	   
	 
	
	 
		
		
		
	};


