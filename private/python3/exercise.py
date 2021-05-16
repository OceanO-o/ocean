dic1 = {"test": "dic1"}
dic2 = {"test2": "dic2"}
dic3 = {"test3": "dic3"}


# class ListNode:
#
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#     def __repr__(self):
#         return repr(self.data)
#
#
# class SinglyLinkedList:
#
#     def __init__(self):
#         # 时间复杂度 O(1)
#         self.head = None
#
#     def __repr__(self):
#         # 时间复杂度 O(n)
#         nodes = []
#         curr = self.head
#         while curr:
#             nodes.append(repr(curr))
#             curr = curr.next
#         return'[' + ', '.join(nodes) + ']'
#
#     def prepend(self, data):
#         # 时间复杂度 O(1)
#         self.head = ListNode(data=data, next=self.head)
#
#     def append(self, data):  # 时间复杂度 O(n)
#         if not self.head:
#             self.head = ListNode(data=data)
#             return
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = ListNode(data=data)
#
#     def find(self, key):  # 时间复杂度 O(n)
#         curr = self.head
#         while curr and curr.data != key:
#             curr = curr.next
#         return curr  # Will be None
#
#     def remove(self, key):  # 时间复杂度 O(n)
#         curr = self.head
#         prev = None
#         while curr and curr.data != key:
#             prev = curr
#             curr = curr.next
#         if prev is None:
#             self.head = curr.next
#         elif curr:
#             prev.next = curr.next
#             curr.next = None
#
#
# ls = SinglyLinkedList()
# ls.append(1)
# ls.append(2)
# print(ls.__repr__())
#
# ls.prepend(3)
# print(ls.__repr__())


# class ListNode(object):
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return repr(self.data)
#
#
# class SingleList(object):
#
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         if not self.head:
#             self.head = ListNode(data)
#             return
#         # 1 2
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = ListNode(data)
#
#     def prepend(self, data):
#         tmp = self.head
#         self.head = ListNode(data)
#         self.head.next = tmp
#
#     def remove(self, data):
#         # return None or data
#         # 1 2 3
#         cur = self.head
#         prev = None
#         while cur and cur.data != data:
#             prev = cur
#             cur = cur.next
#         # if prev
#
#
#     def __repr__(self):
#         list_node = []
#
#         cur = self.head
#         while cur:
#             list_node.append(repr(cur))
#             cur = cur.next
#         return '[' + ",".join(list_node) + ']'
#
#
# def g(num):
#     # yield from range(num, 0, -1)
#     # yield from range(num)
#     for key in range(num):
#         yield key
#
# f = g(5)
# for key in f:
#     print(key)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleList(object):

    def __init__(self):
        self.head = None

    def __repr__(self):
        lists = []
        cur = self.head
        while cur:
            lists.append(cur.data)
            cur = cur.next
        return lists

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = Node(data)

    def add(self, data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur

    def insert(self, position, data):
        if position <= 0:
            self.add(data)
            return
        if position >= len(self.__repr__()):
            self.append(data)
            return
        # 1 2 3
        cur = self.head
        index = 0
        while index < position - 1:
            cur = cur.next
            index += 1
        node = Node(data)
        node.next = cur.next
        cur.next = node

    def delete(self, data):
        if data not in self.__repr__():
            return
        # 1 2 3
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if cur == self.head:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return
            else:
                prev = cur
                cur = cur.next


sl = SingleList()
sl.append(1)
sl.append(2)
sl.add(3)
sl.insert(2, 8)
print(sl.__repr__())
sl.delete(8)
print(sl.__repr__())


class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super(Singleton, self).__init__()


def quick_sort(array, left, right):
    if left >= right:
        return array

    low = left
    high = right
    base = array[left]

    while left < right:
        while left < right and array[right] >= base:
            right -= 1
        array[left] = array[right]

        while left < right and array[left] <= base:
            left += 1
        array[right] = array[left]
    array[right] = base

    quick_sort(array, low, left-1)
    quick_sort(array, left+1, high)
    return array


lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
print(quick_sort(lists, 0, len(lists)-1))


