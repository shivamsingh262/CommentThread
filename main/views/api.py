from ..helpers import *


def website_save(request):
    response = {'token': None, 'summary': 'Website saved'}
    code = 200
    try:
        user_id = request.authenticate()
        if user_id:
            data = request.json
            response['token'] = save_website(data['url'], user_id)
        else:
            code = 403
            response['summary'] = "Not Authorized"
    except Exception as e:
        code = 502
        response['summary'] = str(e)
    return request.Response(json=response, code=code)


def comment_save(request):
    response = {'comment_id': None, 'summary': 'Comment saved'}
    code = 200
    try:
        user_id = request.authenticate()
        if user_id:
            data = request.json
            response['comment_id'] = save_comment(
                data['text'], data['parent_id'], user_id)
        else:
            code = 403
            response['summary'] = "Not Authorized"
    except Exception as e:
        code = 502
        response['summary'] = str(e)
    return request.Response(json=response, code=code)


def comment_get(request):
    response = {'data': [], 'summary': 'Comments Data'}
    code = 200
    try:
        user_id = request.authenticate()
        if user_id:
            data = request.query
            response['data'] = get_comment(data['parent_id'])
        else:
            code = 403
            response['summary'] = "Not Authorized"
    except Exception as e:
        code = 502
        response['summary'] = str(e)
    return request.Response(json=response, code=code)


def user_register(request):
    response = {'summary': 'Registration successful'}
    code = 200
    try:
        data = request.json
        success = register_user(
            data['email'], data['username'], data['password'])
        if not success:
            code = 400
            response['summary'] = 'Error in registering'
    except Exception as e:
        code = 502
        response['summary'] = str(e)
    return request.Response(json=response, code=code)


def user_login(request):
    response = {'token': None, 'summary': 'User logged in'}
    code = 200
    try:
        data = request.json
        token = login_user(data['username'], data['password'])
        if token:
            response['token'] = token.decode("utf-8")
        else:
            code = 400
            response['summary'] = 'Error logging in'
    except Exception as e:
        code = 502
        response['summary'] = str(e)
    return request.Response(json=response, code=code)


def vote_add(request):
    response = {'summary': 'Vote added'}
    code = 200
    try:
        user_id = request.authenticate()
        if user_id:
            data = request.json
            add_vote(data['comment_id'], data['vote_type'], user_id)
        else:
            code = 403
            response['summary'] = "Not Authorized"
    except Exception as e:
        code = 502
        response['summary'] = str(e)
    return request.Response(json=response, code=code)
