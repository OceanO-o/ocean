# coding=utf-8
import threading
from contextlib import contextmanager

lock = threading.Lock()


@contextmanager
def openlock():
    print('Acquire')
    lock.acquire()
    yield
    print('Releasing')
    lock.release()

with openlock():
    print('Lock is locked: {}'.format(lock.locked()))
    print 'Do some stuff'


@contextmanager
def openlock2():
    print('Acquire')
    with lock: # threading.Lock其实就是个with的上下文管理器.
        # __enter__ = acquire
        yield
    print('Releasing')

with openlock2():
    print('Lock is locked: {}'.format(lock.locked()))
    print 'Do some stuff'

import pymongo

@contextmanager
def operation(database, host='localhost', port=27017):
    db = pymongo.MongoClient(host, port)[database]
    yield db
    db.connection.disconnect()

with operation('test') as db:
    print(db.test.find_one())
