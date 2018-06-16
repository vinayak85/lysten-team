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
	
	'''Stockist Section For Given User'''
	stockist_with_commas=frappe.db.sql("""select GROUP_CONCAT(stockist) as comma_stock from  `tabStockist For User` 
	where parent={0} and enable=1;""".format("'"+User+"'"), as_dict=1)
	
	stockist_with_commas=stockist_with_commas[0].comma_stock;
	
	list_of_stockist=[];
	list_of_stockist=stockist_with_commas.split (',');
	
	'''Product Section For Branch'''
	branch=product_list(branch_p[0].branch)
	#frappe.msgprint(_(branch));
	prod_list=[];
	prod_list=branch.split (',')
	datasets1=[];
	datasets2=[];
	for pp in list_of_stockist:		
		datasets2=[];
		tot_sale_qty=0;
		tot_sale_value=0;
		tot_ret_qty=0;
		tot_ret_value=0;
		emp_of_stockist=count_employee_of_stockist(pp)
		#frappe.msgprint(_(pp+" "+str(emp_of_stockist[0].tot_emp)+" "+emp_of_stockist[0].emp));
		for qq in prod_list:
			prod_sale_data = get_sale_data_for_select_stockist(pp,FromDate,ToDate,qq);
			tot_sale_qty+=prod_sale_data[0].qty;
			tot_sale_value+=prod_sale_data[0].value;
			datasets2.append({ #'Stockist':User
			  	  #,'Stockist':pp,
				  'product':qq
				  ,'sale_qty':str(prod_sale_data[0].qty)
				  ,'sale_value':str(prod_sale_data[0].value)
				  ,'ret_qty':str(0)
				  ,'ret_value':str(0)
		    		  #,'tot_emp':str(emp_of_stockist[0].tot_emp)
			  	  #,'emp':str(emp_of_stockist[0].emp)
				 #,'flag':'S'
				});
			#frappe.msgprint(_(pp+" "+qq+" "+User+" "+));
			pass
		datasets1.append({ 'employee':User
			  	  ,'stockist':pp				  
				  ,'tot_emp':str(emp_of_stockist[0].tot_emp)
			  	  ,'emp':str(emp_of_stockist[0].emp)
				  ,'tot_sale_qty':tot_sale_qty
				  ,'tot_sale_value':tot_sale_value
				  ,'tot_ret_qty':tot_ret_qty
				  ,'tot_ret_value':tot_ret_value
				  ,'from_date':FromDate
				  ,'to_date':ToDate
				  ,'product_data':datasets2				  		    		  				 
				});
		pass
	return datasets1;

    


@frappe.whitelist()
def get_sale_data_for_select_stockist_no_important(Stockist,FromDate,ToDate,Product):
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
def get_sale_data_for_select_stockist(Stockist,FromDate,ToDate,Product):
  msg = frappe.db.sql("""select ifnull(sum(`qty`),0) as "qty",ifnull(sum(`net_amount`),0) as "value" from `tabSales Invoice Item` 
where `item_code`={0} and parent in(select name from `tabSales Invoice` where name like "SI-%" and status in('Draft','Unpaid','Overdue') and `tabSales Invoice`.`customer_name`={1} and posting_date between {2} and {3});
""".format("'"+Product+"'","'"+Stockist+"'","'"+FromDate+"'","'"+ToDate+"'"), as_dict=1)    
  #frappe.msgprint(_(msg));
  return msg;

#@frappe.whitelist()
def get_return_data_for_select_stockist(Stockist,FromDate,ToDate,Product):
  msg = frappe.db.sql("""select ifnull(sum(`qty`),0) as "qty",ifnull(sum(`net_amount`),0) as "value" from `tabSales Invoice Item` 
where `item_code`={0} and parent in(select name from `tabSales Invoice` where name like "SI-%" and status in('Draft','Unpaid','Overdue') and `tabSales Invoice`.`customer_name`={1} and posting_date between {2} and {3});
""".format("'"+Product+"'","'"+Stockist+"'","'"+FromDate+"'","'"+ToDate+"'"), as_dict=1)    
  #frappe.msgprint(_(msg));
  return msg;

def count_employee_of_stockist(Stockist):
	'''emp_of_stockist=frappe.db.sql("""select GROUP_CONCAT(parent)as emp,count(parent)as tot_emp 
	from  `tabStockist For User` where stockist={0} and enable=1""".format("'"+Stockist+"'"), as_dict=1)'''
	emp_of_stockist=frappe.db.sql("""select group_concat(full_name)as emp,count(name)as tot_emp from `tabUser` 
	where branch='Main' and designation='TBM'and 
	name in(select parent from `tabStockist For User` 
	where stockist={0} and enable=1)""".format("'"+Stockist+"'"), as_dict=1)
	return emp_of_stockist;

#@frappe.whitelist()
def product_list(branch): 
    msg=''
    if(branch == ''):
        msg=''      
    else:
        msg = frappe.db.sql("""select GROUP_CONCAT(name) as comma_product from `tabItem` 
        where branch={0} group by branch""".format("'"+branch+"'"), as_dict=1)        
    
    return msg[0].comma_product ;

def user_list(stockist_name): 
    users=''
    if(branch == ''):
        users=''      
    else:
        users = frappe.db.sql("""select GROUP_CONCAT(name) as comma_product from `tabItem` 
        where branch={0} group by branch""".format("'"+stockist_name+"'"), as_dict=1)        
    
    return users[0].comma_product ;

def stockist_list(branch): 
    msg=''
    if(branch == ''):
        msg='Empty Branch...'      
    else:
        msg = frappe.db.sql("""select GROUP_CONCAT(name) as comma_product from `tabItem` 
        where branch={0} group by branch""".format("'"+branch+"'"), as_dict=1)        
    
    return msg[0].comma_product ;
