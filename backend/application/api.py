from flask_restful import Resource, Api
api = Api()
from .models import Subject,db
from flask_security import auth_required,roles_required


class SubjectsAPI(Resource):
    @auth_required('token')
    def get(self):
        subjects = Subject.query.all()
        subs = []
        for sub in subjects:
            subs.append({"name" : sub.sub_name , "desc" : sub.sub_desc , "id":sub.sub_id})
        
        return subs,200

    

api.add_resource(SubjectsAPI, '/api/subjects')
        