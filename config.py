#!/usr/bin/env python3
# encoding: utf-8
"""
@license: Apache Licence
@author: andy cheng
@file: config.py
@time: 5/20/18 7:25 PM
"""
import os

DEBUG = True
SECRET_KEY = os.urandom(24)
DRIVER = 'pymysql'
DIALECT = 'mysql'
DATABASE = '    '
USERNAME = 'root'
PASSWORD = '5032'
HOST = '127.0.0.1'
PORT = '3306'
# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:5032@127.0.0.1/blogger"
SQLALCHEMY_TRACK_MODIFICATIONS = False