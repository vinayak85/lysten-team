from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _

__version__ = '0.0.1'


@frappe.whitelist()
def get_date_and_app_support():
    
    july = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-July-CHIRAYU PHARMA'""", as_dict=0)
    
    aug = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Aug-CHIRAYU PHARMA'""", as_dict=0)
    
    sept = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Sept-CHIRAYU PHARMA'""", as_dict=0)
    
    oct = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Oct-CHIRAYU PHARMA'""", as_dict=0)
    
    nov = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Nov-CHIRAYU PHARMA'""", as_dict=0)
    
    dec = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Dec-CHIRAYU PHARMA'""", as_dict=0)
    
    jan = frappe.db.sql("""select sum(opn_tot*item_rate) as "Opening",sum(rec_tot*item_rate) as "Primary/Received",
    sum(close_tot*item_rate) as "Closing",sum(sale_tot*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2018-Jan-CHIRAYU PHARMA'""", as_dict=0)
    
   
    
    datasets = [];
    datasets.append({'title': 'July', 'values': july[0]})
    datasets.append({'title': 'Aug', 'values': aug[0]})
    datasets.append({'title': 'Sept', 'values': sept[0]})
    datasets.append({'title': 'Oct', 'values': oct[0]})
    datasets.append({'title': 'Nov', 'values': nov[0]})
    datasets.append({'title': 'Dec', 'values': dec[0]})
    datasets.append({'title': 'Jan', 'values': jan[0]})
    
    #dict = {'datasets': []}
  
    #dict['datasets'] = datasets;
    #return dict
    return datasets;
