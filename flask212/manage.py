from flask import Flask, render_template
from flask_script import Manager
# 创建实例
app = Flask(__name__)
# 实例化manager对象
manager = Manager(app)
@app.route('/')
def index():
    # context={
    #     'username': 'kang',
    #     'age': 19,
    #     'country': 'china',
    # }
    context = {
        'users': ['摇滚是假的', '喜欢代码是假的', '喜欢钱是真的'],
        'person': {
            'username': 'kangba',
            'age': 19,
            'country': 'China'
        },
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 10.22
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 10.22
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 10.22
            },
            {
                'name': '西游记',
                'author': '尼玛',
                'price': 10.22
            }
        ]
    }
    #return render_template('hello.html', name='wang', age='23')
    return render_template('hello.html', **context)
if __name__ == '__main__':
    app.run(debug=True)