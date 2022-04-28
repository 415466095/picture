# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from flask import Flask, jsonify
import MySQLdb
import json
import pymysql
from flask_cors import CORS
from sqlalchemy.testing import db

from testdb import testdb_page
from login import login_page

# 连接数据库
pymysql.install_as_MySQLdb()

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(login_page)
app.register_blueprint(testdb_page)
app.secret_key =b'\x15f\x07\xd3\xd9\xbf*\x82\xd1\xe6\xb4\xf2\x95\xdd\x8f\x12'

@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify('Hello World!!!!')

@app.route('/son', methods=['GET'])
def nmsl():
    return jsonify('nmsl!!!!')

@app.route('/hello')
def helloworld():
  returnData = {'code': 0, 'msg': 'success', 'data': 'hello world' }
  return json.dumps(returnData),200


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1234,debug=True,threaded=False)

