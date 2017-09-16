from __future__ import unicode_literals
import frappe
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def lock_master_forms(employee,formname):
    lock_flag=0
    if(formname == 'profile'):
        lock_flag = frappe.db.sql("""select m_pro from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
        return lock_flag

    elif formname == "patch":
         lock_flag = frappe.db.sql(""" select m_pat from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
         return lock_flag

    elif formname == "doctor":
        lock_flag = frappe.db.sql(""" select m_doc from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
        return lock_flag

    elif formname == "chemist":
         lock_flag = frappe.db.sql(""" select m_che from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)
         return lock_flag

    else:
        return lock_flag

def lock_transaction_forms(employee,formname,date):
    lock_flag=0
    frmdate=""
    todate=""
    locktime=""
    today_date = frappe.utils.data.get_datetime().strftime('%Y/%m/%d')
    current_time = local_time()
    if(formname == 'T_Obj'):
        frmdate,todate,locktime = frappe.db.sql(""" select ifnull(t_obj1,'')as obj_frm_date,ifnull(t_obj2,'')as obj_to_date,ifnull(t_obj_time,'')as obj_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_DrC":
        frmdate,todate,locktime = frappe.db.sql(""" select ifnull(t_drc1,'')as doc_frm_date,ifnull(t_drc2,'')as doc_to_date,ifnull(t_drc_time,'')as doc_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_ChC":
        frmdate,todate,locktime = frappe.db.sql(""" select ifnull(t_chc1,'')as che_frm_date,ifnull(t_chc2,'')as che_to_date,ifnull(t_chc_time,'')as che_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_CmC":
        frmdate,todate,locktime = frappe.db.sql(""" select ifnull(t_cmc1,'')as cam_frm_date,ifnull(t_cmc2,'')as cam_to_date,ifnull(t_cmc_time,'')as cam_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    else:
        lock_flag=0

    if frmdate != "" and todate != "" and locktime != "":
        if(date >= frmdate and date <= todate):
            lock_flag=1
        elif(today_date == date):
            if current_time<=locktime:
                lock_flag=1
            else:
                lock_flag=0
        else:
            lock_flag=0
    else:
        lock_flag=0

    return lock_flag

#Europe/Berlin
def local_time(zone='Asia/Kolkata'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%T')


    #import datetime
    #print(datetime.datetime.now().time())
    ###from datetime import datetime
    ###from pytz import timezone

    #Europe/Berlin
    ###def local_time(zone='Asia/Kolkata'):
    ###  other_zone = timezone(zone)
    ###  other_zone_time = datetime.now(other_zone)
    ###  return other_zone_time.strftime('%T')


    ###print(local_time())
