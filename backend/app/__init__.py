from flask import Flask
from flask_cors import CORS
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config.from_object('config.Config')

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    return app