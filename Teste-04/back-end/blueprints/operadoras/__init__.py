from flask import Blueprint

bp = Blueprint('operadoras', __name__, url_prefix='/operadoras')

from blueprints.operadoras import routes