# SVNlog-printware

### SVNlog-printware介绍

SVNlog_printware是一个开源代码统计程序，通过从Subversion版本库中取得信息的，比如：代码行数的时间线；针对每个开发者的代码及文档数量；针对每个开发者所在组的代码及文档数量等。StatSVN当前版本能够生成一组包括表格与图表的动态HTML文档。

![mainPage](https://github.com/TonyWang972/SVNlog-printware/blob/main/pic/mainPage.png)

### SVNlog-printware使用条件

SVNlog-printware是一个python&Vue写的开源代码统计程序，是从Subversion版本库中取得信息的，所以使用SVNlog-printware有两个限制。

1. 需要安装python的运行环境（python3.9&flask）  
2. 需要使用svn客户端，必须保证本机的svn客户端命令可用

### SVNlog-printware运行方法

1. 将svnlog-printware-server.py拷贝至SVN文件夹下（可以正常运行SVNlog语句的文件夹）
2. 根据需求修改相关代码配置文件
3. 运行`python3 svnlog-printware-server.py `
4. 使用Vue运行网页端，即可看到相关信息的表格和可视化数据





