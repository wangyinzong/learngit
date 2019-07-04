# import urllib.parse
# strings = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
#
# print(urllib.parse.unquote(strings))
#
# strings1 = "https://movie.douban.com/j/search_subjects?type=tv&tag=热门&page_limit=50&page_start=0"
# print(urllib.parse.quote(strings1))

import urllib
import json
from urllib import request
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
for i in range(100):
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d" % (i *20)
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode()
    # print(content)
    data = json.loads(content)
    datalist =data.get('data')
    for movie in datalist:
        title = movie['title']
        casts = movie['casts']
        rate = movie['rate']
        with open('douban.txt','a+',encoding='utf-8') as fp:
            fp.write(str((title,casts,rate))+"\n")
            fp.flush() #不回车我也会往里写数据

