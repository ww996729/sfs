#-*-coding:utf-8-*-
import urllib.request#请求
import re
from collections import deque


def geteveryurl(data):
    alllist=[]
    mylist1=[]
    mylist2=[]
    mylist1=gethttpall(data)
    if len(mylist1)>0:

      mylist2=getabsurl(mylist1[0],data)
    alllist.extend(mylist1)
    alllist.extend(mylist2)
    return alllist
def getabsurl(url,data):
    listurl=[]
    regex=re.compile("href=\"(.*?)\"",re.IGNORECASE)
    httplist=regex.findall(data)
    newhttplist=httplist.copy()
    for data in newhttplist:
        if data.find("http://")!=-1:
            httplist.remove(data)
        if data.find("javascript")!=-1:
            httplist.remove(data)
    hostname=gethostname(url)
    if hostname!=None:
        for i in range(len(httplist)):
            httplist[i]=str(hostname)+httplist[i]

    return httplist
def gethostname(httpstr):
     try:
        mailragex=re.compile(r"(http://\S*?)/",re.IGNORECASE)#忽略异常
        # mystr=urllib.request.urlopen(data).read()
        mylist=mailragex.findall(httpstr)
        # print(mylist)
        if len(mylist)==0:
            return None
        else:
            return mylist
        return mylist
     except:
        return None
def gethttpall(data):
     try:
        mailragex=re.compile(r"(http://\S*?)[\"|>|）]",re.IGNORECASE)#忽略异常
        # mystr=urllib.request.urlopen(data).read()
        mylist=mailragex.findall(data)
        # print(mylist)
        return mylist
     except:
        return ""
def getalleamil(data):
    try:
        mailragex=re.compile("([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})",re.IGNORECASE)#忽略异常
        # mystr=urllib.request.urlopen(data).read()
        mylist=mailragex.findall(data)
        # print(mylist)
        return mylist
    except:
        return ""
def getdata(url):
    try:
        data=urllib.request.urlopen(url).read().decode("utf-8")
        return data
    except:
        return""
def BFS(urlstr):
   urlquere=deque([])
   urlquere.append(urlstr)
   while len(urlquere)!=0:
       url=urlquere.popleft()
       print(url)
       pagedata=getdata(url)
       emaillist=getalleamil(pagedata)
       if len(emaillist)!=0:
           for emaill in emaillist:
               print(emaill)
       newurlliat=geteveryurl(pagedata)
       if len(newurlliat)!=0:
           for urlstr in newurlliat:
               if urlstr not in urlquere:
                   urlquere.append(urlstr)
BFS("https://tieba.baidu.com/p/2366935784?red_tag=2187001860")

