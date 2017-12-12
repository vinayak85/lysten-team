from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist(employee)
def form16_package():    
    package_cnt='';
    if(len(employee)>0):
        employee="'"+employee+"'";
        package_cnt= frappe.db.sql("""select  count(distinct base)as cnt from `tabSalary Structure Employee` where employee={0} 
        """.format(employee), as_dict=1)
    if(package_cnt[0].cnt>1):
        package_cnt= frappe.db.sql("""select base from `tabSalary Structure Employee` where employee={0} 
        """.format(employee), as_dict=1)        
    dict = {'package': ''
           }
    
    dict['package']=package;
    return dict
