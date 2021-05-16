# 斐波那契额
    # 未使用生成器
# def fib(num):
#     x, y = 0, 1
#     while num > 0:
#         x, y = y, x+y
#         print(x)
#         num -= 1
#
#
# fib(10)

    # 使用生成器
# def fib(num):
#     x, y = 0, 1
#     while num > 0:
#         x, y = y, x+y
#         yield x
#         num -= 1
#
#
# f = fib(10)
#
#
# def get_fib():
#     for data in f:
#         print(data)
#
#
# get_fib()


# 单例模式
# class Singleton(object):
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         super(Singleton, self).__init__()
#
#
# s1 = Singleton()
# s2 = Singleton()
# print(id(s1), id(s2))


# 计算列表中字符出现的次数
# setdefault(key, 0)   # 存在的话就是那个值，没有的话值是0
# list1 = ["a", "b", "a", "c", "d", "d", "t", "p", "p", "b"]
#
#
# def get_count(list1):
#     count_dict = dict()
#     for key in list1:
#         count_dict[key] = count_dict.setdefault(key, 0) + 1
#     return count_dict
#
#
# count = get_count(list1)
# print(count)

# 也可以这样
# def count2(list_1):
#     import collections
#     count_dict = collections.defaultdict(int)
#     for key in list_1:
#         count_dict[key] += 1
#     return count_dict


# 异步yield
# def framework(logic):
#     try:
#         it = logic()
#         s = next(it)
#         print("[FX] logic: ", s)
#         print("[FX] do something")
#         it.send("async: " + s)
#     except StopIteration:
#          pass
#
# def logic():
#      s = "mylogic"
#      r = yield s
#      print(r)

# >>> framework(logic)
# [FX] logic:  mylogic
# [FX] do something
# async: mylogic
# framework(logic)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        print(self.data)


class SingleList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        list_node = []
        cur = self.head
        while cur:
            cur = cur.next
            list_node.append(cur.data)
        return list_node

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    def find(self):
        pass

    def length(self):
        return len(self.__repr__())

    def delete(self, data):
        if not self.head:
            return
        # 1->2->3
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if cur == self.head:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                break
            else:
                prev = cur
                cur = cur.next

    def insert(self, pos, data):
        if not self.head:
            return
        # 1->2->3

        if pos <= 0:   # 插在头部
            self.add(data)
            return
        if pos >= self.length():  # 插在头部
            self.append(data)
            return

        count = 0
        cur = self.head

        while count < pos - 1:
            count += 1
            cur = cur.next

        node = Node(data)
        node.next = cur.next
        cur.next = node


# def quick_sort(array, left, right):
#     if left >= right:
#         return array
#
#     low = left
#     high = right
#     base = array[left]
#
#     while left < right:
#         while left < right and array[right] >= base:
#             right -= 1
#         array[left] = array[right]
#
#         while left < right and array[left] <= base:
#             left += 1
#         array[right] = array[left]
#     array[right] = base
#
#     quick_sort(array, low, left-1)
#     quick_sort(array, left+1, high)
#     return array
# lists=[30,24,5,58,18,36,12,42,39]
# print(quick_sort(lists, 0, len(lists)-1))


# def giant_ten():
#     # res = list(map(lambda x: x*x, range(1, 6)))
#     # 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数
#     res = [x for x in list(map(lambda x: x*x, range(1, 6))) if x > 10]
#     print(res)




