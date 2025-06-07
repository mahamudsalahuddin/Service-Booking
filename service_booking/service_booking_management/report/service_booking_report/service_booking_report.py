# Developer: Salah Uddin (Software Engineer, Frappe Developer)
# Description: Custom report for Service Booking DocType in ERPNext

import frappe
from frappe import _

def execute(filters=None):
    # Define report columns with labels, fieldnames, types, and widths
    columns = [
        {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 180},
        {"label": _("Service Type"), "fieldname": "service_type", "fieldtype": "Data", "width": 120},
        {"label": _("Preferred Date/Time"), "fieldname": "preferred_datetime", "fieldtype": "Datetime", "width": 180},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]

    # Build SQL WHERE conditions based on filters provided
    conditions = []
    if filters.get("service_type"):
        conditions.append("service_type = %(service_type)s")
    if filters.get("status"):
        conditions.append("status = %(status)s")

    # Combine conditions into a WHERE clause if any filter is set
    where_clause = " AND ".join(conditions)
    if where_clause:
        where_clause = "WHERE " + where_clause

    # Execute parameterized SQL query to fetch filtered booking records
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

