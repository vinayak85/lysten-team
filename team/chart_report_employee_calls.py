from __future__ import unicode_literals
import frappe
from datetime import datetime
from datetime import datetime, timedelta
from frappe import msgprint, _

__version__ = '0.0.1'


@frappe.whitelist()
def get_call_summary():  
  nine_hours_from_now = datetime.now() + timedelta(hours=9)
  frappe.msgprint(_("time:"+": "+datetime.now()+"   "+nine_hours_from_now));
