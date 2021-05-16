def singleton(cls):
    class deco(cls):
        def __new__(cls, *args, **kwargs):
            o = getattr(cls, "__instance__", None)
            if o is None:
                o = object.__new__(cls)
                cls.__instance__ = o
            return o
    return deco

@singleton
class A(object):
    def common(self):
        print hex(id(self))


a, b = A(), A()
a is b
a.common()
