from datetime import datetime

from common import config

from peewee import *
from playhouse.postgres_ext import *


db = config()['db-postgre']

database_postgre = PostgresqlExtDatabase(
    db['name'],
    user=db['user'],
    password=db['password'],
    host=db['hostname'],
    port=db['port']
)


class BaseModel(Model):
    class Meta:
        database = database_postgre

class Rents(BaseModel):
    id = IntegerField()
    site = CharField()
    url = TextField()
    state = TextField(null=True)
    city = TextField(null=True)
    neighborhood = TextField(null=True)
    rooms = IntegerField(default=None)
    bathrooms = FloatField(default=None)
    parking = IntegerField(default=0)
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)
    content = TextField(null=True)
    title = TextField(null=True)

def create_table():
    Rents.create_table()