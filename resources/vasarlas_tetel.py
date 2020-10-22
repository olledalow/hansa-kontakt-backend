from flask_restful import Resource, reqparse
from models.vasarlas_tetel import VasarlasTetelModel

class VasarlasTetel(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('partnerctid', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('vasarlasid', type=int, required=True, help="This field cannot be left blank!")
    parser.add_argument('mennyiseg', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('brutto', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('partnerid', type=int, required=True, help="This field cannot be left blank!")
    
    def return_single_json(self, vasarlas_tetel):
        return {
            'vasarlas_tetel': {
                'id': vasarlas_tetel.id,
                'partnerctid': vasarlas_tetel.partnerctid, 
                'vasarlasid': vasarlas_tetel.vasarlasid,
                'mennyiseg': vasarlas_tetel.mennyiseg,
                'brutto': vasarlas_tetel.brutto, 
                'partnerid': vasarlas_tetel.partnerid,
                }
            }
    
    def return_multiple_json(self, vasarlas_tetelek):
        vasarlas_tetelek_json = []
        for tetel in vasarlas_tetelek:
            # print(tetel)
            vasarlas_tetelek_json.append({
                'id': tetel.id,
                'partnerctid': tetel.partnerctid, 
                'vasarlasid': tetel.vasarlasid,
                'mennyiseg': tetel.mennyiseg,
                'brutto': tetel.brutto, 
                'partnerid': tetel.partnerid,
                })
        return {'vasarlas_tetelek': vasarlas_tetelek_json}

    def get(self):
        vasarlas_tetelek = VasarlasTetelModel.find_all()
        if vasarlas_tetelek:
            return self.return_multiple_json(vasarlas_tetelek)
        return {'message': 'no vasarlas_tetel found'}, 404
    
    def post(self):
        data = VasarlasTetel.parser.parse_args()

        if VasarlasTetelModel.find_by_id(data['id']):
            return {'message': 'Tetel already exists.'}
        
        vasarlas_tetel = VasarlasTetelModel(data['id'], data['partnerctid'], data['vasarlasid'], data['mennyiseg'], data['brutto'], data['partnerid'])

        if vasarlas_tetel.save_to_db():
            return {'message': f'Tetel {vasarlas_tetel.id} created successfully.'}
        return {'message': 'Tetel could not be saved to database :('}

class VasarlasTetelById(VasarlasTetel):
    def get(self, id):
        cikk = VasarlasTetelModel.find_by_id(id)
        if cikk:
            return self.return_single_json(cikk)
        return {'message': 'tetel not found'}, 404

class VasarlasTetelByPartnerctid(VasarlasTetel):
    def get(self, partnerctid):
        vasarlastetel = VasarlasTetelModel.find_by_partnerctid(partnerctid)
        if vasarlastetel:
            return self.return_multiple_json(vasarlastetel)
        return {'message': 'tetel not found'}, 404

class VasarlasTetelByVasarlasid(VasarlasTetel):
    def get(self, vasarlasid):
        VasarlasTetel = VasarlasTetelModel.find_by_vasarlasid(vasarlasid)
        if VasarlasTetel:
            return self.return_multiple_json(VasarlasTetel)
        return {'message': 'tetel not found'}, 404

class VasarlasTetelByMennyiseg(VasarlasTetel):
    def get(self, mennyiseg):
        VasarlasTetel = VasarlasTetelModel.find_by_mennyiseg(mennyiseg)
        if VasarlasTetel:
            return self.return_multiple_json(VasarlasTetel)
        return {'message': 'tetel not found'}, 404

class VasarlasTetelByBrutto(VasarlasTetel):
    def get(self, brutto):
        VasarlasTetel = VasarlasTetelModel.find_by_brutto(brutto)
        if VasarlasTetel:
            return self.return_multiple_json(VasarlasTetel)
        return {'message': 'tetel not found'}, 404

class VasarlasTetelByPartnerid(VasarlasTetel):
    def get(self, partnerid):
        VasarlasTetel = VasarlasTetelModel.find_by_partnerid(partnerid)
        if VasarlasTetel:
            return self.return_multiple_json(VasarlasTetel)
        return {'message': 'tetel not found by nettoegysegar'}, 404
