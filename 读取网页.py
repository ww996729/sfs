#-*-coding:utf-8-*-
import urllib
import urllib.request#请求
mystr=urllib.request.urlopen("http://bbs.tianya.cn/post-140-393973-1.shtml").read()
print(mystr.decode("utf-8"))
