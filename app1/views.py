# 日本語

# coding: utf-8
#
from flask import request, redirect, url_for, render_template, flash
from app1 import app, db
from app1.models.entry import Entry
#from app1.models.task import Task
#from app1.models.book import Book
#
@app.route('/')
def route_call():
    return "Hello, Flask! "


