from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

# this method is used for android heirachy user
 #it will featch all top and down users of selected user
@frappe.whitelist()
def tree_territory(employee, designation,limit, offset):
 if designation == "'ABM'":
      frappe.msgprint(_("abm"))
   else
   frappe.msgprint(_("tbm"))
