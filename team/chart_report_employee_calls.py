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
  now = frappe.utils.data.nowtime ()
  #frappe.utils.data.nowtime () +
  now_plus_10 =  frappe.utils.data.to_timedelta(10)
  frappe.msgprint(_("time:"+": "+str(now)+"  "+str(now_plus_10)));
 
def local_time(zone='Asia/Kolkata'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%T')
