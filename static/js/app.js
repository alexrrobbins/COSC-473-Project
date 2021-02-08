/////Render Template Functions/////
function display_signup_page() {
  window.location = "/signup";
}

function display_login_page() {
  window.location = "/login";
}

//////Logical functioms//////
//Function to get sign-up information from the sign-up page
function get_sign_up_info() {
  // Get values and establish JSON
  var email = $("#inputEmail").val();
  var password = $("#inputPassword").val();
  var username = $("#inputUsername").val();
  var hashed_password = stringToHash(password);
  var sign_up_info = {email: email, password: hashed_password, username: username};
  // Pass values to controller
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(sign_up_info),
    url: "/register",
    success: function(e) {
      console.log(e);
      window.location = "/welcome";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

function get_login_info() {
  var email = $("#inputEmail").val();
  var password = $("#inputPassword").val();
  var hashed_password = stringToHash(password);
  var login_info = {email: email, password: hashed_password}
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(login_info),
    url: "/login_verify",
    success: function(e) {
      console.log(e);
      window.location = "/welcome";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

////////Helper functions///////
//Hash function borrowed from https://www.geeksforgeeks.org/how-to-create-hash-from-string-in-javascript/
function stringToHash(string) {
  var hash = 0;
  if (string.length == 0) return hash;
  for (i = 0; i < string.length; i++) {
    char = string.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash;
  }
  return hash;
}
