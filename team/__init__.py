# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
__version__ = '0.0.1'

@frappe.whitelist(limit, offset)
def ping():
 	return frappe.db.sql(""" SELECT doctor_name as dname,reg_no,pin_code,
  per_mobile,per_phone,email FROM `tabDoctor Master` LIMIT  1 OFFSET 0""",as_dict=True)

