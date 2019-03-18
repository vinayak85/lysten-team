from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def test(against_inv,sr):
  frappe.msgprint(_(against_inv + "," + sr))
