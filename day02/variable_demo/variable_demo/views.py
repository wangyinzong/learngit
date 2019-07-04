from django.shortcuts import render
class Person(object):
    def __init__(self,username):
        self.uername = username
def index(request):
    p = Person('CXK')

    # context = {
    #     'person':p
    # }
    # context = {
    #     'person':{
    #         'username':'cxk'
    #     }
    # }
    # context = {
    #     'person':(
    #         'ni shi cxk',
    #         'fj',
    #         'sc'
    #     )
    # }
    # context = {
    #     'age':20,
    #
    # }
    # context = {
    #     'heros': [
    #         '高斯',
    #         '拉格朗日',
    #         '泰勒',
    #         'cxk'
    #     ]
    # }
    # context = {
    #     'persons':{
    #         'username':'wang',
    #         'age':20,
    #         'height':222
    #     }
    # }
    # context = {
    #     'persons':[
    #         '王爷',
    #         '大哥',
    #         '谢谢'
    #     ]
    # }
    # context = {
    #     'comments':[
    #         '你真sixsixsix'
    #     ],
    #     'books':[
    #         {
    #             'name':'水浒',
    #             'author':'wang',
    #             'price':20
    #         },            {
    #             'name':'雪中',
    #             'author':'yin',
    #             'price':23
    #         },            {
    #             'name':'jianlai',
    #             'author':'信息',
    #             'price':2022
    #         }
    #     ]
    # }
    context = {
        "info":"<a href='http://www.baidu.com'></a>"
    }

    return render(request,'index.html',context=context)
