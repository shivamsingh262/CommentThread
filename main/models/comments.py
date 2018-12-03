from ..settings import mongoengine as me
import uuid
import hashlib
from datetime import datetime as dt


def enc_password(password):
    salt = hashlib.sha512(password.encode('utf-8'))
    salt.update('qwerty'.encode('utf-8'))
    hashed_password = salt.hexdigest()
    return hashed_password


def generate_token():
    token = uuid.uuid4()
    return token.hex


class Website(me.Document):
    url = me.StringField()
    token = me.StringField(default=generate_token)
    timestamp = me.DateTimeField(default=dt.now)


class Comment(me.Document):
    parent_id = me.StringField()
    text = me.StringField()
    added_by = me.StringField()
    timestamp = me.DateTimeField(default=dt.now)
    comment_id = me.StringField(default=generate_token)


class User(me.Document):
    user_id = me.StringField(default=generate_token)
    username = me.StringField(unique=True, required=True)
    email = me.StringField(unique=True, required=True)
    password = me.StringField(required=True)
    is_active = me.BooleanField(default=False)
