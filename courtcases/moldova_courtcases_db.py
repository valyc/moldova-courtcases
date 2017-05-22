from peewee import *
from dbconfig import * 

database = MySQLDatabase(DATABASE_NAME, **{'host': '127.0.0.1', 'password': DATABASE_PASSWORD, 'port': 3306, 'user': DATABASE_USERNAME})

class Courtcase(Model):
    courtName  = CharField()
    caseNumber  = CharField()
    deliveryDate  = CharField()
    createdDate  = CharField()
    publishedDate  = CharField()
    title  = CharField()
    caseType  = CharField()
    theme  = CharField()
    pdfFile = CharField()

    class Meta:
        database = database

Courtcase.create_table(True)
