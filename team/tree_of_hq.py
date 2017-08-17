from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def tree_territory(territory,limit, offset):
 frappe.msgprint(_("No entry"))
