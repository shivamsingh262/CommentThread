import jwt


def generate_user_token(username):
    encode_obj = {
        "username": username
    }
    token = jwt.encode(encode_obj, 'power', algorithm='HS256')
    return token
