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
def get_call_summary():
  #fromdate,todate,intervaltime,workstarttime,workendtime
  fromdate='2018-01-04'
  todate='2018-01-05';
  intervaltime=30*60;
  workstarttime='08:00:00';
  workendtime='09:30:00';
  #while (fromdate <= todate):
    #frappe.msgprint(_("time:"+": "+str(fromdate)));
    #fromdate=frappe.utils.data.add_days (fromdate, 1);
    #frappe.msgprint(_("time:"+": "+str(fromdate)));
  #dt_form_s_time=fromdate+' '+workstarttime
  while (workstarttime <= workendtime):
    dt_form_s_time=fromdate+' '+workstarttime
    c = time.strptime(dt_form_s_time,"%Y-%m-%d %H:%M:%S") 
    t = time.mktime(c) 
    t = t + intervaltime #30 minutes is 1800 secs
    dt_form_t_time = datetime.fromtimestamp(t)  
    #frappe.msgprint(_("time:"+": "+str(dt_form_t_time)));
    workstarttime = str(dt_form_t_time).split(' ')[1]
    #frappe.msgprint(_("time:"+": "+str(workstarttime)));  
    frappe.msgprint(_("From:"+": "+str(dt_form_s_time)+" To:"+str(dt_form_t_time)));    
    
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
