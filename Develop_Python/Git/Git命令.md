# Git命令

# 一、生成秘钥—本机电脑
```shell
ssh-keygen -t rsa -C "zhangsan@126.com"
```
# 二、主机配置
配置本地主机的邮箱和姓名，因为git是分布式版本控制系统，所以每台机器都必须自报家门
```shell
git config --global user.email "zhangsan@126.com"
git config --global user.name "zhangsan"
# 查看所有本机配置
git config -l
# 查看本机配置邮箱
git config user.email
# 查看本机配置名字
git config user.name
```
# 三、四个概念
工作区（Working Directory）
暂存区（index /stage）
本地仓库（Local Repository）
远程仓库(Remote Repository)

工作区(Working Directory)  
工作区是指我们当前正在进行开发工作的目录,在该目录下可以新增、修改和删除文件。工作区是我们平时编写代码的地方，它是我们与Git交互的起点。
说明:任何对象都是在工作区中诞生和被修改

暂存区(Index/Stage/Staging Area)  
暂存区也被称为索引(Index),它是位于.git目录下的一个文件,用于临时存储我们想要提交到Git仓库的文件变动.
在将文件提交到暂存区之前, 我们需要使用git add命令将文件添加到暂存区，这样Git就会跟踪这些文件的变动.不保存实体，通过id指向每个文件实体.
说明: 可以使用 git status查看暂存区的状态.任何修改都是进入暂存区才开始被版本控制。

本地仓库(Local Repository)  
本地仓库是指存储在本地计算机上的Git仓库副本.当我们使用git commit命令将暂存区中的文件变动提交时，这些提交记录会保存在本地仓库中。
本地仓库还包括Git对象数据库和分支信息等.
git commit 后同步index的目录到本地仓库,方便下一步通过git push 同步本地仓库与远程仓库
说明1:只有把修改提交到本地仓库,改修改才能在仓库中留下痕迹。
说明2:可以在任何地方新建本地仓库,只需要在目标目录下执行"git init" 指令，就会将此目录自动初始化为本地仓库，同时他会新建.git目录。

远程仓库(Remote Repository)  
的内容可能被分布在多个地点的处于协作关系的本地仓库修改，因此它可以与本地仓库同步，也可能不同步，但是它的内容是最旧的。
说明:与协作者分享本地的修改，可以把他们push到远程仓库来共享。

# 四、分支管理
```shell
#查看分支,前面带星号的分支表示当前工作分支
git branch
#查看所有分支
git branch -a
#创建分支,说明基于a分之创建b分支，此时b分之会拥有a分之全部内容。在创建b分之时保持a分之"干净"状态。
git branch [branch_name]
#切换到已有分支
git checkout branch_name
#创建一个分支并切换到这个分支上
git checkout -b branch_name
# 合并分支,先切换的父分支上，之后在合并该父分支的子分支
git merge master  #(master为待合并的分支)
#冲突问题是合并分支过程中最为棘手的问题，当分支合并时，原分支和以前的分支发生了变化就会产生冲突，
#当合并分支时添加新的模块（文件），这种冲突可以自动解决，只需要自己决定commit操作即可。
#当合并分支时两个分支值只修改了同一个文件，则需要手动解决冲突.
# 将分支复制合并到其他分支上
git rebase master
#删除分支
git branch -d [branch_name]
```
# 四、日志、删除与恢复
```shell
#从暂存区撤回
git rm --cached <文件>
# 查看提交记录的哈希值
git log
# 若是嫌输出内容太多 可以用:
git log --pretty=oneline #只显示一行
#将暂存区或某个commit 点文件恢复到工作区
git checkout -- [file]
#移动或删除文件
git mv [flle] [path]
git rm [files]
#注意这两个操作会修改工作区内容，同时将操作记录到暂存区

#从暂存区恢复工作区
git resotre --worktree readme.txt
#从master恢复暂存区
git restore --staged readme.txt
#从master同时恢复工作区和暂存区
git restore --source=HEAD --staged --worktree readme.txt
#显示当前项目状态
git status
#提交项目到本地仓库
git commit -m "备注信息"
git diff file
# 回退到上一个版本
git reset --hard HEAD^
# 回退到上100个版本
git reset --hard HEAD~100
# 回退到最新的版本
git reset --hard id
# 查看你的每一条命令
git reflog
```

# 五、标签管理

标签：在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代  
```shell
#创建标签
git tag [tag_name] [commit_id] -m [message]
#说明：commit_id可以不写则默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。
#查看标签列表
git tag 
#查看详细的标签
git show tag_name 
#删除标签
git tag -d tag_name 
```

# 六、工作区管理

```shell
#保护工作区内容,将工作区未提交的修改封存，让工作区回到修改前的状态。
git stash save [message]
#查看封存的工作区，说明：最新保存的工作区在最上面
git stash list
#应用到某个工作区
git stash apply [stash@{n}]
#删除某一个工作区
git stash drop [stash@{n}]
#删除所有保存的工作区
git stash clear
```

# 七、远程仓库管理

```shell
#查看当前绑定的仓库
git remote -v
#删除库地址
git remote remove gitee
#添加远程仓库
git remote add gitee  https://gitee.com/kql789/kqltest.git
#用于本地仓库比远程仓库版本旧时强行推送本地版本,即强制推送
git push --force origin
#推送本地标签到远程
git push origin [tag]
#推送本地所有标签到远程
git push origin --tags
#删除远程仓库标签
git push origin --delete tag [tagname]
#推送本地分支到远程仓库
git push -u origin [local_branch_name]
#删除远程仓库分支
git push origin :[yuancheng_branch_name]
git push origin --delete [yuancheng_branch_name]
#从远程获取代码
git pull

#将远程分支master拉去到本地，作为tmp分支， git fetch origin master:tmp
#区别：
#pull将远程内容直接拉取到本地，并和对应的分支内容进行合并
#fetch将远程分支内容拉去到本地，但是不会和本地对应分值合并，可以自己判断后再使用merge合并

# 本地分支与远程分支进行关联
git branch --set-upstream-to=gitee/远程分支名 本地分支名
# 创建远程分支并关联到远程分支
git push --set-upstream 远程主机名 本地分支名:远程分支名
git push --set-upstream gitee dev1:dev9
# 创建远程分支
# 方法1:直接在远程仓库创建，在本地pull
# 方法2: 语法git push 远程主机名 远程分支名 (注：远程分支名在本地必须存在才可以直接创建并push)

# 将本地分支数据push到远程分支上
git push 远程主机名 本地分支名:远程分支名
git push gitee dev1:dev8
# 如果当前分支与多个主机存在追踪关系，则可以使用 -u 选项指定一个默认主机，这样后面就可以不加任何参数使用git push
git push -u gitee master
# 将本地的master分支推送到gitee主机，同时指定gitee为默认主机，后面就可以不加任何参数使用git push了，
git push -u gitee master 相当于 git branch --set-upstream-to=gitee/master master #将远程仓库gitee的master分支与本地仓库master分支关联 加 git push gitee master）
```

# 八、其他问题汇总
```shell
#删除文件
# 情况一：工作区文件删除，无其他操作
1. rm test.txt
#以下命令可恢复文件
git restore test.txt
# 情况二：工作区文件删除，版本库文件删除
1. rm test.txt
2. git rm test.txt
3. git commit -m "remove test.txt"

# git branch 相关命令
git branch       #查看本地所有分支
git branch -r    #查看远程所有分支
git branch -a    #查看本地和远程所有分支
git branch -d <branchname>   #删除本地分支
git branch -d -r <branchname> #删除远程分支 注：删除之后一定要push  例: git branch -d -r dev2 / git push gitee :dev2
git branch -m oldbranch newbranch #重命名分支 -M 为强制重命名
git branch -vv   #查看本地分支与远程分支的关联情况

# 为什么git比其他版本控制系统设计的优秀？
# 因为Git跟踪并管理的是修改，而非文件。
git diff HEAD -- file 查看工作区和版本库里面最新版本的区别

# 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令
git checkout --file #最新版本： git restore file

# 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令
1. git reset HEAD <file> #就回到了场景1，  最新版本： git restore --staged file
2. 按场景1操作

# 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

情况1:在工作区做了修改，并未添加到暂存区，想撤销工作区的修改，用 git restore file;

情况2:在工作区做了修改，并用git add 添加到了暂存区，未提交；想撤销，分两步，1.先撤销暂存区的修改，用 git restore --staged file, 2.然后参考情况1撤销工作区的修改

情况3:在工作区做了修改,且git add git commit添加并提交了内容,想撤销本次提交，直接用 git reset --hard HEAD^回退版本，即可保证工作区，暂存区，版本库都是上次的内容

# git跟不同的参数，比较不同的区间的版本。
git diff:是查看working tree与index的差别的。
git diff --cached:是查看index与repository的差别的。
git diff HEAD:是查看working tree和repository的差别的。其中：HEAD代表的是最近的一次commit的信息。
综上所述:git diff 后面跟文件名称是是查看工作区（working tree）与暂存区（index）的差别的


git pull 与git clone的区别
git clone 将远程仓库完完整整的克隆下来，本地无需初始化仓库，clone操作是一个从从到有的克隆操作。再次强调无需git clone
git pull 是拉取远程仓库更新到本地仓库的操作，比如仓库仓库里面的文件内容有变化，需要把新内容下载下来，就可以使用git pull命令。事实上，
git pull是相当于从远程仓库获取最新版本，然后在于本地分支merge(合并)

# 场景1：假设项目有以下分支，master、dev1、dev2、dev3、dev4，当前团队处于dev2分支，可能其他团队所属分支dev1或dev2修改了代码，
# 并合并到master分支，当前团队需要从master分支获取最新的代码，合并到本地。
git pull gitee master  # 执行此操作后，master分支的代码将会合并到本地当前分支，即dev2分支

# 场景2 拉取远程仓库指定分支并与本地分支进行,即拉取dev4分支与本地dev2进行合并
git pull gitee master:dev4

# 场景3，可以先下载在合并。先执行git fetch 再执行git merge。
# 这种方式更安全也更符合实际要求，因为可以在merge前，我们可以查看更新情况，根据实际情况再决定是否合并
git fetch  gitee master:dev4
git merge dev4

```

