#!/usr/bin/env python3
# coding:UTF-8
""" ponchiki/__init__.py """


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

