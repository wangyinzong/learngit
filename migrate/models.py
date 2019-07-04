from exts import db

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