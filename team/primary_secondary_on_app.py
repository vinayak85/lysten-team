from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _

__version__ = '0.0.1'

@frappe.whitelist()
def get_date_and_app_support(User,Stockist,FromDate,ToDate,Products):
	#User,Branch,Stockist,FromDate,ToDate,Products,flag_of_operation
	branch_p=frappe.db.sql("""select branch from `tabUser` 
	where name={0} and enabled=1;""".format("'"+User+"'"), as_dict=1)
	
	'''Stockist Section For Given User'''
	stockist_with_commas=frappe.db.sql("""select GROUP_CONCAT(stockist) as comma_stock from  `tabStockist For User` 
	where parent={0} and enable=1;""".format("'"+User+"'"), as_dict=1)
	
	full_name=frappe.db.sql("""select full_name from `tabUser` 
	where name={0} and enabled=1;""".format("'"+User+"'"), as_dict=1)
	
	stockist_with_commas=stockist_with_commas[0].comma_stock;
	
	list_of_stockist=[];
	list_of_stockist=stockist_with_commas.split (',');
	
	'''Product Section For Branch'''
	branch=branch_p[0].branch;
	branch_product=product_list(branch_p[0].branch)
	#frappe.msgprint(_(branch));
	prod_list=[];
	prod_list=branch_product.split (',')
	datasets1=[];
	datasets2=[];
	for pp in list_of_stockist:		
		datasets2=[];
		tot_sale_qty=0;
		tot_sale_value=0;
		tot_ret_qty=0;
		tot_ret_value=0;
		emp_of_stockist=count_employee_of_stockist(pp,branch)
		#frappe.msgprint(_(pp+" "+str(emp_of_stockist[0].tot_emp)+" "+emp_of_stockist[0].emp));
		
		#ab="";
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
			
			#ab+='{'+'product:'+qq+',sale_qty:'+str(prod_sale_data[0].qty)+',sale_value:'+str(prod_sale_data[0].value)+',ret_qty:0,ret_value:0'+'},';
			#frappe.msgprint(_(pp+" "+qq+" "+User+" "+));
			
			pass
		#ab=ab[:-1];
		datasets1.append({ 'employee':User
				  ,'full_name':str(full_name[0].full_name)
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

def count_employee_of_stockist(Stockist,branch):
	'''emp_of_stockist=frappe.db.sql("""select GROUP_CONCAT(parent)as emp,count(parent)as tot_emp 
	from  `tabStockist For User` where stockist={0} and enable=1""".format("'"+Stockist+"'"), as_dict=1)'''
	emp_of_stockist=frappe.db.sql("""select group_concat(full_name)as emp,count(name)as tot_emp from `tabUser` 
	where branch={0} and designation='TBM'and 
	name in(select parent from `tabStockist For User` 
	where stockist={1} and enable=1)""".format("'"+branch+"'","'"+Stockist+"'"), as_dict=1)
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


@frappe.whitelist()
def stockist_list_for_top_hierarchy(employee,designation,limit, offset):
	#frappe.msgprint(_(employee+'  '+designation))	
	if designation == "ABM":
		return frappe.db.sql(""" SELECT distinct stockist as name,full_name,territory 
		FROM 1bd3e0294da19198.`tabStockist For User` 
		where parent in(Select name from `tabUser` 
		where abm={0} and enabled=1) and enable=1 LIMIT {1} offset {2}""".format(employee,limit,offset),as_dict=True)
	elif designation == "RBM":
		return frappe.db.sql(""" SELECT distinct stockist as name,full_name,territory 
		FROM 1bd3e0294da19198.`tabStockist For User` 
		where parent in(Select name from `tabUser` 
		where rbm={0} and enabled=1) and enable=1 LIMIT {1} offset {2}""".format(employee,limit,offset),as_dict=True)
	elif designation == "ZBM":
		return frappe.db.sql(""" SELECT distinct stockist as name,full_name,territory
		FROM 1bd3e0294da19198.`tabStockist For User` 
		where parent in(Select name from `tabUser` 
		where zbm={0} and enabled=1) and enable=1 
		LIMIT {1}  OFFSET {2} ;""".format(employee,limit,offset),as_dict=True)
	elif designation == "SM":
		return frappe.db.sql(""" SELECT distinct stockist as name,full_name,territory 
		FROM 1bd3e0294da19198.`tabStockist For User` 
		where parent in(Select name from `tabUser` 
		where sm={0} and enabled=1) and enable=1 
		LIMIT {1}  OFFSET {2} ;""".format(employee,limit,offset),as_dict=True)
	elif designation == "NBM":
		return frappe.db.sql(""" SELECT distinct stockist as name,full_name,territory 
		FROM 1bd3e0294da19198.`tabStockist For User` 
		where parent in(Select name from `tabUser` 
		where nbm={0} and enabled=1) and enable=1 
		LIMIT {1}  OFFSET {2} ;""".format(employee,limit,offset),as_dict=True)
	elif designation == "CRM": 
		return frappe.db.sql(""" SELECT distinct stockist as name,full_name,territory
		FROM 1bd3e0294da19198.`tabStockist For User` 
		where parent in(Select name from `tabUser` 
		where crm={0} and enabled=1) and enable=1 
		LIMIT {1}  OFFSET {2} ;""".format(employee,limit,offset),as_dict=True)
	elif (designation == "Head of Marketing and Sales"):#Sales Head 
		branch = frappe.db.sql("""select branch from 1bd3e0294da19198.`tabUser` 
		where name={0} and enabled=1""".format(employee), as_dict=1) 
		
		return frappe.db.sql(""" SELECT distinct stockist as name,full_name,territory 
		FROM 1bd3e0294da19198.`tabStockist For User` 
		where parent in(select name from 1bd3e0294da19198.`tabUser` 
		where `tabUser`.`enabled`=1 and branch={0} and `tabUser`.`designation` in('TBM')) and enable=1
		LIMIT {1}  OFFSET {2} ;""".format("'"+branch[0].branch+"'",limit,offset),as_dict=True)
	elif (designation == "HR Manager" or designation == "Admin"):
		return frappe.db.sql(""" SELECT distinct stockist as name,full_name,territory FROM 1bd3e0294da19198.`tabStockist For User` where enable=1 
		LIMIT {1}  OFFSET {2} ;""".format(employee,limit,offset),as_dict=True)
	else:
		frappe.msgprint(_("No entry"))



@frappe.whitelist()
def get_primary_data_of_stockist(User,Stockist,FromDate,ToDate,Products):
	'''
	Employee List For Given Stockist:
	select Group_Concat(full_name,concat(' [ ',headquarter,' ]')) as user from 1bd3e0294da19198.`tabUser` 
  where `tabUser`.`enabled`=1 and name in (SELECT parent FROM 1bd3e0294da19198.`tabStockist For User` where stockist='Drug Distributor' and enable=1) and branch='Main' and `tabUser`.`designation` in('TBM');
  '''
	
	#User,Branch,Stockist,FromDate,ToDate,Products,flag_of_operation
	branch_p=frappe.db.sql("""select branch from `tabUser` 
	where name={0} and enabled=1;""".format("'"+User+"'"), as_dict=1)
	
	'''Stockist Section For Given User'''
	stockist_with_commas=frappe.db.sql("""select GROUP_CONCAT(stockist) as comma_stock from  `tabStockist For User` 
	where parent={0} and enable=1;""".format("'"+User+"'"), as_dict=1)
	
	full_name=frappe.db.sql("""select full_name from `tabUser` 
	where name={0} and enabled=1;""".format("'"+User+"'"), as_dict=1)
	
	stockist_with_commas=stockist_with_commas[0].comma_stock;
	
	list_of_stockist=[];
	list_of_stockist=stockist_with_commas.split (',');
	
	'''Product Section For Branch'''
	branch=branch_p[0].branch;
	branch_product=product_list(branch_p[0].branch)
	#frappe.msgprint(_(branch));
	prod_list=[];
	prod_list=branch_product.split (',')
	datasets1=[];
	datasets2=[];
	for pp in list_of_stockist:		
		datasets2=[];
		tot_sale_qty=0;
		tot_sale_value=0;
		tot_ret_qty=0;
		tot_ret_value=0;
		emp_of_stockist=count_employee_of_stockist(pp,branch)
		#frappe.msgprint(_(pp+" "+str(emp_of_stockist[0].tot_emp)+" "+emp_of_stockist[0].emp));
		
		#ab="";
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
				});
			
			pass
		datasets1.append({ 'employee':User
				  ,'full_name':str(full_name[0].full_name)
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

