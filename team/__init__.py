# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
__version__ = '0.0.1'

@frappe.whitelist()
def ping():
 	return frappe.db.sql_list("""select name from `tabDoctor Master` """)

