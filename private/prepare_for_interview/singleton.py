

# 重写new方法
class Singleton(object):
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		super(Singleton, self).__init__()


s1 = Singleton()
s2 = Singleton()

if id(s1) == id(s2):
	print("hello we are same.")

# 装饰器模式
def singleton(cls):
	_instance = {}

	def _singleton(*args, **kwargs):
		if cls not in _instance:
			_instance[cls] = cls(*args, **kwargs)
		return _instance[cls]

	return _singleton


# @singleton
class A(object):
	pass


a1 = A()
a2 = A()
print(id(a1), id(a2))


