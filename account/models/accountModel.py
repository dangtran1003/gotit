from account.controllers.validateToken import validateToken
from config import ERROR, SUCCESS
from models.dbModel import dbModel


class accountModel():
    @classmethod
    def register(cls, data):
        user_id = None
        user_id = validateToken.validate_token(data['access_token'], data['flag'])
        # print user_id
        if user_id != None:
            info_check = dbModel.query_one("SELECT email FROM account WHERE email='" + data['email'] + "'")
            if info_check['data'] == None:
                cls.helper_register(user_id, data['flag'], data['email'])
            else:
                return {"message": "Email existed", "error": 1}
            return SUCCESS

    @classmethod
    def helper_register(cls, user_id, flag, email):
        # facebook
        if flag == 0:
            info = dbModel.insert(
                "INSERT INTO account (email, facebook_id, status, type) VALUE ('%s','%s','%s','%s')" % (
                email, str(user_id), 0, str(flag)))
            if (info['success']):
                return SUCCESS
        # google
        elif flag == 1:
            info = dbModel.insert(
                "INSERT INTO account (email, google_id, status, type) VALUE ('%s','%s','%s','%s')" % (
                    email, str(user_id), 0, str(flag)))
            if (info['success']):
                return SUCCESS

    @classmethod
    def update_id(cls, data):
        email = data['email']
        token_1 = data['token_1']
        token_2 = data['token_2']
        flag = data['flag']
        user_id = validateToken.validate_token(token_2, flag)
        if user_id == None:
            return ERROR
        check_email = dbModel.query_one(
            "SELECT email FROM account WHERE google_id='" + user_id + "' OR facebook_id='" + user_id + "'")
        if check_email['data']['email'] == None or check_email['data']['email'] != email:
            return ERROR
        else:
            info = None
            if flag == 0:
                info = dbModel.update("UPDATE account SET google_id='" + token_1 + "'")
            elif flag == 1:
                info = dbModel.update("UPDATE account SET facebook_id = '" + token_1 + "'")
            if info['success']:
                return SUCCESS
        return 0

    @classmethod
    def update_info(cls, data):
        access_token = data['access_token']
        info_1 = data['info_1']  # name
        info_2 = data['info_2']  # phone or labor
        flag = data['flag']
        if info_1 == None or info_2 == None:
            return ERROR
        user_id = validateToken.validate_token(access_token, flag)
        if user_id == None:
            return ERROR
        # facebook
        if flag == 0:
            info = dbModel.update(
                "UPDATE account SET name='" + info_1 + "',phone='" + info_2 + "',status=1 WHERE facebook_id='" + user_id + "'")
            if info['success']:
                return SUCCESS
        # google
        elif flag == 1:
            if info_2 == 3:  # 1: hoc sinh,2 : giao vien, 3: khac
                info_3 = data['info_3']  # labor khac
                info = dbModel.update(
                    "UPDATE account SET name='" + info_1 + "',labor='" + info_2 + "',note='" + info_3 + "'status=1 WHERE google_id='" + user_id + "'")
            else:
                info = dbModel.update(
                    "UPDATE account SET name='" + info_1 + "',labor='" + info_2 + "',status=1 WHERE google_id='" + user_id + "'")
            if info['success']:
                return SUCCESS

    @classmethod
    def login(cls, data):
        access_token = data['access_token']
        flag = data['flag']
        user_id = validateToken.validate_token(access_token, flag)
        if user_id == None:
            return {"message": "Login false", "error": 1}
        info = dbModel.query_one(
            "SELECT * FROM account WHERE facebook_id ='" + user_id + "' OR google_id ='" + user_id + "'")
        if (info['data'] != None):
            return info['data']
