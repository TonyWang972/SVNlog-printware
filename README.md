# SVNlog-printware

### SVNlog-printware介绍

SVNlog_printware是一个开源代码统计程序，通过从Subversion版本库中取得信息的，比如：代码行数的时间线；针对每个开发者的代码及文档数量；针对每个开发者所在组的代码及文档数量等。StatSVN当前版本能够生成一组包括表格与图表的动态HTML文档。

![mainPage](https://github.com/TonyWang972/SVNlog-printware/blob/main/pic/mainPage.png?raw=true)

### SVNlog-printware使用条件

SVNlog-printware是一个python&Vue写的开源代码统计程序，是从Subversion版本库中取得信息的，所以使用SVNlog-printware有两个限制。

1. 需要安装python和一些依赖包的运行环境（python3.9&flask&pexpect）         

   执行以下命令：

   1. `pip3 install flask`
   2. `pip3 install -I pexpect`
   3. `pip3 install gevent`

2. 需要在服务器上安装Vue和Nginx服务器

3. 需要使用svn客户端，必须保证本机的svn客户端命令可用

### SVNlog-printware本地运行方法

	#### 后端部署：

1. 将svnlog-printware-server.py拷贝至SVN文件夹下（可以正常运行SVNlog语句的文件夹）

2. 根据需求修改相关代码配置文件

3. 后台持续运行Flask`nohup python3 svnlog-printware-server.py & `

   ##### 辅助调试命令

   1. 检查当前运行python端口进程：netstat -tunlp | grep 5000
   2. 停止该进程：kill { pid }

   

	#### 前端部署：

1. 安装Nginx服务器
2. 将Vue导出的网页放在指定文件夹并进行配置（防止js、css等文件被过滤）
3. 访问指定ip和端口:  ` { ip }:{ port }/svn`

### SVNlog-printware服务器运行方法

**Nginx重新启动**：

`/usr/local/nginx/sbin/nginx -v
/usr/local/nginx/sbin/nginx -s reload`



### 代码适配

设置SVN服务器的账户和密码用于SVN文件更新：`svn update --username qiyunjie --password qiyunjie`



### 后台接口文档

按员工统计：http://192.168.123.121:5000/getUserMsg

按组统计：http://192.168.123.121:5000/getGroupMsg

展示详细信息：http://192.168.123.121:5000/getDetailMsg



### TempMsg

ssh -x server@192.168.123.121

cd data_backup/svn_server_everyday_backup/

svn log -r {2022-3-10}:{2022-3-11} -v --xml >weeklogfile.log

python3 svnlog-printware-server.py 

python3 svnlog-printware-server-source.py 

nohup python3 svnlog-printware-server.py &



有任何bug、疑问和二次开发需求，欢迎联系我，QQ：710093245



