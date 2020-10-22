from flask_restful import Resource, reqparse
from models.bolt import BoltModel


class Bolt(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('nev', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('partnerid', type=int, required=True, help="This field cannot be left blank!")

    def return_single_json(self, bolt):
        return {
            'bolt': {
                'id': bolt.id,
                'nev': bolt.nev, 
                'partnerid': bolt.partnerid,
            }
        }

    def return_multiple_json(self, boltok):
        boltok_json = []
        for bolt in boltok:
            boltok_json.append({
                "id": bolt.id,
                "nev": bolt.nev,
                "partnerid": bolt.partnerid,
                })
        return {'boltok': boltok_json}

    def get(self):
        boltok = BoltModel.find_all()
        if boltok:
            return self.return_multiple_json(boltok)
        return {'message': 'no boltok found'}, 404
    
    def post(self):
        data = Bolt.parser.parse_args()
        print([*data])

        if BoltModel.find_by_id(data['id']):
            return {'message': 'Bolt already exists.'}
        
        bolt = BoltModel(data['id'], data['nev'], data['partnerid'])

        if bolt.save_to_db():
            return {'message': f'Bolt {bolt.nev} created successfully.'}
        return {'message': 'Bolt could not be saved to database :('}


class BoltById(Bolt):
    def get(self, id):
        bolt = BoltModel.find_by_id(id)
        if bolt:
            return self.return_single_json(bolt)
        return {'message': 'bolt not found'}, 404


class BoltByPartnerid(Bolt):
    def get(self, partnerid):
        boltok = BoltModel.find_by_partnerid(partnerid)
        if boltok:
            return self.return_multiple_json(boltok)
        return {'message': 'no boltok found'}, 404


class BoltByNev(Bolt):
    def get(self, nev):
        bolt = BoltModel.find_by_nev(nev)
        if bolt:
            return self.return_single_json(bolt)
        return {'message': 'bolt not found'}, 404
        