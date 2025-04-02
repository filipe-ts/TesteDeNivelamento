from flask import Flask
from config import Config
from flask_cors import CORS
import pandas as pd


def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={"/*": {"origins": "*"}})

    # carregando csv
    app.df = pd.read_csv(app.config['CSV_PATH'], delimiter=';')

    # Register blueprints here
    from blueprints.operadoras import bp as operadoras_bp
    app.register_blueprint(operadoras_bp)
    # from app.team import bp as team_bp
    # app.register_blueprint(team_bp, url_prefix='/team')

    @app.route('/health/')
    def test_page():
        return '<h1>Healthy!</h1>'

    return app