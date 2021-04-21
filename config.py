import os


BASE_DIR = os.path.dirname(__file__)

#접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

#SQLALCHEMY의 이벤트 처리 옵션(False=비활성화)
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"
