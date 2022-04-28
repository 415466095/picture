from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref
from werkzeug.security import check_password_hash, generate_password_hash
from database import Base
import uuid


class Operator(Base):
    # query = Base.query
    __tablename__ = 'operators'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), unique=False, nullable=False)
    alternativeID = Column(String(200), unique=True, nullable=False)

    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        # 加盐加密函数，通过随机产生不同salt(盐粒)混入原文，使每次产生的密文不一样。
        self.password = generate_password_hash(username + password)
        self.alternativeID = str(uuid.uuid1())

    def __repr__(self):
        return '<operator %r>' % self.username

    def verifyPassword(self, password=None):
        if password is None:
            return False
        return check_password_hash(self.password, self.username + password)


class OperatorSession(Base):
    __tablename__ = 'oper_sessions'
    id = Column(Integer, primary_key=True)
    sessionID = Column(String(200), nullable=False)
    exp_utc = Column(DateTime, nullable=False)
    operator_id = Column(Integer, ForeignKey('operators.id'), nullable=False)
    operator = relationship(Operator, backref=backref('operators',
                                                      uselist=True,
                                                      cascade='delete,all'))


class OperatorRank(Base):
    __tablename__ = 'oper_ranks'
    id = Column(Integer, primary_key=True)
    # sessionID = Column(String(200), nullable=False)
    # exp_utc = Column(DateTime, nullable=False)
    # operator_id = Column(Integer, ForeignKey('operators.id'), nullable=False)
    name = Column(String(200), nullable=False)
    picturebtye = Column(LargeBinary(length=(2 ** 32) - 1), nullable=False)
    rank = Column(FLOAT(precision=10, scale=2), nullable=True)
    # operator = relationship(Operator, backref=backref('operators',
    #                                                   uselist=True,
    #                                                   cascade='delete,all'))


class ObjectiveRank(Base):
    __tablename__ = 'oper_ObjectRank'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    rank = Column(Integer, nullable=True)
    operator_id = Column(String(200), nullable=False)

    def __init__(self, id=None, name=None, rank=None, operator_id=None):
        self.id = id
        self.name = name
        self.rank = rank
        self.operator_id = operator_id


class piclabel(Base):
    __tablename__ = 'oper_piclabel'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    label1 = Column(String(200), nullable=True)
    label2 = Column(String(200), nullable=True)
    label3 = Column(String(200), nullable=True)
    label4 = Column(String(200), nullable=True)
    label5 = Column(String(200), nullable=True)

    def __init__(self, id=None, name=None, label1=None, label2=None, label3=None, label4=None, label5=None):
        self.id = id
        self.name = name
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.label5 = label5
