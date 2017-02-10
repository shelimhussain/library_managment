import frappe
from frappe import _
from frappe.utils import nowdate, add_days



@frappe.whitelist()
def get_rags(sid):

  return frappe.db.sql("""select
    rag_name from `tabRag`
    where shelf_id = 1""", as_dict=True)

	frappe.msgprint(_("got it"))
