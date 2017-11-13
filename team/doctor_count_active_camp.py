from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def count_active_camp_doctors(employee):
    tot_doc='0'
    active_doc='0'
    inactive_doc='0'
    camp_doc='0'    
    tot_doc = frappe.db.sql(""" select count(*)as tot_doc from 1bd3e0294da19198.`tabDoctor Master` where user= {0} """.format(employee), as_dict=1)
    active_doc = frappe.db.sql(""" select count(*)as active_doc from 1bd3e0294da19198.`tabDoctor Master` where user= {0} and active=1 ;""".format(employee), as_dict=1)
    inactive_doc = frappe.db.sql(""" select count(*)as inactive_doc from 1bd3e0294da19198.`tabDoctor Master` where user={0} and inactive=1; """.format(employee), as_dict=1)
    camp_doc = frappe.db.sql(""" select count(*)as camp_doc from 1bd3e0294da19198.`tabDoctor Master` where user={0} and campaign_book=1; """.format(employee), as_dict=1)
        
    dict = {'tot_doc': '',
            'active_doc': '',
            'inactive_doc': '',
            'camp_doc': ''
           }

    dict['tot_doc'] = tot_doc[0].tot_doc;
    dict['active_doc'] = active_doc[0].active_doc;
    dict['inactive_doc'] = inactive_doc[0].inactive_doc;
    dict['camp_doc'] = camp_doc[0].camp_doc;
    
    return dict
