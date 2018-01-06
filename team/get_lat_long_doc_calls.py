
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
	c = frappe.db.sql("""SELECT name,latitude,longitude,SUBSTRING(creation, 12, 5) as time_call,doctor_name,patch_id,jwf_with,jwf_with2 
  FROM 1bd3e0294da19198.`tabDoctor Calls`where date={0} and dr_call_by_user_id={1} """.
  format("'"+date+"'","'"+emp+"'"), as_dict=1);
	
	return c;
