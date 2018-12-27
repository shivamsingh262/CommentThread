from ..models import *
from datetime import datetime as dt
from mongoengine import DoesNotExist
from .middleware import *
from mongoengine.queryset.visitor import Q
from ..settings import *


def save_website(url, user_id):
    try:
        website = Website.objects.get(url=url)
        return None
    except DoesNotExist:
        website = Website()
        website.url = url
        website.added_by = user_id
        website.save()
    return website.token


def save_comment(text, parent_id, user_id):
    comment = Comment()
    comment.text = text
    comment.parent_id = parent_id
    comment.added_by = user_id
    comment.save()
    return comment.comment_id


def get_votes(comment_id):
    votes = Vote.objects(comment_id=comment_id)
    upvotes = sum(1 for x in votes if x['vote_type'] == True)
    downvotes = len(votes) - upvotes
    return upvotes, downvotes


def get_comment(parent_id):
    comments = Comment.objects(parent_id=parent_id)
    data = []
    for comment in comments:
        di = {}
        di['text'] = comment['text']
        di['comment_id'] = comment['comment_id']
        di['added_by'] = comment['added_by']
        di['added_by_name'] = User.objects.get(
            user_id=comment['added_by'])['username']
        di['timestamp'] = dt.strftime(comment['timestamp'], '%Y-%m-%d %H:%M')
        upvotes, downvotes = get_votes(comment['comment_id'])
        di['upvotes'] = upvotes
        di['downvotes'] = downvotes
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


def get_user(user_id):
    try:
        user = User.objects.get(user_id=user_id)
        return user.username
    except DoesNotExist:
        return None


def add_vote(comment_id, vote_type, user_id):
    try:
        vote = Vote.objects.get(comment_id=comment_id, added_by=user_id)
        if vote.vote_type != vote_type:
            vote.vote_type = vote_type
            vote.save()
        else:
            vote.delete()
    except DoesNotExist:
        vote = Vote()
        vote.comment_id = comment_id
        vote.vote_type = vote_type
        vote.added_by = user_id
        vote.save()


def render_page(token):
    website = Website.objects.get(token=token)
    comments = get_comment(token)
    template_var = {'website':website['url'],'comments':comments}
    html_out = main_template.render(template_var)
    return html_out