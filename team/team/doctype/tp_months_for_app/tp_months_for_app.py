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
def get_tp_months(user_id):
	#datasets = [];	
	user_id="'"+user_id+"'";
	tp_months_found=frappe.db.sql("""select concat(year,"-",if(month<10,concat('0',month),month))as "ym" 
	from `tabTP Months for App` where active=1 and name in(select parent from `tabTP Months Active user`
	where user_id={0})""".format(user_id), as_dict=1);
	
	datasets1=[];
	for f in tp_months_found:
		
		###datasets1=[];			
        	#frappe.msgprint(_(f.ym));
		#datasets1.append(f.ym);
		
		ym="'"+f.ym+"'";
		ym_="'"+f.ym+"-%'";
		days=frappe.db.sql(""" SELECT DAY(LAST_DAY(concat({0},'-01'))) as "dd" """.format(ym), as_dict=1);
		holiday_sun_cnt=frappe.db.sql("""SELECT count(case when description='Sunday' then 1 end)as "sunday",
		count(case when description!='Sunday' then 1 end)as "holiday_day" FROM 1bd3e0294da19198.`tabHoliday`
		where parent=(select holiday_list from tabEmployee where name =(SELECT employee_code from tabUser 
		where name={0})) and holiday_date like {1} """.format(user_id,ym_), as_dict=1);
		tp_days_cnt=frappe.db.sql(""" select ifnull(count(case when tp_flag=1 then 1 end),0)as "tp_days_cnt",
		ifnull(count(case when doctor_flag=1 then 1 end),0)as "cnt_dcr",
		ifnull(count(case when meeting_flag=1 then 1 end),0)as "cnt_meeting",
		ifnull(count(case when camp_flag=1 then 1 end),0)as "cnt_camp",
		ifnull(count(case when leave_flag=1 then 1 end),0)as "cnt_leave" 
		from 1bd3e0294da19198.`tabObjective` 
		where select_date like {0}
		and user= {1} and tp_flag=1
		ORDER BY `tabObjective`.`name` DESC LIMIT 1""".format(ym_,user_id), as_dict=1);''', as_dict=1'''
		
		#frappe.msgprint(_('"' + 'days' + '":' + '"' + str(days[0].dd) + '"'));			
		
		datasets1.append({ 'days':str(days[0].dd),
				  'sunday':str(holiday_sun_cnt[0].sunday)
				  ,'holiday_day':str(holiday_sun_cnt[0].holiday_day)
				  ,'tp_days_cnt':str(tp_days_cnt[0].tp_days_cnt)
				 ,'cnt_dcr':str(tp_days_cnt[0].cnt_dcr)
				 ,'cnt_meeting':str(tp_days_cnt[0].cnt_meeting)
				 ,'cnt_leave':str(tp_days_cnt[0].cnt_leave)
				 ,'ym':str(f.ym)}); 		
				
		#datasets.append(datasets1);	
		pass;
	return (datasets1);''', as_dict=1 datasets'''
	
        
    

