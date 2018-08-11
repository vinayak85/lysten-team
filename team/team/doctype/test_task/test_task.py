# -*- coding: utf-8 -*-
# Copyright (c) 2018, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import msgprint, _

class test_task(Document):
	pass

@frappe.whitelist()
def test_start():
	'''INSERT INTO 1bd3e0294da19198.tabtest_task (note)
   VALUES
   ('');'''
	td_entry = frappe.new_doc("test_task")
	#td_entry.name = 'test_task/' + '000001'
	td_entry.note = 'aaaaa'
	'''td_entry.salary_slip = ss.name'''
	#td_entry.docstatus = 1
	td_entry.save()
	
	#op = frappe.db.sql(""" INSERT INTO 1bd3e0294da19198.tabtest_task (note) VALUES ('aaaaa');""");
	frappe.msgprint(_("arjun "));


