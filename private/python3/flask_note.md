# __name__ 和 __main__
一个python文件通常有两种使用方法，第一是作为脚本直接执行，第二是 import 到其他的 
python 脚本中被调用（模块重用）执行 (https://blog.csdn.net/q2605894893/article/details/82345814)
脚本中 __name__ 的值是 __main__
脚本被其他脚本调用时（在a.py 里面import b.py, b.py里面有一个 if __name__ == "__main__", 则不会执行
 b.py里面的逻辑处理， 此时输出b.__name__ 的值是b，不是main）
 
# host参数 app.run(host="0.0.0.0")
让服务器被公开访问,只要在命令行上简单的加上 --host=0.0.0.0
$ flask run --host=0.0.0.0
这行代码告诉你的操作系统监听所有公开的 IP 

# 路由重定向
@app.route('/projects/')
@app.route('/about')
访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。
也就是你访问时加不加斜杠都不会出错
about 的 URL 没有尾部斜杠，如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误
@app.route('/about') 和 @app.route('/about/')
保证了url的唯一性



