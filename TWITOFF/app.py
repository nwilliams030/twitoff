"""Code for our app"""
# Convention is to load imports in alphabetical order
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

#make our app factory

def create_app():
    app = Flask(__name__)

    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = confif('DATABASE_URL')

    # stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        # pulls users in w. a flask query, don't forget to import user!
        users = User.query.all()
        # title arg shows up here again from base.html
        return render_template('base.html', title = 'Home', users=users)
    return app
