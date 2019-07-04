from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'ligongda'
USERNAME = 'root'
PASSWORD = 'wangyinzong'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "User(username:%s)" % self.username
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("user.id"))

    author = db.relationship("User", backref="articles")

    def __repr__(self):
        return "Article(title:%s,content:%s" % (self.title, self.content)
@app.route('/')
def index():
    return 'hello'

#db.drop_all()
db.create_all()
user = User(username="user1")
article = Article(title="title1", content="content1")
article.author = user
db.session.add(article)
db.session.commit()

user = User.query.order_by(User.id.desc()).all()
print(user)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)