from ..models import *


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
