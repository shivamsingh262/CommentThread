from main import app
from .report import *

app.router.add_route("/website/save", website_save, methods=['POST'])
