flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import numpy as np
import pandas as pd

app = Flask(__name__)

db = SQLAlchemy(app)

app.config.from_object('config')

app.SECRET_KEY = 'secreta123'

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)


from app.models import tables, forms
from app.controllers import default
