# 类变量在子父类中被修改时引起的变化
class Parent(object):
	x = 1

class Child1(Parent):
	pass

class Child2(Parent):
	pass

print(Parent.__dict__)
print(Child1.__dict__)
print(Child2.__dict__)
print(Parent.x, Child1.x, Child2.x)  # 1 1 1
Child1.x = 2
print("---------------")
print(Parent.__dict__)
print(Child1.__dict__)
print(Child2.__dict__)
print(Parent.x, Child1.x, Child2.x)  # 1 2 1
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)  # 3 2 3
# 在Python 中，类变量在内部是作为字典处理的如果一个变量的名字没有在当前类的字典中发现，
# 将搜索祖先类（比如父类）直到被引用的变量名被找到
# (如果这个被引用的变量名既没有在自己所在的类又没有在祖先类中找到，会引发一个AttributeError 异常
# 父类中设置x = 1 会使得类变量 x 在引用该类和其任何子类中的值为 1
# 如果任何它的子类重写了该值（例如，我们执行语句 Child1.x = 2 ），然后，该值仅仅在子类中被改变。
# 如果该值在父类中被改变（例如，我们执行语句Parent.x = 3 ），这个改变会影响到任何未重写该值的子类当中的值



# class Parent(object):
# 	x = 1
#
# class Child1(Parent):
# 	pass
#
# class Child2(Parent):
# 	pass
#
# child1 = Child1()
# parent = Parent()
#
# print(type(child1) == type(Child1()))
# print(isinstance(child1, Child1))
#
# print(type(child1) == type(parent))
# print(isinstance(child1, Parent))

class A:
	def __init__(self):
		self.a = 1
		self.b = 2

# print(A.__dict__)
setattr(A, 'c', 3)
print(A.__dict__)
a1 = A()
print(a1.__dict__)
print(a1.c)
# print(a1.__dict__)

# print(A.__dict__)
# a = A()
# print(a.__dict__)
# print(a.c)
