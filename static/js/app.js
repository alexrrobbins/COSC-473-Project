//Function to get sign-up information from the sign-up page
function get_register_info() {
  // Get values and establish JSON
  var email = $("inputEmail").val();
  var password = $("inputPassword").val();
  var username = $("inputUsername").val();
  var hashed_password = stringToHash(password)
  var sign_up_info = {email: email, password: hashed_password, username: username}
  // Pass values to controller
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(sign_up_info),
    dataType: 'json',
    url: "/regsiter",
    success: function(e) {
      console.log(e);
      window.location = "/register";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

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
