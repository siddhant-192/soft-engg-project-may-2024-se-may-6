from application.workers import celery

@celery.task()
def createConversation():
    pass

@celery.task()
def hintCode():
    pass