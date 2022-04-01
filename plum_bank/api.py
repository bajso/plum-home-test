from flask import Blueprint, jsonify


api = Blueprint('api', __name__)


@api.route('/test-api', methods=['POST'])
def my_test_api():
    return jsonify({})
