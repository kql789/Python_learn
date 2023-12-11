#!/bin/bash

# 使用Shell结合Pytho迁移的相关命令，使其每次更新自动进行迁移
# 设置虚拟环境的地址
virtualenv_path="/root/.virtualenvs/shubiao"

echo "进入虚拟环境!"

#激活虚拟环境
source "$virtualenv_path/bin/activate"

if [[ "$VIRTUAL_ENV" == *shubiao* ]]; then
        echo "当前虚拟环境: $(basename $VIRTUAL_ENV)"
        python manage.py makemigrations
        python manage.py migrate
        python manage.py collectstatic --noinput

else
        echo "错误:未进入shubiao 虚拟环境"

fi

#退出虚拟环境
deactivate

echo "退出虚拟环境!"
echo "Migrate Successful!"