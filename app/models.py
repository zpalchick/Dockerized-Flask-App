from app import db

class City(db.Model):
    name = db.Column(db.String(64), primary_key=True)

    def __repr__(self):
        return '<City %r>' % (self.name)

