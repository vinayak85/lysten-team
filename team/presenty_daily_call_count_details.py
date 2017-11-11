# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'


@frappe.whitelist()
# this method is used for android heirachy user
 #it will featch all top and down users of selected user
  
@frappe.whitelist()
def presenty_daily_call_count(fromdate,todate, designation,limit, offset):
  if((len(fromdate)) == 0 or (len(todate)) == 0):
    fromdate = frappe.utils.data.get_datetime().strftime('%Y/%m/%d')
    todate = frappe.utils.data.get_datetime().strftime('%Y/%m/%d')
  else:
    fromdate=fromdate
    todate=todate
  
  #today_date="'"+today_date+"'"
  fromdate="'"+fromdate+"'"
  todate="'"+todate+"'"

  if (designation == "HR Manager" or designation == "Head of Marketing and Sales" or designation == "Admin"):
   return frappe.db.sql(""" Select distinct 
   obj.select_date,
   concat(first_name,' ',last_name,' (',designation,' )')as emp_name,
   designation,
   (select count(name) from `tabDoctor Calls` where dr_call_by_user_id=tu.name and date=obj.select_date)as drc,
   (select count(name) from `tabChemist Call` where call_by_user_id=tu.name and date=obj.select_date)as chec,
   (select count(name) from `tabcampaign_booking` where call_by_user_id=tu.name and date=obj.select_date)as cmp_bk,
   (Select if(count(name)>0,'P','A')as `present` from 1bd3e0294da19198.tabObjective 
   where select_date=obj.select_date and `user`=tu.name 
   and (tabObjective.doctor_flag=1 or tabObjective.meeting_flag=1 or tabObjective.camp_flag=1))as 'Presenty',
   (Select distinct IF(objective != '' && doctor_flag=0 && meeting_flag=0 && camp_flag=0 && leave_flag=0,CONCAT('PLAN OF DAY : ',objective,' '),IF(doctor_flag=1 && camp_flag=1 && meeting_flag=1 && leave_flag=0,Concat('PLAN OF DAY : DCR  |  CAMP BOOKING  |  MEETING','\n','DCR Agenda:',call_agenda,'\n','CAMP Agenda:',camp_agenda,'\n','Meeting Agenda:',meeting_agenda),IF(doctor_flag=1 && camp_flag=1 && meeting_flag=0 && leave_flag=0,Concat('PLAN OF DAY : DCR  |  CAMP BOOKING','\n','DCR Agenda:',call_agenda,'\n','CAMP Agenda:',camp_agenda),IF(doctor_flag=1 && camp_flag=0 && meeting_flag=1 && leave_flag=0,Concat('PLAN OF DAY : DCR  |  MEETING','\n','DCR Agenda:',call_agenda,'\n','Meeting Agenda:',meeting_agenda),IF(doctor_flag=1 && camp_flag=0 && meeting_flag=0 && leave_flag=0,Concat('PLAN OF DAY : DCR ','\n','DCR Agenda:',call_agenda),IF(doctor_flag=0 && camp_flag=1 && meeting_flag=1 && leave_flag=0,Concat('PLAN OF DAY : CAMP BOOKING  |  MEETING','\n','CAMP Agenda:',camp_agenda,'\n','Meeting Agenda:',meeting_agenda),IF(doctor_flag=0 && camp_flag=1 && meeting_flag=0 && leave_flag=0,Concat('PLAN OF DAY : CAMP BOOKING','\n','CAMP Agenda:',camp_agenda),IF(doctor_flag=0 && camp_flag=0 && meeting_flag=1 && leave_flag=0,Concat('PLAN OF DAY : MEETING','\n','Meeting Agenda:',meeting_agenda),IF(doctor_flag=0 && camp_flag=0 && meeting_flag=0 && leave_flag=1,if(leave_type1=1,'PLAN OF DAY : CAUSUAL LEAVE',if(leave_type2=1,'PLAN OF DAY : PRIVILEGE LEAVE',if(leave_type3=1,'PLAN OF DAY : SICK LEAVE','PLAN OF DAY : Leave'))),'PLAN NOT CREATED FOR THAT DAY...'))))))))) as calling
   from 1bd3e0294da19198.tabObjective 
   where select_date=obj.select_date and `user`=tu.name limit 1 ) as `obj`
   ,(Select count(name)
   from 1bd3e0294da19198.tabObjective 
   where select_date=obj.select_date and `user`=tu.name ) as `count` 
   from 1bd3e0294da19198.tabUser `tu` 
   left outer join 
   tabObjective `obj` on obj.`user`=tu.`name` 
   where enabled=1 and designation in('TBM','ABM','RBM','SM','NBM') and select_date between {0} and {1} 
   order by select_date,FIELD(`designation`,'NBM','SM','RBM','ABM','TBM') 
   LIMIT {2}  OFFSET {3} """.format(fromdate,todate,limit,offset),as_dict=True)
  
  
