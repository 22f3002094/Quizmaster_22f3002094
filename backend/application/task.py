from celery import shared_task
import time
from .models import db, Subject,User, Role,Quiz
import csv
import os 
from .utils import prepare_temp
from .mail import send_email
@shared_task(name = "test task" )
def test_task():
    time.sleep(30)
    return "it's done"  

@shared_task(name = "download_csv_admin")
def csv_down_ad():
    subs =Subject.query.all()
    os.makedirs("./static" ,exist_ok= True )

    filename = "admin_csv_download.csv" 
    time.sleep(20)
    with open( f"./static/{filename}", "w") as csvfile:
        csv_obj = csv.writer(csvfile , delimiter=",")

        csv_obj.writerow(["No." , "Subject Name" , "Description" ,"No.Chapters"])
        for index , sub in enumerate(subs):
            csv_obj.writerow([index+1 , sub.sub_name , sub.sub_desc , len(sub.chapters)])
    

    return filename

@shared_task(name="admin monthly report ")
def admin_monthly_report():
    
    subs =Subject.query.all()

    ad = Role.query.filter_by(name="admin").first().bearers[0]
    data = {"username" :ad.name , "subjects" : subs}
    output_temp = prepare_temp("./templates/adminmail.html" ,data)
    send_email(ad.email , "Monthly Report " , output_temp)
    return "Mail Sent"
    

@shared_task(name="user monthly report ")
def user_monthly_report():
    
    subs =Subject.query.all()

    users = Role.query.filter_by(name="student").first().bearers
    for user in users:
        data = {"username" :user.name , "subjects" : subs}
        output_temp = prepare_temp("./templates/adminmail.html" ,data)
        send_email(user.email , "Monthly Report " , output_temp)
    return "Mail Sent"

@shared_task(name="quiz alert report ")
def Quiz_alert(quiz_id):
    
    quiz =Quiz.query.filter_by(quiz_id = quiz_id).first()
    

    users = Role.query.filter_by(name="student").first().bearers
    for user in users:
        data = {"username" :user.name , "quiz" : quiz}
        output_temp = prepare_temp("./templates/quizalert.html" ,data)
        send_email(user.email , "One quiz awaits you" , output_temp)
    return "Mail Sent"