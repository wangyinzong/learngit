from sqlalchemy import create_engine
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'mydb'
USERNAME = 'root'
PASSWORD = 'wangyinzong'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'.format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)

#创建连接
with engine.connect() as con:
    rs = con.execute('SELECT version()')
    print (rs.fetchone())
class Person():
    name = 'wang'
    age = 11
    contry = 'china'
p = Person('xx', 'ss')
# create table person(id int(11) primary key, name varchar(32),age int,country varchar(32))