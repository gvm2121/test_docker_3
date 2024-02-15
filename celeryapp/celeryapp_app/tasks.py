from celery import Celery
from celery.schedules import crontab

#app = Celery('tasks', broker='pyamqp://guest@localhost//')

app = Celery('celeryapp_app')

@app.task(bind=True)
def testeo(self):
    print("*************************** IMPRIMIENDO EL CRON 30 sgs")
