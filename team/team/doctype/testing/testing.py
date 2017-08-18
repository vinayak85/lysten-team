# -*- coding: utf-8 -*-
# Copyright (c) 2017, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.model.document import Document

class testing(Document):
	pass
@frappe.whitelist()
def ching():
 	return frappe.db.sql(""" SELECT doctor_name as dname,reg_no,pin_code,
  per_mobile,per_phone,email FROM `tabDoctor Master` LIMIT 5  OFFSET 0""",as_dict=True)
frappe.msgprint(_("call me"))
