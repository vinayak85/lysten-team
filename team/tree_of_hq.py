from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 


@frappe.whitelist()
def tree_territory(b,limit, offset):
  frappe.msgprint(_(b))
