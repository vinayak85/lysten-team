from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _ 
__version__ = '0.0.1'

@frappe.whitelist()
def get_count_of_objectives_of_bottom_emp(employee, designation,date_pass,app_ver):
 #frappe.msgprint(_(tree_user_bottom(employee, designation)))
 #return tree_user_bottom(employee, designation)
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
 for email_emp in tree_user_bottom(employee, designation):
  email_list = email_list + "'"+email_emp.name + "',"
  count_of_emp=count_of_emp+1
  if(email_emp.designation =='TBM'):
   email_list_only_TBM=email_list_only_TBM + "'"+email_emp.name + "',"
   count_of_emp_tbm=count_of_emp_tbm+1
  
 email_list=email_list[:-1]
 email_list_only_TBM=email_list_only_TBM[:-1]
 
 if(designation == 'TBM'):
  email_list=employee
  email_list_only_TBM=employee
 #return str(len(email_list)) + "ssss " + str(len(email_list_only_TBM))
 #frappe.msgprint(_(email_list_only_TBM))
 
 if(len(email_list)>0):
  count_of_emp_objective= frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.tabObjective
where 1bd3e0294da19198.tabObjective.user in ({0}) and
1bd3e0294da19198.tabObjective.select_date={1}""".format(email_list,today_date), as_dict=1)
 #return (today_date, str(count_of_emp) as cnt_emp,count_of_emp_objective)
 
 
  count_of_emp_dcr= frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.`tabDoctor Calls` where 
1bd3e0294da19198.`tabDoctor Calls`.dr_call_by_user_id in ({0}) and
1bd3e0294da19198.`tabDoctor Calls`.date={1}""".format(email_list,today_date), as_dict=1)
 
  count_of_emp_dcr_only_tbm= frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.`tabDoctor Calls` where 
1bd3e0294da19198.`tabDoctor Calls`.dr_call_by_user_id in ({0}) and
1bd3e0294da19198.`tabDoctor Calls`.date={1}""".format(email_list_only_TBM,today_date), as_dict=1)
 
  count_of_emp_chem= frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.`tabChemist Call` where 
1bd3e0294da19198.`tabChemist Call`.call_by_user_id in ({0}) and
1bd3e0294da19198.`tabChemist Call`.date={1}""".format(email_list,today_date), as_dict=1) 
 
  count_of_emp_camp= frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.`tabcampaign_booking` where 
1bd3e0294da19198.`tabcampaign_booking`.call_by_user_id in ({0}) and
1bd3e0294da19198.`tabcampaign_booking`.date={1}""".format(email_list,today_date), as_dict=1)
 
  objective= frappe.db.sql(""" SELECT objective as obj FROM 1bd3e0294da19198.`tabObjective` where 
1bd3e0294da19198.`tabObjective`.user = {0} and
1bd3e0294da19198.`tabObjective`.`select_date`={1} """.format(employee,today_date), as_dict=1)
 ## TBM calculation
 if(len(email_list_only_TBM)>0):
  count_of_emp_only_TBM= frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.`tabDoctor Calls` where 
1bd3e0294da19198.`tabDoctor Calls`.dr_call_by_user_id in ({0}) and
1bd3e0294da19198.`tabDoctor Calls`.date={1}""".format(email_list_only_TBM,today_date), as_dict=1)
  
  count_of_emp_chem_only_tbm= frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.`tabChemist Call` where 
1bd3e0294da19198.`tabChemist Call`.call_by_user_id in ({0}) and
1bd3e0294da19198.`tabChemist Call`.date={1}""".format(email_list_only_TBM,today_date), as_dict=1)
  
  
 app_ver_count =frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.`tabAppVersions` where 
1bd3e0294da19198.`tabAppVersions`.versionCode = {0} and
1bd3e0294da19198.`tabAppVersions`.supported=true""".format(app_ver), as_dict=1)
  
 

 if len(objective) > 0:
  objj=objective[0].obj
 else:
  objj='No Objective Today'
 
 expected_dcr_call_tbm=0
 actual_dcr_call_tbm=0
 percent_tbm_dcr_call=0
 expected_chem_call_tbm=0
 actual_chem_call_tbm=0
 percent_tbm_chem_call=0
  
 if (count_of_emp_tbm>0):
  expected_dcr_call_tbm=count_of_emp_tbm*10
  actual_dcr_call_tbm=count_of_emp_dcr_only_tbm[0].cnt_ob
  #percent_tbm_dcr_call=(actual_dcr_call_tbm/expected_dcr_call_tbm)*100.0
  percent_tbm_dcr_call=100.0 * actual_dcr_call_tbm / expected_dcr_call_tbm
  expected_chem_call_tbm=count_of_emp_tbm*10
  actual_chem_call_tbm=count_of_emp_chem_only_tbm[0].cnt_ob
  percent_tbm_chem_call=100.0 * actual_chem_call_tbm / expected_chem_call_tbm
  
  
 #frappe.msgprint(_(objective))
 dict = {'today_date': '',
         'cnt_emp': '',
         'count_of_emp_only_TBM':'',
         'cnt_emp_objective': '',
         'cnt_of_emp_dcr': '',
         'cnt_of_emp_chem': '',
         'cnt_of_emp_camp':'',
         'obj':'',
         'expected_dcr_call_tbm':0,
         'actual_dcr_call_tbm':0,
         'percent_tbm_dcr_call':0,
         'expected_chem_call_tbm':0,
         'actual_chem_call_tbm':0,
         'percent_tbm_chem_call':0,
         'app_ver_count':0,
         'lock':0
         }
 
 dict['today_date'] = today_date;
 dict['cnt_emp'] = count_of_emp;
 dict['cnt_emp_objective'] = count_of_emp_objective[0].cnt_ob;
 dict['cnt_of_emp_dcr'] = count_of_emp_dcr[0].cnt_ob;
 dict['cnt_of_emp_chem'] = count_of_emp_chem[0].cnt_ob;
 dict['cnt_of_emp_camp'] = count_of_emp_camp[0].cnt_ob;
 dict['count_of_emp_only_TBM']=count_of_emp_tbm;
 dict['obj'] = objj;
 dict['expected_dcr_call_tbm']=expected_dcr_call_tbm;
 dict['actual_dcr_call_tbm']=actual_dcr_call_tbm;
 dict['percent_tbm_dcr_call']=frappe.utils.data.flt (percent_tbm_dcr_call, precision=2);
 dict['expected_chem_call_tbm']=expected_chem_call_tbm;
 dict['actual_chem_call_tbm']=actual_chem_call_tbm;
 dict['percent_tbm_chem_call']=frappe.utils.data.flt (percent_tbm_chem_call, precision=2);
 dict['app_ver_count']=app_ver_count[0].cnt_ob;
 dict['lock']=0;
 
 
 return dict
#return email_list
# qry='SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.tabObjective where 1bd3e0294da19198.tabObjective.select_date=' + ''' +  str(today_date) + ''' + ' and 1bd3e0294da19198.tabObjective.user in (' + str(email_list) + ')' 
#where 1bd3e0294da19198.tabObjective.select_date={0} and
# this method is used for android heirachy user
#it will featch all top and down users of selected user
def tree_user_bottom(employee, designation): 
 if designation == 'TBM':
   return frappe.db.sql(""" select name,designation from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`abm`={0}  or `tabUser`.`name` in(
 (select rbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select zbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select crm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select sm from 1bd3e0294da19198.`tabUser` where `name`={0})
 ,(select nbm from 1bd3e0294da19198.`tabUser` where `name`={0})
 )  """.format(employee), as_dict=1)
  
 elif designation == "ABM":
  return frappe.db.sql(""" select name,designation from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`abm`={0} """.format(employee), as_dict=1)
 
 elif designation == "RBM":
  return frappe.db.sql(""" select name,designation from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`rbm`={0} """.format(employee), as_dict=1)
 
 elif designation == "ZBM":
  return frappe.db.sql(""" select name,designation from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`zbm`={0} """.format(employee), as_dict=1)
 
 elif designation == "SM":
  return frappe.db.sql(""" select name,designation from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`sm`={0} """.format(employee), as_dict=1)
 
 elif designation == "NBM":
  return frappe.db.sql(""" select name,designation from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`nbm`={0} """.format(employee), as_dict=1)
 
 elif designation == "CRM":
  return frappe.db.sql(""" select name,designation from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`crm`={0}
 """.format(employee), as_dict=1)
 
 elif (designation == "HR Manager" or designation == "Head of Marketing and Sales" or designation == "Admin"):
  return frappe.db.sql(""" select name,designation from 1bd3e0294da19198.`tabUser` 
 where `tabUser`.`enabled`=1 and `tabUser`.`designation` in('TBM','ABM','RBM','ZBM','SM','NBM','CRM')
 """.format(employee), as_dict=1)
 
 else:
   return ""
