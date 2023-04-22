from app import db
import datetime

available = db.Table('available',
    db.Column('country_id', db.Integer, db.ForeignKey('country.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True)
)
category_film = db.Table('category_film',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True)
)
director_film = db.Table('director_film',
    db.Column('director_id', db.Integer, db.ForeignKey('director.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True)
)

class Film(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(100))
	release_date = db.Column(db.DateTime, default=datetime.datetime.now())
	created_in_country = db.Column(db.Integer, db.ForeignKey('country.id'))
	available_in_countries = db.relationship('Country', secondary=available, lazy='dynamic', backref=db.backref('films_available', lazy=True))
	category = db.relationship('Category', secondary=category_film, lazy='dynamic', backref=db.backref('films', lazy=True))
	director = db.relationship('Director', secondary=director_film, lazy='dynamic', backref=db.backref('films', lazy=True))
class Country(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(50))
	films = db.relationship('Film', backref='country', lazy='dynamic')


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(50))

class Director(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(100))

