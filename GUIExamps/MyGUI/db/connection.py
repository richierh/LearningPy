#!/usr/bin/env python
"""
Code file ini berfungsi untuk membuat semua entitas databases yang dibuat 
menggunakan ERD (Entity Relational Diagram) PonyORM Tools terdata/map ke
dalam databases sqlite,mysqlite, atau yang lainnya

"""

from pony.orm import *
from ormpony import *


class connectdb():

    def __init__(self):
        db.bind(provider='sqlite', filename='mydatabase.sqlite', create_db=True)
       
        show(DataPersonal)
        # sql_debug digunakan untuk mengetahui proses yang terjadi selama 
        # program di jalankan
        sql_debug(True)

        """create_tables=True adalah metode untuk mempertahankan entitas
        database pada suatu table yang sudah dibuat
        """ 
        db.generate_mapping(create_tables=True)


