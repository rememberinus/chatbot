import os

# 데이터 베이스 환경설정
BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI: 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLALCHEMY_TRACK_MODIFICATIONS: SQLAlchemy의 이벤트를 처리하는 옵션 (True: 활성화, False: 비활성화)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLite: 주로 소규모 프로젝트에서 사용하는 가벼운 파일을 기반으로 한 데이터베이스

SECRET_KEY = 'dev'