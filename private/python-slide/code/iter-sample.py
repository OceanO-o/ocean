class Data(object):
    def __init__(self):
        self._data = []

    def add(self, x):
        self._data.append(x)

    def data(self):
        return iter(self._data)

d = Data()
d.add(1)
d.add(2)
d.add(3)
for x in d.data():
    print(x)

class Data(object):
    def __init__(self, *args):
        self._data = list(args)
        self._index = 0

    def __iter__(self):
        return self

    def next(self):
        if self._index >= len(self._data):
            raise StopIteration()
        d = self._data[self._index]
        self._index += 1
        return d

d = Data(1, 2, 3)
for x in d:
    print(x)

d = Data(1, 2, 3)
it = iter(d)
next(it)
next(it)
