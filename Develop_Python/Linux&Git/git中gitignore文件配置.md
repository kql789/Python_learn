## .gitignore的配置

**注意:**

.gitignore最好放在根目录中。如果gitignore放在被忽略的父目录中，那忽略文件就无法生效。

## 1.1 .gitignore使用规则

.gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。即.gitignore文件需要再做git版本控制前就创建好，才能实现忽略文件的功能。  

如果已经做了版本控制的代码，需要在中途添加.gitignore文件，那么.gitignore文件是无效的，即不起作用。具体方式就是先把本地缓存删除(改变成未track状态)，具体方法如下： 
```shell
#第一步,保证git status是干净状态

#第二步,清除缓存,在根目录下输入下面命令（注意：不要忘记“.”）
git rm -r --cached .

#第三步,添加所有文件
git add .

# 第四步,提交更新
git commit -m 'xxxxxx'

# 第五步,推送远程仓库
git push origin(远程仓库名)
```

## 1.2 Git忽略规则匹配语法
```shell

空格不匹配任意文件，可作为分隔符，可用反斜杠转义
开头的文件标识注释，可以使用反斜杠进行转义
# 表示用于注释一段内容
! 不忽略指定的文件或者文件夹，如：!readme.md，不忽视readme.md文件以及不忽略每个migrations文件夹下的__init__.py文件
/ 斜杠在后(结束模式)：匹配项目跟目录，如：name/，则表示无指定路径下在名为name的文件夹。即只匹配文件夹以及在该文件夹路径下的内容，但是不匹配该文件。
/ 斜杠在前(开始模式)：匹配项目跟目录，如：/name，则表示指定路径下的名为name的文件或者文件夹。即匹配项目跟目录，如果一个模式不包含斜杠，则它匹配相对于当前 .gitignore 文件路径的内容，如果该模式不在 .gitignore 文件中，则相对于项目根目录
** 匹配多级目录，可在开始，中间，结束。
? 通用匹配单个字符，匹配除 / 外的任意一个字符
* 通用匹配零个或多个字符，如：*.log ,忽视所有后缀为.log的文件
[] 通用匹配单个字符列表
```

## 1.3 常用匹配示例 

```shell
bin/: 忽略当前路径下的bin文件夹，该文件夹下的所有内容都会被忽略，但是不忽略bin文件。
/bin: 忽略根目录下的bin文件
/*.c: 忽略cat.c,不忽略build/cat.c
debug/*.obj: 忽略debug/io.obj，不忽略 debug/common/io.obj 和tools/debug/io.obj
**/foo: 忽略/foo.a/foo,a/b/foo等
a/**/b: 忽略a/b,a/x/b,a/x/y/b等
!/bin/run.sh: 不忽略bin目录下的run.sh文件
*.log: 忽略所有的.log文件
config.php:忽略当前路径下的config.php文件

```

## 1.4 Python Django框架常用配置
```shell
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
 
# C extensions
*.so
 
# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
 
# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec
 
# Installer logs
pip-log.txt
pip-delete-this-directory.txt
 
# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/
 
# Translations
*.mo
*.pot
 
# Django stuff:
*.log
zero_demo/local_settings.py
db.sqlite3
db.sqlite3-journal
 
# Flask stuff:
instance/
.webassets-cache
 
# Scrapy stuff:
.scrapy
 
# Sphinx documentation
docs/_build/
 
# PyBuilder
.pybuilder/
target/
 
# Jupyter Notebook
.ipynb_checkpoints
 
# IPython
profile_default/
ipython_config.py
 
# pdm
.pdm.toml
 
# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/
 
# Celery stuff
celerybeat-schedule
celerybeat.pid
 
# SageMath parsed files
*.sage.py
 
# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
 
# Spyder project settings
.spyderproject
.spyproject
 
# Rope project settings
.ropeproject
 
# mkdocs documentation
/site
 
# mypy
.mypy_cache/
.dmypy.json
dmypy.json
 
# Pyre type checker
.pyre/
 
# pytype static type analyzer
.pytype/
 
# Cython debug symbols
cython_debug/
 
# PyCharm
.idea/
 
.DS_Store
 
#database migrations
**/migrations/*.py
!**/migrations/__init__.py
```

**注意以下代码:**
```shell
#database migrations
*/migrations/*.py
!*/migrations/__init__.py
```
这里加两个“**”表示migrations文件不在一级app目录下，这里是由项目的目录结构决定的，不同项目的migrations需要在这里根据不同情况修改。
