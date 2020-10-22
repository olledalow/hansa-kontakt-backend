import mysql.connector
from flask_restful import Resource, reqparse
from models.vasarlas import VasarlasModel

class Vasarlas(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('esemenydatumido', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('vasarlasosszeg', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('penztargepazonosito', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('partnerid', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('boltid', type=int, required=True, help="This field cannot be left blank!")
    
    def return_single_json(self, vasarlas):
        return {'vasarlas': {
                'id': vasarlas.id,
                'esemenydatumido': vasarlas.esemenydatumido.strftime("%Y-%m-%d %H:%M:%S"),
                'vasarlasosszeg': vasarlas.vasarlasosszeg,
                'penztargepazonosito': vasarlas.penztargepazonosito,
                'partnerid': vasarlas.partnerid,
                'boltid': vasarlas.boltid}}
    
    def return_multiple_json(self, vasarlasok):
        vasarlasok_json = []
        for vasarlas in vasarlasok:
            vasarlasok_json.append({
                'id': vasarlas.id,
                'esemenydatumido': vasarlas.esemenydatumido.strftime("%Y-%m-%d %H:%M:%S"),
                'vasarlasosszeg': vasarlas.vasarlasosszeg,
                'penztargepazonosito': vasarlas.penztargepazonosito,
                'partnerid': vasarlas.partnerid,
                'boltid': vasarlas.boltid
            })
        return {'vasarlasok': vasarlasok_json}
    
    def get(self):
        vasarlasok = VasarlasModel.find_all()
        if vasarlasok:
            return self.return_multiple_json(vasarlasok)
        return {'message': 'no vasarlas found'}, 404
    
    def post(self):
        data = Vasarlas.parser.parse_args()

        if VasarlasModel.find_by_id(data['id']):
            return {'message': 'Vasarlas already exists.'}
        
        vasarlas = VasarlasModel(data['id'], data['esemenydatumido'], data['vasarlasosszeg'], data['penztargepazonosito'], data['partnerid'], data['boltid'])

        if vasarlas.save_to_db():
            return {'message': f'Vasarlas {vasarlas.id} created successfully.'}
        return {'message': 'Vasarlas could not be saved to database :('}



class VasarlasById(Vasarlas):
    def get(self, id):
        vasarlas = VasarlasModel.find_by_id(id)
        if vasarlas:
            return self.return_single_json(vasarlas)
        return {'message': 'vasarlas not found'}, 404

class VasarlasByEsemenydatumido(Vasarlas):
    def get(self, esemenydatumido):
        vasarlasok = VasarlasModel.find_by_esemenydatumido(esemenydatumido)
        if vasarlasok:
            return self.return_multiple_json(vasarlasok)
        return {'message': 'no vasarlas found'}, 404

class VasarlasByVasarlasosszeg(Vasarlas):
    def get(self, vasarlasosszeg):
        vasarlasok = VasarlasModel.find_by_vasarlasosszeg(vasarlasosszeg)
        if vasarlasok:
            return self.return_multiple_json(vasarlasok)
        return {'message': 'no vasarlas found'}, 404

class VasarlasByPenztargepazonosito(Vasarlas):
    def get(self, penztargepazonosito):
        vasarlasok = VasarlasModel.find_by_penztargepazonosito(penztargepazonosito)
        if vasarlasok:
            return self.return_multiple_json(vasarlasok)
        return {'message': 'no vasarlas found'}, 404
    
class VasarlasByPartnerid(Vasarlas):
    def get(self, partnerid):
        vasarlasok = VasarlasModel.find_by_partnerid(partnerid)
        if vasarlasok:
            return self.return_multiple_json(vasarlasok)
        return {'message': 'no vasarlas found'}, 404

class VasarlasByBoltid(Vasarlas):
    def get(self, boltid):
        vasarlasok = VasarlasModel.find_by_boltid(boltid)
        if vasarlasok:
            return self.return_multiple_json(vasarlasok)
        return {'message': 'no vasarlas found'}, 404
