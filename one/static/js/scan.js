$(document).ready(function(){
    var items = [];

    $("#scan").on("click", function (){
        $("#code").focus();
        $('#code').val('');
    });

    $("#code").change(function addItem() {
        $.getJSON($SCRIPT_ROOT + '/checkout/scan', {
            code: $('#code').val()
          }, function(data) {
            if ($("#action").val() == "out") {
                if(!(items.includes(data.id)) && data.status == "In"){
                  items.push(data.id)
                  $("#items").append(data.name +"<br>");
                  $('#ids').val(items);
                }
                else {
                    alert("Item is checked out or not existent!")
                }
            }
            else if ($("#action").val() == "in") {
                if(!(items.includes(data.id)) && data.status == "Out"){
                    items.push(data.id)
                    $("#items").append(data.name + "<br>");
                    $('#ids').val(items);
                  }
                  else {
                    alert("Item is not checked out or not existent!")
                  }
            }
          });
          return false;
    })

    $('form input').keydown(function (e) {
      if (e.keyCode == 13) {
          e.preventDefault();
          $("#code").blur()
          $("#code").focus();
          $('#code').val(''); 
          return false;
      }
  });
})
