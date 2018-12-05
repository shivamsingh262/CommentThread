import jwt
from ..models import User


def generate_user_token(username):
    encode_obj = {
        "username": username
    }
    token = jwt.encode(encode_obj, 'power', algorithm='HS256')
    return token


def decode_token(token):
    try:
        encode_obj = jwt.decode(token, 'power', algorithms=['HS256'])
        user = User.objects.get(
            username=encode_obj['username'], is_active=True)
        return user['user_id']
    except Exception:
        return None


def authenticate(request):
    token = request.headers.get('Token')
    user_id = decode_token(token)
    return user_id
