
from __future__ import unicode_literals
import frappe
import subprocess
from frappe import msgprint, _ 
import frappe.utils
from frappe.model.document import Document
from frappe.utils import cstr, flt, getdate, cint
from frappe.model.naming import make_autoname
from frappe import _
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def get_lat_long_details(emp, date):
	#doc_name=year + "-" + month + "-" + stockist;
	c = frappe.db.sql("""
	SELECT name,latitude,longitude, time_call,concat("Obj: " ,subject) as "subject",patch_id,jwf_with,jwf_with2 
  FROM(  
SELECT name,latitude,longitude,SUBSTRING(creation, 12, 5) as time_call,
(SELECT IF(objective != '' && doctor_flag=0 && meeting_flag=0 && camp_flag=0 && leave_flag=0,
CONCAT('PLAN OF DAY : ',objective,' '),
IF(doctor_flag=1 && camp_flag=1 && meeting_flag=1 && leave_flag=0,
Concat('PLAN OF DAY : DCR  |  CAMP BOOKING  |  MEETING','\n',concat('Patch:',select_patch),'DCR Agenda:',call_agenda,'\n',concat('Patch',camp_patch),'CAMP Agenda:',camp_agenda,'\n',concat('Meeting with: ',meeting_with),'Meeting Agenda:',meeting_agenda),
IF(doctor_flag=1 && camp_flag=1 && meeting_flag=0 && leave_flag=0,
Concat('PLAN OF DAY : DCR  |  CAMP BOOKING','\n',concat('Patch:',select_patch),'DCR Agenda:',call_agenda,'\n',concat('Patch',camp_patch),'CAMP Agenda:',camp_agenda),
IF(doctor_flag=1 && camp_flag=0 && meeting_flag=1 && leave_flag=0,
Concat('PLAN OF DAY : DCR  |  MEETING','\n',concat('Patch:',select_patch),'DCR Agenda:',call_agenda,'\n',concat('Meeting with: ',meeting_with),'Meeting Agenda:',meeting_agenda),
IF(doctor_flag=1 && camp_flag=0 && meeting_flag=0 && leave_flag=0,
Concat('PLAN OF DAY : DCR ','\n',concat('Patch:',select_patch),'DCR Agenda:',call_agenda),
IF(doctor_flag=0 && camp_flag=1 && meeting_flag=1 && leave_flag=0,
Concat('PLAN OF DAY : CAMP BOOKING  |  MEETING','\n',concat('Patch',camp_patch),'CAMP Agenda:',camp_agenda,'\n',concat('Meeting with: ',meeting_with),'Meeting Agenda:',meeting_agenda),
IF(doctor_flag=0 && camp_flag=1 && meeting_flag=0 && leave_flag=0,
Concat('PLAN OF DAY : CAMP BOOKING','\n',concat('Patch',camp_patch),'CAMP Agenda:',camp_agenda),
IF(doctor_flag=0 && camp_flag=0 && meeting_flag=1 && leave_flag=0,
Concat('PLAN OF DAY : MEETING','\n',concat('Meeting with: ',meeting_with),'Meeting Agenda:',meeting_agenda),
IF(doctor_flag=0 && camp_flag=0 && meeting_flag=0 && leave_flag=1,if(leave_type1=1,concat('PLAN OF DAY : CAUSUAL LEAVE ' ,reason)
,if(leave_type2=1,concat('PLAN OF DAY : PRIVILEGE LEAVE ',reason),
if(leave_type3=1,concat('PLAN OF DAY : SICK LEAVE ',reason),'PLAN OF DAY : Leave'))),'PLAN NOT CREATED FOR THAT DAY...'))))))))) as calling 
from 1bd3e0294da19198.`tabObjective` JOIN 1bd3e0294da19198.`tabUser`
 ON (1bd3e0294da19198.`tabUser`.`name` = 1bd3e0294da19198.`tabObjective`.user) 
where select_date = {0} and user={1}) as subject
,"" as patch_id,join_name1 as "jwf_with",join_name2  as "jwf_with2"
  FROM 1bd3e0294da19198.`tabObjective`where select_date={0} and user ={1}
  
  union sELECT name,latitude,longitude,SUBSTRING(creation, 12, 5) as time_call,concat("DR call: " ,doctor_name) as subject,patch_id,jwf_with,jwf_with2 
  FROM 1bd3e0294da19198.`tabDoctor Calls`where date={0} and dr_call_by_user_id ={1}
  union
  sELECT name,latitude,longitude,SUBSTRING(creation, 12, 5) as time_call,concat("CHEM call: " ,chemist_name) as subject,patch_id,jwf_with,jwf_with2 
  FROM 1bd3e0294da19198.`tabChemist Call`where date={0} and user_id ={1}) as temp order by temp.time_call
""".format("'"+date+"'","'"+emp+"'"), as_dict=1);
	
	return c;
