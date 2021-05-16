docker和虚拟机技术的不同
    传统虚拟机，虚拟出一条硬件，运行一个完整的操作系统，然后在这个系统上安装和运行软件
    容器内的应用直接运行在宿主机的内容，容器是没有自己的内核的，也没有虚拟我们的硬件，所以就轻便了
    每个容器间是互相隔离，每个容器内都有一个属于自己的文件系统，互不影响
高效的计算资源利用
    Docker是内核级别的虚拟化，可以在一个物理机上可以运行很多的容器实例！服务器的性能可以被压榨到极致
Docker的基本组成
    镜像  容器  仓库
    镜像相当于一个模板
    镜像run起来就形成一个容器，容器理解为就是一个简易的 Linux系统。
为什么Docker比Vm快
    1、docker有着比虚拟机更少的抽象层。由于docker不需要Hypervisor实现硬件资源虚拟化,运行在
    docker容器上的程序直接使用的都是实际物理机的硬件资源。因此在CPU、内存利用率上docker将会在
    效率上有明显优势。
    2、docker利用的是宿主机的内核,而不需要Guest OS。
    GuestOS： VM（虚拟机）里的的系统（OS）;
    HostOS：物理机里的系统（OS）；
    因此,当新建一个 容器时，docker不需要和虚拟机一样重新加载一个操作系统内核。然而避免引导、加
    载操作系统内核是个比较费时费资源的过程，当新建一个虚拟机时，虚拟机软件需要加载GuestOS，返
    个新建过程是分钟级别的。而docker由于直接利用宿主机的操作系统,则省略了这个复杂的过程，因此
    新建一个docker容器只需要几秒钟。
docker常用命令
  镜像命令
    docker version #显示docker的版本信息。
    docker info #显示docker的系统信息，包括镜像和容器的数量
    docker 命令 --help #帮助命令
    镜像命令
        docker images     docker images-aq -a全部 -q只显示id
        docker search     docker search mysql -f=STARS=5000搜索stars大于等于5000的mysql
        docker pull       docker pull mysql[:tag] tag可选项默认latest
        docker rmi        docker rmi -f id    docker rmi -f $(docker images -aq)删除所有镜像
  容器命令
        docker run 镜像id 新建容器并启动
            --name 容器名字     容器名字用来区分容器
            -d 后台方式运行
            -it 使用交互方式运行，进入容器查看内容
            -p 主机端口:容器端口(常用)
            -P(大写) 随机指定端口
            docker run --name my_ubuntu -it ubuntu /bin/bash
        退出容器
            exit # 容器直接退出
            ctrl +P +Q #容器退出时继续运行
        docker ps 
            docker ps -a
            docker ps
            docker ps -aq
            docker ps -n=3
        docker rm 容器id 
            docker rm -f $(docker ps -aq) #删除指定的容器
            docker ps -a -q|xargs docker rm #删除所有的容器
        动和停止容器的操作
            docker start 容器id #启动容器
            docker restart容器id #重启容器
            docker stop 容器id #停止当前正在运行的容器
            docker kill 容器id #强制停止当前容器
  常用其他命令
    后台启动命令  docker run -d ubuntu
    查看日志 
    显示日志 
        -tf #显示日志信息（一直更新）
        --tail number #需要显示日志条数
        docker logs -tf --tail n 容器id 
        docker logs -tf 容器id 
    查看容器中进程信息
        docker top 容器id
    查看镜像的元数据
        docker inspect 容器id
    进入当前正在运行的容器
        docker exec -it 容器id /bin/bash
        docker attach 容器id
        docker exec #进入当前容器后开启一个新的终端，可以在里面操作。（常用）
        docker attach # 进入容器正在执行的终端
    从容器内拷贝到主机上
        docker cp 容器id :/test.py / #拷贝
    查看容器内存情况
        docker stats 容器id 
        docker 启动容器时可以设置内存大小，可以找相关参数
Docker镜像加载原理
    docker的镜像实际上由一层一层的文件系统组成，这种层级的文件系统UnionFS。
    boots(boot file system）主要包含 bootloader和 Kernel, bootloader主要是引导加 kernel,
    Linux刚启动时会加bootfs文件系统，在 Docker镜像的最底层是 boots。这一层与我们典型的
    Linux/Unix系统是一样的，包含boot加載器和内核。当boot加载完成之后整个内核就都在内存中了，此时
    内存的使用权已由 bootfs转交给内核，此时系统也会卸载bootfs。
    rootfs（root file system),在 bootfs之上。包含的就是典型 Linux系统中
    的/dev,/proc,/bin,/etc等标准目录和文件。 rootfs就是各种不同的操作系统发行版，比如 Ubuntu,
    Centos等等
    平时我们安装进虚拟机的CentOS都是好几个G，为什么Docker这里才200M？
        对于精简的OS,rootfs可以很小，只需要包合最基本的命令，工具和程序库就可以了，因为底层直接用
        Host的kernel，自己只需要提供rootfs就可以了。由此可见对于不同的Linux发行版， boots基本是一致
        的，rootfs会有差別，因此不同的发行版可以公用bootfs.
        虚拟机是分钟级别，容器是秒级！
commit镜像
    docker commit 提交容器成为一个新的副本
    # 命令和git原理类似
    docker commit -m="描述信息" -a="作者" 容器id 目标镜像名:[TAG]
    docker commit -a="this is a commit" -m="add webapps app" 容器id tomcat02:1.0
容器数据卷
    什么是容器卷？
    将应用和环境打包成一个镜像！如果数据都在容器中，那么我们容器删除，数据就会丢失！需求：数据可以持久化
    MySQL，容器删除了，删库跑路！需求：MySQL数据可以存储在本地！
    容器之间可以有一个数据共享的技术！Docker容器中产生的数据，同步到本地！
    这就是卷技术！目录的挂载，将我们容器内的目录，挂载到Linux上面！
    docker run -it -v 主机目录:容器内目录 -p 主机端口:容器内端口
    docker run -it -v :/home ubuntu /bin/bash
    这样则会保证容器内外都可修改文件，并且能够同步。无论容器是否停止都会同步停止再启动后依然能看到同样的内容
具名和匿名挂载（容器数据同步到本地防止丢失）
     三种挂载： 匿名挂载、具名挂载、指定路径挂载
        -v 容器内路径 #匿名挂载
        -v 卷名：容器内路径 #具名挂载
        -v /宿主机路径：容器内路径 #指定路径挂载 docker volume ls 是查看不到的
        通过 docker volume ls 查看都有哪些挂载的volume
        docker volume ls查看到后。通过docker volume inspect volume_id 查看具体在那个位置
        docker run -d -P --name nginx05 -v juming:/etc/nginx:rw nginx rw 读写 ro只读
数据卷容器（两个容器同步数据）
    --volumes-from 容器id 通过这种方式让两个容器同步数据，一个容器挂载到另一个容器上去
    多个MySQL同步数据！命名的容器挂载数据卷！
    docker run -d -p 3306:3306 -v /home/mysql/conf:/etc/mysql/conf.d -v
    /home/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name mysql01 mysql:5.7
    docker run -d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=12345 --name mysql02 --volumes-from mysql01 mysql:5.7
    容器一通过具名或者匿名的方式先行挂载一个volume, 即，先把自己的数据目录挂载到主机上的一个
    目录，然后第二个容器--volumes-from直接挂载第一个容器，则相当于第二个容器也把自己的mysql数据目录挂载到和
    第一个容器挂载的相同的主机目录，则实现了数据共享，同步。无论删除哪一个容器，数据都不会丢掉，此时就是有三
    份数据。两个容器各一份，主机上也有一份。
DockerFile 
    # DockerFile常用指令
    FROM # 基础镜像，一切从这里开始构建
    MAINTAINER # 镜像是谁写的， 姓名+邮箱
    RUN # 镜像构建的时候需要运行的命令
    ADD # 步骤，tomcat镜像，这个tomcat压缩包！添加内容 添加同目录
    WORKDIR # 镜像的工作目录
    VOLUME # 挂载的目录
    EXPOSE # 保留端口配置
    CMD # 指定这个容器启动的时候要运行的命令，只有最后一个会生效，可被替代。
    ENTRYPOINT # 指定这个容器启动的时候要运行的命令，可以追加命令
    区别 CMD  ENTRYPOINT https://www.cnblogs.com/sparkdev/p/8461576.html
    ONBUILD # 当构建一个被继承 DockerFile 这个时候就会运行ONBUILD的指令，触发指令。
    COPY # 类似ADD，将我们文件拷贝到镜像中
    ENV # 构建的时候设置环境变量！
Docker 网络（docker容器可以相互通信，veth-pair技术桥接）
    Docker安装完后会自动生成一个虚拟网卡，为docker0. 之后每启动一个docker容器，
    docker就会给docker容器分配一个ip， 而这个容器带来网卡，都是一对对的出现的。
    在宿主机出现一个，而后在容器中也出现一个，相互对应起来。550:eth0@if551
    这就是veth-pair技术
    evth-pair 就是一对的虚拟设备接口，他们都是成对出现的，一端连着协议，一端彼此相连
    正因为有这个特性 veth-pair 充当一个桥梁，连接各种虚拟网络设备的
    总结
    Docker使用的是Linux的桥接，宿主机是一个Docker容器的网桥 docker
Docker两个容器如何不通过ip就能互相ping通
    docker run -link 可以在容器内添加hostname可以通过hostname ping 通，不推荐
    自定义网络
        docker network create --driver bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 mynet
        docker network inspect mynet
        dokcer run -d -P --name server1 --net mynet ubuntu 自定义添加网络启动容器
        dokcer run -d -P --name server2 --net mynet ubuntu 自定义添加网络启动容器
        则server1可以直接通过 ping server2 ping通，而不需要使用ip来ping
Docker两个容器有各自的网络，怎么打通
    docker 容器1  ubuntu1  使用docker run 默认添加网络，网段和docker0一样为 192.18.0.2
    docker 容器2  ubuntu2  使用 mynet 网络 网段为192.168.0.2
    连通就是将 ubuntu1加到 mynet网络，一个容器两个ip 类似与一个公网IP一个内网ip
    docker network connect mynet 容器id 
     # redis + mysql + flask + docker + celery + rabbitmq + python 


Docker进阶
    
Docker Compose
    docker 手动操作，单个容器
    docker compose轻松高效部署管理多个容器微服务，运行多个容器。批量编排
docker compose运行时
    1.创建网络
        这个网络compose_net就和之前mynet一样，让docker所有容器可以直接通过域名访问，不需要通过ip
        （ip会换，当一个mysql挂掉重启一个时ip会换，但域名还是这个）
    2.执行compose ymal  里面的dockerfile生成web服务和容器
    3.启动服务     
docker yaml规则
    3层   # docker-compose up -d后台启动 docker-compose up --build重新构建
    version '' 版本
    service 
        web
            images
            network
            build
        redis
            images
    其他配置
    volumes
    networks
    configs
docker swarm集群
    docker swarm --help
    docker swarm init初始化节点
    docker swarm join-token manager/work 获取work 或 manager 的加入令牌
    docker swarm join --token token 加入集群中一个work或manager
Raft一致性协议
    
        

    
    
