# -*- encoding: utf-8 -*-

from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

from app import views
