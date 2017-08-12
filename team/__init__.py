# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def ping(limit, offset):
 	return frappe.db.sql(""" SELECT doctor_name as dname,reg_no,pin_code,
  per_mobile,per_phone,email FROM `tabDoctor Master` LIMIT {0}  OFFSET {1} """.format(limit,offset),as_dict=True)

 
@frappe.whitelist()
def ting(employee, designation):
 if designation == 'TBM':
   return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1  and `tabUser`.`name` in(
 (select abm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select rbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )""".format(employee),as_dict=True)
 elif designation == "ABM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`abm`={0}  or `tabUser`.`name` in(
 (select rbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )""".format(employee),as_dict=True)
 elif designation == "RBM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`rbm`={0}  or `tabUser`.`name` in(
 (select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )""".format(employee),as_dict=True)
 elif designation == "ZBM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`zbm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )""".format(employee),as_dict=True)
 elif designation == "SM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`sm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )""".format(employee),as_dict=True)
 elif designation == "NBM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`nbm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )""".format(employee),as_dict=True)
 elif designation == "CRM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`crm`={0} """.format(employee),as_dict=True)
 elif (designation == "HR Manager" or designation == "Head of Marketing and Sales"):
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`designation` in('TBM','ABM','RBM','ZBM','SM','NBM','CRM')""".format(employee),as_dict=True)
 else:
   frappe.msgprint(_("No entry"))
