# Copyright (c) 2026, moneer and contributors
# MIT License. See license.txt

import frappe
from frappe import _


def execute(filters=None):
    f = frappe._dict(filters or {})
    columns = [
        {"label": _("التاريخ"), "fieldname": "posting_date", "fieldtype": "Date", "width": 110},
        {"label": _("عدد الفواتير"), "fieldname": "inv_count", "fieldtype": "Int", "width": 110},
        {"label": _("إجمالي المبيعات"), "fieldname": "total", "fieldtype": "Currency", "width": 140},
        {"label": _("المحصل"), "fieldname": "collected", "fieldtype": "Currency", "width": 140},
        {"label": _("المتبقي"), "fieldname": "outstanding", "fieldtype": "Currency", "width": 140},
    ]
    data = frappe.db.sql(
        """select posting_date, count(name) as inv_count, sum(grand_total) as total,
            sum(grand_total - outstanding_amount) as collected, sum(outstanding_amount) as outstanding
            from `tabSales Invoice`
            where docstatus = 1 and company = %(company)s and posting_date between %(from_date)s and %(to_date)s
            group by posting_date order by posting_date desc""",
        f, as_dict=True,
    )
    return columns, data
