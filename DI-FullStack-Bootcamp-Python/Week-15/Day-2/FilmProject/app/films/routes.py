import flask
from app import db

from app.films import films
from app.films.forms import AddFilmForm
from app.films.forms import AddDirectorForm
from app.models import Director



@films.route("/")
def homepage():
    directors = Director.query.all()
    return flask.render_template("homepage.html", directors=directors)

@films.route("/addFilm")
def addFilm():
    form = AddFilmForm()
    return flask.render_template("film/addFilm.html", form=form)

@films.route("/addDirector", methods=['GET'])
def getDirector():
    form = AddDirectorForm()
    return flask.render_template("director/addDirector.html", form=form)

@films.route("/addDirector", methods=['POST'])
def postDirector():
    form = AddDirectorForm()
    if form.validate_on_submit():
        director = Director(first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(director)
        db.session.commit()
    return flask.redirect(flask.url_for('films.homepage'))
