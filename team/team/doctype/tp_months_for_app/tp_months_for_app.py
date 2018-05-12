# -*- coding: utf-8 -*-
# Copyright (c) 2018, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
from frappe.model.document import Document

class TPMonthsforApp(Document):
	pass

@frappe.whitelist()
def get_user(branch):
	branch="'"+branch+"'";
	
	return frappe.db.sql("""SELECT name,full_name FROM 1bd3e0294da19198.tabUser
where enabled=1 and branch={0}""".format(branch), as_dict=1);


@frappe.whitelist()
def test(test_email):
	datasets = []; 
	test_email="'"+test_email+"'";
	tp_months_found=frappe.db.sql("""select concat(year,"-",if(month<10,concat('0',month),month))as "yyyy-mm" 
	from `tabTP Months for App` where active=1 and name in(select parent from `tabTP Months Active user`
	where user_id={0})""".format(test_email), as_dict=1);
	
	for f in tp_months_found:
		datasets1=[];		
        	frappe.msgprint(_(ff[0]));
		pass;
	
        
    

