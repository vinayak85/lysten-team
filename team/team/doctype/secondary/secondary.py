# -*- coding: utf-8 -*-
# Copyright (c) 2017, Vinayak Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _ 
import frappe.utils
from frappe.model.document import Document


@frappe.whitelist()
def make_stock_entry(year, month,stockist,name):
	#frappe.msgprint(_(aa+"hello"+bb));
	#frappe.msgprint(_(name.year))
	Secondary.test();
	  


class Secondary(Document):
    def autoname(self):
        self.name = self.year + "-" + self.month + "-" + self.stockist;
	

    def on_update(self):
        self.name = self.year + "-" + self.month + "-" + self.stockist;
	if self.name != new_name and not self.is_new():
		frappe.rename_doc(self.doctype,self.name,new_name)
        
    def validate(self):
	pass;
        #frappe.msgprint(_("validate"));

    def test():
	pass;
	#frappe.msgprint(_("hiii"));
	
  	 
	
    '''    
    def before_save():
        frappe.msgprint(_("before_save"));
        
   
        
    def before_submit(self): 
        frappe.msgprint(_("before_submit"));
        
    def before_update_after_submit(self):
        frappe.msgprint(_("before_update_after_submit"));
   
    def on_change(self):
        frappe.msgprint(_("on_change")); '''

