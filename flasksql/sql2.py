from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
# Session = sessionmaker(engine) # 这是一个类
# session = Session()       # 这才是对象
session = sessionmaker(engine)()    # 这才是对象
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True,
                autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)
    country = Column(String(20))
    # 格式化直观显示自定义内容
    def __str__(self):
        return 'Person(id:%d,name:%s,age:%d,country:%s)' % (self.id, self.name, self.age, self.country)
def add_data():
    # p = Person(name='王敢当', age=18, country='China')
    # session.add(p)
    p1 = Person(name='我是', age=11, country='Z')
    p2 = Person(name='你', age=22, country='C')
    session.add_all([p1, p2])
    session.commit()
def show_data():
    # select * from person;
    # all_person = session.query(Person).all()
    # for p in all_person:
    #     print(p)
    # all_person = session.query(Person).filter_by(name='王敢当').all()
    # for p in all_person:
    #     print(p)
    # all_person = session.query(Person).filter(Person.name=='王敢当').all()
    oneperson = session.query(Person).first()
    print(oneperson)
def update_data():
    p = session.query(Person).first()
    p.name = '狗屎'
    session.commit()
def delete_data():
    p = session.query(Person).first()
    session.delete(p)
    session.commit()
if __name__ == '__main__':
    # add_data()
    # show_data()
    # update_data()
    delete_data()