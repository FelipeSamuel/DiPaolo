from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_cors import CORS

from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from flask_mail import Mail

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')
cors = CORS(app, resources={r"/*": {"origins": "*"}})
mail = Mail(app)

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)

migrate = Migrate(app, db)
mg_manager = Manager(app)

mg_manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)

import DiPaolo.models
import DiPaolo.controllers
import DiPaolo.routes
import DiPaolo.views