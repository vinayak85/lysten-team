from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def test(against_inv,sr):
  #frappe.msgprint(_(against_inv + "," + sr))
  #posting_date
  return frappe.db.sql(""" select posting_date from 1bd3e0294da19198.`tabSales Invoice`
  where `tabSales Invoice`.`enabled`=1 and `name`={0}""".format(sr), as_dict=1)