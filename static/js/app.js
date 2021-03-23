/////Render Template Functions/////
function display_signup_page() {
  window.location = "/signup";
}

function display_login_page() {
  window.location = "/login";
}

function display_schedule_page() {
  window.location = "/schedule-actions";
}

function display_passcode_page() {
  window.location = "/schedule-id-passcode";
}

function change_password_page() {
  window.location = "/change-password";
}

//////Alert functions - need to be fixed and added later//////////
function check_for_bad_credentials() {
  if (document.referrer !== '') {
    alert("Username or password incorrect, please try again");
  }
}
function check_for_bad_registration() {
  if (document.referrer !== '') {
    alert("Email or username is already in use, please try again");
  }
}

//////Logical functioms - user functionality//////

function get_sign_up_info() {
  var email = $("#inputEmail").val();
  var password = $("#inputPassword").val();
  var username = $("#inputUsername").val();
  var hashed_password = stringToHash(password);
  var sign_up_info = {email: email, password: hashed_password, username: username};
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

function user_logout() {
  $.ajax({
    type: 'POST',
    url: "/user_logout",
    success: function(e) {
      console.log(e);
      window.location = "/";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

function email_change_password_request() {
  var email = $('#useremail_pwd').val();
  var email_info = {email: email};
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(email_info),
    url: "/email_change_password_request",
    success: function(e) {
      console.log(e);
      window.location = "/change-password-2";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

function reset_password() {
  var email = $('#useremail_pwd_2').val();
  var reset_pin = $('#pwd_reset_pin').val();
  var new_pwd = stringToHash($('#new_pwd').val());
  var reset_info = {email: email, reset_pin: reset_pin, new_pwd: new_pwd};
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(reset_info),
    url: "/change_password_request",
    success: function(e) {
      console.log(e);
      window.location = "/login";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

///Logical functions - schedule functionality

function create_new_schedule() {
  $.ajax({
    type: 'POST',
    url: "/create_new_schedule",
    success: function(e) {
      console.log(e);
      window.location = "/schedule";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

function delete_schedule() {
  $.ajax({
    type: 'POST',
    url: "/delete_schedule",
    success: function(e) {
      console.log(e);
      window.location = "/schedule-actions";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

function retrieve_schedule() {
  var schedule_id = $('#inputScheduleID').val();
  var passcode = $('#inputSchedulePassword').val();
  var schedule_info = {schedule_id: schedule_id, passcode: passcode};
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(schedule_info),
    url: "/retrieve_schedule",
    success: function(e) {
      console.log(e);
      window.location = "/schedule";
    },
    error: function(error) {
              console.log(error);
          }
  });
}

function add_event() {
  var event_date = $('#eventDate').val();
  var event_title = $('#eventTitle').val();
  var event_time = $('#eventTime').val();
  var event_info = {Date: event_date, Title: event_title};
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify(event_info),
    url: "/add_event",
    success: function(e) {
      console.log(e);
      window.location = "/schedule";
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
