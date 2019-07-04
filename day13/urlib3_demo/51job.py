import urllib
from urllib import request
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
}

# 前程无忧接口

url = "https://search.51job.com/list/130200,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
# 创建请求对象

req = urllib.request.Request(url=url, headers=headers)
# 返回数据
response = urllib.request.urlopen(req)

# print(response)
html = response.read().decode('gbk')
# print(html)
# print(type(html)) #<class 'str'>
# print(html)
#
# # 处理数据
jobnum_re = '<div class="rt">(.*?)</div>'
comp = re.compile(jobnum_re,re.S)
job_str = comp.findall(html)[0]

# print(job_str)
# #
# # #提取数字
num_re = ".*?(\d+).*"
num = re.findall(num_re,job_str)
print(num)
print(num[0])
print(int(num[0]))
#
#
# # 获取第一个岗位的名称
#
re_str = '<div class="el">(.*?)</div>'
job_list = re.findall(re_str, html, re.S)
# print(job_list[0])
#
# re_str1 = 'onmousedown="">(.*?)</a>'
# job_list2 = re.findall(re_str1, html, re.S)
# print(job_list2)
# print("第一个岗位名称:%s" % job_list2[0].strip())
#
for job in job_list:
    re_str2 = 'onmousedown="">(.*?)</a>'
    job_list3 = re.findall(re_str2, job, re.S)
    print("岗位名称:%s" % job_list3[0].strip())
