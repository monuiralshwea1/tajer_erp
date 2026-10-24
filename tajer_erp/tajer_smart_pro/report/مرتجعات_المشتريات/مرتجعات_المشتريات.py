# Copyright (c) 2026, moneer and contributors
# MIT License. See license.txt

import frappe
from frappe import _


def execute(filters=None):
    f = frappe._dict(filters or {})
    columns = [
        {"label": _("المرتجع"), "fieldname": "name", "fieldtype": "Link", "options": "Purchase Invoice", "width": 140},
        {"label": _("التاريخ"), "fieldname": "posting_date", "fieldtype": "Date", "width": 100},
        {"label": _("المورد"), "fieldname": "supplier_name", "fieldtype": "Data", "width": 160},
        {"label": _("ضد الفاتورة"), "fieldname": "return_against", "fieldtype": "Link", "options": "Purchase Invoice", "width": 140},
        {"label": _("الإجمالي"), "fieldname": "grand_total", "fieldtype": "Currency", "width": 120},
        {"label": _("الحالة"), "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]
    conds = ["docstatus = 1", "is_return = 1", "company = %(company)s",
             "posting_date between %(from_date)s and %(to_date)s"]
    if f.get("supplier"):
        conds.append("supplier = %(supplier)s")
    data = frappe.db.sql(
        """select name, posting_date, supplier, supplier_name, return_against, grand_total, status
            from `tabPurchase Invoice` where {c} order by posting_date desc, creation desc""".format(
            c=" and ".join(conds)
        ),
        f, as_dict=True,
    )
    return columns, data
