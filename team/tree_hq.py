# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def tttt(des,limit, offset):
 	if des == 'ABM':
   frappe.msgprint(_("ABM"))
  else:
    frappe.msgprint(_("TBM"))
