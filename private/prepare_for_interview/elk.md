file_beats  --> 配置日志目录收集日志  
-->  logstash --> 过滤日志
        --> elasticsearch -->  文档存储以及索引
           --> kibana  --> 可视化界面

Elasticsearch:
它提供了

一套简单一致的 RESTful API 来实现存储和检索
在 Elasticsearch 中有几个基本的概念，如节点、索引、文档节点  --> 单个Elasticsearch实例为一个节点，多个节点组成一个集群
索引  --> 相当于MySQL里面的数据库
文档  --> 
Relational DB -> Databases -> Tables -> Rows -> Columns
Elasticsearch -> Index -> Types -> Documents -> Fields    