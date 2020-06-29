#-*-coding:utf-8-*-
import urllib.request#请求
import re
QQ=re.compile(r"[1-9]\d{4,10}",re.IGNORECASE)#忽略异常

for line in urllib.request.urlopen("http://bbs.tianya.cn/post-140-393973-1.shtml"):
    line=line.decode("utf-8")
    if line.find("QQ")!=-1 or line.find("Qq")!=-1 or line.find("qq")!=-1:

       mylist=QQ.findall(line)
       if mylist:

              print(mylist)