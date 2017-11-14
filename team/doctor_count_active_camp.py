from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def count_active_camp_doctors(employee):
    heqdquarter=''
    tot_doc='0';
    active_doc='0';
    inactive_doc='0';
    camp_doc='0';   
    #flag_active='0'
    #flag_camp='0'
    flag_action='0';
    msg='';
    active1 = 125;
    active2 = 80;
    campp = 40;
    
    tot_doc = frappe.db.sql(""" select count(*)as tot_doc from 1bd3e0294da19198.`tabDoctor Master` where user= {0} """.format(employee), as_dict=1)
    active_doc = frappe.db.sql(""" select count(*)as active_doc from 1bd3e0294da19198.`tabDoctor Master` where user= {0} and active=1 ;""".format(employee), as_dict=1)
    inactive_doc = frappe.db.sql(""" select count(*)as inactive_doc from 1bd3e0294da19198.`tabDoctor Master` where user={0} and inactive=1; """.format(employee), as_dict=1)
    camp_doc = frappe.db.sql(""" select count(*)as camp_doc from 1bd3e0294da19198.`tabDoctor Master` where user={0} and campaign_book=1; """.format(employee), as_dict=1)
    
    heqdquarter = frappe.db.sql(""" select headquarter_name as hq from 1bd3e0294da19198.`tabUser` where name={0} and enabled=1; """.format(employee), as_dict=1)
    
    active=active_doc[0].active_doc
    camp=camp_doc[0].camp_doc
    
    
    if(active < active1 and camp < campp):
        flag_action=1
        #flag_active='1'
        #flag_camp='1'
        msg='Both Are Enable For Update Active AND CAMP'
    elif(active >= active1 and camp <= campp):
        flag_action=2
        #flag_active='0'
        #flag_camp='1'
        msg='Lock ACTIVE and UPDATE only Active DOCTOR FOR CAMP'        
    elif(active <= active1 and camp >= campp):
        flag_action=3
        #flag_active='1'
        #flag_camp='0'
        msg='ONLY ACTIVE and Lock CAMP'        
    elif(active > active1 and camp > campp):
        flag_action=0
        #flag_active='0'
        #flag_camp='0'
        msg='Both Locked'
    else:
        flag_action=0
        #flag_active='0'
        #flag_camp='0'
        msg='Wrong Selection'        
      
    
    dict = {'tot_doc': '',
            'active_doc': '',
            'inactive_doc': '',
            'camp_doc': '',
            'flag_action':'',
            'msg':''
           }
#'flag_active':'',
            #'flag_camp':'',
    dict['tot_doc'] = tot_doc[0].tot_doc;
    dict['active_doc'] = active_doc[0].active_doc;
    dict['inactive_doc'] = inactive_doc[0].inactive_doc;
    dict['camp_doc'] = camp_doc[0].camp_doc;
    dict['flag_action']=flag_action
    #dict['flag_active'] = flag_active;
    #dict['flag_camp'] = flag_camp;
    dict['msg'] = msg;
    
    return dict
