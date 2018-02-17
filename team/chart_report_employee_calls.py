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
  #from datetime import datetime, timedelta
  #nine_hours_from_now = datetime.now() + timedelta(hours=9)
  #current_time = local_time()
  
  #now = frappe.utils.now().split(' ')[1]
  
  #now = frappe.utils.data.nowtime ()
  #now_plus_10 =  frappe.utils.data.to_timedelta(10)
  #frappe.msgprint(_("time:"+": "+str(now)+"  "+str(now_plus_10)));
  
  c = time.strptime('2018-01-09 08:00:00',"%Y-%m-%d %H:%M:%S")
  t = time.mktime(c) 
  t = t + 1800 #30 minutes is 1800 secs
  #dt=time.mktime(t)
  #dt=time.strftime("%Y-%m-%d %H:%M:%S", t)
  #dt_obj = datetime.fromtimestamp(t)
  frappe.msgprint(_("time:"+": "+str(t)));
 
def local_time(zone='Asia/Kolkata'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%T')
