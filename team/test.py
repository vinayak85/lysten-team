from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def get_plan_of_today(employee, designation,date_pass,app_ver):
 email_list=""
 email_list_only_TBM=""
 count_of_emp=0
 count_of_emp_tbm=0
 #i = datetime.now()
 #test=i.strftime('%Y/%m/%d %H:%M:%S')
 if((len(date_pass)) == 0):
  today_date = frappe.utils.data.get_datetime().strftime('%Y/%m/%d')
 else:
  today_date=date_pass
  
 today_date="'"+today_date+"'"
 
 objective= frappe.db.sql(""" SELECT doctor_flag as dc,camp_flag as cm,meeting_flag as mt,leave_flag as lv,call_agenda as dc_a,
  camp_agenda as cm_a,meeting_agenda as mt_a,reason as lv_a FROM 1bd3e0294da19198.`tabObjective` where 
  1bd3e0294da19198.`tabObjective`.user = {0} and
  1bd3e0294da19198.`tabObjective`.`select_date`={1} """.format(employee,today_date), as_dict=1)
  
 if len(objective) > 0:
  if objective[0].dc==1 and objective[0].cm==1 and objective[0].mt==1 and objective[0].lv==0:
    objj="";
    objj="""PLAN OF DAY : DCR  |  CAMP BOOKING  |  MEETING 
    DCR Agenda:{0}
    CAMP Agenda:{1}
    Meeting Agenda:{2}""".format( objective[0].dc_a,objective[0].cm_a,objective[0].mt_a);
    #'\033[1m' + 'This is my text string.' + '\033[0m';#'Hiii';
    #"<b>PLAN OF DAY :</b>"+ " DCR  |  CAMP BOOKING  |  MEETING \n\n"+"<b>DCR Agenda: </b>" + objective[0].dc_a +"\n"+"<b>CAMP Agenda: </b>" +objective[0].cm_a +"\n"+"<b>Meeting Agenda: </b>" +objective[0].dc_mt;
          
  elif objective[0].dc==1 and objective[0].cm==1 and objective[0].mt==0 and objective[0].lv==0:
    objj="";
    objj="""PLAN OF DAY : DCR  |  CAMP BOOKING 
    DCR Agenda:{0}
    CAMP Agenda:{1}""".format( objective[0].dc_a,objective[0].cm_a);
    #objj="<b>PLAN OF DAY :</b>"+ " DCR  |  CAMP BOOKING \n\n"+"<b>DCR Agenda: </b>" + objective[0].dc_a +"\n"+"<b>CAMP Agenda: </b>" +objective[0].cm_a +"\n"+"<b>Meeting Agenda: </b>" +objective[0].dc_mt;
          
  elif objective[0].dc==1 and objective[0].cm==0 and objective[0].mt==1 and objective[0].lv==0:
    objj="";
    objj="""PLAN OF DAY : DCR  |  MEETING 
    DCR Agenda:{0}
    Meeting Agenda:{1}""".format( objective[0].dc_a,objective[0].mt_a);
    #objj="<b>PLAN OF DAY :</b>"+ " DCR  |  MEETING \n\n"+"<b>DCR Agenda: </b>" + objective[0].dc_a +"\n"+"<b>Meeting Agenda: </b>" +objective[0].dc_mt;
        
  elif objective[0].dc==1 and objective[0].cm==0 and objective[0].mt==0 and objective[0].lv==0:
    objj="";
    objj="""PLAN OF DAY : DCR 
    DCR Agenda:{0}""".format( objective[0].dc_a);
    #objj="<b>PLAN OF DAY :</b>"+ " DCR \n\n"+"<b>DCR Agenda: </b>" + objective[0].dc_a;
  
  elif objective[0].dc==0 and objective[0].cm==1 and objective[0].mt==1 and objective[0].lv==0:
    objj="";
    objj="""PLAN OF DAY : CAMP BOOKING  |  MEETING 
    CAMP Agenda:{0}
    Meeting Agenda:{0}""".format( objective[0].cm_a,objective[0].mt_a);
    #objj="<b>PLAN OF DAY :</b>"+ " CAMP BOOKING  |  MEETING \n\n"+"<b>CAMP Agenda: </b>" +objective[0].cm_a +"\n"+"<b>Meeting Agenda: </b>" +objective[0].dc_mt;
        
  elif objective[0].dc==0 and objective[0].cm==1 and objective[0].mt==0 and objective[0].lv==0:
    objj="";
    objj="""PLAN OF DAY : CAMP BOOKING 
    CAMP Agenda:{0}""".format( objective[0].cm_a);
    #objj="<b>PLAN OF DAY :</b>"+ " CAMP BOOKING \n\n"+"<b>CAMP Agenda: </b>" +objective[0].cm_a;
      
  elif objective[0].dc==0 and objective[0].cm==0 and objective[0].mt==1 and objective[0].lv==0:
    objj="";
    objj="""PLAN OF DAY : MEETING 
    Meeting Agenda:{0}""".format( objective[0].mt_a);
    #objj="<b>PLAN OF DAY :</b>"+ " MEETING \n\n"+"<b>Meeting Agenda: </b>" +objective[0].dc_mt;
      
  elif objective[0].dc==0 and objective[0].cm==0 and objective[0].mt==0 and objective[0].lv==1:
    objj="";
    objj="PLAN OF DAY : LEAVE";

  else:
    objj="PLAN NOT CREATED FOR TODAY...";
 else:
  objj='No Objective Today'
 

  
 #frappe.msgprint(_(objective))
 dict = {
   'obj':''
 }
 
 dict['obj'] = objj;
 
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
    #frappe.msgprint(_(formname))
    
    if(formname == 'T_Obj'):
        a='a'
        dataarray = frappe.db.sql(""" select ifnull(t_obj1,'')as frm_date,ifnull(t_obj2,'')as to_date,ifnull(t_obj_time,'')as lock_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)               
    
    elif formname == 'T_DrC':
        a='b'
        dataarray = frappe.db.sql(""" select ifnull(t_drc1,'')as date,ifnull(t_drc2,'')as to_date,ifnull(t_drc_time,'')as lock_time,ifnull(t_drc_s_time,'')as start_time from 1bd3e0294da19198.`tabUser` where name= {0} """.format(employee), as_dict=1)

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
        frappe.msgprint(_(locktime))
        frappe.msgprint(_(dataarray[0].frm_date+' '+dataarray[0].to_date))
        frappe.msgprint(_(today_date+' '+date))
        
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
                        msg='Ok !!! Chemist Call Request Request For Today...'
                    elif a=='d':
                        msg='Ok !!! Campaign Booking Request For Today...'
                    lock_flag = '1'
                
                elif minutes >= 0:
                    if a=='a':
                        msg='Ok !!! Objective Request For Today; Time Is In Range...'
                        
                    elif a=='b':
                        msg='Ok !!! Doctor Call Request For Today; Time Is In Range...'
                        
                    elif a=='c':
                        msg='Ok !!! Chemist Call Request Request For Today; Time Is In Range...'
                        
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
                        msg='Oops !!! Chemist Call Request Request For Today; Time is Over...'
                        
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
                        msg='Ok !!! Chemist Call Request Request For Today...'
                    elif a=='d':
                        msg='Ok !!! Campaign Booking Request For Today...'
                    lock_flag = '1'
                
                elif minutes >= 0:
                    if a=='a':
                        msg='Ok !!! Objective Request For Today; Time Is In Range...'
                        
                    elif a=='b':
                        msg='Ok !!! Doctor Call Request For Today; Time Is In Range...'
                        
                    elif a=='c':
                        msg='Ok !!! Chemist Call Request Request For Today; Time Is In Range...'
                        
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
                        msg='Oops !!! Chemist Call Request Request For Today; Time is Over...'
                        
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
                    msg='Ok !!! Chemist Call Request Request For Today...'
                
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
                    msg='Ok !!! Chemist Call Request Request For Today...'
                
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
       #time_diff = datetime.datetime.strptime(locktime, '%H:%M:%S') - datetime.datetime.strptime(current_time, '%H:%M:%S')
       #minutes = int(time_diff.total_seconds()/60) 
       
       time_diff = datetime.datetime.strptime(starttime, '%H:%M:%S') - datetime.datetime.strptime(current_time, '%H:%M:%S')
       minutes = int(time_diff.total_seconds()/60)
       
       #########
       if str(locktime)=="00:00:00":               
        if a=='b':
         if int(cnt_obj[0].obj_cnt)>0:
          msg='Ok !!! Doctor Call Request For Today...'
          lock_flag = '1'
         else:
          msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
          lock_flag = '0'
        elif a=='c':
         if int(cnt_obj[0].obj_cnt)>0:
          msg='Ok !!! Chemist Call Request Request For Today...'
          lock_flag = '1'
         else:
          msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
          lock_flag = '0'
       #########   
       elif minutes >= 0:
        if a=='b':
         if int(cnt_obj[0].obj_cnt)>0:         
           msg='Ok !!! Doctor Call Request For Today; Time Is In Range...'
           lock_flag = '1'         
         else:
          msg='Ooops !!! Doctor Call Locked Due To Missing Objective...'
          lock_flag = '0'
                        
        elif a=='c':
         if int(cnt_obj[0].obj_cnt)>0:        
           msg='Ok !!! Chemist Call Request Request For Today; Time Is In Range...'
           lock_flag = '1'         
         else:
          msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
          lock_flag = '0'
       #########  
       elif minutes <= 0:
        if a=='b':
         if int(cnt_obj[0].obj_cnt) > 0:
          if int(cnt_dc[0].dc_cnt) > 0:
           msg='Ok !!! Doctor Call Request For Today;'
           lock_flag = '1'
          else:
           msg='Ooops !!! Doctor Call Locked Due To No Calls In Start Time...'
           lock_flag = '0'
         else:
          msg=cnt_obj[0].obj_cnt
          #'Ooops !!! Doctor Call Locked Due To Missing Objective...aa'
          lock_flag = '0'
          
        elif a=='c':
         if int(cnt_obj[0].obj_cnt)>0:
          if int(cnt_ch[0].ch_cnt)>0:
           msg='Ok !!! Chemist Call Request Request For Today;'
           lock_flag = '1'
          else:
           msg='Ooops !!! Chemist Call Locked Due To No Calls In Start Time...'
           lock_flag = '0'
         else:
          msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
          lock_flag = '0'               
        #return lock_flag
       else:
        if a=='b':
         msg='Oops !!! Doctor Call Request For Today; Time is Over...'                        
        elif a=='c':
         msg='Oops !!! Chemist Call Request Request For Today; Time is Over...'                                     
        lock_flag = '0'
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
          msg='Ok !!! Chemist Call Request Request For Today...'
          lock_flag = '1'
         else:
          msg='Ooops !!! Chemist Call Locked Due To Missing Objective...'
          lock_flag = '0'       
       
           
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


