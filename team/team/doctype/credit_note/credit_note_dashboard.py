from frappe import _

def get_data():
	return {
		'fieldname': 'credit_note',
		'non_standard_fieldnames': {
			'Delivery Note': 'against_sales_invoice',
			'Journal Entry': 'reference_name',
			'Payment Entry': 'reference_name',
			'Payment Request': 'reference_name',
			'credit_note': 'return_against'
		},
		'internal_links': {
			'Sales Order': ['items', 'sales_order']
		},
		'transactions': [
			{
				'label': _('Payment'),
				'items': ['Payment Entry', 'Payment Request', 'Journal Entry']
			},
			{
				'label': _('Reference'),
				'items': ['Timesheet', 'Delivery Note', 'Sales Order']
			},
			{
				'label': _('Returns'),
				'items': ['credit_note']
			},
		]
	}
