// Copyright (c) 2025, Salah Uddin and contributors
// For license information, please see license.txt

frappe.query_reports["Service Booking Report"] = {
    "filters": [
        {
            "fieldname": "service_type",
            "label": "Service Type",
            "fieldtype": "Select",
            "options": ["", "Therapy", "Spa", "Others"]
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": ["", "Requested", "Approved", "Completed"]
        }
    ]
};
