from flask import Flask
# app reference
app = Flask(__name__)


# Setup Routes
def get_register_blueprints():
    # Admin API
    from app.routes.transaction.transaction_view import transaction_route

    # API Blueprints
    return [
        # Public
        transaction_route
        # Admin
    ]


# Promote routes
[app.register_blueprint(blueprint)
 for blueprint in get_register_blueprints()]
