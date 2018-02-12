from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe import msgprint, _

__version__ = '0.0.1'


@frappe.whitelist()
def get_date_and_app_support(stockist_name,products,months):
    
    stockist_name=stockist_name;
    
    #pp=product_return_names(products);
    #months=['2017-July','2017-Aug','2017-Sept','2017-Oct','2017-Nov','2017-Dec','2018-jan'];
    frappe.msgprint(_("pp: "+months));
    datasets = []; 
    #for f in months:
    for idx, f in enumerate(months):
        #frappe.msgprint(_("mm: "+"'-"+f+"-'","'-"+stockist_name+"'"));
        frappe.msgprint(_("mm: "+"'-"+f+"-'","'-"+stockist_name+"'"));
        op = frappe.db.sql("""select sum(opn_qty*item_rate) as "Opening",sum(rec_qty*item_rate) as "Primary/Received",
    sum(close_qty*item_rate) as "Closing",sum(value_credit_note_qty) as "Credit note"
    ,sum(sale_qty*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like concat({0},{1}) and  item_code2 IN ({2})""".format("'-"+f+"-'","'-"+stockist_name+"'",products), as_dict=0)
        datasets.append({'title': f,'values': op[0]})
        pass;
    
    ''' previos code   
        
    july = frappe.db.sql("""select sum(opn_qty*item_rate) as "Opening",sum(rec_qty*item_rate) as "Primary/Received",
    sum(close_qty*item_rate) as "Closing",sum(value_credit_note_qty) as "Credit note"
    ,sum(sale_qty*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-July-CHIRAYU PHARMA'""", as_dict=0)
    
    aug = frappe.db.sql("""select sum(opn_qty*item_rate) as "Opening",sum(rec_qty*item_rate) as "Primary/Received",
    sum(close_qty*item_rate) as "Closing",sum(value_credit_note_qty) as "Credit note",
    sum(sale_qty*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Aug-CHIRAYU PHARMA'""", as_dict=0)
    
    sept = frappe.db.sql("""select sum(opn_qty*item_rate) as "Opening",sum(rec_qty*item_rate) as "Primary/Received",
    sum(close_qty*item_rate) as "Closing",sum(value_credit_note_qty) as "Credit note",
    sum(sale_qty*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Sept-CHIRAYU PHARMA'""", as_dict=0)
    
    oct = frappe.db.sql("""select sum(opn_qty*item_rate) as "Opening",sum(rec_qty*item_rate) as "Primary/Received",
    sum(close_qty*item_rate) as "Closing",sum(value_credit_note_qty) as "Credit note",
    sum(sale_qty*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Oct-CHIRAYU PHARMA'""", as_dict=0)
    
    nov = frappe.db.sql("""select sum(opn_qty*item_rate) as "Opening",sum(rec_qty*item_rate) as "Primary/Received",
    sum(close_qty*item_rate) as "Closing",sum(value_credit_note_qty) as "Credit note",
    sum(sale_qty*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Nov-CHIRAYU PHARMA'""", as_dict=0)
    
    dec = frappe.db.sql("""select sum(opn_qty*item_rate) as "Opening",sum(rec_qty*item_rate) as "Primary/Received",
    sum(close_qty*item_rate) as "Closing",sum(value_credit_note_qty) as "Credit note",
    sum(sale_qty*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2017-Dec-CHIRAYU PHARMA'""", as_dict=0)
    
    jan = frappe.db.sql("""select sum(opn_qty*item_rate) as "Opening",sum(rec_qty*item_rate) as "Primary/Received",
    sum(close_qty*item_rate) as "Closing",sum(value_credit_note_qty) as "Credit note",
    sum(sale_qty*item_rate) as "Secondary/Sale" from `tabsec_item_qty` where parent  
    like '2018-Jan-CHIRAYU PHARMA'""", as_dict=0)
    
   
    
    datasets = [];
    datasets.append({'title': 'July','values': july[0]})
    datasets.append({'title': 'Aug', 'values': aug[0]})
    datasets.append({'title': 'Sept','values': sept[0]})
    datasets.append({'title': 'Oct', 'values': oct[0]})
    datasets.append({'title': 'Nov', 'values': nov[0]})
    datasets.append({'title': 'Dec', 'values': dec[0]})
    datasets.append({'title': 'Jan', 'values': jan[0]})
    
    #dict = {'datasets': []}
  
    #dict['datasets'] = datasets;
    #return dict
    '''
    return datasets;
@frappe.whitelist()
def getmonthly():
    opening=[];
    primary=[];
    closing=[];
    credit=[];
    saling=[];
   
    pets=['2017-July','2017-Aug','2017-Sept','2017-Oct','2017-Nov','2017-Dec','2018-jan']
    for f in pets:
        opn=0;prim=0;clos=0;cred=0;sale=0;
        opn=frappe.db.sql("""select sum(opn_qty*item_rate) as opn from `tabsec_item_qty` where parent  
    like concat({0},'-CHIRAYU PHARMA')""".format("'"+f+"'"), as_dict=1);
        opening.append(opn[0].opn);
        
        prim=frappe.db.sql("""select sum(rec_qty*item_rate) as prim from `tabsec_item_qty` where parent  
    like concat({0},'-CHIRAYU PHARMA')""".format("'"+f+"'"), as_dict=1);
        primary.append(prim[0].prim);
            
        clos=frappe.db.sql("""select sum(close_qty*item_rate) as clos from `tabsec_item_qty` where parent  
    like concat({0},'-CHIRAYU PHARMA')""".format("'"+f+"'"), as_dict=1);
        closing.append(clos[0].clos);
        
        cred=frappe.db.sql("""select sum(value_credit_note_qty) as cred from `tabsec_item_qty` where parent  
    like concat({0},'-CHIRAYU PHARMA')""".format("'"+f+"'"), as_dict=1);
        credit.append(cred[0].cred);
        
        sale=frappe.db.sql("""select sum(sale_qty*item_rate) as sale from `tabsec_item_qty` where parent  
    like concat({0},'-CHIRAYU PHARMA')""".format("'"+f+"'"), as_dict=1);
        saling.append(sale[0].sale);
        pass;
    datasets = [];
    datasets.append({'title': 'opening','values': opening})
    datasets.append({'title': 'primary', 'values': primary})
    datasets.append({'title': 'closing','values': closing})
    datasets.append({'title': 'credit', 'values': credit})
    datasets.append({'title': 'sale', 'values': saling})
 
    
    #dict = {'datasets': []}
  
    #dict['datasets'] = datasets;
    #return dict
    return datasets;
def product_return_names(codes):
    names=[];
    for f in codes:
        frappe.msgprint(_(f));
        names.append(code_to_names(f));
        pass;
    return names;
def code_to_names(code):
    if (code == '1'):
        return 'ACTIRAB - D CAP'
    elif (code == '2'):
        return 'ACTIRAB - L CAP'
    elif (code == '3'):
        return 'ACTIRAB -DV Cap'
    elif (code == '4'):
        return 'ACTIRAB TAB'
    elif (code == 5):
        return 'EMPOWER - OD TAB'
    elif (code == 6):
        return 'GLUCOLYST -G1 TAB'
    elif (code == 7):
        return 'LYCOLIC 10ml DROP'
    elif (code == 8):
        return 'LYCOREST 60ml SUSP'
    elif (code == 9):
        return 'LYCOREST TAB'
    elif (code == 10):
        return 'LYCORT 1 ml INJ'
    elif (code == 11):
        return 'REGAIN - XT TAB'
    elif (code == 12):
        return 'STAND - MF 60ml SUSP'
    elif (code == 13):
        return 'STAND MF +'
    elif (code == 14):
        return 'STAND -SP TAB'
    elif (code == 15):
        return 'STAR T TAB'
    elif (code == 16):
        return 'TEN-ON 30 ml SYRUP'
    elif (code == 17):
        return 'TRYGESIC TAB'
    elif (code == 18):
        return 'WEGO GEL 20mg'
    elif (code == 19):
        return 'WEGO GEL 30mg'
            

