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
        msg='Empty Employee Code or Branch In Profile ???Contact With Office...'      
    else:
        emp_branch = frappe.db.sql("""select branch from 1bd3e0294da19198.`tabEmployee` where name= {0} """.format(employee), as_dict=1)
        user_branch = frappe.db.sql("""select branch from 1bd3e0294da19198.`tabUser` where name= {0} """.format(userid), as_dict=1)
      if(emp_branch == 'profile'):
        lock_flag = frappe.db.sql("""select m_pro from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
        if lock_flag[0].m_pro > 0:
          msg='Oops !!! Locked Profile...'
        else:
            msg='Unlock Profile'
        temp_flag=str(lock_flag[0].m_pro)

      elif formname == "patch":
        lock_flag = frappe.db.sql(""" select m_pat from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
        if lock_flag[0].m_pat > 0:
          msg='Oops !!! Locked Patch...'
        else:
            msg='Unlock Patch'
        temp_flag=str(lock_flag[0].m_pat)

      elif formname == "doctor":
        lock_flag = frappe.db.sql(""" select m_doc from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
        if lock_flag[0].m_doc > 0:
          msg='Oops !!! Locked Doctor...'
        else:
          msg='Unlock Doctor'
        temp_flag=str(lock_flag[0].m_doc)

      elif formname == "chemist":
        lock_flag = frappe.db.sql(""" select m_che from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
        if lock_flag[0].m_che > 0:
          msg='Oops !!! Locked Chemist...'
        else:
          msg='Unlock Chemist'
        temp_flag=str(lock_flag[0].m_che)

      else:
        lock_flag = '0'
        msg='Empty Employee Code or Branch In Profile ???Contact With Office...'
        temp_flag='0'
        #return lock_flag
        
    dict = {'veri_flag': '',
            'message': ''
           }

    dict['veri_flag'] = temp_flag;
    dict['message'] = msg;
    
    return dict
