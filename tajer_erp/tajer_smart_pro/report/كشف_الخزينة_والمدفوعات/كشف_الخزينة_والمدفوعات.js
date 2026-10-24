frappe.query_reports["كشف الخزينة والمدفوعات"] = {
	"filters": [
		{ "fieldname": "company", "label": __("Company"), "fieldtype": "Link", "options": "Company", "default": frappe.defaults.get_default("company"), "reqd": 1 },
		{ "fieldname": "from_date", "label": __("From Date"), "fieldtype": "Date", "default": frappe.datetime.month_start(), "reqd": 1 },
		{ "fieldname": "to_date", "label": __("To Date"), "fieldtype": "Date", "default": frappe.datetime.get_today(), "reqd": 1 },
		{ "fieldname": "payment_type", "label": __("Payment Type"), "fieldtype": "Select", "options": "\nReceive\nPay\nInternal Transfer" },
		{ "fieldname": "mode_of_payment", "label": __("Mode of Payment"), "fieldtype": "Link", "options": "Mode of Payment" },
	]
};
