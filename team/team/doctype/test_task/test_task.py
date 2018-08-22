# -*- coding: utf-8 -*-
# Copyright (c) 2018, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import datetime
from datetime import datetime
from pytz import timezone
import frappe
from frappe.model.document import Document
from frappe import msgprint, _

import urllib
import re
import schedule
import time

class test_task(Document):
	pass

@frappe.whitelist()
def btn_2_job():
	schedule.clear()
	
@frappe.whitelist()
def test_start1():
	'''INSERT INTO 1bd3e0294da19198.tabtest_task (note)
   VALUES
   ('');
   
   tabtest_task_child
   note
   date
   time
   '''
	'''td_entry = frappe.new_doc("test_task")
	#td_entry.name = 'test_task/' + '000001'
	td_entry.note = 'aaaaa'
	#td_entry.salary_slip = ss.name
	#td_entry.docstatus = 1
	td_entry.save()'''
	
	today_date = frappe.utils.data.get_datetime().strftime('%Y-%m-%d')
	current_time = local_time()
	
	td_entry = frappe.new_doc("test_task_child")
	#td_entry.name = 'test_task/' + '000001'
	td_entry.note = 'aaaaaaaa'
	td_entry.date = str(today_date)
	td_entry.time = str(current_time)
	td_entry.save()
	
	#aop = frappe.db.sql(""" INSERT INTO 1bd3e0294da19198.tabtest_task (note) VALUES ('aaaaa');""");
	frappe.msgprint(_("arjun "));


######################################

#import datetime import datetime
@frappe.whitelist()
def btn_1_job():
	#job()
	schedule.every(1).seconds.do(job)
	schedule.clear()
	'''while 1:
		schedule.run_pending()
		time.sleep(5)'''

def job():
	frappe.msgprint(_("arjun "));


	
#################
	
def local_time(zone='Asia/Kolkata'):
    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%T')
