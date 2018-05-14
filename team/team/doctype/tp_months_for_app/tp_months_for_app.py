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
	tp_months_found=frappe.db.sql("""select concat(year,"-",if(month<10,concat('0',month),month))as "ym" 
	from `tabTP Months for App` where active=1 and name in(select parent from `tabTP Months Active user`
	where user_id={0})""".format(test_email), as_dict=1);
	
	for f in tp_months_found:
		datasets1=[];		
        	#frappe.msgprint(_(f.ym));
		datasets1.append(f.ym);
		ym="'"+f.ym+"'";
		days=frappe.db.sql(""" SELECT DAY(LAST_DAY(concat({0},'-01'))) as "dd" """.format(ym), as_dict=1);
		holiday_sun_cnt=frappe.db.sql("""SELECT count(case when description='Sunday' then 1 end)as "sunday",count(case when description!='Sunday' then 1 end)as "holiday_day" FROM 1bd3e0294da19198.`tabHoliday` where parent=(select holiday_list from tabEmployee where name =(SELECT employee_code from tabUser where name={0})) and holiday_date like ={1} """.format(test_email,ym), as_dict=1);
		datasets1.append(days[0].dd); 
		datasets1.append(holiday_sun_cnt[0].sunday);
		datasets1.append(holiday_sun_cnt[0].holiday_day);
		datasets.append(datasets1);
		
		pass;
	frappe.msgprint(_(datasets));
        
    

