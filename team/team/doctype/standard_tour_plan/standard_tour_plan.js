// Copyright (c) 2018, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('Standard Tour Plan', {
	refresh: function(frm) {

	},
	setup: function(frm) {
		frm.set_query("user", function() {		

			return {
				filters: {
					
					"enabled": 1,
					"company": frm.doc.company
				}
			}
		});

         }
});
 frappe.ui.form.on("Standard Tour Plan", "fetch_and_add_in_your_plan", function(frm, cdt, cdn)  
 {
	 alert("hi");
	 calcRoute();
 });

//define calcRoute function
function calcRoute() {
    //create request
    var request = {
        origin: 'Kolhapur',
        destination: 'Sangli',
        travelMode: google.maps.TravelMode.DRIVING, //WALKING, BYCYCLING, TRANSIT
        unitSystem: google.maps.UnitSystem.METRIC 
    }
   var directionsService = new google.maps.DirectionsService();
    //pass the request to the route method
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

loadjscssfile("https://maps.googleapis.com/maps/api/js?key=AIzaSyAy01k6-CrPpjZZaBp1Rw0ELflgI-5ZbjI&libraries=places", "js");



