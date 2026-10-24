# Copyright (c) 2026, moneer and contributors
# MIT License. See license.txt

import frappe
from frappe import _

TYPE_AR = {"Receive": "قبض", "Pay": "دفع", "Internal Transfer": "تحويل داخلي"}


def execute(filters=None):
    f = frappe._dict(filters or {})
    columns = [
        {"label": _("التاريخ"), "fieldname": "posting_date", "fieldtype": "Date", "width": 95},
        {"label": _("الرقم"), "fieldname": "name", "fieldtype": "Link", "options": "Payment Entry", "width": 130},
        {"label": _("العملية"), "fieldname": "type_ar", "fieldtype": "Data", "width": 90},
        {"label": _("الطرف"), "fieldname": "party_name", "fieldtype": "Data", "width": 160},
        {"label": _("المبلغ"), "fieldname": "paid_amount", "fieldtype": "Currency", "width": 120},
        {"label": _("طريقة الدفع"), "fieldname": "mode_of_payment", "fieldtype": "Data", "width": 120},
    ]
    conds = ["docstatus = 1", "company = %(company)s", "posting_date between %(from_date)s and %(to_date)s"]
    if f.get("payment_type"):
        conds.append("payment_type = %(payment_type)s")
    if f.get("mode_of_payment"):
        conds.append("mode_of_payment = %(mode_of_payment)s")
    rows = frappe.db.sql(
        """select name, posting_date, payment_type, party, party_name, paid_amount, mode_of_payment
            from `tabPayment Entry` where {c} order by posting_date desc, creation desc""".format(
            c=" and ".join(conds)
        ),
        f, as_dict=True,
    )
    data = []
    for r in rows:
        r["type_ar"] = TYPE_AR.get(r.pop("payment_type"), "")
        r["party_name"] = r.get("party_name") or r.get("party") or ""
        data.append(r)
    return columns, data
