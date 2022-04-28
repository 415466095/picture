import base64
import json
import re
import uuid

from MySQLdb.cursors import Cursor
from flask_login import UserMixin
from sqlalchemy import and_
from werkzeug.security import check_password_hash, generate_password_hash
from jwt_token import genToken, verfiyToken
from datetime import datetime, timedelta, time
from models import Operator, OperatorSession, OperatorRank, ObjectiveRank, piclabel
# from test.database import db_session
from database import init_db, db_session
# from 后端.search import fuzzy_finder

USERS = [
    {
        "id": 1,
        "name": "admin",
        "password": generate_password_hash('123'),
        "alternativeID": generate_password_hash('1' + generate_password_hash('123')),
        "sessionID": []
    },
    {
        "id": 2,
        "name": "李四",
        "password": generate_password_hash('123'),
        "alternativeID": generate_password_hash('2' + generate_password_hash('123')),
        "sessionID": []
    },
]

def fuzzy_finder(key, data):
    """
    模糊查找器
    :param key: 关键字
    :param data: 数据
    :return: list
    """
    result=[]
    pattern = '.*%s.*'%(key)
    # 编译正则表达式
    regex = re.compile(pattern)
    i=0
    for cla in data:
        for item in cla:
            match = regex.search(item)
            if match:
                result.append(i)
        i+=1
    result = list(set(result))# 去重
    return result



class User(UserMixin):
    def __init__(self, operator, sessionID=None):
        # self.id = user.get("id")
        # self.userName = user.get("name")
        # self.password_hash = user.get("password")
        # self.alternativeID = user.get("alternativeID")
        # self.sessionID = None
        # self.token = None
        # self.oper = user
        # self.sessionID = None
        # self.token = None
        # self.clearOvertimeSeesionID(user)

        self.id = operator.id
        self.userName = operator.username
        self.alternativeID = operator.alternativeID
        # oper为当前操作的数据库数据对象
        self.oper = operator
        # 每个用户的有效时间
        exp = datetime.now() + timedelta(seconds=3600)
        self.genSessionID(exp, sessionID)
        self.genToken(exp)

    def get_id(self):
        return self.id

    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        # for oper in USERS:
        #     if str(oper.get('id')) == str(user_id):
        #         return User(oper)
        user = Operator.query.filter_by(id=user_id).first()
        # print('None')
        return User(user)

    # 验证密码
    def verifyPassword(self, password):
        # if self.password_hash is None:
        #     return False
        return self.oper.verifyPassword(password)

    # 为登录的对象设置session，可以理解为cookie，记录该次登录的时间等操作
    def genSessionID(self, exp, sessionID=None):
        if sessionID == None:
            print("enter")
            self.sessionID = str(uuid.uuid4())
            os = OperatorSession(sessionID=self.sessionID, exp_utc=exp, operator=self.oper)
            db_session.add(os)
            # self.oper["sessionID"].append({'id':self.sessionID,'exp':exp})
            db_session.commit()
        else:
            print(">>>")
            self.sessionID = sessionID

    def genToken(self, exp):
        token = genToken(exp, {'alternativeID': self.alternativeID, 'sessionID': self.sessionID})
        self.token = token
        # 这里的token包括了用户数据的sessionID
        # print(self.token)
        return token

    # 查找是否存在该用户，存在就返回该数据库对象
    @staticmethod
    def queryUser(**kwargs):
        # if 'userID' in kwargs:
        #     return User.queryUserByID(kwargs['userID'])
        if 'userName' in kwargs:
            print('1')
            username = kwargs['userName']
            user = Operator.query.filter_by(username=username).first()
            return User(user)
        elif ('alternativeID' in kwargs) and ('sessionID' in kwargs):
            print('2')
            alternativeID = kwargs['alternativeID']
            sessionID = kwargs['sessionID']
            user = db_session.query(Operator).filter_by(alternativeID=alternativeID).join(OperatorSession).filter_by(
                sessionID=sessionID).first()
            db_session.close()
            if user:
                print('3')
                return User(user, sessionID)
            # return User.queryUserBySessionID(kwargs['alternativeID'], kwargs['sessionID'])
            else:
                print('4')
                return None

    # 增加用户逻辑
    @staticmethod
    def queryall(**kwargs):
        if 'userName' in kwargs:
            username = kwargs['userName']
            password = kwargs['password']
            user = Operator.query.filter_by(username=username).first()
            if user is None:
                # print(password)
                newuser = Operator(Operator.query.count() + 1, username, password)
                # print(Operator.query.all())
                # print(Operator.query.count())
                db_session.add(newuser)
                db_session.commit()
            return user
        else:
            return "Error!"

    # 查找用户
    @staticmethod
    def queryused(**kwargs):
        if 'userName' in kwargs:
            username = kwargs['userName']
            user = Operator.query.filter_by(username=username).first()
            if user is None:
                return False
            return True
        else:
            return "Error!"

    @staticmethod
    def verfiyUserToken(token):
        payload = verfiyToken(token)
        print(payload)
        if not payload:
            print("来验证是否超时，如果有,进行删除操作")
            removeSessions = db_session.query(OperatorSession).filter(
                OperatorSession.exp_utc > (datetime.now() + timedelta(hours=0.5))).delete(synchronize_session=False)
            print(removeSessions)
            # print('1123')
            # if removeSessions is None:
            #     print('无')
            # db_session.delete(removeSessions)
            db_session.commit()
        # print(payload)
        return payload

    def objectiveranks(**kwargs):
        if 'name' in kwargs:
            name = kwargs['name']
            rank = kwargs['rank']
            username = kwargs['operator_id']
            print(name, rank, username, '666')
            for i in OperatorRank.query.filter_by(name=name).all():
                print(i.rank)
            if ObjectiveRank.query.filter_by(name=name):
                # flag = 0
                for i in ObjectiveRank.query.filter_by(name=name).all():
                    # print(i.operator_id)
                    if i.operator_id == username:
                        print("同一个人评论一个了！修改吧。")
                        # user = ObjectiveRank.query.filter_by(name=i.name).update({"rank": rank})
                        i.rank = rank
                        db_session.commit()
                        # 评分有改动，过滤出所有参与该评分的项目然后四舍五入
                        flag = 0
                        accumulate = 0
                        # for j in ObjectiveRank.query.filter_by(name=name).all():
                        #     flag = flag + 1
                        #     accumulate += j.rank
                        # newrank = accumulate / flag
                        # print(newrank)
                        return "评分已更新"
                newuser = ObjectiveRank(ObjectiveRank.query.count() + 1, name, rank, username)
                db_session.add(newuser)
                db_session.commit()
                return "同作品不同人"
            else:
                newuser = ObjectiveRank(ObjectiveRank.query.count() + 1, name, rank, username)
                db_session.add(newuser)
                db_session.commit()
                return "不同作品人也许一样"

        else:
            return "Error!"

# 返回用户主观打分（已加权平均）的字典
    @staticmethod
    def zhuguan(newlist):
        dic2 = []
        dic1 = newlist
        dict1 = {}
        for i in newlist:
            flag = 0
            accumulate = 0
            for j in db_session.query(ObjectiveRank).all():
                # print(i.operator_id)
                # 评分有改动，过滤出所有参与该评分的项目然后四舍五入
                # flag = flag + 1
                # accumulate += i.rank
                if i == j.name:
                    flag = flag + 1
                    accumulate += j.rank
            if accumulate:
                newrank = accumulate / flag
                dic2.append(newrank)
            else:
                dic2.append(0)
        dict1 = dict(zip(dic1,dic2))
        # print(dict1)
        return dict1

    @staticmethod
    def label(**kwargs):
        name = kwargs['name']
        label = kwargs['label']
        exist = piclabel.query.filter_by(name=name).first()
        if exist is None:
            # 第一次给一张图添加标签方式
            newuser = piclabel(piclabel.query.count() + 1, name, label)
            db_session.add(newuser)
            db_session.commit()
            return "添加成功"
        else:
            for i in db_session.query(piclabel).all():
                if i.name == name:
                    if i.label1 is not None and i.label1 != label:
                        if i.label2 is None:
                            i.label2 = label
                            db_session.commit()
                            return '添加成功'
                        else:
                            if i.label2 == label:
                                return "该标签已存在"
                            if i.label3 is None:
                                i.label3 = label
                                db_session.commit()
                                return '添加成功'
                            else:
                                if i.label3 == label:
                                    return "该标签已存在"
                                if i.label4 is None:
                                    i.label4 = label
                                    db_session.commit()
                                    return '添加成功'
                                else:
                                    if i.label4 == label:
                                        return "该标签已存在"
                                    if i.label5 is None:
                                        i.label5 = label
                                        db_session.commit()
                                        return '添加成功'
                                    else:
                                        if i.label5 == label:
                                            return "该标签已存在"
                                        return "full"
                    else:
                        return "该标签已存在"

    @staticmethod
    def match(name):
        list1 = []
        list2 = []
        list3 = []
        exist = db_session.query(piclabel).all()
        for i in exist:
            list3.append(i.name)
            t1 = i.label1
            t2 = i.label2
            t3 = i.label3
            t4 = i.label4
            t5 = i.label5
            if t1 is None:
                t1=''
            if t2 is None:
                t2=''
            if t3 is None:
                t3=''
            if t4 is None:
                t4=''
            if t5 is None:
                t5=''
            list1 = [t1, t2, t3, t4, t5]
            list2.append(list1)
        # print(list2)
        result = fuzzy_finder(name, list2)
        finalresult = []
        if result:
            dict1 = dict(zip(list3,list2))
            for i in result:
                finalresult.append(list3[i])
            # print(dict1)
            # print(finalresult)
            return finalresult
        else:
            return 1
        # print(name)

    @staticmethod
    def dropSessionID(sessionID):
        removeSession = db_session.query(OperatorSession).filter_by(sessionID=sessionID).first()
        db_session.delete(removeSession)
        db_session.commit()


class Picture:
    def __init__(self, operator):
        self.id = operator.id
        self.name = operator.name
        self.byte = operator.byte
        self.rank = operator.rank
        # oper为当前操作的数据库数据对象
        self.oper = operator
        # 每个用户的有效时间

    @staticmethod
    def ranktable(name, byte, rank=None):
        if name is not None:
            print("进入")
            print(name, rank)
            # sessionID=self.sessionID, exp_utc=exp, operator=self.oper
            user = OperatorRank.query.filter_by(name=name).first()
            if user is None:
                os = OperatorRank(id=OperatorRank.query.count() + 1, name=name, picturebtye=byte, rank=rank)
                db_session.add(os)
                # self.oper["sessionID"].append({'id':self.sessionID,'exp':exp})
                db_session.commit()
            return user
        else:
            print("!!>")
            return "失败"

    # 前端传来的图片编码这里去获取评分！！！！
    @staticmethod
    def torank():
        return 1

    @staticmethod
    def indexpic():
        t = OperatorRank.query.all()
        list1 = []
        list2 = []
        list3 = []
        # 分数映射
        dicts = {}
        for i in t:
            list1.append(i.name)
            list2.append(base64.b64encode(i.picturebtye))
            list3.append(i.rank)

        dicts = dict(zip(list1, list2))

        return dicts, list3


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

# 自定义评价逻辑
# class Objectrank(UserMixin):
#     def __init__(self, operator, sessionID=None):
#         # self.id = operator.id
#         # self.name = operator.name
#         # self.rank = operator.rank
#         # # oper为当前操作的数据库数据对象
#         # self.oper = operator
#         self.oper = None
#         self.id = operator.id
#         self.userName = operator.username
#         self.alternativeID = operator.alternativeID
#         self.rank = operator.rank
#         # oper为当前操作的数据库数据对象
#         # self.name = operator.name
#         # 每个用户的有效时间
#         name = operator.name
#         self.oper = operator
#         # exp = datetime.now() + timedelta(seconds=3600)
#         self.objectable(name, self.rank, sessionID)
#         self.genToken(name)
#
#     def objectable(self, name,rank,sessionID=None):
#         if sessionID == None:
#             print("enter")
#             self.sessionID = str(uuid.uuid4())
#             user = OperatorSession.query.filter_by(name=name).first()
#             if user is None:
#                 os = OperatorSession(id=ObjectiveRank.query.count() + 1, name=name, rank=rank, operator=self.oper)
#                 db_session.add(os)
#             # self.oper["sessionID"].append({'id':self.sessionID,'exp':exp})
#                 db_session.commit()
#             return user
#         else:
#             print(">>>")
#             self.sessionID = sessionID
#
#     def genToken(self, exp):
#         token = genToken(exp, {'alternativeID': self.alternativeID, 'sessionID': self.sessionID})
#         self.token = token
#         # 这里的token包括了用户数据的sessionID
#         # print(self.token)
#         return token

# def objectable(self, name, rank):
#     if name == None:
#         print("xxxxxx")
#         # self.sessionID = str(uuid.uuid4())
#         user = OperatorSession.query.filter_by(name=name).first()
#         if user is None:
#             os = OperatorSession(id=ObjectiveRank.query.count() + 1, operator=self.oper)
#             db_session.add(os)
#         # self.oper["sessionID"].append({'id':self.sessionID,'exp':exp})
#             db_session.commit()
#         return user
#     else:
#         print(">>>")
