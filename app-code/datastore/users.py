import hashlib


def calculate_password_hash(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def create_user(db, config, firstname, lastname, username, password):
    password_hash = calculate_password_hash(config, password)
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count1 = cursor.rowcount
    user_id = cursor.lastrowid

    if row_count1 > 0:
        row_count2 = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count2 > 0:
            return True

    return False


def check_login(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def check_admin(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(user["is_admin"])
    else:
        return False


def get_user_by_id(db, user_id):
    row = db.execute('SELECT * from users where id=?', (user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None


def user_by_username(db, username):
    user_id = user_id_by_username(db, username)
    return get_user_by_id(db, user_id)


def user_id_by_username(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None
