# -*- coding: utf-8 -*-
# Copyright (c) 2019, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.model.document import Document

class CrossCheckSalesReturn(Document):
	pass
frappe.ui.form.on("crosscheck_sales_return", "year", function(frm, cdt, cdn) 
		{
			frappe.msgprint(_("hello"));
		});
