// var app = new Vue({
//   el: '#app',
//   data: {
//     LatLng = {}
//   }
//   methods: {
//
//   }
// })

var geocoder;
var map;
var myLatLng = {lat:39.7285, lng:-121.8375};

function initMap() {
  // alert('You in the initMap()')
        geocoder =  new google.maps.Geocoder();
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 11,
          center: myLatLng
        });
        var locDiv = document.getElementById('locations');
        var locations = locDiv.getElementsByTagName('span');

        var parkNames = document.getElementsByClassName('panel-heading');


        drop(locations, parkNames)
}
google.maps.event.addDomListener(window, 'load', initMap);


function drop(markerArray, parkNames) {
  for (var i =0; i < markerArray.length; i++) {
    contentString = '<h4>' + parkNames[i].innerHTML + '</h4>' +
                    '<a href="#">Create Event here.</a>';
    var infoWindow = new google.maps.InfoWindow({
      content: contentString,
      maxWidth:400
    })
    codeAddress(markerArray[i].innerHTML, infoWindow, i*200);
  }
}

function codeAddress(address, infoWindow, timeout) {
    geocoder.geocode( {'address':address}, function(results, status) {
        setTimeout(function() {
          if (status == 'OK') {
            var marker = new google.maps.Marker({
                map: map,
                animation: google.maps.Animation.DROP,
                position: results[0].geometry.location
            });
            marker.addListener('click', function() {
              infoWindow.open(map, marker);
            })
          }
        }, timeout)
    })
}
