frappe.query_reports["أرصدة المخزون المبسطة"] = {
	"filters": [
		{ "fieldname": "company", "label": __("Company"), "fieldtype": "Link", "options": "Company", "default": frappe.defaults.get_default("company"), "reqd": 1 },
		{ "fieldname": "warehouse", "label": __("Warehouse"), "fieldtype": "Link", "options": "Warehouse" },
		{ "fieldname": "item_group", "label": __("Item Group"), "fieldtype": "Link", "options": "Item Group" },
	]
};
