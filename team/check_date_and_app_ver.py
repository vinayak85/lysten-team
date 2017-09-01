from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _

__version__ = '0.0.1'


@frappe.whitelist()
def get_date_and_app_support(date_pass, app_ver):
    if ((len(date_pass)) == 0):
        today_date = frappe.utils.data.get_datetime().strftime('%Y/%m/%d')
    else:
        today_date = date_pass
    app_ver_count = frappe.db.sql("""SELECT count(*) as cnt_ob FROM 1bd3e0294da19198.`tabAppVersions` where 
    1bd3e0294da19198.`tabAppVersions`.versionCode = {0} and
    1bd3e0294da19198.`tabAppVersions`.supported=true""".format(app_ver), as_dict=1)

    dict = {'today_date': '',
            'app_ver_count': 0
            }
    dict['today_date'] = today_date;
    dict['app_ver_count'] = app_ver_count[0].cnt_ob;
    return dict
