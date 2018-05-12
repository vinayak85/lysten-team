# -*- coding: utf-8 -*-
# Copyright (c) 2018, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TPMonthsforApp(Document):
	pass

@frappe.whitelist()
def get_user(branch):
	branch="'"+branch+"'";
	frappe.msgprint(_(branch));
	return frappe.db.sql("""SELECT name,full_name FROM 1bd3e0294da19198.tabUser
where enabled=1 and branch={1}""".format(branch), as_dict=1);
