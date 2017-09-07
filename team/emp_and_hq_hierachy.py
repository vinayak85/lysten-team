# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'


@frappe.whitelist()
# this method is used for android heirachy user
 #it will featch all top and down users of selected user
@frappe.whitelist()
def tree_user(employee, designation,limit, offset): 
 if designation == 'TBM':
   return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1  and `tabUser`.`name` in(
 (select abm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select rbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ) LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
  
 elif designation == "ABM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`abm`={0}  or `tabUser`.`name` in(
 (select rbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ) LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
 
 elif designation == "RBM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`rbm`={0}  or `tabUser`.`name` in(
 (select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ) LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
 
 elif designation == "ZBM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`zbm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ) LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
 
 elif designation == "SM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`sm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
) LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
 
 elif designation == "NBM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`nbm`={0}  or `tabUser`.`name` in(
 (select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
) LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
 
 elif designation == "CRM":
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`crm`={0}
 LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
 
 elif (designation == "HR Manager" or designation == "Head of Marketing and Sales" or designation == "Admin"):
  return frappe.db.sql(""" select name,username,full_name,first_name,middle_name,last_name,designation,mobile_no1,email,
 modified from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`designation` in('TBM','ABM','RBM','ZBM','SM','NBM','CRM')
 LIMIT {1}  OFFSET {2} """.format(employee,limit,offset),as_dict=True)
 
 else:
   frappe.msgprint(_("No entry"))
   
 # this method is used for android heirachy get Hq based on user territory
#it will featch all HQ of related to the user
@frappe.whitelist()
def tree_territory_get_hq(territory, designation,limit, offset):
 if designation == "ABM":
  return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c1.parent_territory={0} LIMIT {1}  OFFSET {2};
                           """.format(territory,limit,offset),as_dict=True)
 elif designation == "RBM":
  return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c2.parent_territory={0} LIMIT {1}  OFFSET {2};
                           """.format(territory,limit,offset),as_dict=True)
 elif (designation == "ZBM" or designation == "SM") :
  return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c3.parent_territory={0} LIMIT {1}  OFFSET {2};
                           """.format(territory,limit,offset),as_dict=True)
 elif (designation == "HR Manager" or designation == "Head of Marketing and Sales" or designation == "CRM" or designation == "NBM"
       or designation == "Admin"):
  return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           where 
                           c4.parent_territory={0} LIMIT {1}  OFFSET {2};
                           """.format(territory,limit,offset),as_dict=True)
 else:
  frappe.msgprint(_("No entry"))
   
   
