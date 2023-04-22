import flask
from config import Config
import flask_sqlalchemy
import flask_migrate
import os
from flask_bootstrap import Bootstrap

db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()
bootstrap = Bootstrap()

def create_app():
	flask_app = flask.Flask(__name__)
	flask_app.config.from_object(Config)
	basedir = os.path.abspath(os.path.dirname(__file__))

	flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'IMDI.db')

	db.init_app(flask_app)
	migrate.init_app(flask_app, db)
	bootstrap.init_app(flask_app)

	from app.films import films
	from app.accounts import accounts

	flask_app.register_blueprint(films, url_prefix="/films")
	flask_app.register_blueprint(accounts, url_prefix="/accounts")

	return flask_app

from app import models