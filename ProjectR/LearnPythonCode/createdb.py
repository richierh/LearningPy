# /usr/bin/env python
import sqlite3
from peewee import *

#db = sqlite3.connect("databaseku.db")
db = SqliteDatabase("databaseku.db")


class Nuser(Model):
    nama = CharField()
    user = CharField()
    passd = CharField()
    tgl = DateField()

    class Meta():
        database = db


class Login(Model):
    login = ForeignKeyField(Nuser,related_name="userid")

    class Meta:
        database = db

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

        
db.connect()
db.create_tables([Nuser,Login,Pet,Person],True)
