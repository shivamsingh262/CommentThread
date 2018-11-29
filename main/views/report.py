from ..helpers import *


def website_save(request):
    data = request.json
    token = save_website(data['url'])
    return request.Response(json={'token': token})


def comment_save(request):
    data = request.json
    comment_id = save_comment(data['text'], data['parent_id'])
    return request.Response(json={'comment_id': comment_id})


def comment_get(request):
    data = request.query
    data = get_comment(data['parent_id'])
    return request.Response(json={'data': data})
