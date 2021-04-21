from flask import Flask
#app = Flask(__name__)

#------------------------------------------#
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

#전역 변숫 선언
db = SQLAlchemy()
migrate = Migrate()

#------------------------------------------#
def create_app():
    app =Flask(__name__)

    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello, Pybo!'
    #---------------------------------#
    app.config.from_object(config) #config.py 에서 가져오기

    db.init_app(app) #초기화
    migrate.init_app(app, db) #초기화

    from . import models
    #---------------------------------#
    from .views import main_views, question_views, answer_views # main_views.py, question_views.py 내용 가져오기
    app.register_blueprint(main_views.bp) # main_views.py의 bp 객체 등록 
    app.register_blueprint(question_views.bp) # question_views.py의 bp 객체 등록
    app.register_blueprint(answer_views.bp)
    return app