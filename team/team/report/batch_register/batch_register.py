# Copyright (c) 2013, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe.model.meta import get_field_precision
from frappe.utils.xlsxutils import handle_html

def execute(filters=None):
	columns, data = [], []
	if not filters: filters = {}
	columns = get_columns(additional_table_columns)	
	return columns, data

def get_columns(additional_table_columns):
	columns = [
		_("Item Code") + ":Link/Item:120", _("Item Name") + "::120",
		_("Item Group") + ":Link/Item Group:100", _("Invoice") + ":Link/Sales Invoice:120",
		_("Posting Date") + ":Date:80", _("Customer") + ":Link/Customer:120",
		_("Customer Name") + "::120"]

	if additional_table_columns:
		columns += additional_table_columns

	columns += [
		_("Customer Group") + ":Link/Customer Group:120",
		_("Receivable Account") + ":Link/Account:120",
		_("Mode of Payment") + "::120", _("Territory") + ":Link/Territory:80",
		_("Project") + ":Link/Project:80", _("Company") + ":Link/Company:100",
		_("Sales Order") + ":Link/Sales Order:100", _("Delivery Note") + ":Link/Delivery Note:100",
		_("Income Account") + ":Link/Account:140", _("Cost Center") + ":Link/Cost Center:140",
		_("Stock Qty") + ":Float:120", _("Stock UOM") + "::100",
		_("Rate") + ":Currency/currency:120",
		_("Amount") + ":Currency/currency:120"
	]

	return columns
