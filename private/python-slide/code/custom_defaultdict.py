import bisect
from collections import defaultdict


class Mytype(object):
    def __init__(self):
        self._arrs = []
    def insort(self, arr):
        bisect.insort_left(self._arrs, arr)


d = defaultdict(Mytype)
d['l'].insort(1)
d['l'].insort(9)
d['l'].insort(4)
print d['l']._arrs
