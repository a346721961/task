# git 笔记

标签（空格分隔）： 工具

---
##git 安装
在使用git前要将git安装在你的计算机上。
###Linux 上的安装

>`$ sudo yum install git`
###Mac上安装
>`$ sudo brew install git`
###Windows 上安装
直接git官方网站下载，按指导进行安装，此方法在Mac上也好使。
##进入Git
###1、用户信息
安装好后设置自己的用户名称和邮箱地址，设置完成后不可更改。（每次Git提交都会使用这些信息，共同开发项目时会作为一个身份判断。）
###2、Git使用常用流程

>`$ git init`
初始化git仓库，其本质就是在本文件夹添加以.git子目录作为存储仓库。

>`$ git status`
查看工作目录，查看文件状态

>`$ git add . 和 git add 文件`
对文件进行追踪放入暂存区

>`$ git commit -m '名称'`
>`$git commit -am '名称’`
同为将暂存区文件放到git仓库，但是-m 前不必须要执行git add . 命令。相对于git commit -am ‘名称’，后者可跳过git add操作直接将文件上传git仓库（仅限于已经存在的文件的更改）
git rm 可进行移除
git rm --cached 对暂存区文件操作，以后添加会忽略此文件，git rm -f 文件 会直接删除源文件

>`$git log`
可以查看跟新日志
如果想忽略忽略一些内容可编写配置文件 .gitignore文件
至此：为基本的Git操作
###3.分支操作
git 分支操作

>`$git branch '分支名'`
进行创建新的分支. -v可显示所有分支 -d 进行删除分支操作
>`$git checkout '分支名'`
进行分支切换.
>`$git checkout -b '分支名'`
创建新的分支，并切换到该分支下
####远程分支
1.可直接将copy远程仓库到本地
>`$git clone xxxx`
2.将自己本地仓库和远程进行连接可建立多个连接，远程相当于分支。
>`$ git remote add mingzi git仓库地址`
git push mingzi master
将mingzi分支推送到远程git仓库，并作为其master分支。
git commit、git push、git pull、 git fetch、git merge 的含义与区别

 git commit：是将本地修改过的文件提交到本地库中；
 git push：是将本地库中的最新信息发送给远程库；
 git pull：是从远程获取最新版本到本地，并自动merge；
 git fetch：是从远程获取最新版本到本地，不会自动merge；
 git merge：是用于从指定的commit(s)合并到当前分支，用来合并两个分支；
$ git merge -b  // 指将 b 分支合并到当前分支
git pull 相当于 git fetch + git merge。
