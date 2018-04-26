// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Standard Tour Plan', {
	refresh: function(frm) {
		
            loadjscssfile("https://maps.googleapis.com/maps/api/js?key=AIzaSyAy01k6-CrPpjZZaBp1Rw0ELflgI-5ZbjI&libraries=places", "js");
           
		frm.set_query("user", function() {		

			return {
				filters: {
					
					"enabled": 1,
					"company": frm.doc.company
				}
			}
		});
	},
	setup: function(frm) {
		//create autocomplete objects for all inputs
		
		
		

         },
 	onload: function(frm, cdt, cdn) {
		
		frappe.ui.form.on("Standard Tour Plan", "user", function(frm, cdt, cdn)  
		 {
		
		 calcRoute(frm);
 		 });
		frappe.ui.form.on("Standard Tour Plan", "user_hq_name", function(frm, cdt, cdn)  
		 {
		
		 calcRoute(frm);
 		 });

		frappe.ui.form.on("Standard Tour Plan", "fetch_and_add_in_your_plan", function(frm, cdt, cdn)  
		 {
		
		 patch_fetch(frm, cdt, cdn);
            	 dr_and_chem_count_fetch(frm, cdt, cdn);alcRoute(frm);
 		 });
       	         frappe.ui.form.on("Standard Tour Plan", "from_location",  {
	          onchange: function(frm) {
	          
	          }
		 });
	}
	
});




//define calcRoute function
function calcRoute(frm) {
    //create request
	//alert(document.getElementById("from_location").value)
    var request = {
        origin: document.getElementById("from_location").value,
        destination: document.getElementById("to_location").value,
        travelMode: google.maps.TravelMode.DRIVING, //WALKING, BYCYCLING, TRANSIT
        unitSystem: google.maps.UnitSystem.METRIC 
    }
   var directionsService = new google.maps.DirectionsService();
    //pass the request to the route method
	initialize();
    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {
	     
            //Get distance and time
            //$("#output").html("<div class='alert-info'>From: " + document.getElementById("from").value + ".<br />To: " 
		//	      + document.getElementById("to").value + ".<br /> Driving distance: " + result.routes[0].legs[0].distance.text + ".<br />Duration: " + result.routes[0].legs[0].duration.text + ".</div>");
            alert(result.routes[0].legs[0].distance.text);
            //display route
            //directionsDisplay.setDirections(result);
        } else {
            //delete route from map
            //directionsDisplay.setDirections({ routes: [] });
            //center map in London
            //map.setCenter(myLatLng);

            //show error message
            //$("#output").html("<div class='alert-danger'>Could not retrieve driving distance.</div>");
        }
    });
	
//loadjscssfile("https://maps.googleapis.com/maps/api/js?key=AIzaSyAy01k6-CrPpjZZaBp1Rw0ELflgI-5ZbjI&libraries=places", "js");

}

function loadjscssfile(filename, filetype) {
    if (filetype == "js") { //if filename is a external JavaScript file
        var fileref = document.createElement('script')
        fileref.setAttribute("type", "text/javascript")
        fileref.setAttribute("src", filename)
    } else if (filetype == "css") { //if filename is an external CSS file
        var fileref = document.createElement("link")
        fileref.setAttribute("rel", "stylesheet")
        fileref.setAttribute("type", "text/css")
        fileref.setAttribute("href", filename)
    }
    if (typeof fileref != "undefined")
        document.getElementsByTagName("head")[0].appendChild(fileref)
}


function initialize()
{
			
		var options = {
   			 types: ['(cities)']
			 }

		//from_location
		//to_location
		var input1 = document.getElementById("from_location");
		var autocomplete1 = new google.maps.places.Autocomplete(input1, options);

		var input2 = document.getElementById("to_location");
		var autocomplete2 = new google.maps.places.Autocomplete(input2, options);

}


function patch_fetch(frm, cdt, cdn) {
    frappe.call({
        method: 'team.team.doctype.standard_tour_plan.standard_tour_plan.get_patches_doc_and_chem_cnt',
        args: {
            user: frm.doc.of_tbm
        },
        callback: function(r) {
            var tbl_patches = $.map(frm.doc.tbl_patches, function(d) {
                return d.STP_Patches
            });
            for (var i = 0; i < r.message.length; i++) {
                if (tbl_patches.indexOf(r.message[i].name) === -1) {
                    var row = frappe.model.add_child(frm.doc, frm.fields_dict.tbl_patches.df.options, frm.fields_dict.tbl_patches.df.fieldname);
                    row.patch_name = r.message[i].name;
                    row.patch = r.message[i].patch_name;
                    row.user_name = r.message[i].user_name;
                    row.user_email = r.message[i].user;
                }
            }
            frm.refresh_field('tbl_patches');
        }
    });
}

function dr_and_chem_count_fetch(frm, cdt, cdn) {
    frappe.call({
        method: 'team.team.doctype.standard_tour_plan.standard_tour_plan.get_dr_and_chem_count_fetch',
        args: {
            user: frm.doc.of_tbm
        },
        callback: function(r) {
            frm.doc.no_of_dr = r.message.cnt_doc;
            frm.doc.no_chemist = r.message.cnt_chem;
            frm.refresh_field('no_of_dr');
            frm.refresh_field('no_chemist');
        }
    });
}

