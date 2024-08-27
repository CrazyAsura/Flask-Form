import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DB_URL="mysql://root:Nero@3355@localhost/python"