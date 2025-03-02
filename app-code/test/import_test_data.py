from datastore.store import Store
from data.config import Config
import os

test_data_directory = 'test/test_data/'


def import_users(file_name='users.json'):
    users_file = os.path.join(test_data_directory, file_name)
    Store.import_test_data(Config.config, 'users', users_file)


def import_authdata(file_name='authdata.json'):
    authdata_file = os.path.join(test_data_directory, file_name)
    Store.import_test_data(Config.config, 'auth_methods', authdata_file)


def import_things(file_name='things.json'):
    things_file = os.path.join(test_data_directory, file_name)
    Store.import_test_data(Config.config, 'things', things_file)


if __name__ == '__main__':
    print("importing test data...")
    Config()
    Store.migrate_db(Config.config)
    import_users()
    import_authdata()
    import_things()

