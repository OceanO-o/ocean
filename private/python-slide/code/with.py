import pymongo


class Operation(object):
    def __init__(self, database, host='localhost', port=27017):
        self._db = pymongo.MongoClient(host, port)[database]

    def __enter__(self):
        return self._db

    def __exit__(self, *args):
        self._db.connection.disconnect()

with Operation(database='test') as db:
    print db.test.find_one()
