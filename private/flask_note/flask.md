1.flask配置文件加载
    config.py为配置文件
    app.config.from_object('settings')
    或 
        import settings
        app.config.from_object(settings)
2.唯一url
    当路由为/flask/ 时，键入flask或flask/都可以。flask时会301会重定向到flask/
    当路由为/flask时，键入flask/则报错
3.http方法
    get head获取头信息 post put delete options获取资源支持的所有http方法 patch局部更新
3.response
    直接返回response对象
    字符串，此时会将字符串作为主体，状态码为200，MIME为text/html返回，及（str, 200, text/html）
    元组，形式为 (response, status, headers)
4.路由原理
    url - endpoint - view_func
    注册url时，会建立一个url到endpoint的一个映射，如果没有显式添加endpoint，endpoint就是字符串view_func
    之后，endpoint又建立一个到view_func的一个映射。此时两个字典中便可找到url注册上的view是哪个
5.蓝图
    蓝图要注册在核心对象app里面
    拆分文件
6.sqlalchemy
    初始化后注册到app上
7.应用和请求上下文
    当一个请求到达flask时，先去查找是否有app存在于栈中，
    不存在则先推入栈，然后将一个request对象也推入栈中。
8.request 线程隔离
    多个请求都是request,如何区分每一个线程对应的参数
    可以设计一个request字典，request = {thread1: {key: value}, thread2: {key2: value2}}
    每个请求都有一个键。线程隔离
    werkzug.local 封装了 Local，用来线程隔离
    意义：
        使用线程隔离使当前线程能够正确引用到他自己所创建的对象，而不是引用到其他对象
        所创建的对象。    对象是保存状态的地方
9.代码没有面向对象
    描述特征（类变量，实例变量）
    行为方法
    json.dumps(books, default=lambda o:o.__dict__)
10.单页面和网站的区别
    
11.可调用对象
    实现了__call__方法的类， return res = Res()
    class Res()
        def __call__:
            pass 
    简化对象方法的调用 a.func()   ---- a()
    模糊了对象和函数的区别 
        def test(callable):
            callable()是函数就完事了，如果callable是个类，那么就要用class.func() 即callable.func()
            但你不知道callable传进来到底是个啥，所以把类携程callable,就模糊了区别


    
    
    
    
    