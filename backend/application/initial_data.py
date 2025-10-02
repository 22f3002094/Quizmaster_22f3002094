from flask import current_app as app
from .models import db
from flask_security import SQLAlchemyUserDatastore
from flask_security import hash_password

with app.app_context():
    db.create_all()
    
    datastore = app.security.datastore


    
    if not datastore.find_role("admin"):
        datastore.create_role(name="admin", description="superuser")
    if not datastore.find_role("doctor"):
        datastore.create_role(name="doctor", description="doctor")
    if not datastore.find_role("patient"):
        datastore.create_role(name="patient", description="patient")
    

    if (not datastore.find_user(email = "admin@gmail.com")):
        datastore.create_user(name ="admin" , email = 'admin@gmail.com', password = hash_password('pass'), roles = ['admin'] )
    if (not datastore.find_user(email = 'doctor1@gmail.com')):
        datastore.create_user(name="d1" ,email = 'doctor1@gmail.com', password = hash_password('pass'), roles = ['doctor'] )
    if (not datastore.find_user(email = 'patient1@gmail.com')):
        datastore.create_user(name="p1" ,email = 'patient1@gmail.com', password = hash_password('pass'), roles = ['patient'] )
    db.session.commit()
    print("Initial data created")
    
    admin_role= datastore.find_role( "doctor")
    print(admin_role.users[0].email)

