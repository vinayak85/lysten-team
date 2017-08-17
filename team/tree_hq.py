from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

# this method is used for android heirachy user
 #it will featch all top and down users of selected user
@frappe.whitelist()
def tree_territory(employee, designation,limit, offset):
 frappe.msgprint(_("No entry"))
 if designation == 'ABM':
   return frappe.db.sql(""" SELECT c1.`name`,c1.`territory_name`,c1.`parent_territory` FROM 1bd3e0294da19198.`tabTerritory` AS c1 JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
   JOIN 1bd3e0294da19198.`tabTerritory`  AS c3 ON (c3.`territory_name` = c2.`parent_territory`)JOIN 1bd3e0294da19198.`tabTerritory`  AS c4 ON (c4.`territory_name` = c3.`parent_territory`)
   JOIN 1bd3e0294da19198.`tabTerritory`  AS c5 ON (c5.`territory_name` = c4.`parent_territory`)
   where c1.`parent_territory`={0} LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
  else:
    frappe.msgprint(_("No entry"))
