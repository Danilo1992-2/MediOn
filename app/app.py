from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)

from .farmacia.view import farmacia 
app.register_blueprint(farmacia)
from .medico.view import medico 
app.register_blueprint(medico)
from .paciente.view import paciente 
app.register_blueprint(paciente)
from .receita.view import Receita 
app.register_blueprint(Receita)
from .admin.view import admin
app.register_blueprint(admin)


