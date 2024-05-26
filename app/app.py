from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # создание экземпл приложения с указанием на текущий файл (__name__)
app.config.from_object(Configuration)  # передача конфигурации из файла config.py
db = SQLAlchemy(app)  # связывание базы данных с текущим проектом flask
