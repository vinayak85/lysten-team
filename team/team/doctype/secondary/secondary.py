# -*- coding: utf-8 -*-
# Copyright (c) 2017, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Secondary(Document):
	def autoname(self):
		self.name = make_autoname('Sal Slip/' +self.month + '/.#####')
