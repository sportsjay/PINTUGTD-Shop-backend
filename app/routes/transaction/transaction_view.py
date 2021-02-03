from flask import Blueprint

transaction_route = Blueprint("transaction", __name__)


@transaction_route.route("/transaction")
def transaction_test_api():
    return "Welcome to transactions!"
