from application.config import *
from application.database import * 
from application import workers

from flask import *
from flask_cors import CORS
from flask_sse import sse
from flask_restful import *
from flask_caching import Cache


dev=True                        # true for development server

celery = None
app=None
cache = None
api=None

def create_app():
    app = Flask(__name__, template_folder='templates')
    if dev:
        print('starting dev server')
        app.config.from_object(LocalDevConfig)
    else:
        print('starting production server')
        app.config.from_object(ProductionConfig)

    db.init_app(app)
    app.app_context().push()
    celery = workers.celery
    celery.conf.update(broker_url=app.config["CELERY_BROKER_URL"],
                        result_backend=app.config["CELERY_RESULT_BACKEND"],
                        timezone="Asia/Kolkata")
    celery.Task = workers.ContextTask
    CORS(app)
    app.app_context().push()
    cache=Cache(app)
    app.app_context().push()
    return app, celery, cache

app, celery, cache = create_app()
app.app_context().push()
from application.apiEndpoints import *

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug = 'True')