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
	employee={0} and start_date between {1} and {2} and end_date between {1} and {2} and status IN ('Draft', 'Submitted');
	""".format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)	
	
        allowance= frappe.db.sql("""select ifnull(sum(sd.amount),0)as convenience_allowance from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Conveyance Allowance' and ss.employee={0} and 
	ss.start_date between {1} and {2} and ss.status IN ('Draft', 'Submitted'); 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)
	
        perform_allowance= frappe.db.sql("""select ifnull(sum(sd.amount),0)as perform_allow from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Performance Allowance' and ss.employee={0} and 
	ss.start_date between {1} and {2} and ss.status IN ('Draft', 'Submitted'); 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)	
	
	prof_tax= frappe.db.sql("""select ifnull(sum(sd.amount),0)as professional_tax from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Professional Tax' and ss.employee={0} and 
	ss.start_date between {1} and {2} and ss.status IN ('Draft', 'Submitted'); 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)
	
	prov_fund= frappe.db.sql("""select ifnull(sum(sd.amount),0)as provident_fund from `tabSalary Detail` sd 
	left outer join `tabSalary Slip` ss on	sd.parent=ss.name 
	where sd.salary_component='Provident Fund' and ss.employee={0} and 
	ss.start_date between {1} and {2} and ss.status IN ('Draft', 'Submitted'); 
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)
	
	gross_amt_wot_exp= frappe.db.sql(""" SELECT Months,
EMP_NAME as "EmployeeName",
EMP as "EmployeeCode",
GROSS  as "GROSSWithExp",
SUM(BASIC+DA+CA+EA+HRA+SPA+OTHER+Per_Allow+wash_allow+med+E_BA+e_lta) as "GrossWotExp",
SUM(BASIC+DA+CA+EA+HRA+SPA+OTHER+wash_allow+med+E_BA+e_lta) as "GrossWotExpPerform" 

FROM
(

SELECT Months,EMP_NAME,EMP,SUM(GROSS) AS GROSS,SUM(DED) AS DED,SUM(NET) AS NET,
SUM(BASIC) AS BASIC,SUM(DA) AS DA,SUM(CA) AS CA,SUM(EA) AS EA,SUM(HRA) AS HRA,SUM(SPA) AS SPA,
SUM(wash_allow)AS wash_allow,SUM(Per_Allow) AS Per_Allow,sum(OTHER) AS OTHER,SUM(D_PF) AS D_PF,SUM(D_PT) AS D_PT, 

SUM(med) AS med,
SUM(E_BA) AS E_BA,
SUM(e_lta) AS e_lta
FROM

(
SELECT COUNT(employee_name) AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,
SUM(SS.gross_pay) AS GROSS,SUM(SS.total_deduction) AS DED,SUM(SS.rounded_total) AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
 WHERE SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
SUM(SD.AMOUNT) AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_B'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
SUM(SD.AMOUNT) AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_DA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
SUM(SD.AMOUNT) AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_CA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 CA,
SUM(SD.AMOUNT) AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_EA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
SUM(SD.AMOUNT) AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_HRA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
SUM(SD.AMOUNT) AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_SA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
SUM(SD.AMOUNT) AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='wash_allow'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
SUM(SD.AMOUNT) AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='Per_Allow'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
SUM(SD.AMOUNT) AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_OA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
SUM(SD.AMOUNT) AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='D_PF'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
SUM(SD.AMOUNT) AS D_PT,
0 AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='D_PT'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
SUM(SD.AMOUNT) AS med,
0 AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='med'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
SUM(SD.AMOUNT) AS E_BA,
0 AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_BA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT,
0 AS med,
0 AS E_BA,
SUM(SD.AMOUNT) AS e_lta
 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='e_lta'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

) AS TEMP
GROUP BY  EMP_NAME,EMP

 ) AS TAXBLE where EMP={0} GROUP BY  EMP_NAME,EMP
	""".format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)
		
	'''
	gross_amt_wot_exp= frappe.db.sql("""SELECT Months,EMP_NAME as "EmployeeName",EMP as "EmployeeCode",
GROSS  as "GROSSWithExp",
SUM(BASIC+DA+CA+EA+HRA+SPA+OTHER+Per_Allow+wash_allow) as "GrossWotExp",
SUM(BASIC+DA+CA+EA+HRA+SPA+OTHER+wash_allow) as "GrossWotExpPerform" FROM
(SELECT Months,EMP_NAME,EMP,SUM(GROSS) AS GROSS,SUM(DED) AS DED,SUM(NET) AS NET,
SUM(BASIC) AS BASIC,SUM(DA) AS DA,SUM(CA) AS CA,SUM(EA) AS EA,SUM(HRA) AS HRA,SUM(SPA) AS SPA,
SUM(wash_allow)AS wash_allow,SUM(Per_Allow) AS Per_Allow,sum(OTHER) AS OTHER,SUM(D_PF) AS D_PF,SUM(D_PT) AS D_PT FROM(

SELECT COUNT(employee_name) AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,
SUM(SS.gross_pay) AS GROSS,SUM(SS.total_deduction) AS DED,SUM(SS.rounded_total) AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
 WHERE SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL

SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
SUM(SD.AMOUNT) AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_B'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL

SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
SUM(SD.AMOUNT) AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_DA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
SUM(SD.AMOUNT) AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_CA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 CA,
SUM(SD.AMOUNT) AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_EA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
SUM(SD.AMOUNT) AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_HRA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
SUM(SD.AMOUNT) AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_SA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
SUM(SD.AMOUNT) AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='wash_allow'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
SUM(SD.AMOUNT) AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='Per_Allow'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
SUM(SD.AMOUNT) AS OTHER,
0 AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='E_OA'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
SUM(SD.AMOUNT) AS D_PF,
0 AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='D_PF'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name

UNION  ALL
SELECT 0 AS Months,SS.employee_name AS EMP_NAME,SS.Employee AS EMP,0 AS GROSS,0 AS DED,0 AS NET,
0 AS BASIC,
0 AS DA,
0 AS CA,
0 AS EA,
0 AS HRA,
0 AS SPA,
0 AS wash_allow,
0 AS Per_Allow,
0 AS OTHER,
0 AS D_PF,
SUM(SD.AMOUNT) AS D_PT

 FROM 1bd3e0294da19198.`tabSalary Slip` AS SS
  LEFT   JOIN 1bd3e0294da19198.`tabSalary Detail` AS SD ON SD.PARENT = SS.NAME
  WHERE SD.ABBR='D_PT'
  AND SS.start_date >={1} AND SS.start_date <={2}  and status IN ('Draft', 'Submitted')
GROUP BY  SS.Employee,SS.employee_name
) AS TEMP
GROUP BY  EMP_NAME,EMP ) AS TAXBLE where EMP={0} GROUP BY  EMP_NAME,EMP
        """.format("'"+employee+"'","'"+from_date+"'","'"+to_date+"'"), as_dict=1)	
'''	
     
    dict = {'paid_month_count':'',
	    'gross_amt':'',
	    'con_allow': '',
	    'per_allow':'',	    
            'prof_tax': '',
	    'prov_fund': ''
           }
    
    #dict['paid_month_count']=paid_month_count[0].paid_month_count;
    #dict['gross_amt']=gross_amt_wot_exp[0].GrossWotExp;	
    #dict['con_allow']=allowance[0].convenience_allowance;
    #dict['per_allow']=perform_allowance[0].perform_allow;	
    #dict['prof_tax']=prof_tax[0].professional_tax;
    #dict['prov_fund']=prov_fund[0].provident_fund;

    if len(paid_month_count) > 0:
	dict['paid_month_count']=paid_month_count[0].paid_month_count;
    else:
	dict['paid_month_count']=0;

    if len(gross_amt_wot_exp) > 0:
	dict['gross_amt']=gross_amt_wot_exp[0].GrossWotExp;
    else:
	dict['gross_amt']=0;
	
    if len(allowance) > 0:
	dict['con_allow']=allowance[0].convenience_allowance;
    else:
	dict['con_allow']=0;
	
    if len(perform_allowance) > 0:
	dict['per_allow']=perform_allowance[0].perform_allow;
    else:
	dict['per_allow']=0;	
	
    if len(prof_tax) > 0:
	dict['prof_tax']=prof_tax[0].professional_tax;
    else:
	dict['prof_tax']=0;

    if len(prov_fund) > 0:
	dict['prov_fund']=prov_fund[0].provident_fund;
    else:
	dict['prov_fund']=0;


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
