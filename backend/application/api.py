from flask_restful import Resource, Api,request
api = Api()
from .models import Subject,db,Chapter
from flask_security import auth_required,roles_required


class SubjectsAPI(Resource):
    @auth_required('token')
    def get(self):
        subjects = Subject.query.all()
        subs = []
        for sub in subjects:
            subs.append({"name" : sub.sub_name , "description" : sub.sub_desc , "id":sub.sub_id})
        
        return subs,200
    
    def post(self):
        formdata= request.get_json()
        try:
            sub = Subject.query.filter_by(sub_name=formdata.get("name")).first()
            if sub:
                return {"message" :"Subject already exist"} , 409
            else:
                new_sub = Subject(sub_name = formdata.get("name") , sub_desc = formdata.get("description"))
                db.session.add(new_sub)
                db.session.commit()
            
                return {"id": new_sub.sub_id , "name" : new_sub.sub_name , "desc" : new_sub.sub_desc} ,200
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"message" : "internal server error"} , 500
            
        
    def put(self):
        id = request.args.get("id")
        formdata= request.get_json()
        try:
            sub = Subject.query.filter_by(sub_id = id).first()

            if sub:
                if formdata.get("name"):
                    if not  Subject.query.filter(Subject.sub_name.ilike( f"%{formdata.get("name")}%" )).first():
                        sub.sub_name = formdata.get("name")
                    else:
                        return {"message" :"Subject already exist"} , 409
                if formdata.get("description"):
                    sub.sub_desc = formdata.get("description")
                db.session.commit()
                return {"message" :"Subject is updated"} , 200
            else:
                return {"message" :"Subject doesn't exist"} , 404
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"message" : "internal server error"} , 500
            
        

    def delete(self):
        id = request.args.get("id")
        try:
            sub = Subject.query.filter_by(sub_id = id).first()
            if sub:
                db.session.delete(sub)
                db.session.commit()
                return {"message" : "subject is deleted"} , 200
            else:
                return {"message" : "subject doesn't exist"} , 404
        except Exception as e :
            print(e)
            db.session.rollback()
            return {"message" : "internal server error"} , 500
        
class ChaptersAPI(Resource):
    def get(self):
        if request.args.get("sub_name"):
            try:
                sub = Subject.query.filter_by(sub_name = request.args.get("sub_name")).first()

                chapters = Chapter.query.filter_by(sub_id = sub.sub_id ).all()
                L = []
                for chap in chapters:
                    L.append({"id" : chap.ch_id , "name" : chap.ch_name , "description" : chap.ch_desc})
                return L, 200
            except Exception as e:
                print(e)
                db.session.rollback()
                return {"message" :"internal server error" } , 500
        else : 
            try:
                chapters = Chapter.query.all()
                L = []
                for chap in chapters:
                    L.append({"id" : chap.ch_id , "name" : chap.ch_name , "description" : chap.ch_desc})
                    return L, 200
            except Exception as e:
                print(e)
                db.session.rollback()
                return {"message" :"internal server error" } , 500
            
    def post(self):
        
        formdata= request.get_json()
        try:
            chap = Chapter.query.filter_by(ch_name=formdata.get("name")).first()
            if chap:
                return {"message" :"chapter already exist"} , 409
            else:
                sub = Subject.query.filter_by(sub_name = request.args.get("sub_name")).first()
                new_sub = Chapter(ch_name = formdata.get("name") , ch_desc = formdata.get("description") , sub_id = sub.sub_id)
                db.session.add(new_sub)
                db.session.commit()
            
                return {"message" :"chapter Created successfully"} ,200
        
        except Exception as e:
            print(e)
            db.session.rollback()
            return {"message" : "internal server error"} , 500
    
    def delete(self):
        id = request.args.get("ch_id")
        try:
            ch = Chapter.query.filter_by(ch_id = id).first()
            if ch:
                db.session.delete(ch)
                db.session.commit()
                return {"message" : "Chapter is deleted"} , 200
            else:
                return {"message" : "Chapter doesn't exist"} , 404
        except Exception as e :
            print(e)
            db.session.rollback()
            return {"message" : "internal server error"} , 500
            

api.add_resource(SubjectsAPI, '/api/subjects')
api.add_resource(ChaptersAPI, '/api/chapters')
        