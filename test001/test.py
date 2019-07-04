#encoding:utf-8

from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

#创建实例
gongda = Flask(__name__)
bootstrap = Bootstrap(gongda)
manager = Manager(gongda)

#视图函数
@gongda.route('/')
def index():
    # context = {
    #     'username':'你的名字',
    #     'age':16,
    #     'country':'china china china',
    #     'scripts':'<script>alert("kangbazimen")</script>',
    #     'childrens':{
    #         'name':'  test         ',
    #         'height':'181cm',
    #     }
    # }
    return render_template('hello.html')

# @gongda.route('/statics/')
# def statics():
#     return render_template('static.html')

@gongda.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
#启动

if __name__ == "__main__":
    gongda.run(debug=True, threaded=True)
