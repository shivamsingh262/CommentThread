from ..settings import mongoengine as me
import uuid
from datetime import datetime as dt


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


class User(me.Document):
    user_id = me.StringField(default=generate_token)
    firstname = me.StringField()
    lastname = me.StringField()
    email = me.StringField()
