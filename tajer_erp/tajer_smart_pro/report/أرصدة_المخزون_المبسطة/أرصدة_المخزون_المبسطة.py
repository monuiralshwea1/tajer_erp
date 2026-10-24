# Copyright (c) 2026, moneer and contributors
# MIT License. See license.txt

import frappe
from frappe import _


def execute(filters=None):
    f = frappe._dict(filters or {})
    columns = [
        {"label": _("الصنف"), "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 130},
        {"label": _("اسم الصنف"), "fieldname": "item_name", "fieldtype": "Data", "width": 170},
        {"label": _("المستودع"), "fieldname": "warehouse", "fieldtype": "Data", "width": 140},
        {"label": _("الكمية"), "fieldname": "actual_qty", "fieldtype": "Float", "width": 100},
        {"label": _("سعر التقييم"), "fieldname": "valuation_rate", "fieldtype": "Currency", "width": 110},
        {"label": _("القيمة"), "fieldname": "stock_value", "fieldtype": "Currency", "width": 130},
    ]
    conds = ["b.actual_qty != 0", "w.company = %(company)s"]
    if f.get("warehouse"):
        conds.append("b.warehouse = %(warehouse)s")
    if f.get("item_group"):
        conds.append("i.item_group = %(item_group)s")
    data = frappe.db.sql(
        """select b.item_code, i.item_name, b.warehouse, b.actual_qty, b.valuation_rate,
            (b.actual_qty * b.valuation_rate) as stock_value
            from tabBin b inner join tabItem i on i.name = b.item_code
            inner join tabWarehouse w on w.name = b.warehouse
            where {c} order by i.item_name, b.warehouse""".format(c=" and ".join(conds)),
        f, as_dict=True,
    )
    return columns, data
