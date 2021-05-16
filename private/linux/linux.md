1.命令
    进程管理
    ps ef 
    ps aux
    top 
    kill
    pgrep nginx
    fg bg 把任务放到前台和后台
    crontab
    系统管理
    uptime
    free -h
    ifconfig
    htop
    iotop
    glances 监控软件
    网络管理
    ping -c 5 www.baidu.com
    netstat 显示网络状态，列出系统上所有套接字连接情况，端口连接情况
    -at 列出所有tcp连接 -tupnl p是pid n是不显示别名 l是监听状态的 u是udp t是tcp
    netstat -tpnl | grep 8000
    示例 netstat -tunlp | grep 8000 得到这个监听8000端口的pid 11378，再用
    ps -ef | grep 11378 | grep -v grep 可以得到这个pid锁对应的是哪个进程服务，例如http.server服务
    lsof 查看打开的文件 lsof -i :22
    traceroute 跟踪路由
    mtr 也是路由跟踪，但可以看到路由丢包率
    iptraf 监控流量 iptraf -ng
    history | head 3