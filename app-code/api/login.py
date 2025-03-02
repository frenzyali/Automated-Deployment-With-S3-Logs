from bottle import post, request, response
from datastore import users
from data.config import Config


@post('/login')
def do_login(db):
    username = request.json.get('username')
    password = request.json.get('password')
    user_id = users.check_login(db, Config.config, username, password)
    user = None
    if user_id > 0:
        user = users.get_user_by_id(db, user_id)
        name = f"{user['firstname']} {user['lastname']}"
        cookie_content = {
            'username': username,
            'client-ip': request.remote_addr,
            'real-name': name
        }
        response.set_cookie("account", cookie_content, secret=Config.config.cookie_secret, max_age=Config.config.session_ttl)

    response.headers['Content-type'] = 'application/json'
    return dict(login_success=user is not None)


@post('/register')
def register(db):
    firstname = request.json.get('firstname')
    lastname = request.json.get('lastname')
    username = request.json.get('username')
    password = request.json.get('password')
    error_msg = None
    if firstname is not None and lastname is not None and username is not None and password is not None:
        if users.user_by_username(db, username) is not None:
            registration_success = False
            error_msg = 'Username is already in use'
        else:
            registration_success = users.create_user(db, Config.config, firstname, lastname, username, password)
            if not registration_success:
                error_msg = 'Some random error occurred'
    else:
        registration_success=False
        error_msg = 'Mandatory information missing'

    response.headers['Content-type'] = 'application/json'
    return dict(registration_success=registration_success,
                error_msg=error_msg)
