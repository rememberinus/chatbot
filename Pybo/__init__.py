from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(config)  #데이터베이스 설정
app.debug = True

        #ORM 데이터베이스 초기화
db.init_app(app)

if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
    migrate.init_app(app, db, render_as_batch=True)
else:
    migrate.init_app(app, db)

from .views import main_views,question_views,answer_views,auth_views,chatbotviews
app.register_blueprint(main_views.bp)
app.register_blueprint(question_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(chatbotviews.bp)

# 필터 등록
from .filter import format_datetime
app.jinja_env.filters['datetime'] = format_datetime
