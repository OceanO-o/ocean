1.什么是docker
    docker是一个容器化平台，它可以将应用打包为一个容器，应用在容器中独立运行
2.docker与虚拟机的不同
    传统虚拟机，虚拟出一条硬件，运行一个完整的操作系统，然后在这个系统上安装和运行软件
    容器内的应用直接运行在宿主机的内容，容器是没有自己的内核的，也没有虚拟我们的硬件，所以就轻便了
    每个容器间是互相隔离，每个容器内都有一个属于自己的文件系统，互不影响
3.docker运行的几种状态
    运行、已暂停、重新启动、已退出
4.Dockerfile中最常见的指令
    FROM MAINTAINER RUN ADD WORKDIR VOLUME EXPOSE # 保留端口配置
    CMD # 指定这个容器启动的时候要运行的命令，只有最后一个会生效，可被替代。
    ENTRYPOINT # 指定这个容器启动的时候要运行的命令，可以追加命令
    ONBUILD # 当构建一个被继承 DockerFile 这个时候就会运行ONBUILD的指令，触发指令。
    COPY # 类似ADD，将我们文件拷贝到镜像中
    ENV # 构建的时候设置环境变量！
5.Dockerfile中的命令COPY和ADD命令有什么区别
    copy仅支持将本地文件copy到容器中，add可以将本地tar文件提取到镜像当中
6.什么是docker镜像
    docker的镜像实际上由一层一层的文件系统组成，这种层级的文件系统UnionFS
7.Docker使用工作流程
    通过编写dockerfile添加docker命令构建docker镜像容器
    通过docker compose运行dockerfile运行容器
8.生产中监控Docker
    docker stats时，我们获得容器的CPU，内存使用情况
    docker top 容器id
    docker ps查看正在运行的容器
    docker exec或attach进入容器查看
9.容器与主机之间的数据拷贝命令
    容器到主机 docker cp 容器id :/test.py / #拷贝
10.启动nginx容器（随机端口映射），并挂载本地文件目录到容器html的命令
    docker run -P -d --name my-nginx -v /local:/usr/local/ 容器id
11.dockerfile的ONBUILD指令
    当镜像用作另一个镜像构建的基础时，ONBUILD指令向镜像添加将在稍后执行的触发指令
12.什么是docker Swarm
    Docker Swarm是docker的本地群集
镜像
1.批量清理临时镜像文件？
    docker rmi -f $(docker images -qa)
2.如何查看镜像支持的环境变量
    docker run IMAGE env
3.本地的镜像文件都存放在哪里
    /var/lib/docker/目录下，其中container目录存放容器信息，graph目录存放镜像信息，aufs目录下存放具体的镜像底层文件
4.构建docker镜像应该遵循哪些原则？
    整体原则上，尽量保持镜像功能的明确和内容的精简，要点包括:
    尽量选取满足需求但较小的基础系统镜像，建议选择debian:wheezy镜像，仅有86MB大小。
    清理编译生成文件、安装包的缓存等临时文件。
    安装哥哥软件时候要指定准确的版本号，并避免引入不需要的依赖。
    从安全的角度考虑，应用尽量使用系统的库和依赖。
    使用dockerfile创建镜像时候要添加.dockerignore文件或使用干净的工作目录
容器
1.容器退出后，通过docker ps命令查看不到，数据会丢失么？
    容器退出后会处于终止（exited）状态，此时可以通过docker ps -a查看，其中数据不会丢失，
    还可以通过docker start来启动，只要删除容器才会清除数据。
2.如何停止所有正在运行的容器
    docker kill $(docker ps -qa)
3.如何清理批量后台停止容器
    docker rm$(docker ps -aq)
4.如何临时退出一个正在交互的容器的终端，而不终止它
    Ctrl+P+Q
5.很多应用容器都是默认后台运行的，怎么查看他们的输出和日志信息
    docker logs -tf 容器id
6.使用docker port命令映射容器的端口时，系统报错Error：NO public port ‘80’ published for …,是什么意思？
    创建镜像时dockerfile要指定正确的EXPOSE的端口，容器启动时指定PublishAllport=true
7.可以在一个容器中同时运行多个应用进程吗？
    一般不推荐在用以容器内运行多个应用进程，如果有类似需求，可以用过额外的进程管理机制，
    比如supervisord来管理所运行的进程
8.如何控制容器占用系统资源（CPU，内存）的份额？
    在使用docker create命令创建容器或使用docker run 创建并运行容器的时候，
    可以使用-c|-spu-shares[=0]参数来调整同期使用SPU的权重，使用-m|-memory参数来调整容器使用内存的大小。
其他
1.Docker的配置文件放在那里。如何修改配置
    Ubuntu系统下Docker的配置文件是/etc/default/docker,CentOS系统配置文件存放在/etc/sysconfig/docker
2.如何更改docker的默认存储设置
    Docker的默认存放位置是/var/lib/docker，如果希望将docker的本地文件存储到其他分区，
    可以使用Linux软连接的方式来做




