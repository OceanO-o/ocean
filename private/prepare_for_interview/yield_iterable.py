

# 迭代器 1 1 2 3 5 8 13
# 斐波那契
class Fib(object):
	def __init__(self, max):
		self.a = 0
		self.b = 1
		self.max = max

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a > self.max:
			raise StopIteration
		return self.a

def main():
	fib = Fib(10)
	for i in fib:

		print(i)

# main()


# yield
def yield_fib():
	a, b = 0, 1
	while True:
		yield b
		a, b = b, a+b


def yield_main():
	fib = yield_fib()
	for i in range(10):
		print(next(fib))


# yield_main()
# y =(x for x in range(10))
# print(type(y))












