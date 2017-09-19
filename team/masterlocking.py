from __future__ import unicode_literals
import frappe
import datetime
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

@frappe.whitelist()
def lock_transaction_forms(employee,formname,date):    
    lock_flag=0
    dataarray=""
    frmdate=""
    todate=""
    locktime=""
    today_date = frappe.utils.data.get_datetime().strftime('%Y-%m-%d')
    current_time = local_time()
    
    #frappe.msgprint(_(formname))
    if(formname == 'T_Obj'):        
        dataarray = frappe.db.sql(""" select ifnull(t_obj1,'')as frm_date,ifnull(t_obj2,'')as to_date,ifnull(t_obj_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)                

    elif formname == "T_DrC":
        dataarray = frappe.db.sql(""" select ifnull(t_drc1,'')as date,ifnull(t_drc2,'')as to_date,ifnull(t_drc_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_ChC":
        dataarray = frappe.db.sql(""" select ifnull(t_chc1,'')as frm_date,ifnull(t_chc2,'')as to_date,ifnull(t_chc_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_CmC":
        dataarray = frappe.db.sql(""" select ifnull(t_cmc1,'')as frm_date,ifnull(t_cmc2,'')as to_date,ifnull(t_cmc_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    else:
        lock_flag=0
        return lock_flag
    
    frmdate=dataarray[0].frm_date
    todate=dataarray[0].to_date
    locktime=dataarray[0].lock_time
    locktime = locktime[:locktime.find('.')]
    #frappe.msgprint(_(locktime))
    #frappe.msgprint(_(frmdate+todate+date))
    #frappe.msgprint(_(today_date+' '+date))
    if frmdate != "" and todate != "" and locktime != "":        
        if(today_date == date):
            #frappe.msgprint(_(today_date))
            #import datetime
            time_diff = datetime.datetime.strptime(locktime, '%H:%M:%S') - datetime.datetime.strptime(current_time, '%H:%M:%S')
            minutes = int(time_diff.total_seconds()/60)
            if minutes >= 0:
            #if datetime.datetime(*time.strptime(current_time, '%H:%M:%S')).time() <= datetime.datetime(*time.strptime(locktime, '%H:%M:%S')).time():
            #if current_time <= locktime: 
                frappe.msgprint(_(minutes))
                lock_flag=1
                return lock_flag
            else:
                lock_flag=0
                return lock_flag
        elif(date >= frmdate  and date <= todate):
            #frappe.msgprint(_('bbb'))
            lock_flag=1
            #frappe.msgprint(_(lock_flag))
            return lock_flag
        else:
            lock_flag=0
            return lock_flag
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
