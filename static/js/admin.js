//////Logical functioms - admin functionality//////
function remove_user() {
  var email = $("#useremail").val();
  var user_info = {email: email};
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(user_info),
    url: "/remove_user",
    success: function(e) {
      console.log(e);
      window.location = "/welcome";
    },
    error: function(error) {
              console.log(error);
          }
  });
}
function promote_user() {
  var email = $("#useremail").val();
  var user_info = {email: email};
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(user_info),
    url: "/promote_user",
    success: function(e) {
      console.log(e);
      window.location = "/welcome";
    },
    error: function(error) {
              console.log(error);
          }
  });
}
