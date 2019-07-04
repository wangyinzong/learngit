import os
# 获取到 config 所在目录,定义基础目录
base_dir = os.path.abspath(os.path.dirname(__file__))
# 通用配置
class Config:
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wang'
    # 数据库的操作
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件发送
    MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp@163.com"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "15179809270@163.com"
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or "wangyinzong"

    BOOTSTRAP_SERVE_LOCAL = True

    MAX_CONTENT_LENGTH = 1024*1024*8
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir, 'static/upload')

    @staticmethod
    def init_app():
        pass
# 开发环境配置
class DevelomentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir, 'bbs_dev.sqlite')
# 测试环境配置
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir, 'bbs_test.sqlite')

# 生产环境配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir, 'bbs.sqlite')

config = {
    "development": DevelomentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "Default": DevelomentConfig
}