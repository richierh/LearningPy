#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:23:41 2017

@author: pmc
"""

from pony.orm import*

db = Database()

db.bind('sqlite', 'mydb', create_db=True)
db.generate_mapping(create_tables=True)

sql_debug(True)