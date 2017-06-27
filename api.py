from flask import Flask, jsonify, request
from peewee import MySQLDatabase, RawQuery
from courtcases.moldova_courtcases_db import *
application = Flask(__name__)

@application.before_request
def _db_connect():
    database.connect()

@application.teardown_request
def _db_close(exc):
    if not database.is_closed():
        database.close()

def getCourtcases(q):
    rq = Courtcase.select().where(Courtcase.title.contains(q)).limit(100)
    result = []
    for row in rq:
        result.append({
            "title": row.title,
            "court": row.courtName,
            "caseNumber": row.caseNumber,
            "caseType": row.caseType,
            "theme": row.theme,
            "deliveryDate": row.deliveryDate,
        })
    return result

def getCourtcasesCount(q):
    casecount = Courtcase.select().where(Courtcase.title.contains(q)).count()
    return str(casecount)

@application.route('/courtcases')
def courtcases():
    q = request.args.get('q')   
    return jsonify(getCourtcases(q))

@application.route('/courtcasescount')
def courtcasescount():
    q = request.args.get('q')   
    return getCourtcasesCount(q)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8090)
