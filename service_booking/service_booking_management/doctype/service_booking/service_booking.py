# Developer: Salah Uddin (Software Engineer, Frappe Developer)
# Description: Custom ServiceBooking DocType event handlers for ERPNext

import frappe
import requests
from frappe.model.document import Document


class ServiceBooking(Document):
	def on_update(self):
		# Fetch customer's custom email from Customer doctype using the customer_name linked in the booking
		customer_email = frappe.db.get_value("Customer", self.customer_name, "custom_customer_email")
		# Send approval email if booking status is "Approved" and customer email exists
		if self.status == "Approved" and customer_email:
			frappe.sendmail(
				recipients=[customer_email],
				subject="Your Booking is Approved",
				message="""
                    <p>Dear {0},</p>
                    <p>Your service booking has been <strong>approved</strong>.</p>
                    <p>Thank you for choosing us!</p>
                    <p>– Wellness Center</p>
                """.format(self.customer_name)
			)
			# Enqueue email sending
			frappe.enqueue(method="frappe.email.queue.flush", queue='short')



		# Send booking data to webhook
		try:
			webhook_url = "https://webhook.site/a67597fb-58bb-4469-b628-2aacdfcd7930"  # Replace with your URL
			payload = {
				"customer_name": self.customer_name,
				"service_type": self.service_type,
				"preferred_datetime": self.preferred_datetime,
				"status": self.status
			}
			response = requests.post(webhook_url, json=payload)
			frappe.logger().info(f"Webhook sent: {response.status_code}")
		except Exception as e:
			frappe.log_error(frappe.get_traceback(), "Service Booking Webhook Error")
