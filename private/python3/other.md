# 既 REST，何 RPC ？
在 OpenStack 里的进程间通信方式主要有两种，一种是基于HTTP协议的RESTFul API方式，
另一种则是RPC调用。

RESTFUL 主要用于各组件之间的通信（如nova与glance的通信），或者说用于组件对外提供调用接口
    REST 是服务端把方法写好，客户端并不知道具体方法。客户端只想获取资源，所以发起HTTP请求，
    而服务端接收到请求后根据URI经过一系列的路由才定位到方法上面去
RPC 则用于同一组件中各个不同模块之间的通信如nova组件中nova-compute与nova-scheduler的通信
    PRC是服务端提供好方法给客户端调用，客户端需要知道服务端的具体类，具体方法，然后像调
    用本地方法一样直接调用它。
    (由于组件内部是分布式部署，所以使用远程过程调用，而组件之间除了给各个组件提供
    api服务外，也提供给外界可访问的接口，所以使用rest api)
在 OpenStack 中，rpc client 不直接 rpc 调用 rpc server ，而是先把 rpc 调用请求发给 
RabbitMQ ，再由订阅者（rpc server）来取消息,OpenStack 组件繁多，在一个较大的集群内部
每个组件内部通过rpc通信频繁，如果都采用rpc直连调用的方式，连接数会非常地多，开销大，
若有些 server 是单线程的模式，超时会非常的严重。避免超时和消息丢失，使用消息队列。

# WSGI 是什么，因何而生？
它是 Python应用程序（application）或框架（如 Django）和 Web服务器之间的一种协议，一种规范
常见的web应用框架有：Django，Flask等
常用的web服务器软件有：uWSGI，Gunicorn等
https://juejin.im/post/5cff300a6fb9a07ef06f8a43#heading-1

# 单例模式：
全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用；
由于单例模式要求在全局内只有一个实例，因而可以节省比较多的内存空间；
单例可长驻内存，减少系统开销。


 
 
 
 