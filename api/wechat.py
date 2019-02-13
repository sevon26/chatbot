from flask import Blueprint, jsonify, g, request

from common.lang import Lang
from common.wx import *
route_api = Blueprint('api_page', __name__)


@route_api.route('/222', methods=['GET', 'POST'])
def index():
    req = request.args
    text = '简单'
    if text:
        tr_text = Lang.translate(text)
        text = Lang.getModelReply(tr_text)
        return jsonify(text)
    else:
        return 'Please input word'


@route_api.route('/login')
def login():
    send_msg()
    return 'Test'
