from flask import Flask
from flask_cors import CORS

from predict.controllers.predict import predict


def create_app():
    app = Flask(__name__)
    app.config.from_object('predict.settings')

    CORS(app, resources={r"/*": {'origins': app.config['ALLOWED_CORS_ORIGINS']}})

    app.register_blueprint(predict)

    return app
