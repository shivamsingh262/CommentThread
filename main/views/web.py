from ..helpers import *

def return_page(request):
    response = render_page()
    return request.Response(mime_type="text/html",text=response)


def comment_get(request):
    response = None
    try:
        user_id = request.authenticate()
        if user_id:
            data = request.query
            response = render_comments(data['site'])
        else:
            response = "Not Authorized"
    except Exception as e:
        response = str(e)
    return request.Response(mime_type="text/html",text=response)