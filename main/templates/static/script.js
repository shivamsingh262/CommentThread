function show_login_div() {
    document.getElementById('login_form').style.display = 'block';
    document.getElementById('show_login').style.display = 'none';
    document.getElementById('show_logout').style.display = 'none';
    document.getElementById('username').value = null;
    document.getElementById('password').value = null;
}

function ask_login_div() {
    document.getElementById('login_form').style.display = 'none';
    document.getElementById('show_login').style.display = 'block';
    document.getElementById('show_logout').style.display = 'none';
}

function show_user() {
    document.getElementById('login_form').style.display = 'none';
    document.getElementById('show_login').style.display = 'none';
    document.getElementById('show_logout').style.display = 'block';
    document.getElementById('user_info').innerHTML = "Welcome "+username;
}

var login_request = new XMLHttpRequest();
login_request.onreadystatechange = function() {
    if (login_request.readyState == 4){
        var response = JSON.parse(login_request.response);
        token = response.token;
        username = response.username;
        localStorage.setItem('token',token);
        show_user();
    }
}

var user_request = new XMLHttpRequest();
user_request.onreadystatechange = function() {
    if (user_request.readyState == 4){
        var response = JSON.parse(user_request.response);
        username = response.username;
        show_user();
    }
}

function login_user() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    login_request.open('POST','/user/login',true);
    login_request.setRequestHeader("Content-type", "application/json");
    login_request.send(JSON.stringify({username:username,password:password}));
}

function get_user() {
    user_request.open('POST','/user/get',true);
    user_request.setRequestHeader("Content-type", "application/json");
    user_request.setRequestHeader("Token", token);
    user_request.send();
}

function logout() {
    localStorage.clear();
    window.token = null;
    window.username = null;
    ask_login_div();
}

window.onload = function(){
    window.token = localStorage.getItem('token');
    window.username = null;
    if(token){
        get_user();
    }
    else{
        ask_login_div();
    }
}