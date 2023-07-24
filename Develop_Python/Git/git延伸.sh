#1. 退回到上一个节点
git reset --hrad HEAD^

#2. 退回到指定的commit_id节点
git reset --hard [commit_id]

#3. 查询所有的操作记录,最上面的为最新记录
git reflog

#4. 创建标签
#标签：在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代
git tag [tag_name] [commit_id] -m [message]
#说明：commit_id可以不写则默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。
git tag #查看标签列表
git show tag_name #查看详细的标签
git tag -d tag_name #删除标签


# 保护工作区
#1. 保护工作区内容,将工作区未提交的修改封存，让工作区回到修改前的状态。
git stash save [message]
#查看封存的工作区，说明：最新保存的工作区在最上面
git stash list
#应用到某个工作区
git stash apply [stash@{n}]
#删除某一个工作区
git stash drop [stash@{n}]
#删除所有保存的工作区
git stash clear


# 分支管理
#定义：分支即每个人在原有代码的基础上建立自己的工作环境，单独开发，互不干扰。完成工作后再进行分支统一合并。

#查看分支情况
git branch #前面带星号的分支表示当前工作分支

#创建分支
git branch [branch_name]
#说明基于a分之创建b分支，此时b分之会拥有a分之全部内容。在创建b分之时保持a分之"干净"状态。

#切换分支
git checkout [branch_name]

#创建一个分支并切换到这个分支上
git checkout -b [branch_name]


#合并分支
git merge [branch_name] #先切换的父分支上，之后在合并该父分支的子分支

#冲突问题是合并分支过程中最为棘手的问题，当分支合并时，原分支和以前的分支发生了变化就会产生冲突，
#当合并分支时添加新的模块（文件），这种冲突可以自动解决，只需要自己决定commit操作即可。
#当合并分支时两个分支值只修改了同一个文件，则需要手动解决冲突.

#删除分支
git branch -d [branch_name]
