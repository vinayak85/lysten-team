from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _

__version__ = '0.0.1'

@frappe.whitelist()
def get_date_and_app_support(User,Branch,Stockist,FromDate,ToDate,Products,flag_of_operation):
  if(designation=='ABM'):
    msg = frappe.db.sql("""select group_concat(territory_name) from `tabTerritory` where parent_territory='Ichalkaranji(Area)'
    select territory_name from `tabTerritory` where parent_territory={0}""".format("'"+headquarter+"'"), as_dict=1)    
    frappe.msgprint(_(msg));
