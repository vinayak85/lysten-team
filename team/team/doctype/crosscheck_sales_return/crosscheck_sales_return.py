# -*- coding: utf-8 -*-
# Copyright (c) 2019, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.model.document import Document

class CrossCheckSalesReturn(Document):
	pass

@frappe.whitelist()
def get_crosscheck_data(sr):
	sr="'"+sr+"'"
	sr_amount='';
	qry= frappe.db.sql(""" SELECT name,branch,rounded_total,posting_date ,rounded_total FROM 1bd3e0294da19198.`tabSales Invoice`
where docstatus<2 and `name`={0}""".format(sr), as_dict=1)
	if len(qry) > 0:
		sr_amount = qry[0].rounded_total;
		pass
	
	details='';
	details= frappe.db.sql(""" SELECT distinct(against_invoice_) as ai FROM 1bd3e0294da19198.`tabSales Invoice Item`
where parent={0}""".format(sr), as_dict=1)
	datasets = [];
	datasets1 = [];
	
	for f in details:
		datasets1=[];
		f=f.ai;
		f="'"+f+"'";
		cnt1 = frappe.db.sql(""" SELECT count(name) as cnt1 FROM 1bd3e0294da19198.`tabSales Invoice Item`
		where against_invoice_={0}""".format(f), as_dict=1)
		
		crn=frappe.db.sql(""" select name,new_credit_note_number  FROM 1bd3e0294da19198.`tabSales Invoice` where ref_return={0}
		and return_against={1} and docstatus < 2""".format(sr,f), as_dict=1)
		crn_number='';
		if len(crn) > 0:
			crn_number = crn[0].new_credit_note_number+" ("+crn[0].name+")";
			pass
		else:
			crn_number="-"
		
		datasets1.append(f);      
     	   	datasets1.append(cnt1[0].cnt1);
		datasets1.append(crn_number);
		datasets.append(datasets1);
		pass;
	
	
	
	
	
	
	dict = {'details': '',
		'sr_amount': '' 
          }
	dict['details'] = datasets;
	dict['sr_amount'] = sr_amount;
	return dict;
	
