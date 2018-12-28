from ..helpers import *

def return_page(request):
    data = request.query
    response = render_page(data['site'])
    return request.Response(mime_type="text/html",text=response)