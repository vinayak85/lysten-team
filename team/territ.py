# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'


@frappe.whitelist()
def tttt(tt):
 if tt == 'TBM':
  return frappe.db.sql(""" SELECT 	c1.name as 'headquarter_id', c1.territory_name as 'headquarter_name',
                           c1.parent_territory as 'headquarter_parent'
                           FROM 1bd3e0294da19198.tabTerritory  AS c1
                           JOIN 1bd3e0294da19198.tabTerritory  AS c2 ON (c2.territory_name = c1.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c3 ON (c3.territory_name = c2.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c4 ON (c4.territory_name = c3.parent_territory)
                           JOIN 1bd3e0294da19198.tabTerritory  AS c5 ON (c5.territory_name = c4.parent_territory)
                           ;                          
                           """, as_dict=True)
 else:
  frappe.msgprint(_("No entry"))
