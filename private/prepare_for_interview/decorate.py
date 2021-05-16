import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log("hello")
# def test(a="world"):
#     print("in test ...")
#     print(a)
#
#
# test()


def my_deocrate(text):
    def decorate(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print("in decorate inner ...")
            print("{}, {}".format(text, func.__name__))
            return func(*args, **kwargs)
        return inner
    return decorate

@my_deocrate("my deocrate ...")
def test1(a="main"):
    print(a)

# test1()


def out1(func):
    def inner(*args, **kwargs):
        print("this is add log")
        return func(*args, **kwargs)
    return inner

@out1
def hello1():
    print("hello1 ...")

hello1()

def out2(text):
    def middle(func):
        # @functools.wraps(func)
        def inner(*args, **kwargs):
            print("this is add {} log".format(text))
            print(func.__name__)
            return func(*args, **kwargs)
        return inner
    return middle


@out2("out2")
def hello2():
    print("hello2 ...")

hello2()
