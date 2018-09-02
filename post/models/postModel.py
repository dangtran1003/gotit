from account.controllers.validateToken import validateToken
from config import ERROR, SUCCESS
from models.dbModel import dbModel


class postModel():
    # viet bai
    @classmethod
    def write_post(cls, data):
        access_token = data['access_token']
        flag = data['flag']
        title = data['title']
        main = data['main']
        if title == None or main == None:
            return ERROR
        user_id = validateToken.validate_token(access_token, flag)
        info = dbModel.query_one(
            "SELECT email,status FROM account WHERE facebook_id='" + user_id + "' OR google_id='" + user_id + "'")
        if info['data']['status'] != 1:  # 1 :active
            return ERROR
        else:
            check_title = dbModel.query_one("SELECT title FROM post WHERE post_by ='" + info['data']['email'] + "'")
            if check_title['data'] != None:
                return ERROR
            else:
                info_insert = dbModel.insert(
                    "INSERT INTO post (title,main,post_by,count_liked,note) VALUE ('%s','%s','%s','%d','%s')" % (
                        title, main, info['data']['email'], 0, main[0:90]))
                return info_insert['success']

    # index
    @classmethod
    def list_post_all(cls):
        info = dbModel.query_all(
            "SELECT post.id_post as id, post.post_by as post_by, post.title as title, post.note as note, post.count_liked as count_liked,GROUP_CONCAT(post_liked.email) as email FROM post LEFT JOIN post_liked ON post_liked.id_post = post.id_post LIMIT 2")
            #     "SELECT post.id_post as id, post.post_by as post_by, post.title as title, post.note as note, post.count_liked as count_liked,(SELECT post_liked.email FROM post_liked WHERE post_liked.id_post = post.id_post LIMIT 2) as email FROM post")

        if info['success']:
            return info['data']

    # trang ca nhan
    @classmethod
    def list_post_user(cls, data):
        email = data['email']
        data = dbModel.query_one("SELECT id_post,title,note,count_liked FROM post WHERE post_by='" + email + "'")
        if data['success']:
            return data['data']

    # nhung nguoi like bai viet nay
    @classmethod
    def user_like_post(cls, data):
        id_post = data['id_post']
        info = dbModel.query_all("SELECT email FROM post_liked WHERE id_post='" + str(id_post) + "'")
        if info['success']:
            return info['data']

    # bai viet nguoi dung da like
    @classmethod
    def post_liked(cls, data):
        if data['email'] != None:
            posts_liked_by_user = dbModel.query_all(
                "SELECT id_post FROM post_liked WHERE post_by='" + data['email'] + "'")
            if posts_liked_by_user['success']:
                return posts_liked_by_user['id_post']

    # noi dung bai viet
    @classmethod
    def post_detail(cls, data):
        if data['id_post'] != None:
            info = dbModel.query_one(
                "SELECT id_post,title,main,count_liked FROM post WHERE id_post='" + str(data['id_post']) + "'")
            if info['success']:
                return info['data']

    # like bai
    @classmethod
    def like(cls, data):
        access_token = data['access_token']
        flag = data['flag']
        user_id = validateToken.validate_token(access_token, flag)
        info = dbModel.query_one(
            "SELECT email FROM account WHERE facebook_id='" + user_id + "' OR google_id='" + user_id + "'")
        if info['data']['email'] == None:
            return ERROR
        id_post = data['id_post']
        info_insert = dbModel.insert(
            "INSERT INTO post_liked (id_post, email) VALUE ('%s','%s') " % (id_post, info['data']['email']))
        if info_insert['success']:
            info_update = dbModel.update("UPDATE post SET count_liked=count_liked+1 WHERE id_post='" + str(id_post) + "'")
            if info_update['success']:
                return SUCCESS
        return ERROR

    # unlike
    @classmethod
    def unlike(cls, data):
        access_token = data['access_token']
        flag = data['flag']
        user_id = validateToken.validate_token(access_token, flag)
        info = dbModel.query_one(
            "SELECT email FROM account WHERE facebook_id='" + user_id + "' OR google_id='" + user_id + "'")
        if info['data']['email'] == None:
            return ERROR
        id_post = data['id_post']
        info = dbModel.delete(
            "DELETE FROM post_liked WHERE email='" + info['data']['email'] + "' AND id_post='" + str(id_post) + "'")
        if info['success']:
            info_update = dbModel.update("UPDATE post SET count_liked=count_liked-1 WHERE id_post='" + str(id_post) + "'")
            if info_update['success']:
                return SUCCESS
        return ERROR
