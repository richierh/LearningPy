# /usr/bin/env python
from peewee import *

database = SqliteDatabase("my_app.db")

class BaseModel(Model):
    class Meta :
        database=database


class User(BaseModel):
    username =  CharField()


class Tweet(BaseModel):
    user = ForeignKeyField(User,related_name="tweets")
    message = TextField()
