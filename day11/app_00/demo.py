import re
f=open("demo01.txt", "r",encoding='utf-8',errors='ignore')
txt = f.read()
print(txt)
regimg = re.compile('//bookcover.*0')
regauthor = re.compile('59">.{1,10}</a')
mystr_img = regimg.findall(txt)
mystr_author = regauthor.findall(txt)
print(mystr_img)
aa = []
for line in mystr_author:
    a = line[4:-3]
    # print(a)
    aa.append(a)
ids = list(set(aa))
print(ids)
import requests
i = 120
j = 0
for img in mystr_img:
    img_url = "http:" + img
    r = requests.get(img_url)
    with open('./media/images/img%s.jpg'%i, 'wb') as f:
        f.write(r.content)
    f.close()
    with open("./media/data.txt", "a+",encoding='utf-8') as ff:
        ff.writelines(ids[j]+"\n")
    ff.close()
    i= i+1
    j=j+1