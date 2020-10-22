from database.db import db


class VasarlasTetelModel(db.Model):

    __tablename__ = 'vasarlas_tetel'

    id          = db.Column(db.Integer, primary_key=True)
    partnerctid = db.Column(db.Integer, db.ForeignKey('cikkek.id'), nullable=False)
    vasarlasid  = db.Column(db.Integer, db.ForeignKey('vasarlas.id'), nullable=False)
    mennyiseg   = db.Column(db.Float(precision=2))
    brutto      = db.Column(db.Float(precision=2))
    partnerid   = db.Column(db.Integer)

    def __init__(self, id, partnerctid, vasarlasid, mennyiseg, brutto, partnerid):
        self.id          = id,
        self.partnerctid = partnerctid, 
        self.vasarlasid  = vasarlasid
        self.mennyiseg   = mennyiseg,
        self.brutto      = brutto, 
        self.partnerid   = partnerid

    def __repr__(self):
        return f"{self.id, self.partnerctid, self.vasarlasid, self.mennyiseg, self.brutto, self.partnerid}"
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_partnerctid(cls, partnerctid):
        return cls.query.filter_by(partnerctid=partnerctid).all()

    @classmethod
    def find_by_vasarlasid(cls, vasarlasid):
        return cls.query.filter_by(vasarlasid=vasarlasid).all()

    @classmethod
    def find_by_mennyiseg(cls, mennyiseg):
        return cls.query.filter_by(mennyiseg=mennyiseg).all()

    @classmethod
    def find_by_brutto(cls, brutto):
        return cls.query.filter_by(brutto=brutto).all()
    
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
