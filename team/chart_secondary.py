from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _

__version__ = '0.0.1'


@frappe.whitelist()
def get_date_and_app_support():
    
    july = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Oct-CHIRAYU PHARMA'""", as_dict=0)
    
    aug = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Oct-CHIRAYU PHARMA'""", as_dict=0)
    datasets = [];
    datasets.append({'title': 'July', 'values': july[0]})
    datasets.append({'title': 'Aug', 'values': aug[0]})

    #dict = {'app_ver_count': 0}
  
    #dict['app_ver_count'] = datasets;
    #return dict
    return datasets;
