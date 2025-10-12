from celery import shared_task
import time

@shared_task(name = "test task" )
def test_task():
    time.sleep(30)
    return "it's done"  

