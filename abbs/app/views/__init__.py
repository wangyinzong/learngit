from .main import main
from .user import users

# 蓝本配置
DEFAULT_BLUEPRINT = (
    (main, ''),
    (users, '/users')
)
# 封装函数完成蓝本注册
def config_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)