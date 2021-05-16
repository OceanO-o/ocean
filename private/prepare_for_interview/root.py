import os


def judge_root():
	if os.geteuid() == 0:
		print("this is root")
	else:
		print("please run as root")


import copy

ll = [1, 2, 3, [4, 5, 6]]
llp = copy.deepcopy(ll)
print(llp)
#
print(id(ll), id(llp))
ll[0] = 100
print(ll, llp)
#
# ll[3][0] = 100
# print(ll, llp)
print(id(ll[0]), id(llp[0]))

x = 'string'
xp = copy.deepcopy(x)
print(id(x), id(xp))
import sys
print(sys.getrefcount('string'))

xo = copy.deepcopy(x)
print(id(x), id(xo))