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
var myLatLng = {lat:39.649885, lng:-121.567749};

function initMap() {
  // alert('You in the initMap()')
        geocoder =  new google.maps.Geocoder();
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 10,
          center: myLatLng
        });
        var locDiv = document.getElementById('locations');
        var locations = locDiv.getElementsByTagName('span');
        codeAddress(locations)
}
google.maps.event.addDomListener(window, 'load', initMap);


function drop(markerArray) {
  for (var i =0; i < markerArray.length; i++) {
    setTimeout(function() {
      codeAddress(markerArray);
    }, i * 200);
  }
}

function codeAddress(address) {
  for(i = 0; i < address.length; i++)
  {
    geocoder.geocode( {'address':address[i].innerHTML}, function(results, status) {

        setTimeout(function() {
          if (status == 'OK') {
            var marker = new google.maps.Marker({
                map: map,
                animation: google.maps.Animation.DROP,
                position: results[0].geometry.location
            });
          }
        }, i * 200)

    })
  }
}
