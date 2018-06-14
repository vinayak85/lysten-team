from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _

__version__ = '0.0.1'

@frappe.whitelist()
def get_date_and_app_support(User,Stockist,FromDate,ToDate,Products):
	#User,Branch,Stockist,FromDate,ToDate,Products,flag_of_operation
	branch_p=frappe.db.sql("""select branch from `tabUser` 
	where name='kasimmevekari@gmail.com' and enabled=1;""".format("'"+User+"'"), as_dict=1)
	
	branch=product_list(branch_p[0].branch)
	frappe.msgprint(_(branch));
	#prod_list=[];
	#prod_list=branch.split (',')
	#for pp in prod_list:
		#frappe.msgprint(_(pp));
	
	'''if(designation=='ABM'):
		msg = frappe.db.sql("""select group_concat(territory_name) from `tabTerritory` where parent_territory='Ichalkaranji(Area)'
		select territory_name from `tabTerritory` where parent_territory={0}""".format("'"+headquarter+"'"), as_dict=1)    
		frappe.msgprint(_(msg));'''

    


@frappe.whitelist()
def get_sale_data_for_select_stockist(Stockist,FromDate,ToDate,Product):
	datasets1=[];
	msg = get_return_data_for_select_stockist(Stockist,FromDate,ToDate,Product);  
	'''frappe.db.sql("""select ifnull(sum(`qty`),0) as "qty",ifnull(sum(`net_amount`),0) as "value" from `tabSales Invoice Item` 
where `item_code`={0} and parent in(select name from `tabSales Invoice` where name like "SI-%" and status in('Draft','Unpaid','Overdue') and `tabSales Invoice`.`customer_name`={1} and posting_date between {2} and {3});
""".format("'"+Product+"'","'"+Stockist+"'","'"+FromDate+"'","'"+ToDate+"'"), as_dict=1)    
  frappe.msgprint(_(msg));'''
	
	emp_of_stockist=frappe.db.sql("""select GROUP_CONCAT(parent)as emp,count(parent)as tot_emp 
	from  `tabStockist For User` 
	where stockist={0} and enable=1""".format("'"+Stockist+"'"), as_dict=1)
	
	datasets1.append({ 'Stockist':Stockist
				  ,'product':Product
				  ,'qty':str(msg[0].qty)
				  ,'value':str(msg[0].value)
		    		  ,'tot_emp':str(emp_of_stockist[0].tot_emp)
			  	  ,'emp':str(emp_of_stockist[0].emp)
				 ,'flag':'S'});
	return (datasets1);
  
  

#@frappe.whitelist()
def get_return_data_for_select_stockist(Stockist,FromDate,ToDate,Product):
  msg = frappe.db.sql("""select ifnull(sum(`qty`),0) as "qty",ifnull(sum(`net_amount`),0) as "value" from `tabSales Invoice Item` 
where `item_code`={0} and parent in(select name from `tabSales Invoice` where name like "SI-%" and status in('Draft','Unpaid','Overdue') and `tabSales Invoice`.`customer_name`={1} and posting_date between {2} and {3});
""".format("'"+Product+"'","'"+Stockist+"'","'"+FromDate+"'","'"+ToDate+"'"), as_dict=1)    
  #frappe.msgprint(_(msg));
  return msg;


#@frappe.whitelist()
def product_list(branch):   
    temp_flag=''
    msg=''
    test=''
    if(branch == ''):
        msg='Empty Branch...'      
    else:
        msg = frappe.db.sql("""select GROUP_CONCAT(name) as comma_product from `tabItem` 
        where branch={0} group by branch""".format("'"+branch+"'"), as_dict=1)        
    
    return msg;
