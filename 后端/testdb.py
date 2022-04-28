from flask import Flask, jsonify, Blueprint
from database import init_db,db_session
from models import Operator
from database import Base

# app = Flask(__name__)
testdb_page = Blueprint('testdb_page',__name__)


@testdb_page.route('/initdb')
def initdb():
  print("创建")
  init_db()
  return 'init_db'

@testdb_page.route('/addoper')
def addOper():
  oper = Operator(1,'admin', '123')
  db_session.add(oper)
  db_session.commit()
  return 'addOper'

@testdb_page.route('/verifypws/<pws>')
def verifyPassword(pws):
   oper = Operator.query.filter_by(username='admin').first()
   return str(oper.verifyPassword(pws))

# if __name__ == '__main__':
#     # app.run(host='127.0.0.1',port=5000)
#     testdb_page.