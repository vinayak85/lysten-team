from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def lock_master_forms(employee,formname):
    lock_flag='0'
    temp_flag=''
    msg=''
    if(formname == 'profile'):
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
        msg='Failed...'
        temp_flag='0'
        #return lock_flag
        
    dict = {'lock_flag': '',
            'message': ''
           }

    dict['lock_flag'] = temp_flag;
    dict['message'] = msg;
    
    return dict
    
@frappe.whitelist()
def lock_transaction_forms(employee,formname,date):    
    lock_flag='0'
    dataarray=""
    frmdate=""
    todate=""
    locktime=""
    today_date = frappe.utils.data.get_datetime().strftime('%Y-%m-%d')
    current_time = local_time()
    temp_flag=''
    msg=''   
    #frappe.msgprint(_(formname))
    
    if(formname == 'T_Obj'):
        a='a'
        dataarray = frappe.db.sql(""" select ifnull(t_obj1,'')as frm_date,ifnull(t_obj2,'')as to_date,ifnull(t_obj_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)                
    
    elif formname == "T_DrC":
        a='b'
        dataarray = frappe.db.sql(""" select ifnull(t_drc1,'')as date,ifnull(t_drc2,'')as to_date,ifnull(t_drc_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_ChC":
        a='c'
        dataarray = frappe.db.sql(""" select ifnull(t_chc1,'')as frm_date,ifnull(t_chc2,'')as to_date,ifnull(t_chc_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_CmC":
        a='d'
        dataarray = frappe.db.sql(""" select ifnull(t_cmc1,'')as frm_date,ifnull(t_cmc2,'')as to_date,ifnull(t_cmc_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    else:
        msg='Invalid Request...'
        lock_flag = '0'
        #return lock_flag
    
    if a=='a' or a=='b' or a=='c' or a=='d':
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
                import datetime
                time_diff = datetime.datetime.strptime(locktime, '%H:%M:%S') - datetime.datetime.strptime(current_time, '%H:%M:%S')
                minutes = int(time_diff.total_seconds()/60)
                
                if minutes >= 0:
                    if a=='a':
                        msg='Ok !!! Objective Request For Today; Time Is In Range...'
                        
                    elif a=='b':
                        msg='Ok !!! Doctor Call Request For Today; Time Is In Range...'
                        
                    elif a=='c':
                        msg='Ok !!! Chemist Call Request Request For; Today Time Is In Range...'
                        
                    elif a=='d':
                        msg='Ok !!! Campaign Booking Request For Today; Time Is In Range...'
                    
                    lock_flag = '1'
                    #return lock_flag
                else:
                    if a=='a':
                        msg='Oops !!! Objective Request For Today; Time is Over...'
                        
                    elif a=='b':
                        msg='Oops !!! Doctor Call Request For Today; Time is Over...'
                        
                    elif a=='c':
                        msg='Oops !!! Chemist Call Request Request For; Time is Over...'
                        
                    elif a=='d':
                        msg='Oops !!! Campaign Booking Request For Today; Time is Over...'
                                            
                    lock_flag = '0'
                    #return lock_flag
             
            elif(date >= frmdate  and date <= todate):
                #frappe.msgprint(_('bbb'))
                if a=='a':
                    msg='Ok !!! Objective Request For Between Date;Is In Range...'
                        
                elif a=='b':
                    msg='Ok !!! Doctor Call Request For Between Date;Is In Range...'
                        
                elif a=='c':
                    msg='Ok !!! Chemist Call Request For Between Date;Is In Range...'
                        
                elif a=='d':
                    msg='Ok !!! Campaign Booking Request For Between Date;Is In Range...'
                
                lock_flag = '1'
                #return lock_flag
             
            else:
                if a=='a':
                    msg='Oops !!! Objective Request For Selected Date Is Locked...'
                        
                elif a=='b':
                    msg='Oops !!! Doctor Call Request For Selected Date Is Locked...'
                        
                elif a=='c':
                    msg='Oops !!! Chemist Call Request For Selected Date Is Locked...'
                        
                elif a=='d':
                    msg='Oops !!! Campaign Booking Request For Selected Date Is Locked...'
                    
                lock_flag = '0'
                #return lock_flag
        else:
            msg='Please Set From-To Date And Time'
            lock_flag = '0'
            #return lock_flag
        
    dict = {'lock_flag': '',
            'message': ''
           }

    dict['lock_flag'] = lock_flag;
    dict['message'] = msg;
    
    return dict    
    
    
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

