function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
    }
  }
});


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
        get_events();
}

function get_events() {
  $.post('/local_event/')
    .done(function(result) {
      var events = result;
      start_map(events)
    });
}

function start_map(events) {


        var locDiv = document.getElementById('locations');
        var locations = locDiv.getElementsByTagName('span');

        var parkNames = document.getElementsByClassName('panel-heading');


        drop(locations, parkNames, events)
}
google.maps.event.addDomListener(window, 'load', initMap);


function drop(markerArray, parkNames, events) {
  for (var i = 0; i < markerArray.length; i++) {
    var event_list = ''
    for(var e = 0; e < events.length; e++)
    {
      if(events[e]['location']['name'] == parkNames[i].innerHTML)
      {
        event_list += 'Event title: ' + events[e]['name'] + ' ' +
                      'Type of activity: ' + events[e]['activity'] + '<br>'
      }
    }
    contentString = '<h3>' + parkNames[i].innerHTML + '</h3>' +
                    '<h4>Events at this location:<h4>' +
                    '<h5>' + event_list + '</h5>' +
                    '<a href="/events">Create Event here.</a>';
    var infoWindow = new google.maps.InfoWindow({
      content: contentString,
      maxWidth:500
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
