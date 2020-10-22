from database.db import db


class BoltModel(db.Model):
    
    __tablename__ = 'bolt'

    id        = db.Column(db.Integer, primary_key=True)
    nev       = db.Column(db.String(255))
    partnerid = db.Column(db.Integer)
    vasarlas  = db.relationship('VasarlasModel', backref='bolt')

    def __init__(self, id, nev, partnerid):
        self.id = id
        self.nev = nev
        self.partnerid = partnerid

    def __repr__(self):
        return f"{self.id, self.nev, self.partnerid}"

    @classmethod
    def find_by_nev(cls, nev):
        return cls.query.filter_by(nev=nev).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_partnerid(cls, partnerid):
        return cls.query.filter_by(partnerid=partnerid).all()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
