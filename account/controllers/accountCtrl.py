import json

from flask import Blueprint, request, jsonify

from account.models.accountModel import accountModel

account_controller = Blueprint('account', __name__)

#register
@account_controller.route('/account/register', methods=['POST'])
def account_register():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(accountModel.register(data))

#them tk google or facebook
@account_controller.route('/account/updateid', methods=['POST'])
def account_update_id():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(accountModel.update_id(data))

#cap nhat thong tin
@account_controller.route('/account/updateinfo', methods=['POST'])
def account_update_info():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(accountModel.update_info(data))

#dang nhap
@account_controller.route('/account/login', methods=['POST'])
def account_login():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(accountModel.login(data))
