from main import app
from .api import *
from .web import *
from ..helpers import authenticate

app.extend_request(authenticate)

app.router.add_route("/website/save", website_save, methods=['POST'])
app.router.add_route("/comment/save", comment_save, methods=['POST'])
app.router.add_route("/comment/get", comment_get, methods=['GET'])
app.router.add_route("/user/register", user_register, methods=['POST'])
app.router.add_route("/user/login", user_login, methods=['POST'])
app.router.add_route("/user/get", user_get, methods=['POST'])
app.router.add_route("/comment/vote", vote_add, methods=['POST'])

app.router.add_route("/main/page",return_page,methods=['GET'])