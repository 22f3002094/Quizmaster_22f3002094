from flask import current_app as app
from .models import db
from flask_security import SQLAlchemyUserDatastore
from flask_security import hash_password

with app.app_context():
    db.create_all()
    
    datastore = app.security.datastore


    
    if not datastore.find_role("admin"):
        datastore.create_role(name="admin", description="superuser")
    if not datastore.find_role("student"):
        datastore.create_role(name="student", description="student")
    
    

    if (not datastore.find_user(email = "admin@gmail.com")):
        datastore.create_user(name ="admin" , email = 'admin@gmail.com', password = hash_password('pass'), roles = ['admin'] )
    if (not datastore.find_user(email = 'stud1@gmail.com')):
        datastore.create_user(name="stud1" ,email = 'stud1@gmail.com', password = hash_password('pass'), roles = ['student'] )
    
    db.session.commit()
    print("Initial data created")
    

