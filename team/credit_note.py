from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def test(against_inv,sr):
  #frappe.msgprint(_(against_inv + "," + sr))
  #posting_date
  against_inv="'"+against_inv+"'"
  sr="'"+sr+"'"
  ret_date='';
  transporter_id='';
  note=''
  qry= frappe.db.sql(""" select posting_date,note,transporter_id  from 1bd3e0294da19198.`tabSales Invoice`
  where `tabSales Invoice`.`docstatus`< 2 and `name`={0}""".format(sr), as_dict=1)
  if len(qry) > 0:
    ret_date = qry[0].posting_date;
    transporter_id= qry[0].transporter_id;
    note= qry[0].note;
    pass
  else:
    ret_date = ''
    transporter_id= '';
    note= '';
    pass

  
  sr_items=frappe.db.sql(""" SELECT item_code,batch_no,qty,free_quantity FROM 1bd3e0294da19198.`tabSales Invoice Item`
where parent={0} and against_invoice_={1}""".format(sr,against_inv), as_dict=1)
  dict = {'ret_date': '',
          'transporter_id': '',
          'note': '',
          'sr_items':''}
  dict['ret_date'] = ret_date;
  dict['transporter_id'] = transporter_id;
  dict['note'] = note;
  dict['sr_items'] = sr_items;
  return dict;
