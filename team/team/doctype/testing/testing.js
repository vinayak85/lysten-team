// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('testing', {
	refresh: function(frm) {

	}
});
frappe.ui.form.on("testing", "btn1",
    function(frm) {
        frappe.call({
	    alert("hi");
            "method": "team.team.doctype.testing.testing.ching",
            callback: function (data) {
              console.log(data);                
            }
        })
    });
