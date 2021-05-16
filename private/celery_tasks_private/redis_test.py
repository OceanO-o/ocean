import redis

# 连接数据库
r = redis.Redis(host='192.168.60.137', port=6379, db=0)
# 使用连接池连接数据库。这样就可以实现多个Redis实例共享一个连接池
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
# r = redis.Redis(connection_pool=pool)

# =============================1、String 操作===============================

#在Redis中设置值，默认不存在则创建，存在则修改
r.set('name', 'zhangsan')