1.什么是Redis？
    Redis本质上是一个Key-Value类型的内存数据库，整个数据库统统加载在内存当中进行操作.
    redis支持string set hash sortset list等数据结构，redis可以设置过期时间。
    Redis的主要缺点是数据库容量受到物理内存的限制，不能用作海量数据的高性能读写
1.Redis数据结构：        
    String，Hash，List，Set， Sortsort
2.Redis和mysql数据怎么保持数据一致的？
    不管是先写MySQL数据库，再删除Redis缓存；还是先删除缓存，再写库，都有可能出现数据不一致的情况
    1.如果删除了缓存Redis，还没有来得及写库MySQL，另一个线程就来读取，发现缓存为空，则去数据库中
    读取数据写入缓存，此时缓存中为脏数据。
    2.如果先写了库，在删除缓存前，写库的线程宕机了，没有删除掉缓存，则也会出现数据不一致情况。
    异步更新缓存(基于订阅binlog的同步机制)> 读取binlog后分析 ，利用消息队列,
    推送更新各台的redis缓存数据。这样一旦MySQL中产生了新的写入、更新、删除等操作，
    就可以把binlog相关的消息推送至Redis，Redis再根据binlog中的记录，对Redis进行更新。
    其实这种机制，很类似MySQL的主从备份机制，因为MySQL的主备也是通过binlog来实现的数据一致性。
    这里可以结合使用canal(阿里的一款开源框架)，通过该框架可以对MySQL的binlog进行订阅，
    而canal正是模仿了mysql的slave数据库的备份请求，使得Redis的数据更新达到了相同的效果。
    当然，这里的消息推送工具你也可以采用别的第三方：kafka、rabbitMQ等来实现推送更新Redis!
3. 使用过Redis分布式锁么，它是什么回事？
    先拿setnx来争抢锁，抢到之后，再用expire给锁加一个过期时间防止锁忘记了释放。
    如果在setnx之后执行expire之前进程意外crash或者要重启维护了，那会怎么样？
    setnx和expire合成一条指令来用的, jedis.set(String key, String value, 
    String nx, String expx, int time)执行上面的set()方法就只会导致两种结果：
    1. 当前没有锁（key不存在），那么就进行加锁操作，并对锁设置个有效期，同时value表示加锁的客户端。
    2. 已有锁存在，不做任何操作。
4.说说Redis哈希槽的概念？
    一致性哈希： 而一致性Hash算法是对2^32取模， 一致性Hash算法将整个哈希值空间组织成一个虚拟的圆环。
    Redis 集群有16384个哈希槽,每个key通过CRC16校验后对16384取模来决定放置哪个槽.
    集群的每个节点负责一部分hash槽。这种结构很容易添加或者删除节点，并且无论是添加删除或者
    修改某一个节点，都不会造成集群不可用的状态。
5.MySQL里有2000w数据，redis中只存20w的数据，如何保证redis中的数据都是热点数据？
    redis内存数据集大小上升到一定大小的时候，就会施行数据淘汰策略。
    尝试回收最少使用的键（LRU），  回收在过期集合的键，并且优先回收存活时间（TTL）较短的键， 
    回收随机的键使得新添加的数据有空间存放。
6.Redis中的管道有什么用？
    一次请求/响应服务器能实现处理新的请求即使旧的请求还未被响应。这样就可以将多个命令发送到服务器，
    而不用等待回复，最后在一个步骤中读取该答复。 pipeline方式打包命令发送，redis必须在处理完所有
    命令前先缓存起所有命令的处理结果。打包的命令越多，缓存消耗内存也越多。
7.redis事务相关的命令有哪几个？
    redis事务本质是一组命令的集合。redis事务就是一次性、顺序性、排他性的执行一个队列中的一系列命令
    没有隔离，不保证原子性
    watch监视一个或多个key，被监视的key被修改则事务被打断  类似乐观锁
    multi 标记一个事务块的开始 
    exec执行所有事务块的命令，exec执行后取消锁
    discard 取消事务
    unwatch 取消所有watch对key的监控
    乐观锁 悲观锁
8.Redis key的过期时间和永久有效分别怎么设置？
    EXPIRE和PERSIST命令。
10.Redis相比memcached
    都是内存数据库
    redis支持丰富的数据类型，memcache仅仅支持string
    redis可以做持久化，有rdb和aof两种方式
    redis最大可以达到1GB，而memcache只有1MB
    redis是单线程的，memcache是多线程的
    避免了不必要的上下文切换和竞争条件，也不存在多进程或者多线程导致的切换而消耗 CPU，
    不用去考虑各种锁的问题，不存在加锁释放锁操作，没有因为可能出现死锁而导致的性能消耗；
11.Redis两种持久化方式
    RDB
    指定的时间间隔内将内存中的数据集快照写入磁盘，也就是Snapshot快照，恢复时将快照文件直接读到内存里。
    Redis会单独创建fork一个子进程来进行持久化，会先将数据写入到一个临时文件中，待持久化过程
    都结束了，再用这个临时文件替换上次持久化好的文件
    命令save或者是bgsave
    save时只管保存，其他不管，全部阻塞
    bgsave，Redis会在后台异步进行快照操作，快照同时还可以响应客户端请求。可以通过lastsave
    命令获取最后一次成功执行快照的时间。
    如何恢复
    将备份文件（dump.rdb）移动到redis安装目录并启动服务即可
    缺点
    在一定间隔时间做一次备份，所以如果redis意外down掉的话，就会丢失最后一次快照后的所有修改
    Fork的时候，内存中的数据被克隆了一份，大致2倍的膨胀性需要考虑。
    AOF
    以日志的形式来记录每个写操作，将Redis执行过的所有指令记录下来（读操作不记录），只许追加文件
    但不可以改写文件，redis启动之初会读取该文件重新构建数据，换言之，redis重启的话就根据日志文件
    的内容将写指令从前到后执行一次以完成数据的恢复工作
    Rewrite
    AOF 采用文件追加方式，文件会越来越大，为避免出现此种情况，新增了重写机制，当AOF文件的大小
    超过所设定的阈值时，Redis 就会启动AOF 文件的内容压缩，只保留可以恢复数据的最小指令集，可以
    使用命令 bgrewriteaof
    同步策略
    每次修改同步   每秒同步    不同步
    缺点
    相同数据集的数据，aof文件远大于rdb方式，回复速度慢于rdb
    aof运行效率要慢于rdb
12.Redis高可用的可选方案
    主从复制 哨兵模式   
    Redis Master-Slave + Keepalived + VIP。
    这是很经典的db架构，也可以用与mysql的主从切换。基本原理是：Keepalive通过脚本检测master的存活，
    然后通过漂移VIP（Virtual IP）完成主从切换。
    Keepailived有一台主服务器和多台备份服务器，在主服务器和备份服务器上面部署相同的服务配置，
    使用一个虚拟IP地址对外提供服务，当主服务器出现故障时，虚拟IP地址会自动漂移到备份服务器。
13.缓存
    1.缓存穿透，直接把请求打到后台数据库
    布隆过滤器，缓存空对象
    2.缓存击穿 热点数据key在失效的瞬间，持续的大并发就穿破缓存，直接请求数据库
    设置热点数据永不过期,加互斥锁
    3.缓存雪崩 缓存雪崩，是指在某一个时间段，缓存集中过期失效（不可怕）。节点宕机（可怕）
    redis高可用 限流降级 数据预热

   
   