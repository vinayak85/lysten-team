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
  transporter_name='';
  transporter_address='';
  transporter_gst_no='';
  transporter_state_code='';
  transporter_pan_no='';
  note=''
  if_existed=''
  new_crn=''
  qry= frappe.db.sql(""" select posting_date,note,transporter_id,transporter_name,transporter_address ,transporter_gst_no,
  transporter_state_code,transporter_pan_no  from 1bd3e0294da19198.`tabSales Invoice`
  where `tabSales Invoice`.`docstatus`< 2 and `name`={0}""".format(sr), as_dict=1)
  if len(qry) > 0:
    ret_date = qry[0].posting_date;
    transporter_id= qry[0].transporter_id;
    transporter_name= qry[0].transporter_name;
    transporter_address= qry[0].transporter_address;
    transporter_gst_no= qry[0].transporter_gst_no;
    transporter_state_code= qry[0].transporter_state_code;
    transporter_pan_no= qry[0].transporter_pan_no;
    note= qry[0].note;
    pass
  else:
    ret_date = ''
    transporter_id= '';
    transporter_name= '';
    transporter_address= '';
    transporter_gst_no= '';
    transporter_state_code= '';
    transporter_pan_no= '';
    note= '';
    pass
  
  qry1= frappe.db.sql(""" select name    from 1bd3e0294da19198.`tabSales Invoice` where return_against={0} and ref_return={1}""".format(against_inv,sr), as_dict=1)
  if len(qry1) > 0:
    if_existed = qry1[0].name;
    pass
  else:
    if_existed = 'no'
    pass
  
  #qry2= frappe.db.sql(""" select new_credit_note_number    from 1bd3e0294da19198.`tabSales Invoice`
#where  ref_return={0}""".format(sr), as_dict=1)
  #if len(qry2) > 0:
   # new_crn = qry1[0].name;
    #new_crn=
    #pass
  #else:
   # new_crn = sr+'--1'
   # pass
  
  
  sr_items=frappe.db.sql(""" SELECT item_code,batch_no,qty,free_quantity FROM 1bd3e0294da19198.`tabSales Invoice Item`
where parent={0} and against_invoice_={1}""".format(sr,against_inv), as_dict=1)
  dict = {'ret_date': '',
          'transporter_id': '',
          'transporter_name': '',
          'transporter_address': '',
          'transporter_gst_no': '',
          'transporter_state_code': '',
          'transporter_pan_no': '',
          'note': '',
          'sr_items':'',
          'if_existed':''
          }
  dict['ret_date'] = ret_date;
  dict['transporter_id'] = transporter_id;
  dict['transporter_name'] = transporter_name;
  dict['transporter_address'] = transporter_address;
  dict['transporter_gst_no'] = transporter_gst_no;
  dict['transporter_state_code'] = transporter_state_code;
  dict['transporter_pan_no'] = transporter_pan_no;
  dict['note'] = note;
  dict['sr_items'] = sr_items;
  dict['if_existed'] = if_existed;
    
  return dict;
