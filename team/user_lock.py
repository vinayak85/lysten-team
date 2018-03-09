from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def lock_check_with_std_lock(user):
    lock_prof='0'
    lock_patch='0'
    lock_doc='0'
    lock_chem='0'
    trans_obj='0'
    trans_doc='0'
    trans_chem='0'
    active_flag=''
    std_lock=''
    form_lock=''    
    
    if(user!=""):
      std_lock = frappe.db.sql("""select profile_master,patch_master,doctor_master,chemist_master,
      objective_lock_time,doctor_start_time,chemist_start_time from `tabStandard Lock`;""", as_dict=1)      
      
      form_lock = frappe.db.sql("""select m_pro,m_pat,m_doc,m_che,t_obj_time,
      t_chc_s_time,t_drc_s_time,enabled from `tabUser` where name= {0} """.format("'"+user+"'"), as_dict=1)      
      '''frappe.msgprint(_("pp: "+str(form_lock[0].enabled)));
      frappe.msgprint(_("pp: "+str(form_lock[0].t_drc_s_time)));
      frappe.msgprint(_("pp: "+str(form_lock[0].t_chc_s_time)));'''
      if(form_lock[0].enabled!=0):
        #profile master
        if(form_lock[0].m_pro==std_lock[0].profile_master):
          lock_prof='1'
        else:
          lock_prof='0' 

        #patch master          
        if(form_lock[0].m_pat==std_lock[0].patch_master):
          lock_patch='1'
        else:
          lock_patch='0' 
          
        #doctor master          
        if(form_lock[0].m_doc==std_lock[0].doctor_master):
          lock_doc='1'
        else:
          lock_doc='0'          

        #Chemist master          
        if(form_lock[0].m_che==std_lock[0].chemist_master):
          lock_chem='1'
        else:
          lock_chem='0'          

        #Objective Lock Time          
        if(form_lock[0].t_obj_time==std_lock[0].objective_lock_time):
          trans_obj='1'
        else:
          trans_obj='0'
 
        #Doctor Call Lock Time          
        if(form_lock[0].t_drc_s_time==std_lock[0].doctor_start_time):
          trans_doc='1'
        else:
          trans_doc='0'

        #Chemist Call Lock Time          
        if(form_lock[0].t_chc_s_time==std_lock[0].chemist_start_time):
          trans_chem='1'
        else:
          trans_chem='0'          
        active_flag='1'       
      else:
        lock_prof='0'
        lock_patch='0'
        lock_doc='0'
        lock_chem='0'
        trans_obj='0'
        trans_doc='0'
        trans_chem='0'
        active_flag='0'      
    else:
      lock_prof='0'
      lock_patch='0'
      lock_doc='0'
      lock_chem='0'
      trans_obj='0'
      trans_doc='0'
      trans_chem='0'
      active_flag='0'
       
        
    dict = {'lock_prof': '',
            'lock_patch': '',
            'lock_doc': '',
            'lock_chem': '',
            'trans_obj': '',
            'trans_doc': '',
            'trans_chem': '',
            'active_flag': ''
           }

    dict['lock_prof'] = lock_prof;
    dict['lock_patch'] = lock_patch;
    dict['lock_doc'] = lock_doc;
    dict['lock_chem'] = lock_chem;
    dict['trans_obj'] = trans_obj;
    dict['trans_doc'] = trans_doc;
    dict['trans_chem'] = trans_chem;
    dict['active_flag'] = active_flag;    
    
    return dict

@frappe.whitelist()
def update_user_lock_time_and_date(m_pro,m_pat,m_doc,m_che,t_obj_time,t_drc_s_time,t_chc_s_time):
    flag=0;
    frappe.msgprint(_("a"));
    if(m_pro!="" and m_pat!="" and m_doc!="" and m_che!="" and t_obj_time!="" and t_drc_s_time!="" and t_chc_s_time!=""):
        frappe.msgprint(_("b"));
        frappe.db.sql("""update `tabUser` 
        set 
        m_pro={0},
        m_pat={1},
        m_doc={2},
        m_che={3},
        t_obj_time={4},
        t_drc_s_time={5},
        t_chc_s_time={6},
        t_drc1="",
        t_drc2="",
        t_obj1="",
        t_obj2="",
        t_chc1="",
        t_chc2=""
        where enabled=1 and 
        designation in ('TBM','ABM','RBM','SM','NBM') """.format(m_pro,m_pat,m_doc,m_che,t_obj_time,t_drc_s_time,t_chc_s_time), as_dict=1)  
        flag=1;
    else:
        frappe.msgprint(_("c"));
        flag=0;
        
    dict = {'flag': 0}
    dict['flag'] = flag;
    return dict
    
