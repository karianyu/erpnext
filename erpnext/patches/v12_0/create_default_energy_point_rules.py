import frappe

from erpnext.setup.install import create_default_energy_point_rules


def execute():
	# ponytail: Energy Points were dropped in Frappe v16
	if not frappe.db.exists("DocType", "Energy Point Rule"):
		return
	frappe.reload_doc("social", "doctype", "energy_point_rule")
	create_default_energy_point_rules()
