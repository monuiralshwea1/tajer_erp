# Copyright (c) 2026, moneer and contributors
# MIT License. See license.txt

import frappe
from frappe import _


def execute(filters=None):
    f = frappe._dict(filters or {})
    columns = [
        {"label": _("الفاتورة"), "fieldname": "name", "fieldtype": "Link", "options": "Sales Invoice", "width": 130},
        {"label": _("التاريخ"), "fieldname": "posting_date", "fieldtype": "Date", "width": 100},
        {"label": _("العميل"), "fieldname": "customer_name", "fieldtype": "Data", "width": 170},
        {"label": _("الإجمالي"), "fieldname": "grand_total", "fieldtype": "Currency", "width": 120},
        {"label": _("المدفوع"), "fieldname": "paid_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("المتبقي"), "fieldname": "outstanding_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("الحالة"), "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]
    conds = ["docstatus = 1", "company = %(company)s", "posting_date between %(from_date)s and %(to_date)s"]
    if f.get("customer"):
        conds.append("customer = %(customer)s")
    if f.get("status"):
        conds.append("status = %(status)s")
    data = frappe.db.sql(
        """select name, posting_date, customer, customer_name, grand_total,
            (grand_total - outstanding_amount) as paid_amount, outstanding_amount, status
            from `tabSales Invoice` where {c} order by posting_date desc, creation desc""".format(
            c=" and ".join(conds)
        ),
        f, as_dict=True,
    )
    return columns, data
