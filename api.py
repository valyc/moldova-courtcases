from flask import Flask, jsonify, request
from peewee import MySQLDatabase, RawQuery
from courtcases.moldova_courtcases_db import *
app = Flask(__name__)

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

@app.route('/courtcases')
def courtcases():
    q = request.args.get('q')   
    return jsonify(getCourtcases(q))

@app.route('/courtcasescount')
def courtcasescount():
    q = request.args.get('q')   
    return getCourtcasesCount(q)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)