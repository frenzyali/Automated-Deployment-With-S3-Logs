from bottle import get, request, response, HTTPError
from datastore import users
from data.config import Config


@get('/user/current')
def current_user(db):
    cookie_content = request.get_cookie("account", secret=Config.config.cookie_secret)
    if cookie_content:
        current_username = cookie_content['username']
        return users.user_by_username(db, current_username)
    return HTTPError(401, 'Access denied')


@get('/user/<username>')
def user_by_username(db, username):
    cookie_content = request.get_cookie("account", secret=Config.config.cookie_secret)
    if cookie_content:
        current_username = cookie_content['username']
        if users.check_admin(db, current_username):
            return users.user_by_username(username)
    return HTTPError(401, 'Access denied')

