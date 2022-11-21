/* function handleCredentialResponse(response) {
    console.log("Encoded JWT ID token: " + response.credential);
  } */
  window.onload = function () {
    google.accounts.id.initialize({
      client_id: "110677803877-7q6bu0bs7rb51r05g84qs3660frbt7ju.apps.googleusercontent.com",
      callback: handleCredentialResponse
    });
    google.accounts.id.renderButton(
      document.getElementById("buttonDiv"),
      { theme: "outline", size: "large" }
    );
    google.accounts.id.prompt();
  } 
 
 function handleCredentialResponse(response) {
    var profile = decodeJwtResponse(response.credential);
    $("#name").text(profile.name);
    $("#email").text(profile.email);
    $("#image").attr('src', profile.picture);
    $(".data").css("display", "block");
    $(".g-signin2").css("display", "none");
    $( ".data" ).load("dashboard.html");
 }

 


/* function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        alert("You have been signed out successfully");
        $(".g-signin2").css("display", "block");
        $(".data").css("display", "none");
    });
} */

function decodeJwtResponse(token) {
    var base64Url = token.split(".")[1];
    var base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
    var jsonPayload = decodeURIComponent(
      atob(base64)
        .split("")
        .map(function (c) {
          return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
        })
        .join("")
    );

    return JSON.parse(jsonPayload);
  }

