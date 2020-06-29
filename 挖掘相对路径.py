#-*-coding:utf-8-*-
import urllib.request#请求
import re
#
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
# print(getdata("http://bbs.tianya.cn/post-140-393973-1.shtml"))
# print(getalleamil(getdata("http://bbs.tianya.cn/post-140-393973-1.shtml")))
# print(getalleamil("http://bbs.tianya.cn/post-140-393973-1.shtml"))
# print(gethttpall(getdata("http://bbs.tianya.cn/post-140-393973-1.shtml")))
# print(gethttpall("http://bbs.tianya.cn/post-140-393973-1.shtml"))
pagedata=getdata("http://bbs.tianya.cn/post-140-393973-1.shtml")
# mylist=gethttpall(pagedata)
# hostname=gethostname(mylist[0])
# # print(mylist[0])
# myhostname=gethostname(mylist[0])
# print(getabsurl(mylist[0],pagedata))
print(geteveryurl(pagedata))
print(getalleamil(pagedata))
