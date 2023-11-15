from flask import Flask
import os
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Cofiguracion de la DB

USER_DB = os.getenv("USER_DB")
PASS_DB = os.getenv("PASSW_DB")
URL_DB = os.getenv("URL_DB")
NAME_DB = os.getenv("NAME_DB")


FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'


app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializacion del objeto db de sqlalchemy
db = SQLAlchemy(app)

# configurar flask-migrate
migreate = Migrate()
migreate.init_app(app, db)


class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)

    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Nombre: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Email: {self.email}'
        )
