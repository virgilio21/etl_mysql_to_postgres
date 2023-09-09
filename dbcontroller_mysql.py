from datetime import datetime

from common import config

from peewee import *


db = config()['db-mysql']

database_mysql = MySQLDatabase(
    db['name'],
    user=db['user'],
    password=db['password'],
    host=db['hostname'],
    port=db['port']
)


class BaseModel(Model):
    class Meta:
        database = database_mysql


class Rents(BaseModel):
    site = CharField()
    url = TextField(unique=True)
    state = TextField(null=True)
    city = TextField(null=True)
    neighborhood = TextField(null=True)
    rooms = IntegerField(default=None)
    bathrooms = FloatField(default=None)
    parking = IntegerField(default=0)
    latitude = FloatField()
    longitude = FloatField()
    content = TextField(null=True)
    title = TextField(null=True)

def create_table():
    Rents.create_table()