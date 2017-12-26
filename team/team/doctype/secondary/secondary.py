# -*- coding: utf-8 -*-
# Copyright (c) 2017, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import subprocess
from frappe import msgprint, _ 
import frappe.utils
from frappe.model.document import Document
from frappe.utils import cstr, flt, getdate, cint
from frappe.model.naming import make_autoname
from frappe import _
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_stock_entry(year, month,stockist):
	frappe.msgprint(_("hello"));	
	
@frappe.whitelist()
def check_duplicate(year, month,stockist):
	doc_name=year + "-" + month + "-" + stockist;
	c = frappe.db.sql("""SELECT ifnull(count(name),0) as name FROM tabSecondary where name like {0}""".format("'"+doc_name+"'"), as_dict=1);
	#return c[0].name;
	dict = {'count': 0}
	dict['count'] = c[0].name;
	return dict;
	#frappe.msgprint(_(doc_name));
	#cnt=0;
	#frappe.msgprint(_(frappe.db.sql("""SELECT count(name) FROM tabSecondary where name like {0}""".format("'"+doc_name+"'"))))
	#for c in frappe.db.sql("""SELECT count(name) as name FROM tabSecondary where name like {0}""".format("'"+doc_name+"'")):
	#	frappe.msgprint(_(c[0]));
	
	#if(cnt > 0):
	
	#frappe.msgprint(_(cnt));
		
	
@frappe.whitelist()
def get_items(year, month,stockist):
	
	#frappe.msgprint(_(frappe.get_list('Item',filters=args['filters'], fields=['name', 'item_name'])));
	#return frappe.get_list('Item',filters=args['filters'], fields=['name', 'item_name'])
	#return frappe.db.sql("""SELECT name,item_name FROM 1bd3e0294da19198.tabItem
	#where 1bd3e0294da19198.tabItem.used_for_secondary=1""", as_dict=1)
	yearmonth="";
	stockist_0=stockist;
	stockist="'"+stockist+"'";
	result=return_pre_month_year(year, month);
	#frappe.msgprint(_(result.get('mm')));
	#frappe.msgprint(_(result.get('yy')));
	yearmonth="'"+year+"-"+return_month_in_number(month)+"%'";
	prev_month_doc_name="'"+str(result.get('yy'))+"-"+result.get('mm')+"-"+stockist_0+"'";
	 
	return frappe.db.sql("""SELECT  tbl.item_name as name ,tbl.item_name as item_name,
sum(tbl.qty) as qty, sum(tbl.f_qty) as f_qty,sum(tbl.tot_qty) as tot_qty ,
sum(tbl.q_amt) as q_amt,(sum(tbl.f_amt)) as f_amt,
avg(tbl.avg_rate) as avg_rate,
sum(tbl.cr_qty) as cr_qty, sum(tbl.cr_f_qty) as cr_f_qty,sum(tbl.cr_tot_qty) as cr_tot_qty,
sum(tbl.cr_q_amt) as cr_q_amt,(sum(tbl.cr_f_amt)) as cr_f_amt,
avg(tbl.cr_avg_rate) as cr_avg_rate,
sum(tbl.close_tot) as close_tot,
sum(tbl.close_qty) as close_qty,
sum(tbl.close_free) as close_free
from
(select  t_i.name as item_name,
0 as qty, 0 as f_qty,0 as tot_qty,
0 as q_amt,0 as f_amt,
0 as avg_rate,
0 as cr_qty, 0 as cr_f_qty,0 as cr_tot_qty,
0 as cr_q_amt,0 as cr_f_amt,
0 as cr_avg_rate,
0 as close_tot,
0 as close_qty,
0 as close_free
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
avg(t_sit.base_net_rate) as cr_avg_rate,
0 as close_tot,
0 as close_qty,
0 as close_free
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
avg(t_sit.base_net_rate) as cr_avg_rate,
0 as close_tot,
0 as close_qty,
0 as close_free
from tabItem as t_i
LEFT OUTER JOIN 1bd3e0294da19198.`tabSales Invoice Item` as t_sit
on t_i.`name`=t_sit.`item_name`
LEFT OUTER JOIN 1bd3e0294da19198.`tabSales Invoice` as t_si
on t_si.`name`=t_sit.`parent`
where t_i.used_for_secondary=1
and t_si.`posting_date` like {0}
and t_si.`customer`={1}
and t_si.`name` like 'SR-0%'
group by  t_i.item_name

union 

select item_code2 as item_name,
0 as qty, 0 as f_qty,0 as tot_qty,
0 as q_amt,0 as f_amt,
0 as avg_rate,
0 as cr_qty, 0 as cr_f_qty,0 as cr_tot_qty,
0 as cr_q_amt,0 as cr_f_amt,
0 as cr_avg_rate,
ifnull(close_tot,0) as close_tot,
ifnull(close_qty,0) as close_qty,
ifnull(close_free,0) as close_free
 from tabsec_item_qty as t_sitem
 where parent={2}) 
as tbl
group by   tbl.item_name
order by tbl.item_name
""".format(yearmonth,stockist,prev_month_doc_name), as_dict=1);

def return_month_in_number(month):
	if(month=="Jan"):
		return "01";
	elif(month=="Feb"):
		return "02";
	elif(month=="March"):
		return "03";
	elif(month=="Apr"):
		return "04";
	elif(month=="May"):
		return "05";
	elif(month=="June"):
		return "06";
	elif(month=="July"):
		return "07";
	elif(month=="Aug"):
		return "08";
	elif(month=="Sept"):
		return "09";
	elif(month=="Oct"):
		return "10";
	elif(month=="Nov"):
		return "11";
	elif(month=="Dec"):
		return "12";
	pass

def return_pre_month_year(year,month):
	year=int(year);
	if(month=="Jan"):
		return {'mm': 'Dec', 'yy': year-1};
	elif(month=="Feb"):
		return {'mm': 'Jan', 'yy': year};
	elif(month=="March"):
		return {'mm': 'Feb', 'yy': year};
	elif(month=="Apr"):
		return {'mm': 'March', 'yy': year};
	elif(month=="May"):
		return {'mm': 'Apr', 'yy': year};
	elif(month=="June"):
		return {'mm': 'May', 'yy': year};
	elif(month=="July"):
		return {'mm': 'June', 'yy': year};
	elif(month=="Aug"):
		return {'mm': 'July', 'yy': year};
	elif(month=="Sept"):
		return {'mm': 'Aug', 'yy': year};
	elif(month=="Oct"):
		return {'mm': 'Sept', 'yy': year};
	elif(month=="Nov"):
		return {'mm': 'Oct', 'yy': year};
	elif(month=="Dec"):
		return {'mm': 'Nov', 'yy': year};
	


	
class Secondary(Document):
    def autoname(self):
        self.name = self.year + "-" + self.month + "-" + self.stockist;
	

    def on_update(self):
        pass;

        
    def validate(self):
	
        duplicate_pos=self.check_any_duplicate_item() # vin return -1 if not duplicate else return greater than 0
	if(duplicate_pos>=0):
		frappe.throw(_("Duplicate Item "+self.sec_items_qty[duplicate_pos].item_code2))
	else:
		new_name = self.year + "-" + self.month + "-" + self.stockist;
		if self.name != new_name and not self.is_new():
			frappe.rename_doc(self.doctype,self.name,new_name)
		
	

    def check_any_duplicate_item(self):
	duplicate_pos=-1;
	cnt=0
	for d in self.sec_items_qty:
		cnt=cnt+1                  #vin get all items count
	count=0
	while count < cnt:		   #outer loop
		count1=count+1
		while count1 < cnt:	   #inside loop		
			if((self.sec_items_qty[count].item_code2)==(self.sec_items_qty[count1].item_code2)):  #check duplicate
				duplicate_pos=count;			
			count1 += 1
		count += 1
	
	return duplicate_pos;
	
			
	
	



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

