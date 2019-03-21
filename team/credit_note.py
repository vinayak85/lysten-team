from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def test(against_inv,sr):
  #frappe.msgprint(_(against_inv + "," + sr))
  #posting_date
  #against_inv="'"+against_inv+"'"
  #sr="'"+sr+"'"
  ret_date='';
  ret_date= frappe.db.sql(""" select posting_date  from 1bd3e0294da19198.`tabSales Invoice`
  where `tabSales Invoice`.`docstatus`< 2 and `name`={0}""".format(sr), as_dict=1)
  if len(ret_date) > 0:
    ret_date = ret_date[0].posting_date
    pass
  else:
    ret_date = ''
    pass
  
  sr_items=frappe.db.sql(""" SELECT item_code,batch_no,qty,free_quantity FROM 1bd3e0294da19198.`tabSales Invoice Item`
where parent={0} and against_invoice_={1}""".format(sr,against_inv), as_dict=1)
  dict = {'ret_date': '',
          'sr_items':''}
  dict['ret_date'] = ret_date;
  dict['sr_items'] = sr_items;
  return dict;
