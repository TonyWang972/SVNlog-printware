# SVNlog-printware

### 1  SVNlog-printware介绍

SVNlog_printware是一个开源代码统计程序，通过从Subversion版本库中取得信息的，比如：代码行数的时间线；针对每个开发者的代码及文档数量；针对每个开发者所在组的代码及文档数量等。StatSVN当前版本能够生成一组包括表格与图表的动态HTML文档。

![mainPage](https://github.com/TonyWang972/SVNlog-printware/blob/main/pic/mainPage.png?raw=true)

### 2  SVNlog-printware使用条件

SVNlog-printware是一个python&Vue写的开源代码统计程序，是从Subversion版本库中取得信息的，所以使用SVNlog-printware有两个限制。

1. 需要安装python和一些依赖包的运行环境（python3.9&flask&pexpect）         

   执行以下命令：

   1. `pip3 install flask`
   2. `pip3 install -I pexpect`
   3. `pip3 install gevent`

2. 需要在服务器上安装Vue和Nginx服务器

3. 需要使用svn客户端，必须保证本机的svn客户端命令可用

### 3  SVNlog-printware服务器运行方法

#### 3.1  后端部署：

1. 将svnlog-printware-server.py拷贝至SVN文件夹下（可以正常运行SVNlog语句的文件夹）

2. 根据需求修改相关代码配置文件

3. 后台持续运行Flask`nohup python3 svnlog-printware-server.py & `

   ##### 辅助调试命令

   1. 检查当前运行python端口进程：netstat -tunlp | grep 5000
   2. 停止该进程：kill { pid }

**python启动/重新启动**

1. netstat -tunlp | grep 5000（重新启动时需要）
2. kill { pid }（重新启动时需要）
3. nohup python3 svnlog-printware-server.py &



#### 3.2  前端部署：

1. 安装Nginx服务器

2. 将Vue导出的网页放在指定文件夹并进行配置（防止js、css等文件被过滤）
3. 访问指定ip和端口:  ` { ip }:{ port }/svn`

**Nginx重新启动**（一般不需要重新启动，重新配置端口后需要重新启动）

`/usr/local/nginx/sbin/nginx -v
/usr/local/nginx/sbin/nginx -s reload`

**前端重新部署**

1. vue生产html：`npm run build`
2. 将dist文件夹的文件复制到nginx指定目录



#### 3.3  代码适配

置SVN服务器的账户和密码用于SVN文件更新：**`svn update --username qiyunjie --password qiyunjie`

**增加新文件格式：**

1. 在对应的列表（从上至下分别为代码、文档、图片、视频）中加上所需要的格式

```
# 判断类型
codeArray = ['java', 'c','msg', 'cpp', 'py','h','dart','yaml','xml', 'html', 'css', 'js','vue','class','iml', 'cc', 'gitignore', 'hpp', 'sh', 'json', 'arxml']
docArray = ['doc', 'docx','ppt','pptx','xls','xlsx','txt','md', 'zip','rar', 'rp', 'xmind', 'vsdx', 'vsd', 'csv']
picArray = ['gif', 'png', 'bmp', 'ico', 'jpg', 'jpeg']
videoArray = ['mp4', 'm4v', 'mkv', 'webm', 'avi', 'wmv', 'mpg', 'flv', 'mov']
```

2. 添加完成后重新运行python文件



### 4  后台接口文档

根据传入type的不同分别支持按当天、上周、diy自定义统计

按员工统计：http://{ ip }:5000/getUserMsg?type={day/week/diy}

按组统计：http://{ ip }:5000/getGroupMsg?type={day/week/diy}

展示详细信息：http://{ ip }:5000/getDetailMsg?type={day/week/diy}



### 5  相关Linux命令

连接本地SVN服务器（若无可省略）：`ssh -x server@192.168.123.121`

到运行目录：`cd data_backup/svn_server_everyday_backup/`

生产log文件命令：`svn log -r {2022-3-16}:{2022-3-18} -v --xml >weeklogfile.log --username { username }--password { password }`

python运行命令：`python3 svnlog-printware-server.py `

python运行命令（持续运行）：`nohup python3 svnlog-printware-server.py &`



有任何bug、疑问和二次开发需求，欢迎联系我，QQ：710093245



