# -*- coding: utf-8 -*-
# Copyright (c) 2017, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import msgprint, _ 
import frappe.utils
from frappe.utils import cstr, flt, getdate, cint
from frappe.model.naming import make_autoname
from frappe import _
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def get_calculations(fromdate, todate):
	#return frappe.db.sql("""call attendence1({0},{1})""".format(fromdate,todate), as_dict=1);
	frappe.msgprint(_(call attendence1({0},{1})""".format(fromdate,todate), as_dict=1));

class AttendenceCalculation(Document):
	pass
