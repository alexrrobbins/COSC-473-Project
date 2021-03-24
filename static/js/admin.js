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
function admin_change_user_password() {
  var email = $("#useremail").val();
  var new_password = stringToHash($('#new_user_password').val());
  var user_info = {email: email, new_password: new_password};
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(user_info),
    url: "/admin_change_password",
    success: function(e) {
      console.log(e);
      window.location = "/welcome";
    },
    error: function(error) {
              console.log(error);
          }
  });
}
