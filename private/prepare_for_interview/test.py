# class Parent(object):
# 	x = 1
#
# class Child1(Parent):
# 	pass
#
# class Child2(Parent):
# 	pass
#
# print(Parent.x, Child1.x, Child2.x)
#
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
#
#
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)
#
#
#
# def bibao():
# 	local_str = "local"
# 	def inner():
# 		return local_str
# 	return inner
#
# x = bibao()
# print(x())

x = (1, 2, 3)
print(x, type(x))
print(*x, )
print([x for x in range(10)])
pp = (x for x in range(10))
for x in pp:
	print(x)