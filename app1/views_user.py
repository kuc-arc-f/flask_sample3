# 日本語

# coding: utf-8
#
from flask import request, redirect, url_for, render_template, flash
from app1 import app, db
#from flaskr.models.entry import Entry
#from flaskr.models.task import Task
#from flaskr.models.book import Book

#
@app.route('/user_test')
def user_test():
    from app1.include.test_class import  TestClass
    te= TestClass()
    te.test()
    return "user_test"



