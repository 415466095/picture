import base64
import re
import time
import json
from flask import Blueprint, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from pandas import np
from werkzeug.datastructures import CombinedMultiDict
import base64
from rank import finalrank, lighting, duibidus, objectassessment, evaluate_rank
from liangdu import read_path
from duibidu import duibidu
from otherobject import mains

from user import User, USERS, Picture, MyEncoder
from jwt_token import genToken, verfiyToken
from database import init_db, db_session
from evaluate_inception_resnet import run

login_page = Blueprint('login_page', __name__)

login_manager = LoginManager()
login_manager.login_view = 'helloworld'


@login_page.record_once
def on_load(state):
    login_manager.init_app(state.app)


# @login_manager.user_loader
# def load_user(user_id):
#   return User.get(user_id)

# 下面为验证用户是否登录在线的逻辑/在第一次进入界面的时候会设置一个初始的cookie来防止前端路由得不到flask回应导致500
@login_manager.request_loader
def load_user_from_request(request):
    token = request.headers.get('Authorization')
    if token == 'undefined':
        return None
    if token == None:
        return None
    # print(token)
    payload = User.verfiyUserToken(token)
    # users = User.getuser(11)
    # print(current_user)
    # print(payload)
    if payload != None:
        alternativeID = payload['data']['alternativeID']
        sessionID = payload['data']['sessionID']
        user = User.queryUser(alternativeID=alternativeID, sessionID=sessionID)
    else:
        user = None
    return user


# 登录状态的确认
@login_page.route('/first')
@login_required
def firstPage():
    returnData = {'code': 0, 'msg': 'success',
                  'data': {'token': current_user.token,
                           'tips': current_user.userName}}
    return returnData, 200


# 登录逻辑，查询用户是否存在，并验证密码，加入token
@login_page.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        user = User.queryUser(userName=username)
        print(user)
        if (user != None) and (user.verifyPassword(password)):
            print("sadsdasda")
            login_user(user)
            msg = True
            users = username
            # token = genToken({'username': username, 'password': '******'})
            returnData = {'code': 0, 'msg': msg, 'data': {'token': user.token}, 'user': users}
            return json.dumps(returnData), 200
        else:
            msg = False
            returnData = {'code': 1, 'msg': msg, 'data': 'password is not correct,please try again'}
            return json.dumps(returnData), 200


@login_page.route('/finduser', methods=['POST'])
def finduser():
    if request.method == 'POST':
        username = request.form['username']
        # password = request.form['password']
        print(username)
        user = User.queryused(userName=username)
        if not user:
            msg = False
            returnData = {'code': 3, 'msg': 'success',
                          'data': {'msg': msg, 'data': 'This account does not exist,please check it again.'}}
            return returnData, 200
        else:
            msg = True
            returnData = {'code': 4,
                          'data': {'msg': msg, 'data': 'welcome!'}}
            return returnData, 200


# 增加新用户
@login_page.route('/adduser', methods=['POST'])
def adduser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        user = User.queryall(userName=username, password=password)
        if user is None:
            returnData = {'code': 2, 'msg': 'success', 'data': '已成功注册!'}
            return returnData, 200
        else:
            msg = "该用户已注册，请直接登录!"
            returnData = {'code': 2, 'msg': 'success', 'data': msg}
            return returnData, 200


# 用户注销
@login_page.route('/logout')
@login_required
def logout():
    username = current_user.userName
    # alternativeID = current_user.alternativeID
    sessionID = current_user.sessionID
    User.dropSessionID(sessionID)
    logout_user()
    returnData = {'code': 0, 'msg': 'success', 'data': {'tips': 'Bye ' + username}}
    return json.dumps(returnData), 200


## 以下为评分组件逻辑
@login_page.route('/sum')
# @login_required
def sum():
    # if request.method == 'GET':
    #     t = request.form
    # sums = finalrank(evaluate_rank(), lighting(), duibidus(), objectassessment())
    sums = 's'
    print(sums)
    returnData = {'code': 0, 'msg': 'success', 'data': sums}
    return json.dumps(returnData), 200


# 对上传的图片计算客观总分
@login_page.route('/rankpic', methods=['POST'])
# @login_required
def ranks():
    news = request.form.to_dict()
    list1 = []
    list2 = []
    dicts = {}
    for i in news.items():
        if re.search(r'name', i[0]):
            list1.append(i[1])
        else:
            list2.append(i[1])
    dicts = dict(zip(list1, list2))
    s = {}
    l1 = []
    l2 = []
    for i in dicts:
        l1.append(i)
        l2.append(dicts[i].split(',')[1])
    s = dict(zip(l1, l2))
    # rank1为模型跑出的评分
    rank1 = run(s)
    # rank2为亮度
    rank2 = read_path(s)
    # rank3为对比度
    rank3 = duibidu(s)
    # rank4为其他客观评价标准分数
    rank4 = mains(s)
    ultimate = finalrank(evaluate_rank(rank1), lighting(rank2), duibidus(rank3), objectassessment(rank3))
    print(ultimate)
    rankin = []
    for i in rank1:
        new1 = np.float64(ultimate[i]).item()
        # print(new1)
        rankin.append(new1)
    # 下面是入库操作
    t = 0
    finals = {}
    for i in dicts:
        dicts[i] = dicts[i].split(',')[1]
        page_content = base64.b64decode(dicts[i])
        Picture.ranktable(name=i, byte=page_content, rank=rankin[t])
        t = t + 1
    if request.method == 'POST':
        print("说明有数据！！")
        # print(type(request.values))

    returnData = {'code': 0, 'msg': 'success', 'data': ultimate}
    return json.dumps(returnData), 200


# 主客观最终融合
@login_page.route('/getpic', methods=['POST'])
def getpic():
    msg, p = Picture.indexpic()
    lists = []
    print(type(msg))
    t = 0
    print(p)
    # 这里为客观分数区间映射
    k = float(5 / (max(p) - min(p)))
    t1 = "%.2f" % k
    t1 = float(t1)
    print(t1)
    transform_value = [round(t1 * (x - min(p)), 2) for x in p]
    # 这里为主观分数映射
    newlist = []
    for i in msg:
        newlist.append(i)
    substantial = {}
    substantial = dict(zip(newlist, transform_value))
    objectiverank = User.zhuguan(newlist)
    marger = {}
    for i in objectiverank:
        if objectiverank[i] == 0:
            marger[i] = substantial[i]
        else:
            marger[i] = round((objectiverank[i] * 0.8 + substantial[i] * 0.2), 2)
    # print(marger)
    for i in msg:
        lists.append({'name': i, 'url': msg[i], 'rank': marger[i]})
        # print(p[t])
        t = t + 1
        # print(msg[i])
    returnData = {'code': 0, 'msg': 'success', 'data': lists}
    return json.dumps(returnData, cls=MyEncoder, indent=4), 200


# 修改密码相关逻辑
# @login_page.route('/changepws')
# @login_required
# def changepws():
#   return json.dumps(returnData),200

# 图片主观评分
@login_page.route('/accountstar', methods=['POST'])
@login_required
def accountstar():
    if request.method == 'POST':
        picname = request.form['name']
        picstar = request.form['star']
        username = current_user.userName
        print(picname)
        print(picstar)
        print(username)
        msg = User.objectiveranks(name=picname, rank=picstar, operator_id=username)
        # user = User.queryused(userName=username)
        # if not user:
        #     msg = False
        #     returnData = {'code': 3, 'msg': 'success',
        #                   'data': {'msg': msg, 'data': 'This account does not exist,please check it again.'}}
        #     return returnData, 200
        # else:
        returnData = {'code': 4, 'data': {'msg': msg, 'data': 'welcome!'}}
        return returnData, 200
    else:
        print("uuu")


# 标签存储
# labels
@login_page.route('/labels', methods=['POST'])
@login_required
def labels():
    if request.method == 'POST':
        picname = request.form['name']
        label = request.form['label']
        # username = current_user.userName
        print(picname)
        print(label)
        newp = User.label(name=picname, label=label)
        # if newp == 'full':
        #     msg = "这张图的标签已经满啦"
        returnData = {'code': 4, 'data': {'msg': newp, 'data': 'welcome!'}}
        return returnData, 200
    else:
        print("uuu")


# 标签搜索

@login_page.route('/getlabel', methods=['POST'])
@login_required
def getlabel():
    if request.method == 'POST':
        label = request.form['name']
        # print(label)
        list1 = User.match(label)
        if list1 == 1:
            msg1 = "没有找到相关标签的图片!"
            returnData = {'code': 2, 'msg': 'notfound', 'data': msg1}
            return returnData, 200
        else:
            msg, p = Picture.indexpic()
            # 找分
            lists = {}
            print(type(msg))
            t = 0
            # print(p)
            # 这里为客观分数区间映射
            k = float(5 / (max(p) - min(p)))
            t1 = "%.2f" % k
            t1 = float(t1)
            transform_value = [round(t1 * (x - min(p)), 2) for x in p]
            # 这里为主观分数映射
            newlist = []
            for i in msg:
                newlist.append(i)
            substantial = {}
            substantial = dict(zip(newlist, transform_value))
            objectiverank = User.zhuguan(newlist)
            marger = {}
            for i in objectiverank:
                if objectiverank[i] == 0:
                    marger[i] = substantial[i]
                else:
                    marger[i] = round((objectiverank[i] * 0.8 + substantial[i] * 0.2), 2)
            # print(marger)
            result = {}
            for i in list1:
                for j in msg:
                    if i == j:
                        result[i] = msg[j]
            list2 = []
            sums = 0
            for i in result:
                for j in marger:
                    if i == j:
                        lists[i] = marger[j]
            # print(lists) !!!lists保存着匹配到的图片与其评分
            for i in result:
                list2.append({'name': i, 'url': result[i], 'rank': lists[i]})
                # print(p[t])
                # print(i, lists[i])
            returnData = {'code': 0, 'msg': 'success', 'data': list2}
            return json.dumps(returnData, cls=MyEncoder, indent=4), 200
    else:
        print("uuu")
        return "出错"
