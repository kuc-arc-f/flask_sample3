# 日本語

# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app1.config')

db = SQLAlchemy(app)

#views
import app1.views
import app1.views_user
import app1.views_admin
