# -*- coding:utf-8 -*-
import re
import json
from flask import Flask, jsonify
from gevent import pywsgi

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
file = "weeklogfile.log"

msg = {}
userList = []
dataList = []
userDict = {}

codeArray = ['java', 'c', 'cpp', 'py','h','dart', 'xml', 'html', 'css', 'js', 'vue']
docArray = ['doc', 'docx','txt', 'zip', 'rp']
picArray = ['gif', 'png', 'bmp', 'ico', 'jpg', 'jpeg']
videoArray = ['mp4', 'm4v', 'mkv', 'webm', 'avi', 'wmv', 'mpg', 'flv', 'mov']

def getType(type):
   if type=='A':
       return 'create'
   elif type=='M':
       return 'mod'
   elif type=='D':
       return 'del'
   else:
       return 'other'

def getSourceMsg():
   msg = {}
   userList = []
   userLogentryList = []
   userMsgList = []
   str = read_log()

   msg['author_name'] = re.findall(r'<author>(.*?)</author>',
                                   str)
   msg['logentry'] = re.findall(r'<logentry([\s\S]*?)</logentry>',
                                str)
   for index in range(len(msg['author_name'])):
       if msg['author_name'][index] not in userList:
           userLogentryDict = {'name': msg['author_name'][index], 'logentryMsg': msg['logentry'][index]}
           userDict = {'name': msg['author_name'][index]}
           userList.append(msg['author_name'][index])
           userLogentryList.append(userLogentryDict)
           userMsgList.append(userDict)
       else:
           for j in range(len(userLogentryList)):
               if userLogentryList[j]['name'] == msg['author_name'][index]:
                   userLogentryList[j]['logentryMsg'] = userLogentryList[j]['logentryMsg'] + (
                   msg['logentry'][index])

   for index in range(len(userLogentryList)):
       pathStr = userLogentryList[index]['logentryMsg']
       userLogentryList[index]['path'] = re.findall(r'<path\n   ([\s\S]*?)</path>',
                                                    pathStr)

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

@app.route('/getDetailMsg')
def getDetailMsg():
    msgList = getSourceMsg()
    data = json.dumps(msgList)
    return data

@app.route('/getMsg')
def getMsg():
    msgList=[]
    userMsgList=getSourceMsg()
    for index in range(len(userMsgList)):
        print(userMsgList[index]['detailMsgDictList'])
        userDict = {'name': userMsgList[index]['name'], 'totalNum': 0, 'createCode': 0, 'createDoc': 0,
                    'createPic': 0,
                    'createVideo': 0, 'createOther': 0
            , 'modCode': 0, 'modDoc': 0, 'modPic': 0, 'modVideo': 0, 'modOther': 0
            , 'delCode': 0, 'delDoc': 0, 'delPic': 0, 'delVideo': 0, 'delOther': 0}
        for indexPath in range(len(userMsgList[index]['detailMsgDictList'])):
            if index==0 and indexPath==0:
                continue
            if userMsgList[index]['detailMsgDictList'][indexPath]['kind']=='file':
                userDict['totalNum'] = userDict['totalNum'] + 1
                if (userMsgList[index]['detailMsgDictList'][indexPath]['suffix'] in codeArray):
                    userDict[getType(userMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Code'] += 1
                elif (userMsgList[index]['detailMsgDictList'][indexPath]['suffix'] in docArray):
                    userDict[getType(userMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Doc'] += 1
                elif (userMsgList[index]['detailMsgDictList'][indexPath]['suffix'] in picArray):
                    userDict[getType(userMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Pic'] += 1
                elif (userMsgList[index]['detailMsgDictList'][indexPath]['suffix'] in videoArray):
                    userDict[getType(userMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Video'] += 1
                else:
                    userDict[getType(userMsgList[index]['detailMsgDictList'][indexPath]['action']) + 'Other'] += 1
        msgList.append(userDict)
    data = json.dumps(msgList)
    return data

def read_log():
    f = open(file,'r',encoding='UTF-8')  # 设置文件对象
    str = f.read()  # 将txt文件的所有内容读入到字符串str中
    f.close()  # 将文件关闭
    return str

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
    # app.run()
