// Copyright (c) 2016, myself and contributors
// For license information, please see license.txt
frappe.ui.form.on('Book', {
	shelf_no: function(frm,cdt,cdn){


		var m_att = frappe.model.get_doc(cdt,cdn);

		if(m_att.shelf_no){


			frappe.call({
				method: "library_managment.lms.doctype.book.book.get_rags",
				args: {
					   sid:m_att.shelf_no
				},
				callback: function(r) {
					frappe.model.set_value(cdt,cdn,"rag_no",r.message);
				}
			});
		} else{
			   frappe.model.set_value(cdt,cdn,"rag_no",null);
		}

	}

});

frappe.ui.form.on('Book', {
	refresh: function(frm) {

	}
});
