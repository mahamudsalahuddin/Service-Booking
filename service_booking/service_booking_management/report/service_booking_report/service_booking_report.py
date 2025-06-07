# Copyright (c) 2025, Salah Uddin and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data




import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 180},
        {"label": _("Service Type"), "fieldname": "service_type", "fieldtype": "Data", "width": 120},
        {"label": _("Preferred Date/Time"), "fieldname": "preferred_datetime", "fieldtype": "Datetime", "width": 180},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]

    conditions = []
    if filters.get("service_type"):
        conditions.append("service_type = %(service_type)s")
    if filters.get("status"):
        conditions.append("status = %(status)s")

    where_clause = " AND ".join(conditions)
    if where_clause:
        where_clause = "WHERE " + where_clause

    data = frappe.db.sql(f"""
        SELECT
            customer_name,
            service_type,
            preferred_datetime,
            status
        FROM `tabService Booking`
        {where_clause}
        ORDER BY preferred_datetime DESC
    """, filters, as_dict=True)

    return columns, data

