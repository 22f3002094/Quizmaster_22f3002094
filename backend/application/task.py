from celery import shared_task
import time
from .models import db, Subject
import csv
import os 

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