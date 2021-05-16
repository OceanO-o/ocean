1.flask介绍
    flask是一个轻量级的web框架，它灵活可扩展性强，第三方库全面。架构需要自己设计，这点和django
    有所区别。主要包含了路由功能 ，图片难过blueprint 组织路由，实现应用模块化。依赖两个库，werkzug
    和jinja,jinja实现模板渲染，werkzug提供框架底层的东西，比如在实现上下文时的底层封装。
2.Django和Flask有什么区别？
    flask 轻量级框架，开发大型网站需要自己设计架构，使用orm需要借助sqlalcemy
    django 功能齐全，提供一站式解决方案，自带admin后台管理自带orm.
3.Flask-WTF是什么，有什么特点?
    处理web表单，使用Flask-WTF扩展，它封装了WTForms，有验证表单数据的功能
     Flask-WTF 需要配置参数 SECRET_KEY。CSRF_ENABLED 是为了 CSRF(跨站请求伪造)保护
4.如何在Flask中访问会话?
    from flask import session导入会话对象
5.WSGI
    是Python语言中定义的Web服务器和Web应用程序之间或框架之间的通用接口标准
6.Flask 中请求上下文和应用上下文的区别和作用?
    current_app、g 是应用上下文
    request、session 是请求上下文
    请求上下文:保存了客户端和服务器交互的数据
    应用上下文:flask 应用程序运行过程中，保存的一些配置信息，比如程序名、数据库连接、应用信息等
7.flask上下文
    当用户发起请求线程，在发生请求的过程中，需要创建请求上下文，而创建时先去判断是否存在应用上下文
    也就是通过app_ctx_stack获取栈顶，如果不存在则将一个应用上下文推入栈中(生成一个app_context对象，再
    推入栈中)。此时也将request_ctx_stack推入localstack栈中，他会变成栈顶，request通过localproxy代理
    获取栈顶，即可以拿到上下文请求中的request，就包含这次请求的信息和数据了。
