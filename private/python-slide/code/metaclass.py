# coding=utf-8
class Hello(object):

    def __init__(self, func):
        self.func = func

    def hello(self):
        print 'hello world'


def hello(cls):
    print 'hello world'


def __init__(cls, func):
    cls.func = func


class HelloMeta(type):  # 注意继承至type

    def __new__(cls, name, bases, attrs):  # 这个就是前面说的4个必要属性
        def __init__(cls, func):
            cls.func = func

        def hello(cls):
            print 'hello world'
        t = type.__new__(cls, name, bases, dict(
            attrs.viewitems() | [('hello', hello), ('__init__', __init__)]))
        return t  # 要return创建的类哦


class New_Hello(object):
    __metaclass__ = HelloMeta


hellometa = lambda name, parents, attrs: type(
    name,
    parents,
    dict(attrs.items() + [
        ('__new__', classmethod(
         lambda cls, *args, **kargs:
            super(type(cls), cls).__new__(
                *args, **kargs)
         )),
        ('hello', hello),
        ('__init__', __init__)
    ])
)


class New_Hello2(object):
    __metaclass__ = hellometa
