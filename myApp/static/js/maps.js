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
        //get_locations();
        get_events();

}

function get_events() {
  $.post('/local_event/')
    .done(function(result) {
      drop(result[0], result[1])
    });
}
google.maps.event.addDomListener(window, 'load', initMap);

function fillmodal(title) {
    var info = title.split(",")
    $(".modal-header .modal-title").text(info[0]);
    $(".modal-body").text('Sport: ' + info[1] +
                          '\nDate of event: ' + info[2] +
                          '\nTime of event: ' + info[3])
    $("#myModal").modal()
}

function drop(locations, events) {
  for (var i = 0; i < locations.length; i++) {
    var event_list = ''
    for(var e = 0; e < events.length; e++)
    {
      if(events[e]['location']['name'] == locations[i]['name'])
      {
        //console.log(events)
        event_list +=  '<div class="container">' +
                         '<button onclick="fillmodal(\''+ events[e]['name'] + ',' + events[e]['activity'] + ',' + events[e]['date_of_event'] + ',' + events[e]['time_of_event'] +'\')"'  + '>'+
                              events[e]['name'] +
                         '</button>' +
                        '</div><br>';
      }
    }
    contentString = '<h3>' + locations[i]['name'] + '</h3>' +
                    '<h5> Events at this location: </h5>' +
                      event_list + '<br>' +
                    '<a href="/events">Create Event here.</a>';
    var infoWindow = new google.maps.InfoWindow({
      content: contentString,
      maxWidth:500
    })

    codeAddress(locations[i]['address'], infoWindow, i*200);
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
          }
        }, timeout)
    })
}

function closeMarkers(map,markers) {
  markers.forEach(function(marker) {
    marker.infowindow.close(map,marker);
  })
}


// (\''+ events[e] +'\')
// $(function() {
//         $(document).on('click','button.btn-primary',function(){

//             //alert(events)
//             $(".modal-header .modal-title").text("Title of event");
//             $(".modal-body").text("Relevant Information")
//             $("#myModal").modal()
//         });
// });


// '<div class="modal fade" role="dialog" id=' + events[e]['name'] + '>' +
//   '<div class="modal-dialog">' +
//     '<div class="modal-content">' +
//       '<div class="modal-header">' +
//         '<h4 class="modal-title">' + events[e]['name'] + '</h4>' +
//         '<button type="button" class="close" data-dismiss="modal">&times;</button>' +
//       '</div>' +
//       '<div class="modal-body">' +
//         '<p style="font-size:110%;"><strong>' + 'Created by: </strong>' + events[e]['created_by'] + '</p>' +
//         '<p style="font-size:110%;"><strong>' + 'Sport: </strong>' + events[e]['activity'] + '</p>' +
//         '<p style="font-size:110%;"><strong>' + 'Event on: </strong>' + events[e]['date_of_event'] + '</p>' +
//         '<p style="font-size:110%;"><strong>' + 'Time: </strong>' + events[e]['time_of_event'] + '</p>' +
//         '<a href="#">Join this event</a>' +
//       '</div>' +
//
//       '<div class="modal-footer">' +
//         '<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>' +
//       '</div>' +
//     '</div>' +
//   '</div>' +
// '</div>';
//alert(id)
