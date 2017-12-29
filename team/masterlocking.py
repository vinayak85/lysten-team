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
    cnt_obj=""
    cnt_dc=""
    cnt_ch=""
    frmdate=""
    todate=""
    locktime=""
    starttime=""
    today_date = frappe.utils.data.get_datetime().strftime('%Y-%m-%d')
    current_time = local_time()
    temp_flag=''
    msg='' 
    
    temp1=''
    temp2=''
    call_flag=0;
        
    #frappe.msgprint(_(formname))
    
    if(len(formname)>5):
        temp1=formname[:5)]
        temp2=formname[:-(len(formname)-5)]
        formname=temp1
        call_flag=frappe.db.sql(""" select  allow_calls_without_location as call_flag from 1bd3e0294da19198.`tabDoctor Master` where name= {0} """.format(temp2), as_dict=1)               
    
    if(formname == 'T_Obj'):
        a='a'
        dataarray = frappe.db.sql(""" select ifnull(t_obj1,'')as frm_date,ifnull(t_obj2,'')as to_date,ifnull(t_obj_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)               
    
    elif formname == 'T_DrC':
        a='b'
        dataarray = frappe.db.sql(""" select ifnull(t_drc1,'')as frm_date,ifnull(t_drc2,'')as to_date,ifnull(t_drc_time,'')as lock_time,ifnull(t_drc_s_time,'')as start_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_ChC":
        a='c'
        dataarray = frappe.db.sql(""" select ifnull(t_chc1,'')as frm_date,ifnull(t_chc2,'')as to_date,ifnull(t_chc_time,'')as lock_time,ifnull(t_chc_s_time,'')as start_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    elif formname == "T_CmC":
        a='d'
        dataarray = frappe.db.sql(""" select ifnull(t_cmc1,'')as frm_date,ifnull(t_cmc2,'')as to_date,ifnull(t_cmc_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

    else:
        msg='Invalid Request Form...'
        lock_flag = '0'
        #return lock_flag
    
    if a=='a' or a=='b' or a=='c' or a=='d':
        #if len(dataarray) != 0:
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
                
                if str(locktime)=="00:00:00":
                    if a=='a':
                        msg='Ok !!! Objective Request For Today...'
                    elif a=='b':
                        msg='Ok !!! Doctor Call Request For Today...'
                    elif a=='c':
                        msg='Ok !!! Chemist Call Request For Today...'
                    elif a=='d':
                        msg='Ok !!! Campaign Booking Request For Today...'
                    lock_flag = '1'
                
                elif minutes >= 0:
                    if a=='a':
                        msg='Ok !!! Objective Request For Today; Time Is In Range...'
                        
                    elif a=='b':
                        msg='Ok !!! Doctor Call Request For Today; Time Is In Range...'
                        
                    elif a=='c':
                        msg='Ok !!! Chemist Call Request For Today; Time Is In Range...'
                        
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
                        msg='Oops !!! Chemist Call Request For Today; Time is Over...'
                        
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
        
        elif frmdate == "" and todate == "" and locktime != "":
            if(today_date == date):
                #frappe.msgprint(_(today_date))
                import datetime
                time_diff = datetime.datetime.strptime(locktime, '%H:%M:%S') - datetime.datetime.strptime(current_time, '%H:%M:%S')
                minutes = int(time_diff.total_seconds()/60)
                
                if str(locktime)=="00:00:00":
                    if a=='a':
                        msg='Ok !!! Objective Request For Today...'
                    elif a=='b':
                        msg='Ok !!! Doctor Call Request For Today...'
                    elif a=='c':
                        msg='Ok !!! Chemist Call Request For Today...'
                    elif a=='d':
                        msg='Ok !!! Campaign Booking Request For Today...'
                    lock_flag = '1'
                
                elif minutes >= 0:
                    if a=='a':
                        msg='Ok !!! Objective Request For Today; Time Is In Range...'
                        
                    elif a=='b':
                        msg='Ok !!! Doctor Call Request For Today; Time Is In Range...'
                        
                    elif a=='c':
                        msg='Ok !!! Chemist Call Request For Today; Time Is In Range...'
                        
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
                        msg='Oops !!! Chemist Call Request For Today; Time is Over...'
                        
                    elif a=='d':
                        msg='Oops !!! Campaign Booking Request For Today; Time is Over...'
                                            
                    lock_flag = '0'
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
        
        elif frmdate != "" and todate != "" and locktime == "":
            if(today_date == date):
                if a=='a':
                    msg='Ok !!! Objective Request For Today...'
                    
                elif a=='b':
                    msg='Ok !!! Doctor Call Request For Today...'
                
                elif a=='c':
                    msg='Ok !!! Chemist Call Request For Today...'
                
                elif a=='d':
                    msg='Ok !!! Campaign Booking Request For Today...'
                    
                lock_flag = '1'
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
        
        elif (((str(frmdate) == "None" or str(frmdate) == "") and (str(todate) == "None" or str(todate) == "") and (str(locktime) == "None" or str(locktime) == ""))) :
            if(today_date == date):
                if a=='a':
                    msg='Ok !!! Objective Request For Today...'
                    
                elif a=='b':
                    msg='Ok !!! Doctor Call Request For Today...'
                
                elif a=='c':
                    msg='Ok !!! Chemist Call Request For Today...'
                
                elif a=='d':
                    msg='Ok !!! Campaign Booking Request For Today...'                    
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
            msg = "Invalid Request..."
            lock_flag = '0'
            #return lock_flag
    
    
    ###################################        
    
    if a=='b' or a=='c':
     if(today_date == date):
      starttime=dataarray[0].start_time
      if starttime != "":
       starttime = starttime[:starttime.find('.')]
       
       #locktime=dataarray[0].lock_time
       #locktime = locktime[:locktime.find('.')]
       #1bd3e0294da19198.`tabObjective`
       #get count for start time...
       #cnt_obj = frappe.db.sql(""" select concat(count(*), '') as obj_cnt from 1bd3e0294da19198.`tabObjective` where 1bd3e0294da19198.`tabObjective`.`user` = {0} and 1bd3e0294da19198.`tabObjective`.`select_date` = {1}; """.format(employee,date), as_dict=1)       
       date_="'"+date+"'"
       cnt_obj = frappe.db.sql(""" select count(*) as obj_cnt from 1bd3e0294da19198.`tabObjective` where 1bd3e0294da19198.`tabObjective`.`user`= {0} and 1bd3e0294da19198.`tabObjective`.`select_date`= {1} """.format(employee,date_), as_dict=1)
       cnt_dc = frappe.db.sql(""" select count(*) as dc_cnt from 1bd3e0294da19198.`tabDoctor Calls` where dr_call_by_user_id={0} and date={1}; """.format(employee,date_), as_dict=1)
       cnt_ch = frappe.db.sql(""" select count(*) as ch_cnt from 1bd3e0294da19198.`tabChemist Call` where call_by_user_id={0} and date={1}; """.format(employee,date_), as_dict=1)
       #frappe.msgprint(_(cnt_obj))
       
       import datetime
       time_diff = datetime.datetime.strptime(locktime, '%H:%M:%S') - datetime.datetime.strptime(current_time, '%H:%M:%S')
       off_minutes = int(time_diff.total_seconds()/60) 
       
       time_diff = datetime.datetime.strptime(starttime, '%H:%M:%S') - datetime.datetime.strptime(current_time, '%H:%M:%S')
       minutes = int(time_diff.total_seconds()/60)
       
       
       ##############################
       if str(locktime)=="00:00:00" and str(starttime)=="00:00:00":               
          if a=='b':
            if int(cnt_obj[0].obj_cnt)>0:
              msg='Ok !!! Doctor Call Request For Today...'
              lock_flag = '1'
            else:
              msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
              lock_flag = '0'
          elif a=='c':
            if int(cnt_obj[0].obj_cnt)>0:
              msg='Ok !!! Chemist Call Request For Today...'
              lock_flag = '1'
            else:
              msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
              lock_flag = '0'
       ##############################
       elif str(locktime)!="00:00:00" and str(starttime)!="00:00:00":
         if off_minutes >=0:
            if minutes >= 0:
              if a=='b':
                if int(cnt_obj[0].obj_cnt)>0:
                  msg='Ok !!! Doctor Call Request For Today; Time Is In Range...'
                  lock_flag = '1'
                else:
                  msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
                  lock_flag = '0'
              elif a=='c':
                if int(cnt_obj[0].obj_cnt)>0:
                  msg='Ok !!! Chemist Call Request For Today; Time Is In Range...'
                  lock_flag = '1'
                else:
                  msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
                  lock_flag = '0'
            elif minutes <= 0:
              if a=='b':
                if int(cnt_obj[0].obj_cnt) > 0:
                  if int(cnt_dc[0].dc_cnt) > 0:
                    msg='Ok !!! Doctor Call Request For Today;'
                    lock_flag = '1'
                  else:
                    msg='Ooops !!! Doctor Call Locked Due To No Calls In Start Time...'####
                    lock_flag = '0'
                else:
                  msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
                  lock_flag = '0'
              elif a=='c':
                if int(cnt_obj[0].obj_cnt)>0:
                  if int(cnt_ch[0].ch_cnt)>0:
                    msg='Ok !!! Chemist Call Request For Today;'
                    lock_flag = '1'
                  else:
                    msg='Ooops !!! Chemist Call Locked Due To No Calls In Start Time...'####
                    lock_flag = '0'
                else:
                 msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
                 lock_flag = '0'
            else:
               if a=='b':
                 msg='Oops !!! Doctor Call Request For Today; Time is Over...'####
               elif a=='c':
                 msg='Oops !!! Chemist Call Request For Today; Time is Over...'####
               lock_flag = '0'
         else:
           if a=='b':
             msg='Oops !!! Doctor Call Request For Today; Time is Over...'
           elif a=='c':
             msg='Oops !!! Chemist Call Request For Today; Time is Over...'
           lock_flag = '0'       
       
       ##############################
       elif str(locktime)!="00:00:00" and str(starttime)=="00:00:00":
         if off_minutes >=0:
           if a=='b':
             if int(cnt_obj[0].obj_cnt)>0:
               msg='Ok !!! Doctor Call Request For Today...'
               lock_flag = '1'
             else:
               msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
               lock_flag = '0'
           elif a=='c':
             if int(cnt_obj[0].obj_cnt)>0:
               msg='Ok !!! Chemist Call Request For Today...'
               lock_flag = '1'
             else:
               msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
               lock_flag = '0'
         else:
           if a=='b':
             msg='Oops !!! Doctor Call Request For Today; Time is Over...'####
           elif a=='c':
             msg='Oops !!! Chemist Call Request For Today; Time is Over...'####
           lock_flag = '0'       
       
       ##############################
       elif str(locktime)=="00:00:00" and str(starttime)!="00:00:00":
         if minutes >= 0:
           if a=='b':
             if int(cnt_obj[0].obj_cnt)>0:
               msg='Ok !!! Doctor Call Request For Today; Time Is In Range...'
               lock_flag = '1'
             else:
               msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
               lock_flag = '0'
           elif a=='c':
             if int(cnt_obj[0].obj_cnt)>0:
               msg='Ok !!! Chemist Call Request For Today; Time Is In Range...'
               lock_flag = '1'
             else:
               msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
               lock_flag = '0'
         elif minutes <= 0:
           if a=='b':
             if int(cnt_obj[0].obj_cnt) > 0:
               if int(cnt_dc[0].dc_cnt) > 0:
                 msg='Ok !!! Doctor Call Request For Today;'
                 lock_flag = '1'
               else:
                 msg='Ooops !!! Doctor Call Locked Due To No Calls In Start Time...'####
                 lock_flag = '0'
             else:
               msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
               lock_flag = '0'
           elif a=='c':
             if int(cnt_obj[0].obj_cnt)>0:
               if int(cnt_ch[0].ch_cnt)>0:
                 msg='Ok !!! Chemist Call Request For Today;'
                 lock_flag = '1'
               else:
                 msg='Ooops !!! Chemist Call Locked Due To No Calls In Start Time...'####
                 lock_flag = '0'
             else:
               msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
               lock_flag = '0'
           else:
             if a=='b':
               msg='Oops !!! Doctor Call Request For Today; Time is Over...'
             elif a=='c':
               msg='Oops !!! Chemist Call Request For Today; Time is Over...'
             lock_flag = '0'        
       
       ##############################
       else:
         if a=='b':
           if int(cnt_obj[0].obj_cnt)>0:
             msg='Ok !!! Doctor Call Request For Today...'
             lock_flag = '1'
           else:
             msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
             lock_flag = '0'
         elif a=='c':
           if int(cnt_obj[0].obj_cnt)>0:
             msg='Ok !!! Chemist Call Request For Today...'
             lock_flag = '1'
           else:
             msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
             lock_flag = '0'
            
           
    dict = {'lock_flag': '',
            'message': '',
            'call_flag':0
           }
    
    dict['lock_flag'] = lock_flag;
    dict['message'] = msg;
    
    if formname == 'T_DrC':
        dict['call_flag'] =call_flag=[0].call_flag;    
    
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

