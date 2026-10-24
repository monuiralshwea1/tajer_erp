frappe.query_reports["حركة صنف مبسطة"] = {
	"filters": [
		{ "fieldname": "company", "label": __("Company"), "fieldtype": "Link", "options": "Company", "default": frappe.defaults.get_default("company"), "reqd": 1 },
		{ "fieldname": "item", "label": __("Item"), "fieldtype": "Link", "options": "Item", "reqd": 1 },
		{ "fieldname": "warehouse", "label": __("Warehouse"), "fieldtype": "Link", "options": "Warehouse" },
		{ "fieldname": "from_date", "label": __("From Date"), "fieldtype": "Date", "default": frappe.datetime.month_start(), "reqd": 1 },
		{ "fieldname": "to_date", "label": __("To Date"), "fieldtype": "Date", "default": frappe.datetime.get_today(), "reqd": 1 },
	]
};
