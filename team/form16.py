from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def form16_package(employee):    
    package_cnt='';
    package='';
    
    if(len(employee)>0):
        employee="'"+employee+"'";
        package_cnt= frappe.db.sql("""select  count(distinct base)as cnt from `tabSalary Structure Employee` where employee={0} 
        """.format(employee), as_dict=1)
        
    if(package_cnt[0].cnt > 1):
        employee="'"+employee+"'";
        package= frappe.db.sql("""select GROUP_CONCAT(distinct base) as pckge from `tabSalary Structure Employee` where employee={0} 
        """.format(employee), as_dict=1) 
    else:
        employee="'"+employee+"'";
        package= frappe.db.sql("""select base as pckge from `tabSalary Structure Employee` where employee={0} 
        """.format(employee), as_dict=1)        
        
    dict = {'package': ''
           }
    
    dict['package']=package[0].pckge;
    return dict
