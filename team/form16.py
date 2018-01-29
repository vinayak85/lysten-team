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
    
    dict = {'package': '',
            'paid_month': '',
           }
    
    dict['package']=package[0].pckge;
    dict['paid_month']=package[0].paid_month;
    return dict

@frappe.whitelist()
def form16_allowance(employee,from_date,to_date):
    paid_month_count='';
    allowance='';
    perform_allowance='';	
    prof_tax='';
    prov_fund='';
    gross_amt_wot_exp='';
	
    if(len(employee)>0):
        #employee="'"+employee+"'";
	
        paid_month_count= frappe.db.sql("""select  ifnull(count(name),0)as paid_month_count from `tabSalary Slip` where
	employee={0} and start_date between {1} and {2} and end_date between {1} and {2} ;
	""".format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)	
	
        allowance= frappe.db.sql("""select ifnull(sum(sd.amount),0)as convenience_allowance from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Conveyance Allowance' and ss.employee={0} and 
	ss.start_date between {1} and {2}; 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)
	
        perform_allowance= frappe.db.sql("""select ifnull(sum(sd.amount),0)as perform_allow from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Performance Allowance' and ss.employee={0} and 
	ss.start_date between {1} and {2}; 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)	
	
	prof_tax= frappe.db.sql("""select ifnull(sum(sd.amount),0)as professional_tax from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Professional Tax' and ss.employee={0} and 
	ss.start_date between {1} and {2}; 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)
	
	prov_fund= frappe.db.sql("""select ifnull(sum(sd.amount),0)as provident_fund from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Provident Fund' and ss.employee={0} and 
	ss.start_date between {1} and {2}; 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)
	
	gross_amt_wot_exp= frappe.db.sql("""select (ifnull(sum(ss.gross_pay),0)- ifnull(sum(sd.amount),0))as gross_wot_exp 
	from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Expenses' and ss.employee={0} and 
	ss.start_date between {1} and {2}; 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)	
	
     
    dict = {'paid_month_count':'',
	    'gross_amt':'',
	    'con_allow': '',
	    'per_allow':'',	    
            'prof_tax': '',
	    'prov_fund': ''
           }
    
    dict['paid_month_count']=paid_month_count[0].paid_month_count;
    dict['gross_amt']=gross_amt_wot_exp[0].gross_wot_exp;	
    dict['con_allow']=allowance[0].convenience_allowance;
    dict['per_allow']=perform_allowance[0].perform_allow;	
    dict['prof_tax']=prof_tax[0].professional_tax;
    dict['prov_fund']=prov_fund[0].provident_fund;
    return dict

@frappe.whitelist()
def form16_check_exist(employee,assement_year,from_date,to_date):    
    flag='';
	
    if(len(employee)>0 and len(assement_year)>0 and len(from_date)>0 and len(to_date)>0):
        #employee="'"+employee+"'";
        flag= frappe.db.sql("""select count(*)as cnt from `tabForm 16` 
	where employee={0} and assessment_year={1} and period_from_date={2} and period_to_date={3};
	""".format("'"+employee+"'","'"+assement_year+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)		
	
     
    dict = {'flag': ''
           }
    
    dict['flag']=flag[0].cnt;
    return dict
