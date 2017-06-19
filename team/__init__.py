# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
__version__ = '0.0.1'

@frappe.whitelist()
def ping():
 	return frappe.db.sql(""" SELECT doctor_name as 'dname',degree as 'degree' FROM 1bd3e0294da19198.`tabDoctor Master`""")

