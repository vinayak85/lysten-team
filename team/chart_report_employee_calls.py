from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'


@frappe.whitelist()
def get_call_summary():  
  #from datetime import datetime, timedelta
  #nine_hours_from_now = datetime.now() + timedelta(hours=9)
  #current_time = local_time()
  now = datetime.now()
  #now_plus_10 = (datetime.datetime.now() + datetime.timedelta(minutes=15)).strftime("%H:%M:%S")
  frappe.msgprint(_("time:"+": "+now));
 
def local_time(zone='Asia/Kolkata'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%T')
