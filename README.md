# Service Booking App - ERPNext Developer Assignment

A custom Frappe app developed as part of the **Alfastack ERPNext Developer Assignment**. This module helps a wellness center manage therapy and spa service bookings efficiently using Frappe's framework.

## Features Implemented

- ✅ Custom Doctype: `Service Booking`
  - Fields: Customer Name, Service Type, Preferred Date/Time, Status
- ✅ Workflow: Requested → Approved → Completed
  - Status changes with role-based transitions
- ✅ Email Notification
  - Sends booking confirmation email to the customer on approval
- ✅ Custom Print Format
  - Jinja-based Booking Confirmation receipt
- ✅ Script Report: `Service Booking Report`
  - Filters: Service Type and Status
- ✅ Bonus: Webhook Integration
  - Sends booking data to a dummy REST API via `requests.post`

---

## Setup Instructions

### Prerequisites
- ERPNext + Frappe installed (tested on version 15.x)
- Bench CLI
- Python 3.10+
- Node.js, Redis, MariaDB

### Installation Steps

# Navigate to your bench directory
cd frappe-bench

# Clone this repository
bench get-app https://github.com/mahamudsalahuddin/Service-Booking.git apps/service_booking

# Install the app on your site
bench --site your-site-name install-app service_booking


# Run necessary build and migrations
bench build
bench migrate
bench restart
