import logging

from flask import Blueprint, jsonify, request
from plum_bank.exceptions.user_not_found_exception import UserNotFoundException
from plum_bank.service.account_service import AccountService

api = Blueprint('api', __name__)


@api.route('/accounts/create', methods=['POST'])
def create_new_account():
    content = request.json

    # request validation
    if content.get('user_id') is None:
        logging.error("Missing user_id")
        return jsonify({}), 400

    user_id = content['user_id']
    deposit = content.get('deposit', 0.0)
    try:
        service = AccountService()
        service.create_account(user_id, deposit)
        return jsonify({}), 200
    except UserNotFoundException:
        logging.info("User not found", exc_info=True)
        return jsonify({}), 404
    except (ValueError, TypeError):
        logging.exception("Error creating an account")
        return jsonify({}), 400


@api.route('/balances', methods=['GET'])
def get_balances():
    content = request.json

    # request validation
    if content.get('user_id') is None:
        logging.error("Missing user_id")
        return jsonify({}), 400

    user_id = content['user_id']
    try:
        service = AccountService()
        accounts = service.get_balances(user_id)
        return jsonify(accounts), 200
    except UserNotFoundException:
        logging.info("User not found", exc_info=True)
        return jsonify({}), 404
