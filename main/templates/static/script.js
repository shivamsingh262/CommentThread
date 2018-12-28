function show_login_div() {
    document.getElementById('login_form').style.display = 'block';
    document.getElementById('show_login').style.display = 'none';
    document.getElementById('show_logout').style.display = 'none';
    document.getElementById('comment_box').style.display = 'none';
    document.getElementById('username').value = null;
    document.getElementById('password').value = null;
}

function ask_login_div() {
    document.getElementById('login_form').style.display = 'none';
    document.getElementById('show_login').style.display = 'block';
    document.getElementById('show_logout').style.display = 'none';
    document.getElementById('comment_box').style.display = 'none';
}

function show_user() {
    document.getElementById('login_form').style.display = 'none';
    document.getElementById('show_login').style.display = 'none';
    document.getElementById('show_logout').style.display = 'block';
    document.getElementById('comment_box').style.display = 'block';
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

var add_comment_request = new XMLHttpRequest();
add_comment_request.onreadystatechange = function() {
    if (add_comment_request.readyState == 4){
        get_comment();
        document.getElementById('comment').value = null;
    }
}

var get_comment_request = new XMLHttpRequest();
get_comment_request.onreadystatechange = function() {
    if (get_comment_request.readyState == 4){
        document.getElementById('comment_body').innerHTML = get_comment_request.response;
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

function add_comment() {
    var text = document.getElementById('comment').value;
    var parent_id = site;
    add_comment_request.open('POST','/comment/save',true);
    add_comment_request.setRequestHeader("Content-type", "application/json");
    add_comment_request.setRequestHeader("Token", token);
    add_comment_request.send(JSON.stringify({text:text,parent_id:parent_id}));
}

function get_comment() {
    var url = "/comment/get?site="+site;
    get_comment_request.open('GET',url,true);
    get_comment_request.setRequestHeader("Content-type", "text/html");
    get_comment_request.setRequestHeader("Token", token);
    get_comment_request.send();
}

window.onload = function(){
    window.token = localStorage.getItem('token');
    window.username = null;
    var params = (new URL(document.location)).searchParams;
    window.site = params.get('site');
    if(token){
        get_user();
    }
    else{
        ask_login_div();
    }
    get_comment();
}