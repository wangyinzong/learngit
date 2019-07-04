import os
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app
from app.models import Posts
from app.exts import db

#创建实例
app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def posts_test_data():
    for x in range(1,250):
        content = '内容 %s' % x
        post = Posts(content=content)
        post.uid = 1
        db.session.add(post)
        db.session.commit()
    return '恭喜插入成功'

if __name__ == '__main__':
    manager.run()