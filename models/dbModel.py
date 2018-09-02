# -*- coding: utf-8 -*-
import MySQLdb
from config import *

class dbModel():
    global connection

    def __init__(self):
        global connection
        self.connection = connection
    if True:
        connection = MySQLdb.connect(HOST_DATABASE, USER_DATABASE, PASS_DATABASE, NAME_DATABASE)
        connection.set_character_set('utf8mb4')
        print("connect BD success")

    @classmethod
    def insert(cls, sql):
        try:
            cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
            connection.commit()
            return {"success": True, "data": cursor.lastrowid}
        except Exception as db:
            print ("ERROR QUERY INSERT")
            print(str(db))
            return {"success": False, "message": str(db)}

    @classmethod
    def update(cls, sql):
        try:
            cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            return {"success": True, "data": []}
        except Exception as db:
            print ("ERROR UPDATE")
            print (db)
            print ("QR - " + sql)
            return {"success": False, "message": str(db)}

    @classmethod
    def delete(cls, sql):
        try:
            cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            return {"success" :True}
        except Exception as db:
            print ("ERROR QUERY DELETE")
            print (db)
            print ("QR - " + sql)
            return db

    @classmethod
    def query_one(cls, sql):
        try:
            cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
            result = cursor.fetchone()
            data = None
            if result:
                data = result
                cursor.close()
            return {"success": True, "data": data}
        except Exception as db:
            print ("ERROR")
            print (db)
            return {"success": False, "message": str(db)}

    @classmethod
    def query_all(cls, sql):
        try:
            cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
            results = cursor.fetchall()
            data = None
            if results:
                data = results
                cursor.close()
            return {"success": True, "data": data}
        except Exception as db:
            print("ERROR")
            print (db)
            return {"success": False, "message": str(db)}