from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationships
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'ligongda'
USERNAME = 'root'
PASSWORD = 'wangyinzong'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)
Base = declarative_base(engine)

session = sessionmaker(engine)()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50))

    def __repr__(self):
        return "User(username:%s" % self.username

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey("user.id"))

    def __repr__(self):
        return "Article(title:%s,content:%s" % (self.title,self.content)

Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username="wang")
article = Article(title="别追她了，吃屎吧", content="你是啥吊码", uid=1)
session.add_all([user, article])
session.commit()

article = session.query(Article).first()
uid = article.uid
print(uid)
print(article)

user = session.query(User)
print(user)

