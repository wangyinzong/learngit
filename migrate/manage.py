from flask_script import Manager
from ligong import flask_1
from exts import db
from models import User, Article
from flask_migrate import Migrate, MigrateCommand

manager = Manager(flask_1)

# python manage.py runserver -d -r
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade

Migrate(flask_1, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()