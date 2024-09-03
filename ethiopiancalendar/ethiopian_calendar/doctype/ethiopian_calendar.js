
frappe.ui.form.on("Ethiopian Date Settings", {
	refresh(frm) {
		frappe.boot.ethiopian_date_datepicker_format = frm.doc.ethiopian_date_datepicker_format;
		frappe.boot.ethiopian_date_format = frm.doc.ethiopian_date_format;
        frappe.boot.calendar_type = frm.doc.calendar_type;
	},
});
