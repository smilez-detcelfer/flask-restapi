from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

apipage = Blueprint('api', __name__)
api = Api(apipage)


@apipage.route('/', methods = ['GET'])
def first_api():
    return jsonify({'message': 'welcome'})


userlist = [{'name': 'smilez', 'surname': 'detcelfer'},
            {'name': 'hui', 'surname': 'sobachi'},
            {'name': 'smilez', 'surname': 'thesecond'}]
@apipage.route('/<string:name>', methods=['GET'])
def checkuser(name):
    user_filtered = [user for user in userlist if user['name'] == name]
    return jsonify(user_filtered)