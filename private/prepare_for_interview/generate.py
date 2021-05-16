

# 改写成生成器的方法，使for循环输出同样的结果

def gensquares(N):
    res = []
    for i in range(N):
        res.append(i*i)
    return res


def new_gen(N):
    for i in range(N):
        yield i*i

for item in new_gen(5):
    print(item)
