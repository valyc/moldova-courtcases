from peewee import *

database = MySQLDatabase('moldova_courtcases', **{'host': '127.0.0.1', 'password': 'root123', 'port': 3306, 'user': 'root'})

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
