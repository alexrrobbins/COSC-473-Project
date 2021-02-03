function getLoginInfo() {
  var email = $("inputEmail").value;
  var password = $("inputPassword").value;
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    data: {email: email, password: password},
    dataType: 'json',
    url: '/login'
  })
}
