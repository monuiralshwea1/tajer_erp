frappe.query_reports["ملخص المبيعات اليومي"] = {
	"filters": [
		{ "fieldname": "company", "label": __("Company"), "fieldtype": "Link", "options": "Company", "default": frappe.defaults.get_default("company"), "reqd": 1 },
		{ "fieldname": "from_date", "label": __("From Date"), "fieldtype": "Date", "default": frappe.datetime.month_start(), "reqd": 1 },
		{ "fieldname": "to_date", "label": __("To Date"), "fieldtype": "Date", "default": frappe.datetime.get_today(), "reqd": 1 },
	]
};
