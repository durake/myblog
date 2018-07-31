from app import db
from hashlib import  md5
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nickname = db.Column(db.String(64),index = True,unique = True)
    email = db.Column(db.String(120),index = True,unique = True)
    posts = db.relationship('Posts',backref='author',lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    is_authenticated = True

    is_active = True

    is_anonymous = False

    def get_id(self):
        try:
            return unicode(self.id)
        except:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def avatar(self,size):
       dataMail = self.email
       data_url = 'http://www.gravatar.com/avatar/' + md5(dataMail.encode('utf8')).hexdigest() + '?d=mm&s=' + str(size)
       print(data_url)
       return data_url


class Posts(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' %(self.body)

