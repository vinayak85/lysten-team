from __future__ import unicode_literals
import frappe
import datetime
import time
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from frappe.utils import getdate, nowdate, add_days
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def test(frmdt,todt,inttime,wrkstrttime,wrkendtime):
    fromdate=frmdt
    todate=todt;
    intervaltime=int(inttime)*60;#convert into seconds
    workstarttime=wrkstrttime;
    workendtime=wrkendtime; 
    dt_form_s_time=fromdate+' '+workstarttime
    datetime_object = datetime.strptime(dt_form_s_time, "%Y-%m-%d %H:%M:%S")
    frappe.msgprint(_(fromdate+"  "+todate+"  "+str(intervaltime)+"  "+workstarttime+"  "+str(datetime_object)));
    
@frappe.whitelist()
def get_call_summary(frmdt,todt,inttime,wrkstrttime,wrkendtime):
  #fromdate,todate,intervaltime,workstarttime,workendtime
  '''fromdate='2018-01-04'
  todate='2018-01-05';
  intervaltime=60*60;#convert into seconds
  workstarttime='08:00:00';
  workendtime='21:00:00';'''
    
  fromdate=frmdt
  todate=todt;
  intervaltime=int(inttime)*60;#convert into seconds
  workstarttime=wrkstrttime;
  workendtime=wrkendtime;

  list_of_cnt=[];
    
  while (fromdate <= todate):
    #frappe.msgprint(_("time:"+": "+str(fromdate)));
    cntcall=[];
    flag=0;
    
    while (workstarttime < workendtime):
      
      dt_form_s_time=fromdate+' '+workstarttime
      #dt_form_s_time=datetime.strptime(fromdate+' '+workstarttime, "%Y-%m-%d %H:%M:%S")
      c = time.strptime(dt_form_s_time,"%Y-%m-%d %H:%M:%S") 
      t = time.mktime(c) 
      t = t + intervaltime #30 minutes is 1800 secs
      dt_form_t_time = datetime.fromtimestamp(t)  #calculate to_time using interval time .this may be 30min,1hr,2hr
      
      #frappe.msgprint(_("time:"+": "+str(dt_form_t_time)));
      
      workstarttime = str(dt_form_t_time).split(' ')[1] #get time and use swap method like c=a,a=b,b=c
      curr_select_date = str(dt_form_t_time).split(' ')[0]#get task perform curr date for add in list at position 0
      
      #frappe.msgprint(_("time:"+": "+str(workstarttime)));#frappe.msgprint(_("From:"+": "+str(dt_form_s_time)+" To:"+str(dt_form_t_time)));
      
      cnt_dcr = frappe.db.sql(""" select count(*) as cnt from  1bd3e0294da19198.`tabDoctor Calls` 
      where creation between {0} and {1}; """.format("'"+str(dt_form_s_time)+"'","'"+str(dt_form_t_time)+"'"), as_dict=1)
      
      #frappe.msgprint(_(cnt_dcr[0].cnt));
      if(flag==0):
        cntcall.insert(0,curr_select_date);
      
      cntcall.append(cnt_dcr[0].cnt);
      flag=1;
      #for p in cntcall: 
        #frappe.msgprint(_(p));
        
    list_of_cnt.append(cntcall);
    fromdate=frappe.utils.data.add_days (fromdate, 1); #use for while loop increment in from_date by 1 day upto to_date
    #frappe.msgprint(_("time:"+": "+str(fromdate)));
    workstarttime=wrkstrttime;
    workendtime=wrkendtime;
    
  workstarttime=wrkstrttime;
  workendtime=wrkendtime;
  while (workstarttime < workendtime):
    dt_form_s_time=fromdate+' '+workstarttime
    c = time.strptime(dt_form_s_time,"%Y-%m-%d %H:%M:%S") 
    t = time.mktime(c) 
    t = t + intervaltime #30 minutes is 1800 secs
    dt_form_t_time = datetime.fromtimestamp(t)  #calculate to_time using interval time .this may be 30min,1hr,2hr
    #frappe.msgprint(_("time:"+": "+str(dt_form_t_time)));
    workstarttime = str(dt_form_t_time).split(' ')[1] #get time and use swap method like c=a,a=b,b=c    

    st_time=str(dt_form_s_time).split(' ')[1][:5]
    en_time=str(dt_form_t_time).split(' ')[1][:5]
    
    t1 = time.strptime(st_time, "%H:%M")
    timevalue_12hour_st = time.strftime( "%I:%M %p", t1 )
    
    t2 = time.strptime(en_time, "%H:%M")
    timevalue_12hour_end = time.strftime( "%I:%M %p", t2 )      
    ti_concat=str(timevalue_12hour_st)[:5]+'-'+str(timevalue_12hour_end)[:5]
    
    #frappe.msgprint(_(str(dt_form_s_time).split(' ')[1][:5]+" "+str(dt_form_t_time).split(' ')[1][:5]));
    #frappe.msgprint(_(str(datetime.strptime(str(dt_form_s_time).split(' ')[1][:5], "%H:%M"))+" "+str(datetime.strptime(str(dt_form_t_time).split(' ')[1][:5], "%H:%M"))));
    frappe.msgprint(_(ti_concat))
    
  #for p in list_of_cnt:
    #frappe.msgprint(_(p));
    
    
  #fromdate=frappe.utils.data.add_days (fromdate, 2);
  #if(fromdate <= todate):
    #frappe.msgprint(_("less than from date:"));
  #else:
    #frappe.msgprint(_("High than from date:"));

  
  '''Time Add Auto in Date'''
  
  '''a='2018-01-09'
  b='12:00:00'
  dt=a+' '+b
  c = time.strptime(dt,"%Y-%m-%d %H:%M:%S")  
  t = time.mktime(c) 
  t = t + 1800 #30 minutes is 1800 secs
  dt_obj = datetime.fromtimestamp(t)  
  frappe.msgprint(_("time:"+": "+str(dt_obj)));
  
  dt_time = str(dt_obj).split(' ')[1] get time
  dt_date = str(dt_obj).split(' ')[0] get date
  frappe.msgprint(_("time:"+": "+str(dt_time)));'''
 
def local_time(zone='Asia/Kolkata'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%T')
