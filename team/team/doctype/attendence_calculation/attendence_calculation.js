// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt
//get_calculations

frappe.ui.form.on('Attendence Calculation', {
	refresh: function(frm) {
		frm.add_custom_button(__("Recalculate Attendence"),
			function() { frm.trigger('get_items_all'); }, "fa fa-sitemap", "btn-default");
	},
	get_items_all:function (frm) {
		
		frappe.call({
			method:'team.team.doctype.attendence_calculation.attendence_calculation.get_calculations',
			args:{
				fromdate: frm.doc.month,
				todate: frm.doc.year
				
			},
			callback:function (r) {
				alert("1");
				var attendence_tables = $.map(frm.doc.attendence_table, function(d) { return d.attendence_table });
				alert("2");
				for (var i=0; i< r.message.length; i++) {
					alert("3");
					if (attendence_tables.indexOf(r.message[i].att_date) === -1) {
					      
						alert("4");
						row.att_date = r.message[i].att_date;
						row.emp_code = r.message[i].emp_code;
						row.email = r.message[i].email;
						
						row.app_presenty = r.message[i].app_presenty;
						row.lysten_presenty = r.message[i].lysten_presenty;
						row.objective = r.message[i].objective;
					
						row.working_flag = r.message[i].working_flag;
						row.dcr = r.message[i].dcr;
						row.chem_call = r.message[i].chem_call;
						row.meeting = r.message[i].meeting;
						row.camp = r.message[i].camp;
						row.lve = r.message[i].lve;
						
						
				
					}					
					
				}
				frm.refresh_field('attendence_table');
				
				
			}
		})
		
	}
	});
	

