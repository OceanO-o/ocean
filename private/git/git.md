1.提交到暂存区了git diff看不到怎么办
    git diff --cached
2.分支管理
    git checkout -b test 创建并切换到分支test
3.合并分支
    git checkout master
    git merge test
    先切换到最终要合并到的那个分支，分支提前master分支，把test分支合并到master
4.删除分支
    git branch -D test
5.tag标签
    git tag -a ;
    tag 和 release的区别，tag是github的一次提交，是版本库的变更。release可以记录一个版本所对应的
    全部文件以及二进制文件










    