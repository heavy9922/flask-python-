from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
def list():
    return 'todo list'

@bp.route('/create')
def create():
    return 'crear tarea'