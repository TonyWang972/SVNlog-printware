# -*- coding:utf-8 -*-
import re
import json
import os
from flask import Flask, jsonify, request
from gevent import pywsgi


cmd = 'ls'
app = Flask(__name__)

# 解决中文乱码问题
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

# 获取HTML二进制文件
file = "weeklogfile.log"

#svn命令
# startDate="2022-2-1"
# endDate="2022-2-1"
# svnlog_date="svn log -r {"+endDate+"}:{"+startDate+"} -v --xml > "+file

# 初始化数据集对象
msg = {}
userList = []
dataList = []
userDict = {}

# 判断类型
codeArray = ['java', 'c','msg', 'cpp', 'py','h','dart','yaml','xml', 'html', 'css', 'js','vue','class','iml', 'cc', 'gitignore', 'hpp', 'sh', 'json']
docArray = ['doc', 'docx','ppt','pptx','xls','xlsx','txt','md', 'zip', 'rp', 'xmind', 'vsdx', 'vsd', 'csv']
picArray = ['gif', 'png', 'bmp', 'ico', 'jpg', 'jpeg']
videoArray = ['mp4', 'm4v', 'mkv', 'webm', 'avi', 'wmv', 'mpg', 'flv', 'mov']

# 组员
cloud = ['yangkai','wangcan','guozhen']
software = ['heyufei','sujinya','zhangran','qiancheng','guohuayue','liwei']
hardware = ['shaxiaoyu','shaohongwei']
product = ['wujunnan', 'qiyunjie','yangzenghui']

# 判断状态
def getType(type):
   if type=='A':
       return 'create'
   elif type=='M':
       return 'mod'
   elif type=='D':
       return 'del'
   else:
       return 'other'

# ///////////////////
# 获取元数据
# ///////////////////
def getSourceMsg():
   # 初始化数据集对象
   msg = {}
   userList = []
   userLogentryList = []
   userMsgList = []
   str = read_log()

   msg['author_name'] = re.findall(r'<author>(.*?)</author>',
                                   str)
   msg['logentry'] = re.findall(r'<logentry([\s\S]*?)</logentry>',
                                str)

# ///////////////////
# logentry信息合并
# ///////////////////
   for index in range(len(msg['author_name'])):
       # 第一次出现某用户logentry信息，则初始化
       if msg['author_name'][index] not in userList:
           userLogentryDict = {'name': msg['author_name'][index], 'logentryMsg': msg['logentry'][index]}
           userDict = {'name': msg['author_name'][index]}
           userList.append(msg['author_name'][index])
           userLogentryList.append(userLogentryDict)
           userMsgList.append(userDict)
       # userLogentryList中已有某用户logentry信息，则拼接
       else:
           for j in range(len(userLogentryList)):
               if userLogentryList[j]['name'] == msg['author_name'][index]:
                   userLogentryList[j]['logentryMsg'] = userLogentryList[j]['logentryMsg'] + (
                   msg['logentry'][index])
# TEST
# print(userLogentryList)
# print(len(userLogentryList))

# ///////////////////
# path信息合并
# ///////////////////
   pathDict = {}
   for index in range(len(userLogentryList)):
       pathStr = userLogentryList[index]['logentryMsg']
       userLogentryList[index]['path'] = re.findall(r'<path\n   ([\s\S]*?)</path>',
                                                    pathStr)
       # print(pathStr)

# ///////////////////
# path信息处理
# ///////////////////
   pathMsgStr = ""
   detailMsgList = []
   for index in range(len(userLogentryList)):
       arr = userLogentryList[index]['path']
       for indexPath in range(len(arr)):
           pathMsgStr = userLogentryList[index]['path'][indexPath]
           action = re.search(r'action="(.)"', pathMsgStr).group(1)
           kind = re.search(r'kind="(.*?)"', pathMsgStr).group(1)
           suffix = re.search(r'.([^.]*)$', pathMsgStr).group(1)
           detailMsgDict = {'action': action, 'kind': kind, 'suffix': suffix}
           detailMsgList.append(detailMsgDict)
       userMsgList[index]['detailMsgDictList'] = detailMsgList
       detailMsgList=[]
   return userMsgList

# ///////////////////
# 获取人员元数据
# ///////////////////
def getUserSourceMsg():
    msgList = []
    sourceMsgList=getSourceMsg()
    for index in range(len(sourceMsgList)):
        # print(sourceMsgList[index]['detailMsgDictList'])
        userDict = {'name': sourceMsgList[index]['name'], 'totalNum': 0, 'createCode': 0, 'createDoc': 0,
                    'createPic': 0,
                    'createVideo': 0, 'createOther': 0
            , 'modCode': 0, 'modDoc': 0, 'modPic': 0, 'modVideo': 0, 'modOther': 0
            , 'delCode': 0, 'delDoc': 0, 'delPic': 0, 'delVideo': 0, 'delOther': 0}
        for indexPath in range(len(sourceMsgList[index]['detailMsgDictList'])):
            # 过滤第一条无效信息
            if index==0 and indexPath==0:
                continue
            if sourceMsgList[index]['detailMsgDictList'][indexPath]['kind']=='file':
                userDict['totalNum'] = userDict['totalNum'] + 1
                if (sourceMsgList[index]['detailMsgDictList'][indexPath]['suffix'] in codeArray):
                    userDict[getType(sourceMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Code'] += 1
                elif (sourceMsgList[index]['detailMsgDictList'][indexPath]['suffix'] in docArray):
                    userDict[getType(sourceMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Doc'] += 1
                elif (sourceMsgList[index]['detailMsgDictList'][indexPath]['suffix'] in picArray):
                    userDict[getType(sourceMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Pic'] += 1
                elif (sourceMsgList[index]['detailMsgDictList'][indexPath]['suffix'] in videoArray):
                    userDict[getType(sourceMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Video'] += 1
                else:
                    userDict[getType(sourceMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Other'] += 1
        msgList.append(userDict)
    return msgList

# //////////////////////////////////////
# 获取元数据（后端接口）
# //////////////////////////////////////
@app.route('/getDetailMsg')
def getDetailMsg():
    msgList = getSourceMsg()
    data = json.dumps(msgList)
    # print(data)
    return data

# //////////////////////////////////////
# 获取人员数据（后端接口）
# //////////////////////////////////////
@app.route('/getUserMsg')
def getUserMsg():
    userMsgList = getUserSourceMsg()
    data = json.dumps(userMsgList)
    return data

# //////////////////////////////////////
# 获取组数据（后端接口）
# //////////////////////////////////////
# cloud = ['yangkai','guozhen']
# software = ['heyufei','sujinya','zhangran','qiancheng','guohuayue','wangcan','qiancheng']
# hardware = ['shaxiaoyu','shaohongwei']
# product = ['wujunnan', 'qiyunjie', 'yangzenghui']
@app.route('/getGroupMsg')
def getGroupMsg():
    groupList = ['cloud','software','hardware','product','other']
    groupName = {'cloud':'云平台', 'software': '软件组', 'hardware': '硬件组','product': '产品组','other': '其他',}
    groupMsgList = []
    userMsgList=getUserSourceMsg()
    for index in range(len(groupList)):
        groupDict = {'groupName': groupName[groupList[index]], 'totalNum': 0, 'createCode': 0, 'createDoc': 0,
                    'createPic': 0,
                    'createVideo': 0, 'createOther': 0
            , 'modCode': 0, 'modDoc': 0, 'modPic': 0, 'modVideo': 0, 'modOther': 0
            , 'delCode': 0, 'delDoc': 0, 'delPic': 0, 'delVideo': 0, 'delOther': 0}
        groupMsgList.append(groupDict)

    for indexPath in range(len(userMsgList)):
        if (userMsgList[indexPath]['name'] in cloud):
            groupDict_findAndAdd(groupMsgList,'云平台',userMsgList[indexPath])
        elif (userMsgList[indexPath]['name'] in software):
            groupDict_findAndAdd(groupMsgList,'软件组',userMsgList[indexPath])
        elif (userMsgList[indexPath]['name'] in hardware):
            groupDict_findAndAdd(groupMsgList,'硬件组',userMsgList[indexPath])
        elif (userMsgList[indexPath]['name'] in product):
            groupDict_findAndAdd(groupMsgList,'产品组',userMsgList[indexPath])
        else:
            groupDict_findAndAdd(groupMsgList,'其他',userMsgList[indexPath])
    data = json.dumps(groupMsgList)
    return data

# //////////////////////////////////////
# 根据groupName查找groupDict,并添加数据
# //////////////////////////////////////
def groupDict_findAndAdd(groupMsgList,groupName,addDict):
    for index in range(len(groupMsgList)):
        if(groupMsgList[index]['groupName']==groupName):
            dict_add(groupMsgList[index], addDict)

# //////////////////////////////////////
# addDict加到AddedDict上
# //////////////////////////////////////
def dict_add(AddedDict,addDict):
    for key in AddedDict:
        if(key=='groupName'):
            continue
        # print(AddedDict[key]+addDict[key])
        AddedDict[key]+=addDict[key]

def read_log():
    f = open(file,'r',encoding='UTF-8')  # 设置文件对象
    str = f.read()  # 将txt文件的所有内容读入到字符串str中
    f.close()  # 将文件关闭
    return str

@app.route('/'
           '')
def updateFile():
    cmd='svn update'
    os.system(cmd)

# //////////////////////////////////////
# 传入起始时间，更新log文件
# //////////////////////////////////////
@app.route('/updateLog',methods=['POST'])
def updateLog():
    startTime=request.form.get('startTime')
    endTime=request.form.get('endTime')
    cmd="svn log -r {"+startTime+"}:{"+endTime+"} -v --xml > "+file
    os.system(cmd)

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
    # app.run()
