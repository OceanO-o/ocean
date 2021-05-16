# 利用B修改A的哪个属性，使其成为5
class C(object):
	def __init__(self):
		self.attr1 = 3
		self.attr2 = 4


A = C()
B = "attr1"

setattr(A, B, 5)
print(A.attr1)
# setattr 也可以动态增加属性
setattr(A, "attr3", 6)
print(A.attr3)


#  __slots__
class Slots(object):
	__slots__ = "name", "age"

	def __init__(self, name, age):
		self.name = name
		self.age = age


"使用 __slots__ 来告诉 Python 只给一个固定集合的属性分配空间, 不能动态绑定的属性"
"__slots__ 设置的属性仅对当前类有效，对继承的子类不起效，除非子类也定义了 slots，这样，"
"子类允许定义的属性就是自身的 slots 加上父类的 slots。"

slots = Slots("keke", 24)
slots.job = "computer"
