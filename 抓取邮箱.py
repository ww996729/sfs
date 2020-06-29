#-*-coding:utf-8-*-
import urllib
import urllib.request#请求
import re

mailragex=re.compile("([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})",re.IGNORECASE)#忽略异常
"""
for line in urllib.request.urlopen("http://bbs.tianya.cn/post-140-393973-1.shtml"):
    mylist=mailragex.findall(line.decode("utf-8"))
    if mylist:

     print(mylist)
"""
mystr=urllib.request.urlopen("http://bbs.tianya.cn/post-140-393973-1.shtml").read()
mylist=mailragex.findall(mystr.decode("utf-8"))
print(mylist)
