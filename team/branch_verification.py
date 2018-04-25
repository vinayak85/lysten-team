# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
__version__ = '0.0.1'

# this method is used for android heirachy get Hq based on user territory
#it will featch all HQ of related to the user
@frappe.whitelist()
def lock_master_forms(userid,employee):
    lock_flag='0'
    temp_flag=''
    msg=''
    test=''
    if(employee == ''):
        msg='Empty Employee Code or Branch In Profile ??? Contact With Office...'      
    else:
        emp_branch = frappe.db.sql("""select ifnull(branch,"") as branch  from 
        1bd3e0294da19198.`tabEmployee` where name= {0} """.format(employee), as_dict=1)
        user_branch = frappe.db.sql("""select ifnull(branch,"") as branch  from 
        1bd3e0294da19198.`tabUser` where name= {0} """.format(userid), as_dict=1)
        
        e_branch=str(emp_branch[0].branch)
        u_branch=str(user_branch[0].branch)
        
        if(e_branch == '' and u_branch == ''):
            msg='Empty Branch In Employee,User Form; Inform To Office For Fiil Up...'
            temp_flag='0'
        elif(e_branch == '' and u_branch != ''):
            msg='Empty Branch In Employee Form; Inform To Office For Fiil Up...'
            temp_flag='0'        
        elif(e_branch != '' and u_branch == ''):
            msg='Empty Branch In User Form; Inform To Office For Fiil Up...'
            temp_flag='0'
        elif(e_branch != u_branch):
            msg='Miss Match Branch In Employee,User Form; Inform To Office For Correction...'
            temp_flag='0'      
        else:
            msg='Miss Match Branch In Employee,User Form; Inform To Office For Correction...'
            temp_flag='1'
        
    dict = {'veri_flag': '',
            'message': ''
           }

    dict['veri_flag'] = temp_flag;
    dict['message'] = msg;
    
    return dict
