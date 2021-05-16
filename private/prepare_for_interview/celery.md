1.简介
    Celery是一个专注于实时处理和任务调度的分布式任务队列
2.celery场景
    1. Web应用。当用户触发的一个操作需要较长时间才能执行完成时，
    可以把它作为任务交给Celery去异步执行，执行完再返回给用户。
    这段时间用户不需要等待，提高了网站的整体吞吐量和响应时间。
    2. 定时任务。生产环境经常会跑一些定时任务。假如你有上千台的服务器、
    上千种任务，定时任务的管理很困难，Celery可以帮助我们快速在不同的机器设定不同种任务。
    3. 同步完成的附加工作都可以异步完成。比如发送短信/邮件、推送消息、清理/设置缓存等。
3.Celery的架构
    beat work broker produce resultbackend
    beat用来创建定时任务
    produce发起任务
    消息发给消息代理broker rabbitmq redis
    work是执行任务的消费者
4.指定队列
    指定队列名和routing key
5.任务调度器
    CELERYBEAT_SCHEDULE 
    启动beat celery beat -A projb
    启动work celery -A proj worker -l info
6.任务绑定、记录日志和重试
    @app.task(bind=True) 
    第一个参数是self，使用self.request访问相关的属性
7.子任务
    signature add.signature()
    chain group chord chunk
    