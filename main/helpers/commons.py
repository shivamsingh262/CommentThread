from ..models import *
from datetime import datetime as dt


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
