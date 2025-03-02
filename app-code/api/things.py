from bottle import get
from datastore import things


@get('/things')
def get_things(db):
    return dict(things=things.get_all_things(db))
