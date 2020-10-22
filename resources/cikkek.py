from flask_restful import Resource, reqparse
from models.cikkek import CikkekModel


class Cikkek(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('cikkszam', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('vonalkod', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('nev', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('mennyisegiegyseg', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('nettoegysegar', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('verzio', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('partnerid', type=int, required=True, help="This field cannot be left blank!")

    def return_single_json(self, cikk):
        return {
            'cikk': {
                'id': cikk.id,
                'cikkszam': cikk.cikkszam, 
                'vonalkod': cikk.vonalkod,
                'nev': cikk.nev,
                'mennyisegiegyseg': cikk.mennyisegiegyseg, 
                'nettoegysegar': cikk.nettoegysegar,
                'verzio': cikk.verzio,
                'partnerid': cikk.partnerid
                }
            }
    
    def return_multiple_json(self, cikkek):
        cikkek_json = []
        for cikk in cikkek:
            cikkek_json.append({
                "id": cikk.id,
                "cikkszam": cikk.cikkszam, 
                "vonalkod": cikk.vonalkod,
                "nev": cikk.nev,
                "mennyisegiegyseg": cikk.mennyisegiegyseg, 
                "nettoegysegar": cikk.nettoegysegar,
                "verzio": cikk.verzio,
                "partnerid": cikk.partnerid
                })
        return {'cikkek': cikkek_json}

    def get(self):
        cikkek = CikkekModel.find_all()
        if cikkek:
            return self.return_multiple_json(cikkek)
        return {'message': 'no cikkek found'}, 404
    
    def post(self):
        data = Cikkek.parser.parse_args()
        if CikkekModel.find_by_id(data['id']):
            return {'message': 'Cikk already exists.'}
        
        cikk = CikkekModel(data['id'], data['cikkszam'], data['vonalkod'], data['nev'], data['mennyisegiegyseg'], data['nettoegysegar'], data['verzio'], data['partnerid'])

        if cikk.save_to_db():
            return {'message': f'Cikk {cikk.nev} created successfully.'}
        return {'message': 'Cikk could not be saved to database :('}


class CikkekById(Cikkek):
    def get(self, id):
        cikk = CikkekModel.find_by_id(id)
        if cikk:
            return self.return_single_json(cikk)
        return {'message': 'cikk not found'}, 404


class CikkekByCikkszam(Cikkek):
    def get(self, cikkszam):
        cikkek = CikkekModel.find_by_cikkszam(cikkszam)
        if cikkek:
            return self.return_multiple_json(cikkek)
        return {'message': 'cikk not found'}, 404


class CikkekByVonalkod(Cikkek):
    def get(self, vonalkod):
        cikkek = CikkekModel.find_by_vonalkod(vonalkod)
        if cikkek:
            return self.return_multiple_json(cikkek)
        return {'message': 'cikk not found'}, 404


class CikkekByNev(Cikkek):
    def get(self, nev):
        cikkek = CikkekModel.find_by_nev(nev)
        if cikkek:
            return self.return_multiple_json(cikkek)
        return {'message': 'cikk not found'}, 404


class CikkekByMennyisegiegyseg(Cikkek):
    def get(self, mennyisegiegyseg):
        cikkek = CikkekModel.find_by_mennyisegiegyseg(mennyisegiegyseg)
        if cikkek:
            return self.return_multiple_json(cikkek)
        return {'message': 'cikk not found'}, 404


class CikkekByNettoegysegar(Cikkek):
    def get(self, nettoegysegar):
        cikkek = CikkekModel.find_by_nettoegysegar(nettoegysegar)
        if cikkek:
            return self.return_multiple_json(cikkek)
        return {'message': 'cikk not found by nettoegysegar'}, 404


class CikkekByVerzio(Cikkek):
    def get(self, verzio):
        cikkek = CikkekModel.find_by_verzio(verzio)
        if cikkek:
            return self.return_multiple_json(cikkek)
        return {'message': 'cikk not found'}, 404


class CikkekByPartnerid(Cikkek):
    def get(self, partnerid):
        cikkek = CikkekModel.find_by_partnerid(partnerid)
        if cikkek:
            return self.return_multiple_json(cikkek)
        return {'message': 'cikk not found'}, 404
