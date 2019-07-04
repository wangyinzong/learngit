from .users import User
from .posts import Posts
from app.exts import db


collections = db.Table('collections',
    db.Column('users_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('posts_id',db.Integer,db.ForeignKey('posts.id')),
                       )