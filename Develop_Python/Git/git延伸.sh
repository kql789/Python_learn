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