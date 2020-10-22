from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.bolt import Bolt, BoltById, BoltByNev, BoltByPartnerid 
from resources.vasarlas import Vasarlas, VasarlasById, VasarlasByEsemenydatumido, VasarlasByVasarlasosszeg, VasarlasByPenztargepazonosito, VasarlasByPartnerid, VasarlasByBoltid
from resources.cikkek import Cikkek, CikkekById, CikkekByCikkszam, CikkekByVonalkod, CikkekByNev, CikkekByMennyisegiegyseg, CikkekByNettoegysegar, CikkekByVerzio, CikkekByPartnerid
from resources.vasarlas_tetel import VasarlasTetel, VasarlasTetelById, VasarlasTetelByPartnerctid, VasarlasTetelByVasarlasid, VasarlasTetelByMennyiseg, VasarlasTetelByBrutto, VasarlasTetelByPartnerid


APP = Flask(__name__)
CORS(APP)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/hansa_kontakt'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
API = Api(APP)

# REGISTER BOLT API RESOURCES
API.add_resource(Bolt, '/bolt')
API.add_resource(BoltByNev, '/bolt/nev/<string:nev>')
API.add_resource(BoltById, '/bolt/id/<int:id>')
API.add_resource(BoltByPartnerid, '/bolt/partnerid/<int:partnerid>')

# REGISTER VASARLAS API RESOURCES
API.add_resource(Vasarlas, '/vasarlas')
API.add_resource(VasarlasById, '/vasarlas/id/<int:id>')
API.add_resource(VasarlasByEsemenydatumido, '/vasarlas/esemenydatumido/<string:esemenydatumido>')
API.add_resource(VasarlasByVasarlasosszeg, '/vasarlas/vasarlasosszeg/<int:vasarlasosszeg>')
API.add_resource(VasarlasByPenztargepazonosito, '/vasarlas/penztargepazonosito/<int:penztargepazonosito>')
API.add_resource(VasarlasByPartnerid, '/vasarlas/partnerid/<int:partnerid>')
API.add_resource(VasarlasByBoltid, '/vasarlas/boltid/<int:boltid>')

# REGISTER CIKKEK API RESOURCES
API.add_resource(Cikkek, '/cikkek')
API.add_resource(CikkekById, '/cikkek/id/<int:id>')
API.add_resource(CikkekByCikkszam, '/cikkek/cikkszam/<string:cikkszam>')
API.add_resource(CikkekByVonalkod, '/cikkek/vonalkod/<string:vonalkod>')
API.add_resource(CikkekByNev, '/cikkek/nev/<string:nev>')
API.add_resource(CikkekByMennyisegiegyseg, '/cikkek/mennyisegiegyseg/<string:mennyisegiegyseg>')
API.add_resource(CikkekByNettoegysegar, '/cikkek/nettoegysegar/<float:nettoegysegar>')
API.add_resource(CikkekByVerzio, '/cikkek/verzio/<string:verzio>')
API.add_resource(CikkekByPartnerid, '/cikkek/partnerid/<string:partnerid>')

# REGISTER VASARLAS_TETEL API RESOURCES
API.add_resource(VasarlasTetel, '/vasarlas_tetel')
API.add_resource(VasarlasTetelById, '/vasarlas_tetel/id/<int:id>')
API.add_resource(VasarlasTetelByPartnerctid, '/vasarlas_tetel/partnerctid/<int:partnerctid>')
API.add_resource(VasarlasTetelByVasarlasid, '/vasarlas_tetel/vasarlasid/<int:vasarlasid>')
API.add_resource(VasarlasTetelByMennyiseg, '/vasarlas_tetel/mennyiseg/<int:mennyiseg>')
API.add_resource(VasarlasTetelByBrutto, '/vasarlas_tetel/brutto/<int:brutto>')
API.add_resource(VasarlasTetelByPartnerid, '/vasarlas_tetel/partnerid/<int:partnerid>')


if __name__ == '__main__':
    from database.db import db
    db.init_app(APP)
    APP.run(port=5000, debug=True)
