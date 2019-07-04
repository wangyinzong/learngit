from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_moment import Moment
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_migrate import MigrateCommand, Migrate
# 创建对象
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
migrate = Migrate(db=db)
moment = Moment()
photos = UploadSet('photos', IMAGES)

# 完成对象与实例的绑定
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)

    configure_uploads(app, photos)
    patch_request_class(app, size=None)


