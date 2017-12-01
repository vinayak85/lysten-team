# -*- coding: utf-8 -*-
# Copyright (c) 2017, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
import frappe.utils
from frappe.model.document import Document
from frappe.utils import cstr, flt, getdate, cint
from frappe.model.naming import make_autoname
from frappe import _
from frappe.model.mapper import get_mapped_doc



@frappe.whitelist()
def make_stock_entry(year, month,stockist):
	#frappe.msgprint(_(aa+"hello"+bb));
	#frappe.msgprint(_(name.year))
	Secondary.test();
	
@frappe.whitelist()
def get_items(year, month,stockist):
	#frappe.msgprint(_("hii"));
	#frappe.msgprint(_(frappe.get_list('Item',filters=args['filters'], fields=['name', 'item_name'])));
	#return frappe.get_list('Item',filters=args['filters'], fields=['name', 'item_name'])
	#return frappe.db.sql("""SELECT name,item_name FROM 1bd3e0294da19198.tabItem
	#where 1bd3e0294da19198.tabItem.used_for_secondary=1""", as_dict=1)
	yearmonth="";
	yearmonth=year+"-"+month;
	
	 
	return frappe.db.sql("""SELECT  tbl.item_name as name ,tbl.item_name as item_name,
sum(tbl.qty) as qty, sum(tbl.f_qty) as f_qty,sum(tbl.tot_qty) as tot_qty ,
sum(tbl.q_amt) as q_amt,(sum(tbl.f_amt)) as f_amt,
avg(tbl.avg_rate) as avg_rate,
sum(tbl.cr_qty) as cr_qty, sum(tbl.cr_f_qty) as cr_f_qty,sum(tbl.cr_tot_qty) as cr_tot_qty,
sum(tbl.cr_q_amt) as cr_q_amt,(sum(tbl.cr_f_amt)) as cr_f_amt,
avg(tbl.cr_avg_rate) as cr_avg_rate from
(select  t_i.name as item_name,
0 as qty, 0 as f_qty,0 as tot_qty,
0 as q_amt,0 as f_amt,
0 as avg_rate,
0 as cr_qty, 0 as cr_f_qty,0 as cr_tot_qty,
0 as cr_q_amt,0 as cr_f_amt,
0 as cr_avg_rate
from tabItem as t_i
where t_i.used_for_secondary=1
group by  t_i.item_name

UNION
select  t_i.name as item_name,
sum(t_sit.qty) as qty, sum(t_sit.free_quantity) as f_qty,(sum(t_sit.qty) +sum(t_sit.free_quantity)) as tot_qty,
sum(t_sit.base_net_amount) as q_amt,(sum(t_sit.free_quantity)*avg(t_sit.base_net_rate)) as f_amt,
avg(t_sit.base_net_rate) as avg_rate,
0 as cr_qty, 0 as cr_f_qty,0 as cr_tot_qty,
0 as cr_q_amt,0 as cr_f_amt,
avg(t_sit.base_net_rate) as cr_avg_rate
from tabItem as t_i
LEFT OUTER JOIN 1bd3e0294da19198.`tabSales Invoice Item` as t_sit
on t_i.`name`=t_sit.`item_name`
LEFT OUTER JOIN 1bd3e0294da19198.`tabSales Invoice` as t_si
on t_si.`name`=t_sit.`parent`
where t_i.used_for_secondary=1
and t_si.`posting_date` like {0}
and t_si.`customer`={1}
and t_si.`name` like 'SI-%'
group by  t_i.item_name

union

select  t_i.name as item_name,
0 as qty, 0 as f_qty,0 as tot_qty,
0 as q_amt,0 as f_amt,
0 as avg_rate,
sum(t_sit.qty) as cr_qty, sum(t_sit.free_quantity) as cr_f_qty,(sum(t_sit.qty) +sum(t_sit.free_quantity)) as cr_tot_qty,
sum(t_sit.base_net_amount) as cr_q_amt,(sum(t_sit.free_quantity)*avg(t_sit.base_net_rate)) as cr_f_amt,
avg(t_sit.base_net_rate) as cr_avg_rate
from tabItem as t_i
LEFT OUTER JOIN 1bd3e0294da19198.`tabSales Invoice Item` as t_sit
on t_i.`name`=t_sit.`item_name`
LEFT OUTER JOIN 1bd3e0294da19198.`tabSales Invoice` as t_si
on t_si.`name`=t_sit.`parent`
where t_i.used_for_secondary=1
and t_si.`posting_date` like {0}
and t_si.`customer`={1}
and t_si.`name` like 'SR-0%'
group by  t_i.item_name) 
as tbl
group by   tbl.item_name
order by tbl.item_name
""".format(yearmonth,stockist), as_dict=1);

def return_month_in_number(month):
	if(month=="Jan"):
		return 1;
	elif(month=="Feb"):
		return 2;


	
class Secondary(Document):
    def autoname(self):
        self.name = self.year + "-" + self.month + "-" + self.stockist;
	

    def on_update(self):
        pass;

        
    def validate(self):
	new_name = self.year + "-" + self.month + "-" + self.stockist;
	if self.name != new_name and not self.is_new():
		frappe.rename_doc(self.doctype,self.name,new_name)
        #frappe.msgprint(_("validate"));

    def test():
	pass;
	#frappe.msgprint(_("hiii"));
	
  	 
	
    '''    
    def before_save():
        frappe.msgprint(_("before_save"));
        
   
        
    def before_submit(self): 
        frappe.msgprint(_("before_submit"));
        
    def before_update_after_submit(self):
        frappe.msgprint(_("before_update_after_submit"));
   
    def on_change(self):
        frappe.msgprint(_("on_change")); '''

