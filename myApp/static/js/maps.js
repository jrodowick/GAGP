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

        var parkNames = document.getElementsByClassName('card-header');


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
        event_list +=  '<div class=container">' +
                         '<button type="button" class="btn btn-primary" data-toggle="collapse" data-target=#' + events[e]['name'] + '>' +
                              events[e]['name'] +
                         '</button>' +
                          '<div id=' + events[e]['name'] + ' class="collapse">' +
                            '<div class="container" style="border:dotted;">' +
                              '<br><p><strong>' + 'Sport: </strong>' + events[e]['activity'] + '</p>' +
                              '<p><strong>' + 'Event on: </strong>' + events[e]['date_of_event'] + '</p>' +
                              '<a href="#">Join this event.</a>' +
                            '</div>' +
                          '</div>' +
                        '</div>' +'<br>'

      }
    }
    contentString = '<h3>' + parkNames[i].innerHTML + '</h3>' +
                    '<h5> Events at this location: </h5>' +
                      event_list +
                    '<a href="/events">Create Event here.</a>';
    var infoWindow = new google.maps.InfoWindow({
      content: contentString,
      maxWidth:500
    })

    codeAddress(markerArray[i].innerHTML, infoWindow, i*200);
  }
}

function codeAddress(address, infoWindow, timeout) {
    markers = [];
    geocoder.geocode( {'address':address}, function(results, status) {
        setTimeout(function() {
          if (status == 'OK') {
            var marker = new google.maps.Marker({
                map: map,
                animation: google.maps.Animation.DROP,
                position: results[0].geometry.location,
                infowindow: infoWindow
            });
            markers.push(marker)
            google.maps.event.addListener(marker, 'click', function() {
              closeMarkers(map,markers);
              infoWindow.open(map, marker);
            })



            // marker.addListener('click', function() {
            //   infoWindow.open(map, marker);
            // })
          }
        }, timeout)
    })
}

function closeMarkers(map,markers) {
  markers.forEach(function(marker) {
    marker.infowindow.close(map,marker);
  })
}
