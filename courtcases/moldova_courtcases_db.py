from peewee import *
from dbconfig import * 

database = MySQLDatabase(DATABASE_NAME, **{'host': '127.0.0.1', 'password': DATABASE_PASSWORD, 'port': 3306, 'user': DATABASE_USERNAME})

class Courtcase(Model):
    courtName  = CharField()
    caseNumber  = CharField()
    deliveryDate  = CharField()
    createdDate  = CharField()
    publishedDate  = CharField()
    title  = TextField()
    caseType  = CharField()
    theme  = CharField()
    pdfFile = CharField()

    class Meta:
        database = database
# create table is not created already, if present, True will fail silently
Courtcase.create_table(True)
