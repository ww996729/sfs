#-*-coding:utf-8-*-
import urllib.request#请求
import re
httper=re.compile(r"(http://\S*?)[\"|>|）]",re.IGNORECASE)#忽略异常
for line in urllib.request.urlopen("http://www.baidu.com"):
    line=line.decode("utf-8")
    # if line.find("QQ")!=-1 or line.find("Qq")!=-1 or line.find("qq")!=-1:

    mylist=httper.findall(line)
    if mylist:

              print(mylist)