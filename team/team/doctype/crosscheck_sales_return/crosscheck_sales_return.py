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
def get_date_and_app_support(sr):
	sr="'"+sr+"'"
	sr_amount='';
	qry= frappe.db.sql(""" SELECT name,branch,rounded_total,posting_date ,rounded_total FROM 1bd3e0294da19198.`tabSales Invoice`
where docstatus<2 and `name`={0}""".format(sr), as_dict=1)
	if len(qry) > 0:
		sr_amount = qry[0].rounded_total;
		pass
	
	details='';
	details= frappe.db.sql(""" SELECT name,branch,rounded_total,posting_date ,rounded_total FROM 1bd3e0294da19198.`tabSales Invoice`
where docstatus<2 and `name`={0}""".format(sr), as_dict=1)
	dict = {'details': '',
		'sr_amount': '' 
          }
	dict['details'] = details;
	dict['sr_amount'] = sr_amount;
	return dict;
	
