import jwt
from jwt import exceptions
from datetime import datetime, timedelta

# jwt=api_jwt.PyJWT
PyJwtError = exceptions.PyJWTError
SECRECT_KEY = b'\x92R!\x8e\xc6\x9c\xb3\x89#\xa6\x0c\xcb\xf6\xcb\xd7\xbc'


def genToken(exp, data):
    # expInt = datetime.utcnow() + timedelta(seconds=3)
    # token设置一个小时有效期
    # expInt = datetime.now() + timedelta(seconds=3600)
    # print(data)
    payload = {
        'exp': exp,
        'data': data
    }
    token = jwt.encode(payload, key=SECRECT_KEY, algorithm='HS256')
    token = bytes(token, encoding='utf8')
    return bytes.decode(token)


def verfiyToken(tokenStr):
    try:
        tokenBytes = tokenStr.encode('utf-8')
        payload = jwt.decode(tokenBytes, key=SECRECT_KEY, algorithms='HS256')
        return payload
    except PyJwtError as e:
        print("jwt验证失败: %s" % e)
        return None
