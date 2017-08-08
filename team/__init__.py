# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
__version__ = '0.0.1'

@frappe.whitelist(start, page_len)
def ping():
 	return frappe.db.sql(""" SELECT doctor_name as dname,reg_no,pin_code,
  per_mobile,per_phone,email FROM `tabDoctor Master` limit %(start)s, %(page_len)s""", as_dict=True )

