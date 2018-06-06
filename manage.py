#!/usr/bin/env python3
# encoding: utf-8
"""
@license: Apache Licence
@author: andy cheng
@file: manage.py
@time: 5/26/18 9:44 PM
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from models import User


manager = Manager(app)

# use Migrate connect app to db
migrate = Migrate(app, db)

# add script command to manager
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

