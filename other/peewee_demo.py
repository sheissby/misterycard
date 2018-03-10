# encoding: utf-8
from peewee import *
from datetime import date

db = MySQLDatabase(host='localhost', port=3305, user='root', passwd='', database='people')


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

db.connect()

uncle_bob = Person(name='bob', birthday=date(1960, 1, 5), is_relative=True)
uncle_bob.save()

kitty = Person.create(name='kitty', birthday=date(1988, 1, 1), is_relative=False)
db.close()


