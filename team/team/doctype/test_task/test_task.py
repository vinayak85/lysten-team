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
	frappe.msgprint(_("arjun"));


