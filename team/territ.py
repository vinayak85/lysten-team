# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
# this method is used for android heirachy get Hq based on user territory
#it will featch all HQ of related to the user
@frappe.whitelist()
def tree_territory_get_hq(territory, designation,limit, offset): 
if designation == 'ABM': 
 return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c1.parent_territory={0}  LIMIT {1}  OFFSET {2} ;
                           """.format(territory,limit,offset),as_dict=True)
 
elif designation == 'RBM': 
 return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c2.parent_territory={0}  LIMIT {1}  OFFSET {2} ;
                           """.format(territory,limit,offset),as_dict=True)
 
elif designation == 'ZBM': 
 return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c3.parent_territory={0}  LIMIT {1}  OFFSET {2} ;
                           """.format(territory,limit,offset),as_dict=True)
 
 elif (designation == 'HR Manager' or designation == 'Head of Marketing and Sales'
       or designation == 'SM' or designation == 'CRM' or designation == 'NBM'
       or designation == 'Admin'):
 return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c4.parent_territory={0}  LIMIT {1}  OFFSET {2} ;
                           """.format(territory,limit,offset),as_dict=True) 
 
 else:
   frappe.msgprint(_("No entry"))
