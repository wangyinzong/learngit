# encoding:utf-8
import os
import urllib.parse
from urllib import request


# 只是接受url
# 可以接受 Request类
def baidu_search(params):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    }
    url = "http://www.baidu.com/s?" + params  # 构建url
    req = urllib.request.Request("https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B0%AE%C7%E9&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111", headers=headers)
    res = urllib.request.urlopen(req)  # 把请求对象传过来
    print(res.read())  # 读取内容
    dir = './'
    os.chdir(dir)
    file = urllib.request.urlopen("https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B0%AE%C7%E9&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111").read()
    open("baidu.html", "wb").write(file)  # 保存页面
    print("ok")



if __name__ == "__main__":
    kw = input("请输入要查找的内容")
    params = {
        "wd": kw
    }
    params = urllib.parse.urlencode(params)  # 将字典转成字符串参数
    baidu_search(params)
