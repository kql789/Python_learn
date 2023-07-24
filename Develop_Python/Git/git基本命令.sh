Git 命令大全

# 生成秘钥——本机电脑
ssh-keygen -t rsa -C "zhangsan@126.com"

# 配置本地主机的邮箱和姓名，因为git是分布式版本控制系统，所以每台机器都必须自报家门
git config --global user.email "zhangsan@126.com"
git config --global user.name "zhangsan"

# 查看所有本机配置
git config -l
# 查看本机配置邮箱
git config user.email
# 查看本机配置名字
git config user.name

#查看当前绑定的仓库
git remote -v
#删除库地址
git remote remove gitee
git remote add gitee  https://gitee.com/kql789/kqltest.git  添加新的仓库地址
git commit -m "init"  仓库初始化
git push gitee 上传仓库
git remote add gitee https://gitee.com/kql789/custom-signal.git
git commit 提交记录

# 创建一个新的分支
git branch bigFix
# 切换到新的分支上
git checkout bigFix
git commit
# 合并分支
git merge master (master 为待合并的分支)
# 将分支复制合并到其他分支上
git rebase master
#从暂存区撤回
git rm --cached <文件>
# 查看提交记录的哈希值
git log --pretty=oneline #只显示一行
#查看分支
git branch
#切换到已有分支
git checkout 分支名
#切换到还未建立的分支
git checkout -b 新分支名
#显示当前项目状态
git status
#提交项目到本地仓库
git commit -m "备注信息"
#将本地仓库分支推送到远程仓库并建立分支
git push -u origin 分支名
#更新分支（合并分支）
git merge 分支名
#强制推送到远程仓库
git push --force gitee master
# 创建一个新的分支
git branch bigFix
# 切换到新的分支上
git checkout bigFix
git commit
# 合并分支
git merge master (master 为待合并的分支)
# 将分支复制合并到其他分支上
git rebase master
# 查看提交记录的哈希值
git log
# 相对引用使用 ^ 向上移动1个提交记录 使用^<num> 向上移动多个提交记录，如^3
# 查看修改后的内容
git diff file
# 若是嫌输出内容太多 可以用:
git log --pretty=oneline
# 回退到上一个版本
git reset --hard HEAD^
# 回退到上100个版本
git reset --hard HEAD~100
# 回退到最新的版本
git reset --hard id
# 查看你的每一条命令
git reflog

#比较工作区文件和仓库文件差异
git diff [file]
#将暂存区或某个commit 点文件恢复到工作区
git checkout -- [file]

#移动或删除文件
git mv [flle] [path]
git rm [files]
#注意这两个操作会修改工作区内容，同时将操作记录到暂存区

# 为什么git比其他版本控制系统设计的优秀？
# 因为Git跟踪并管理的是修改，而非文件。
git diff HEAD -- file 查看工作区和版本库里面最新版本的区别

# 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令
git checkout -- file #最新版本： git restore file

# 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令
git reset HEAD <file> #就回到了场景1，  最新版本： git restore --staged file
# 第二步按场景1操作。

# 场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

# 情况1：在工作区做了修改，并未添加到暂存区，想撤销工作区的修改，用 git restore file;

# 情况2：在工作区做了修改，并用git add 添加到了暂存区，未提交；想撤销，分两步，1.先撤销暂存区的修改，用 git restore --staged file, 2.然后参考情况1撤销工作区的修改；

# 情况3：在工作区做了修改，且git add git commit添加并提交了内容，想撤销本次提交，直接用 git reset --hard HEAD^回退版本，即可保证工作区，暂存区，版本库都是上次的内容


#从暂存区恢复工作区
git resotre --worktree readme.txt
#从master恢复暂存区
git restore --staged readme.txt
#从master同时恢复工作区和暂存区
git restore --source=HEAD --staged --worktree readme.txt

#删除文件
# 情况一：工作区文件删除，无其他操作
1. rm test.txt
#以下命令可恢复文件
git restore test.txt

# 情况二：工作区文件删除，版本库文件删除
1. rm test.txt
2. git rm test.txt
3. git commit -m "remove test.txt"


# 至此文件上传至仓库成功
# 要明白这3个概念，工作区（working tree），暂存区（index /stage），本地仓库（repository）
# git跟不同的参数，比较不同的区间的版本。
# git diff：是查看working tree与index的差别的。
# git diff --cached：是查看index与repository的差别的。
# git diff HEAD：是查看working tree和repository的差别的。其中：HEAD代表的是最近的一次commit的信息。
#   综上所述：git diff 后面跟文件名称是是查看工作区（working tree）与暂存区（index）的差别的
git remote add origin git@gitee.com:kql/learntest.git
# 本地分支与远程分支进行关联
# 本地有分支，远程也有分支如下：
git branch --set-upstream-to=origin/远程分支名 本地分支名
# 本地有分支，远程没有分支
git push origin 本地分支名   #创建远程分支名
git branch --set-upstream-to=origin/远程分支名  #关联远程分支













