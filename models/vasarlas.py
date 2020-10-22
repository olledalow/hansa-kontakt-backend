from database.db import db


class VasarlasModel(db.Model):

    __tablename__ = 'vasarlas'
    
    id                  = db.Column(db.Integer, primary_key=True)
    esemenydatumido     = db.Column(db.DateTime)
    vasarlasosszeg      = db.Column(db.Float(precision=2))
    penztargepazonosito = db.Column(db.Integer)
    partnerid           = db.Column(db.Integer)
    boltid              = db.Column(db.Integer, db.ForeignKey('bolt.id'), nullable=False)
    vasarlas_tetel      = db.relationship('VasarlasTetelModel', backref='vasarlas')

    def __init__(self, id, esemenydatumido, vasarlasosszeg, penztargepazonosito, partnerid, boltid):
        self.id = id
        self.esemenydatumido = esemenydatumido
        self.vasarlasosszeg = vasarlasosszeg
        self.penztargepazonosito = penztargepazonosito
        self.partnerid = partnerid
        self.boltid = boltid

    def __repr__(self):
        return f"{self.id, self.esemenydatumido, self.vasarlasosszeg, self.penztargepazonosito, self.partnerid, self.boltid}"

    @classmethod
    def find_all(cls):
        return cls.query.all()  

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_esemenydatumido(cls, esemenydatumido):
        return cls.query.filter_by(esemenydatumido=esemenydatumido).all()

    @classmethod
    def find_by_vasarlasosszeg(cls, vasarlasosszeg):
        return cls.query.filter_by(vasarlasosszeg=vasarlasosszeg).all()
    
    @classmethod
    def find_by_penztargepazonosito(cls, penztargepazonosito):
        return cls.query.filter_by(penztargepazonosito=penztargepazonosito).all()

    @classmethod
    def find_by_partnerid(cls, partnerid):
        return cls.query.filter_by(partnerid=partnerid).all()

    @classmethod
    def find_by_boltid(cls, boltid):
        return cls.query.filter_by(boltid=boltid).all()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
            