from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def get_plan_of_today(employee, designation,date_pass,app_ver):
 email_list=""
 email_list_only_TBM=""
 count_of_emp=0
 count_of_emp_tbm=0
 #i = datetime.now()
 #test=i.strftime('%Y/%m/%d %H:%M:%S')
 if((len(date_pass)) == 0):
  today_date = frappe.utils.data.get_datetime().strftime('%Y/%m/%d')
 else:
  today_date=date_pass
  
 today_date="'"+today_date+"'"

 
 
  objective= frappe.db.sql(""" SELECT doctor_flag as dc,camp_flag as cm,meeting_flag as mt,leave_flag as lv,call_agenda as dc_a,
  camp_agenda as cm_a,meeting_agenda as mt_a,reason as lv_a FROM 1bd3e0294da19198.`tabObjective` where 
  1bd3e0294da19198.`tabObjective`.user = {0} and
  1bd3e0294da19198.`tabObjective`.`select_date`={1} """.format(employee,today_date), as_dict=1)
  
 if len(objective) > 0:
  if objective[0].dc==1 and objective[0].cm==1 and objective[0].mt==1 and objective[0].lv==0:
    objj="";
    objj="<b>PLAN OF DAY :</b>"+ " DCR  |  CAMP BOOKING  |  MEETING \n\n"+
         "<b>DCR Agenda: </b>" + objective[0].dc_a +"\n"+
         "<b>CAMP Agenda: </b>" +objective[0].cm_a +"\n"+
         "<b>Meeting Agenda: </b>" +objective[0].dc_mt;
          
  elif objective[0].dc==1 and objective[0].cm==1 and objective[0].mt==0 and objective[0].lv==0:
    objj="";
    objj="<b>PLAN OF DAY :</b>"+ " DCR  |  CAMP BOOKING \n\n"+
         "<b>DCR Agenda: </b>" + objective[0].dc_a +"\n"+
         "<b>CAMP Agenda: </b>" +objective[0].cm_a +"\n"+
         "<b>Meeting Agenda: </b>" +objective[0].dc_mt;
          
  elif objective[0].dc==1 and objective[0].cm==0 and objective[0].mt==1 and objective[0].lv==0:
    objj="";
    objj="<b>PLAN OF DAY :</b>"+ " DCR  |  MEETING \n\n"+
         "<b>DCR Agenda: </b>" + objective[0].dc_a +"\n"+
         "<b>Meeting Agenda: </b>" +objective[0].dc_mt;
        
  elif objective[0].dc==1 and objective[0].cm==0 and objective[0].mt==0 and objective[0].lv==0:
    objj="";
    objj="<b>PLAN OF DAY :</b>"+ " DCR \n\n"+
         "<b>DCR Agenda: </b>" + objective[0].dc_a;
  
  elif objective[0].dc==0 and objective[0].cm==1 and objective[0].mt==1 and objective[0].lv==0:
    objj="";
    objj="<b>PLAN OF DAY :</b>"+ " CAMP BOOKING  |  MEETING \n\n"+
         "<b>CAMP Agenda: </b>" +objective[0].cm_a +"\n"+
         "<b>Meeting Agenda: </b>" +objective[0].dc_mt;
        
  elif objective[0].dc==0 and objective[0].cm==1 and objective[0].mt==0 and objective[0].lv==0:
    objj="";
    objj="<b>PLAN OF DAY :</b>"+ " CAMP BOOKING \n\n"+
         "<b>CAMP Agenda: </b>" +objective[0].cm_a;
      
  elif objective[0].dc==0 and objective[0].cm==0 and objective[0].mt==1 and objective[0].lv==0:
    objj="";
    objj="<b>PLAN OF DAY :</b>"+ " MEETING \n\n"+
         "<b>Meeting Agenda: </b>" +objective[0].dc_mt;
      
  elif objective[0].dc==0 and objective[0].cm==0 and objective[0].mt==0 and objective[0].lv==1:
    objj="";
    objj="<b>PLAN OF DAY : LEAVE</b>";

  else:
    objj="<b>PLAN NOT CREATED FOR TODAY...</b>";
 else:
  objj='No Objective Today'
 

  
 #frappe.msgprint(_(objective))
 dict = {
   'obj':''
 }
 
 dict['obj'] = objj;
 
 return dict
