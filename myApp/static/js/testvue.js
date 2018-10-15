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


var app = new Vue({
  el: '#app',
  data: {
    response: {}
  },
  mounted: function() {
    this.$nextTick(function() {
      this.getData();
    })
  },
  methods: {
    getData: function() {
      $.post('/test_view/')
        .done(function(result) {
          app.response = result;
        })
      .fail(function(xhr, status, error) {

      })
    }
  }
})
