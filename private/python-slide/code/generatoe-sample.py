class Data(object):
    def __init__(self, *args):
        self._data = list(args)
    def __iter__(self):
        for x in self._data:
            yield x

d = Data(1, 2, 3)
for x in d:
    print(x)
