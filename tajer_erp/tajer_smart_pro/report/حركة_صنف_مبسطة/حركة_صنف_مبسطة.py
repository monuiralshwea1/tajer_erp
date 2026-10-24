# Copyright (c) 2026, moneer and contributors
# MIT License. See license.txt

import frappe
from frappe import _


def execute(filters=None):
    f = frappe._dict(filters or {})
    columns = [
        {"label": _("التاريخ"), "fieldname": "posting_date", "fieldtype": "Date", "width": 95},
        {"label": _("المستند"), "fieldname": "voucher_no", "fieldtype": "Dynamic Link", "options": "voucher_type", "width": 130},
        {"label": _("النوع"), "fieldname": "voucher_type", "fieldtype": "Data", "width": 120},
        {"label": _("المستودع"), "fieldname": "warehouse", "fieldtype": "Data", "width": 130},
        {"label": _("داخل"), "fieldname": "in_qty", "fieldtype": "Float", "width": 90},
        {"label": _("خارج"), "fieldname": "out_qty", "fieldtype": "Float", "width": 90},
        {"label": _("الرصيد"), "fieldname": "qty_after_transaction", "fieldtype": "Float", "width": 100},
    ]
    conds = ["is_cancelled = 0", "company = %(company)s", "item_code = %(item)s",
             "posting_date between %(from_date)s and %(to_date)s"]
    if f.get("warehouse"):
        conds.append("warehouse = %(warehouse)s")
    rows = frappe.db.sql(
        """select posting_date, voucher_type, voucher_no, warehouse, actual_qty, qty_after_transaction
            from `tabStock Ledger Entry` where {c} order by posting_date, creation""".format(
            c=" and ".join(conds)
        ),
        f, as_dict=True,
    )
    data = []
    for r in rows:
        qty = float(r.pop("actual_qty") or 0)
        r["in_qty"] = qty if qty > 0 else 0
        r["out_qty"] = abs(qty) if qty < 0 else 0
        data.append(r)
    return columns, data
