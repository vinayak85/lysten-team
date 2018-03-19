# Copyright (c) 2013, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe.model.meta import get_field_precision
from frappe.utils.xlsxutils import handle_html

def execute(filters=None):
	return _execute(filters)

def _execute(filters=None,  additional_query_columns=None):
	columns, data = [], []
	if not filters: filters = {}
	columns = get_columns()
	monthss=get_months();
	for f in monthss:
		frappe.msgprint(_("mm: "+" "+f));
		op = frappe.db.sql("""select sum(pii.stock_qty) as 'Purchase_Qty',batch_no
		FROM 1bd3e0294da19198.`tabPurchase Invoice` as pi LEFT JOIN 1bd3e0294da19198.`tabPurchase Invoice Item` pii
		ON pi.name = pii.parent where pi.docstatus <> 2 and pii.batch_no='AC6080' and pi.delivery_date 
		like concat({0})""".format(f), as_dict=1)
        
        datasets1.append(f);      
        datasets1.append(op[0].Purchase_Qty);
	return columns, data

def get_columns():
	
	columns = [
		_("Month") + "::120",
		_("Purchase") + "::120",
		_("Sale") + "::120",
		_("Credit Note") + "::120",
		_("Sample") + "::120",
		_("Balance") + "::120",
		_("Batch No") + "::120"
		
	]	

	return columns

def get_months():
	return ['2016-03%','2016-04%','2016-05%']


