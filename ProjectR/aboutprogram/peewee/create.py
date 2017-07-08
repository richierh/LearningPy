# /usr/bin/env python

from peewee import *

# Peewee doesn't able to create database.db just like any other ORM does,
#  you have to create it manually. Peewee only able to create table and
# get connected to the existing database.
db = SqliteDatabase("database.db")


# This is the place to make a database class model for the table
# that we will used

class manusia (Model):
    nama = CharField()
    usia = IntegerField()
    tgllhr = DateField()
    jeniskelamin = CharField()
    alamat = CharField()

    class Meta:
        database = db

class barang(Model):
    a = CharField()
    jenis = CharField()
    satuan = CharField()
    jmlsatuan = IntegerField()
    hrgjual = IntegerField()
    keterangan = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([manusia, barang])
