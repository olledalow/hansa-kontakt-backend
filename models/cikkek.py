from database.db import db


class CikkekModel(db.Model):
    
    __tablename__ = 'cikkek'

    id               = db.Column(db.Integer, primary_key=True)
    cikkszam         = db.Column(db.String(255))
    vonalkod         = db.Column(db.String(255))
    nev              = db.Column(db.String(255))
    mennyisegiegyseg = db.Column(db.String(255))
    nettoegysegar    = db.Column(db.Float(precision=10))
    verzio           = db.Column(db.Integer)
    partnerid        = db.Column(db.Integer)
    vasarlas_tetel   = db.relationship('VasarlasTetelModel', backref='cikkek')

    def __init__(self, id, cikkszam, vonalkod, nev, mennyisegiegyseg, nettoegysegar, verzio, partnerid):
        self.id               = id,
        self.cikkszam         = cikkszam, 
        self.vonalkod         = vonalkod
        self.nev              = nev,
        self.mennyisegiegyseg = mennyisegiegyseg, 
        self.nettoegysegar    = nettoegysegar
        self.verzio           = verzio
        self.partnerid        = partnerid,

    def __repr__(self):
        return f"{self.id, self.cikkszam, self.vonalkod, self.nev, self.mennyisegiegyseg, self.nettoegysegar, self.verzio, self.partnerid}"
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_cikkszam(cls, cikkszam):
        return cls.query.filter_by(cikkszam=cikkszam).all()

    @classmethod
    def find_by_vonalkod(cls, vonalkod):
        return cls.query.filter_by(vonalkod=vonalkod).all()

    @classmethod
    def find_by_nev(cls, nev):
        return cls.query.filter_by(nev=nev).all()

    @classmethod
    def find_by_mennyisegiegyseg(cls, mennyisegiegyseg):
        return cls.query.filter_by(mennyisegiegyseg=mennyisegiegyseg).all()

    @classmethod
    def find_by_nettoegysegar(cls, nettoegysegar):
        return cls.query.filter_by(nettoegysegar=nettoegysegar).all()

    @classmethod
    def find_by_verzio(cls, verzio):
        return cls.query.filter_by(verzio=verzio).all()

    @classmethod
    def find_by_partnerid(cls, partnerid):
        return cls.query.filter_by(partnerid=partnerid).all()

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False