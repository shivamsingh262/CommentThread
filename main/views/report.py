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


def user_register(request):
    data = request.json
    success = register_user(data['email'], data['username'], data['password'])
    if success:
        status = 200
    else:
        status = 400
    return request.Response(json={}, code=status)


def user_login(request):
    data = request.json
    token = login_user(data['username'], data['password'])
    if token:
        result = {'data': token.decode("utf-8")}
        status = 200
    else:
        result = {'data': 'Error logging in'}
        status = 400
    return request.Response(json=result, code=status)
