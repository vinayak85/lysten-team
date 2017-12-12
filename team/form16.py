from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def form16_package():
    package='13.127.22.180';
    dict = {'package': ''
           }
    
    dict['package']=ip;
    return dict
