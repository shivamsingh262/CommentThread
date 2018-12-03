from ..models import *
from datetime import datetime as dt
from mongoengine import DoesNotExist
from .middleware import *


def save_website(url):
    website = Website()
    website.url = url
    website.save()
    return website.token


def save_comment(text, parent_id):
    comment = Comment()
    comment.text = text
    comment.parent_id = parent_id
    comment.save()
    return comment.comment_id


def get_comment(parent_id):
    comments = Comment.objects(parent_id=parent_id)
    data = []
    for comment in comments:
        di = {}
        di['text'] = comment['text']
        di['comment_id'] = comment['comment_id']
        di['added_by'] = None
        di['timestamp'] = dt.strftime(comment['timestamp'], '%Y-%m-%d %H:%M')
        di['comments'] = get_comment(comment['comment_id'])
        data.append(di)
    return data


def register_user(email, username, password):
    try:
        u = User.objects.get(Q(username=username) | Q(email=email))
        return False
    except DoesNotExist:
        user = User()
        user.email = email
        user.username = username
        user.password = enc_password(password)
        user.is_active = True
        user.save()
        return True


def login_user(username, password):
    password = enc_password(password)
    try:
        user = User.objects.get(
            username=username, password=password, is_active=True)
        return generate_user_token(username)
    except DoesNotExist:
        return False
