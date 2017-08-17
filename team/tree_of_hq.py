from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 


@frappe.whitelist()
def tree_territory(a,b,limit, offset): 
 if b == "ABM":
 return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory AS c1 
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c1.parent_territory={0} LIMIT {1}  OFFSET {2};
                           """.format(territory,limit,offset),as_dict=True)
