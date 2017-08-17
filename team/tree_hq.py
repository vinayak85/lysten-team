# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 

@frappe.whitelist()
def tttt(des,limit, offset):
# if des == 'ABM':
   frappe.msgprint(_("ABM"))
#   else:
#   frappe.msgprint(_("TBM"))
