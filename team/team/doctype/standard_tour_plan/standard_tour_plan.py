# -*- coding: utf-8 -*-
# Copyright (c) 2018, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import subprocess
from frappe import msgprint, _ 
import frappe.utils
from frappe.model.document import Document
from frappe.utils import cstr, flt, getdate, cint
from frappe.model.naming import make_autoname
from frappe import _
from frappe.model.mapper import get_mapped_doc


class StandardTourPlan(Document):
	pass

@frappe.whitelist()
#get patches details of specific user with doctor count and chemist count ,this method use in STP after buton clicl
def get_patches_doc_and_chem_cnt(user):
	frappe.msgprint(_("UGHSDUFG"));
	return  frappe.db.sql("""SELECT name,patch_name,user,user_name FROM 1bd3e0294da19198.`tabPatch master`
	where user like {0} and  docstatus !=2""".format("'"+user+"'"), as_dict=1);
	
	
