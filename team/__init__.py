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
 else:
   frappe.msgprint(_("NN"))
