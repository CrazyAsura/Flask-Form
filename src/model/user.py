from src import app
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URL
db = SQLAlchemy(app)
class User:
    def __init__(self, id, name, ddd, number_residence, district, state, password, email, phone, street, city, cep, conf_senha):
        self._id = id
        self._name = name
        self._ddd = ddd
        self._number_residence = number_residence
        self._district = district
        self._state = state
        self._password = password
        self._email = email
        self._phone = phone
        self._street = street
        self._city = city
        self._cep = cep
        self._conf_senha = conf_senha
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120) ,unique=True, nullable=False)
    ddd = db.Column(db.Integer ,unique=True, nullable=False)
    number_residence = db.Column(db.Integer ,unique=True, nullable=False)
    district = db.Column(db.String(120) ,unique=True, nullable=False)
    state = db.Column(db.String(120) ,unique=True, nullable=False)
    password = db.Column(db.String(120) ,unique=True, nullable=False)
    email = db.Column(db.String(120) ,unique=True, nullable=False)
    phone = db.Column(db.Integer ,unique=True, nullable=False)
    street = db.Column(db.String(120) ,unique=True, nullable=False)
    city = db.Column(db.String(120) ,unique=True, nullable=False)
    cep = db.Column(db.Integer ,unique=True, nullable=False)
    conf_senha = db.Column(db.String(120) ,unique=True, nullable=False)
