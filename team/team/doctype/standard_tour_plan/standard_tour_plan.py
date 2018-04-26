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
	def validate(self):
		 #frappe.msgprint(_("validate"));
		pass;
	pass;


@frappe.whitelist()
#get patches details of specific user with doctor count and chemist count ,this method use in STP after buton clicl
def get_patches_doc_and_chem_cnt(user):
	
	return  frappe.db.sql("""SELECT name,patch_name,user,user_name FROM 1bd3e0294da19198.`tabPatch master`
	where user like {0} and  docstatus !=2""".format("'"+user+"'"), as_dict=1);
@frappe.whitelist()
def get_dr_and_chem_count_fetch(user):
	doc = frappe.db.sql("""SELECT ifnull(count(name),0) as name FROM `tabDoctor Master`where user like {0} and  docstatus !=2""".format("'"+user+"'"), as_dict=1);
	chem = frappe.db.sql("""SELECT ifnull(count(name),0) as name FROM `tabChemist Master`where user like {0} and  docstatus !=2""".format("'"+user+"'"), as_dict=1);
	#return c[0].name;
	dict = {'cnt_doc': 0,
	        'cnt_chem': 0}
	dict['cnt_doc'] = doc[0].name;
	dict['cnt_chem'] = chem[0].name;
	return dict;
	
	
