from __future__ import unicode_literals
import frappe
import datetime
from datetime import datetime
from pytz import timezone
from frappe import msgprint, _
__version__ = '0.0.1'

@frappe.whitelist()
def form16_package(employee):    
    package_cnt='';
    package='';
    
    if(len(employee)>0):
        employee="'"+employee+"'";
        package_cnt= frappe.db.sql("""select  count(distinct base)as cnt from `tabSalary Structure Employee` where employee={0} 
        """.format(employee), as_dict=1)
        
    if(package_cnt[0].cnt > 1):
        package= frappe.db.sql("""select GROUP_CONCAT(distinct CAST(base AS UNSIGNED)) as pckge,GROUP_CONCAT(DATE_FORMAT(`from_date`,'%M %Y'))as paid_month
        from `tabSalary Structure Employee` where employee={0} """.format(employee), as_dict=1) 
    else:
        package= frappe.db.sql("""select CAST(base AS UNSIGNED) as pckge,GROUP_CONCAT(DATE_FORMAT(`from_date`,'%M %Y'))as paid_month
        from `tabSalary Structure Employee` where employee={0} """.format(employee), as_dict=1)        
        
     
    '''Convenience Allowance Calucalte Query: Only Sum Of Paid Allowance in Salary::::
    
	select 
		sum(sd.amount)as convenience_allowance  
	from 
		`tabSalary Detail` sd 
	left outer join 
		`tabSalary Slip` ss 
	on
		sd.parent=ss.name 
	where 
		sd.salary_component='Convenience Allowance' and 
        ss.employee='EMP/0015' and 
        ss.start_date between '2017-03-01' and '2017-11-01';
        
        '''
    
    
    dict = {'package': '',
            'paid_month': '',
           }
    
    dict['package']=package[0].pckge;
    dict['paid_month']=package[0].paid_month;
    return dict

@frappe.whitelist()
def form16_allowance(employee,from_date,to_date):    
    allowance='';
    
    if(len(employee)>0):
        #employee="'"+employee+"'";
        allowance= frappe.db.sql("""select sum(sd.amount)as convenience_allowance from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Convenience Allowance' and ss.employee={0} and 
	ss.start_date between {1} and {2}; 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)
        
    
    '''Convenience Allowance Calucalte Query: Only Sum Of Paid Allowance in Salary::::
    
	select sum(sd.amount)as convenience_allowance from `tabSalary Detail` sd left outer join `tabSalary Slip` ss on	sd.parent=ss.name where sd.salary_component='Convenience Allowance' and ss.employee='EMP/0015' and ss.start_date between '2017-03-01' and '2017-11-01';
        
        '''
    
    
    dict = {'con_allow': '',
            'prof_tax': '',
           }
    
    dict['con_allow']=allowance[0].convenience_allowance;
    dict['prof_tax']=0;
    return dict
