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
DIALECT = 'sqlite3'
DATABASE = 'database'
SQLALCHEMY_DATABASE_URI = "{}:///{}".format(DIALECT, DATABASE)
