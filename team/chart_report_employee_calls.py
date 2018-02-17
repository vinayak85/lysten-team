from __future__ import unicode_literals
import frappe
import datetime
import time
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'


@frappe.whitelist()
def get_call_summary(): 
  #fromdate,todate,intervaltime,workstarttime,workendtime
  
  '''Time Add Auto in Date'''
  a='2018-01-09'
  b='12:00:00'
  dt=a+' '+b
  c = time.strptime(dt,"%Y-%m-%d %H:%M:%S")  
  t = time.mktime(c) 
  t = t + 4500 #30 minutes is 1800 secs
  dt_obj = datetime.fromtimestamp(t)  
  frappe.msgprint(_("time:"+": "+str(dt_obj)));
  #frappe.utils.dt_obj.split(' ')[1] 
  dt_time = dt_obj.split(' ')[1]
  frappe.msgprint(_("time:"+": "+str(dt_time)));
 
def local_time(zone='Asia/Kolkata'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%T')
