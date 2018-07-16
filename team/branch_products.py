# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

# this method is used for android heirachy get Hq based on user territory
#it will featch all HQ of related to the user
@frappe.whitelist()
def product_list(branch):   
    temp_flag=''
    msg=''
    test=''
    if(branch == ''):
        msg='Empty Branch...'      
    else:
        msg = frappe.db.sql("""select GROUP_CONCAT(name) as comma_product from `tabItem` 
        where branch={0} group by branch""".format(branch), as_dict=1)        
        
    dict = {'msg': ''
           }

    dict['msg'] = msg[0].comma_product;
    
    return dict

@frappe.whitelist()
def product_list1(branch):   
    temp_flag=''
    msg=''
    test=''
    if(branch == ''):
        msg='Empty Branch...'      
    elif(branch == 'ALL Branch'):
        msg = frappe.db.sql("""select GROUP_CONCAT(name) as comma_product from `tabItem` 
        where branch in('','')""".format(branch), as_dict=1)
    else:
        msg = frappe.db.sql("""select GROUP_CONCAT(name) as comma_product from `tabItem` 
        where branch={0} group by branch""".format(branch), as_dict=1)        
        
    dict = {'msg': ''
           }

    dict['msg'] = msg[0].comma_product;
    
    return dict

