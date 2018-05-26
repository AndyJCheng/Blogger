#!/usr/bin/env python3
# encoding: utf-8
"""
@license: Apache Licence
@author: andy cheng
@file: updatesize.py
@time: 5/26/18 11:39 PM
"""
from PIL import Image


def resize(filein, fileout, width, height):
    img = Image.open(filein)
    out = img.resize((width, height), Image.ANTIALIAS)
    out.save(fileout)


if __name__ == '__main__':
    filein = 'zhiliao.jpg'
    fileout = 'zhiliao1.jpg'
    width = 90
    height = 50

    resize(filein, fileout, width, height)
