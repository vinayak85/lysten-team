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
	datasets1 = []; 
	for f in monthss:
		datasets1=[];
		#frappe.msgprint(_("mm: "+" "+f));
		ss="'"+f+"%'";
		pur_qty = frappe.db.sql("""select sum(pii.stock_qty) as 'Purchase',batch_no
		FROM 1bd3e0294da19198.`tabPurchase Invoice` as pi LEFT JOIN 1bd3e0294da19198.`tabPurchase Invoice Item` pii
		ON pi.name = pii.parent where pi.docstatus <> 2 and pii.batch_no='AC6080' and pi.delivery_date 
		like concat({0})""".format(ss), as_dict=1)
		
		sale_qty = frappe.db.sql("""select sum(sii.stock_qty) as 'Sale',batch_no FROM 1bd3e0294da19198.`tabSales Invoice`
		as si LEFT JOIN 1bd3e0294da19198.`tabSales Invoice Item` sii ON si.name = sii.parent where si.docstatus <> 2
		and sii.batch_no='AC6080'  and 
		(si.name like 'Pre-SI-0%' or si.name like 'SI-0%')
		and si.posting_date like concat({0})""".format(ss), as_dict=1)
		
		sample_pqty = frappe.db.sql("""select sum(sii.stock_qty) as 'Sample',batch_no FROM 1bd3e0294da19198.`tabSales Invoice`
		as si LEFT JOIN 1bd3e0294da19198.`tabSales Invoice Item` sii ON si.name = sii.parent where si.docstatus <> 2
		and sii.batch_no='AC6080'  and 
		(si.name like 'SS-%')
		and si.posting_date like concat({0})""".format(ss), as_dict=1)
		
		cn_qty = frappe.db.sql("""select sum(sii.stock_qty) as 'Credit_Note',batch_no FROM 1bd3e0294da19198.`tabSales Invoice`
		as si LEFT JOIN 1bd3e0294da19198.`tabSales Invoice Item` sii ON si.name = sii.parent where si.docstatus <> 2
		and sii.batch_no='AC6080'  and 
		(si.name like 'Pre-R%' or si.name like 'SR-0%')
		and si.posting_date like concat({0})""".format(ss), as_dict=1)
		
		
		bal_nqty = pur_qty[0].Purchase_Qty-(sale_qty[0].Sale+sample_pqty[0].Sample) + cn_qty[0].Credit_Note;
		
		datasets1.append(f);
		datasets1.append(pur_qty[0].Purchase);
		datasets1.append(sale_qty[0].Sale);
		datasets1.append(sample_pqty[0].Sample);
		datasets1.append(cn_qty[0].Credit_Note);
		datasets1.append(bal_nqty);
		data.append(datasets1);
		pass;
	
	return columns, data

def get_columns():
	columns = [
		_("Month") + "::120",
		_("Purchase_Qty") + "::120",
	]
	'''columns = [
		_("Month") + "::120",
		_("Purchase") + "::120",
		_("Sale") + "::120",
		_("Credit Note") + "::120",
		_("Sample") + "::120",
		_("Balance") + "::120",
		_("Batch No") + "::120"
		
	]'''	
	
	

	return columns

def get_months():
	return ['2016-03','2016-04','2016-05']


