from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'mydb'
USERNAME = 'root'
PASSWORD = 'wangyinzong'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)
Base = declarative_base(engine)
#create table person(id int(11) unsigned not null primary key
# auto_increment, name varchar(20),age tinyint,country varchar(20))
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True,
                autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)
    country = Column(String(20))
# 将类映射到数据库中
Base.metadata.create_all()
