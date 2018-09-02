import json

from flask import Blueprint, request, jsonify

from post.models.postModel import postModel

posts_controller = Blueprint('posts', __name__)


@posts_controller.route('/post/write', methods=['POST'])
def post_write():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(postModel.write_post(data))


@posts_controller.route('/post/like', methods=['POST'])
def post_like():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(postModel.like(data))


@posts_controller.route('/post/unlike', methods=['POST'])
def post_unlike():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(postModel.unlike(data))


@posts_controller.route('/post/list', methods=['GET'])
def list_post_all():
    if request.method == 'GET':
        # data = json.loads(request.data)
        return jsonify(postModel.list_post_all())


@posts_controller.route('/post/user', methods=['POST'])
def list_post_user():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(postModel.list_post_user(data))


@posts_controller.route('/post/userslike', methods=['POST'])
def user_like():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(postModel.user_like_post(data))


@posts_controller.route('/post/postsliked', methods=['POST'])
def post_liked():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(postModel.post_liked(data))


@posts_controller.route('/post/detail', methods=['POST'])
def post_detail():
    if request.method == 'POST':
        data = json.loads(request.data)
        return jsonify(postModel.post_detail(data))
