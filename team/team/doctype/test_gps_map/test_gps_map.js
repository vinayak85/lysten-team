// Copyright (c) 2017, Vinayak Patil and contributors
// For license information, please see license.txt

frappe.ui.form.on('test_gps_map', {
	refresh: function(frm) {

	}
});

/**************** Added Code On 22/02/2018 ****************/


frappe.ui.form.on("test_gps_map", "investigate", function (frm) {

    initialize(frm.doc.fom_date, frm.doc.user);
});
frappe.ui.form.on("test_gps_map", "fom_date", function (frm) {

    initialize(frm.doc.fom_date, frm.doc.user);
});
frappe.ui.form.on("test_gps_map", "user", function (frm) {

    initialize(frm.doc.fom_date, frm.doc.user);
});

function initialize(date, user) {
    if ((String(date) != 'undefined') && (String(user) != 'undefined')) {
        call_dr_gps_data(date, user);

    }


}

function call_dr_gps_data(date, user) {

    frappe.call({
        method: "team.get_lat_long_doc_calls.get_lat_long_details",
        args: {
            date: date,
            emp: user

        },
        callback: function (r) {
            //alert(r);
            //markers=r.message;
            draw_map(r.message);
            //draw_test("fs");
        }
    });
}

function draw_test(mar) {
    if (document.getElementById('map')) {

        var markerLatLng = new google.maps.LatLng(-33.91727341958453, 151.23348314155578);

        var mapOptions = {
            zoom: 16,
            center: markerLatLng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById("map"), mapOptions);

        var markerIcon = {
            url: 'http://image.flaticon.com/icons/svg/252/252025.svg',
            scaledSize: new google.maps.Size(80, 80),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(32, 65)
        };

        var markerLabel = 'Arjun patil!';

        var marker = new MarkerWithLabel({
            map: map,
            animation: google.maps.Animation.DROP,
            position: markerLatLng,
            icon: markerIcon,
            labelContent: markerLabel,
            labelAnchor: new google.maps.Point(18, 12),
            labelClass: "my-custom-class-for-label", // the CSS class for the label
            labelInBackground: true
        });

    }
}

function draw_map(mar) {

    var markers = mar;
    //alert(markers);

    var mapOptions = {
        center: new google.maps.LatLng(markers[0].latitude, markers[0].longitude),
        zoom: 9,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById('map'), mapOptions);
    var infoWindow = new google.maps.InfoWindow();
    var lat_lng = new Array();
    var latlngbounds = new google.maps.LatLngBounds();
    var txtDir = '';
    for (i = 0; i < markers.length; i++) {
        var data = markers[i]
        if ((data.latitude != null) && (data.latitude.length > 4)) {
            var myLatlng = new google.maps.LatLng(data.latitude, data.longitude);

            //alert(data.latitude+","+ data.longitude)

            lat_lng.push(myLatlng);


            var marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
                title: data.doctor_name,
                label: (i) + ": " + data.subject + ", (" + data.time_call + ")"
            });
            txtDir += (i) + ": " + data.subject + ", (" + data.time_call + "), gps: " + data.latitude + "," + data.longitude + "<br />";

            latlngbounds.extend(marker.position);
            (function (marker, data) {
                google.maps.event.addListener(marker, "click", function (e) {
                    infoWindow.setContent(data.doctor_name + ", (" + data.time_call + ")");
                    infoWindow.open(map, marker);
                });
            })(marker, data);
        }

    }

    map.setCenter(markers[0]);
    map.fitBounds(latlngbounds);
/*
    document.getElementById('directions').innerHTML = "";
   

    //Initialize the Path Array
    var path = new google.maps.MVCArray();

    //Initialize the Direction Service
    var service = new google.maps.DistanceMatrixService();

    //Set the Path Stroke Color
    var poly = new google.maps.Polyline({
        map: map,
        strokeColor: '#4986E7'
    });


    //Loop and Draw Path Route between the Points on MAP
    for (var i = 0; i <= lat_lng.length; i++) {
        if ((i + 1) <= lat_lng.length) {
            var src = lat_lng[i];
            var des = lat_lng[i + 1];
            //path.push(src);
            poly.setPath(path);
     // alert("11");
            service.getDistanceMatrix({
                origins: src,
                destinations: des,
                travelMode: google.maps.TravelMode.DRIVING,
                unitSystem: google.maps.UnitSystem.METRIC,
                avoidHighways: false,
                avoidTolls: false
            }, function (response, status) {
                if (status == google.maps.DistanceMatrixStatus.OK && response.rows[0].elements[0].status != "ZERO_RESULTS") {
                    var distance = response.rows[0].elements[0].distance.text;
		alert(distance );
                    var duration = response.rows[0].elements[0].duration.text;
                    var dvDistance = document.getElementById("directions");
                    dvDistance.innerHTML = "";
                    dvDistance.innerHTML += "Distance: " + distance + "<br />";
                    dvDistance.innerHTML += "Duration:" + duration;

                } else {
                    alert("Unable to find the distance via road.");
                }
            });


      

        }
	
    }
*/
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

loadjscssfile("https://maps.googleapis.com/maps/api/js?key=AIzaSyAy01k6-CrPpjZZaBp1Rw0ELflgI-5ZbjI&callback=initialize", "js");
/* loadjscssfile("http://139.59.63.181/files/map_doctor_call.css", "css"); 
loadjscssfile("https://maps.googleapis.com/maps/api/js?v=3.exp&key=AIzaSyBHCmQ_h2FrFT0D1CBOkB89xXTOtQsvNN0&callback=initialize", "js");
loadjscssfile("https://cdn.sobekrepository.org/includes/gmaps-markerwithlabel/1.9.1/gmaps-markerwithlabel-1.9.1.min.js", "js");
*/
