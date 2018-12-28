from ..helpers import *

def return_page(request):
    data = request.query
    response = render_page(data["site"])
    return request.Response(mime_type="text/html",text=response)


def comment_get(request):
    response = None
    data = request.query
    response = render_comments(data['site'])
    return request.Response(mime_type="text/html",text=response)