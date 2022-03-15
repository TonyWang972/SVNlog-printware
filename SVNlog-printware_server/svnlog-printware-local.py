# -*- coding:utf-8 -*-
import re
import json

# 获取HTML二进制文件
file = "weeklogfile.log"
data = []

# 初始化数据集对象
msg = {}
userList = []
dataList = []
# 判断类型
codeArray = ['java', 'c', 'cpp', 'py', 'dart', 'xml', 'html', 'css', 'js', 'vue']
docArray = ['doc', 'docx', 'zip', 'rp']
picArray = ['gif', 'png', 'bmp', 'ico', 'jpg', 'jpeg']
videoArray = ['mp4', 'm4v', 'mkv', 'webm', 'avi', 'wmv', 'mpg', 'flv', 'mov']

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

def changeMsg():
    str=read_log()
    msg['author_name'] = re.findall(r'<author>(.*?)</author>',
                             str)
    msg['date'] = re.findall(r'<date>(.*?)T.*?</date>',
                                   str)
    msg['action'] = re.findall(r'action="(.)"',
                             str)
    msg['suffix'] = re.findall(r'\.(.*?)</path>',
                             str)


    for index in  range(len(msg['author_name'])):
        if msg['author_name'][index] not in userList:
            # 类型：代码、图片、视频、文档、其他
            userDict = {'name': msg['author_name'][index], 'totalNum': 1,'createCode': 0, 'createDoc': 0, 'createPic': 0, 'createVideo': 0, 'createOther': 0
                                                        ,'modCode': 0, 'modDoc': 0, 'modPic': 0, 'modVideo': 0, 'modOther': 0
                                                        ,'delCode': 0, 'delDoc': 0, 'delPic': 0, 'delVideo': 0, 'delOther': 0}
            # userDict = {'name': msg['author_name'][index], 'totalNum': 1, 'ANum': 0, 'MNum': 0, 'DNum': 0,'OtherNum':0}

            if (msg['suffix'][index] in codeArray):
                userDict[getType(msg['action'][index])+'Code']+=1
            elif(msg['suffix'][index] in docArray):
                userDict[getType(msg['action'][index])+'Doc']+=1
            elif (msg['suffix'][index] in picArray):
                userDict[getType(msg['action'][index])+'Pic']+=1
            elif (msg['suffix'][index] in videoArray):
                userDict[getType(msg['action'][index])+'Video']+=1
            else:
                userDict[getType(msg['action'][index])+'Other']+=1
            # if(msg['action'][index]=='A'):
            #     userDict['ANum']+=1
            # elif(msg['action'][index]=='M'):
            #     userDict['MNum']+=1
            # elif(msg['action'][index] == 'D'):
            #     userDict['DNum']+=1
            # else:
            #     userDict['OtherNum'] += 1
            userList.append(msg['author_name'][index])
            dataList.append(userDict)
        else:
            # //print(dataList)
            for j in  range(len(dataList)):
                # print(dataList[j]['name']+" "+userList[j])
                if dataList[j]['name'] == msg['author_name'][index]:
                    dataList[j]['totalNum']=dataList[j]['totalNum']+1
                    if (msg['suffix'][index] in codeArray):
                        userDict[getType(msg['action'][index]) + 'Code'] += 1
                    elif (msg['suffix'][index] in docArray):
                        userDict[getType(msg['action'][index]) + 'Doc'] += 1
                    elif (msg['suffix'][index] in picArray):
                        userDict[getType(msg['action'][index]) + 'Pic'] += 1
                    elif (msg['suffix'][index] in videoArray):
                        userDict[getType(msg['action'][index]) + 'Video'] += 1
                    else:
                        userDict[getType(msg['action'][index]) + 'Other'] += 1
    return 0

def read_log():
    f = open(file,'r',encoding='UTF-8')  # 设置文件对象
    str = f.read()  # 将txt文件的所有内容读入到字符串str中
    f.close()  # 将文件关闭
    return str

if __name__ == '__main__':
    changeMsg()
    data = json.dumps(dataList)
    print(data)

