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

///////////////Event functionality - WIP - Temporary Logic Batch Implementation////////////////
function create_event() {
  for (i = 0; i < events.lenth; i++) {
    date_to_add = events[i]['Date'];
    title_to_add = events[i]['Title'];
    event_info = {Date: date_to_add, Title: title_to_add};
    $.ajax({
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify(event_info),
      url: "/add_event",
      success: function(e) {
        console.log(e);
      },
      error: function(error) {
                console.log(error);
            }
    });
  }
  window.location = "/schedule";
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
