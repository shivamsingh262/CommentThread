from ..helpers import *

def website_save(request):
    data = request.json
    token = save_website(data['url'])
    return request.Response(json={'token':token})