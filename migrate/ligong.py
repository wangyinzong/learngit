from flask import Flask
import config
from exts import db
# 创建实例
flask_1 = Flask(__name__)

# 加载配置文件
flask_1.config.from_object(config)
db.init_app(flask_1)

@flask_1.route('/')
def index():
    return 'hello!!!!'
@flask_1.route('/profile/')
def profile():
    pass

if __name__ == '__main__':
    flask_1.run()

