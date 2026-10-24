# Copyright (c) 2026, moneer and contributors
# MIT License. See license.txt

import frappe
from frappe import _


def execute(filters=None):
    f = frappe._dict(filters or {})
    columns = [
        {"label": _("التاريخ"), "fieldname": "posting_date", "fieldtype": "Date", "width": 100},
        {"label": _("المستند"), "fieldname": "voucher_no", "fieldtype": "Dynamic Link", "options": "voucher_type", "width": 140},
        {"label": _("النوع"), "fieldname": "voucher_type", "fieldtype": "Data", "width": 120},
        {"label": _("الحساب"), "fieldname": "account", "fieldtype": "Data", "width": 170},
        {"label": _("مدين"), "fieldname": "debit", "fieldtype": "Currency", "width": 110},
        {"label": _("دائن"), "fieldname": "credit", "fieldtype": "Currency", "width": 110},
        {"label": _("الرصيد"), "fieldname": "balance", "fieldtype": "Currency", "width": 120},
    ]
    base = ["is_cancelled = 0", "company = %(company)s", "party_type = 'Customer'", "party = %(customer)s"]
    opening = frappe.db.sql(
        "select coalesce(sum(debit - credit), 0) as bal from `tabGL Entry` where {c} and posting_date < %(from_date)s".format(
            c=" and ".join(base)
        ),
        f, as_dict=True,
    )[0]["bal"]
    rows = frappe.db.sql(
        """select posting_date, voucher_type, voucher_no, account, debit, credit
            from `tabGL Entry` where {c} and posting_date between %(from_date)s and %(to_date)s
            order by posting_date, creation""".format(c=" and ".join(base)),
        f, as_dict=True,
    )
    data, bal = [], float(opening or 0)
    if bal:
        data.append({"posting_date": f.get("from_date"), "voucher_no": "رصيد افتتاحي",
                     "voucher_type": "", "account": "", "debit": 0, "credit": 0, "balance": bal})
    for r in rows:
        bal += float(r.debit or 0) - float(r.credit or 0)
        r["balance"] = bal
        data.append(r)
    return columns, data
