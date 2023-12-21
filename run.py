# run.py
from flask import Flask
from config import ConfigDataBase
from app.models import create_tables

app = Flask(__name__)
app.config.from_object(ConfigDataBase)

create_tables()

from app.views import *