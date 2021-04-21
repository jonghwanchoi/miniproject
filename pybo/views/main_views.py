from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/') #이름, 모듈명, URL 프리픽스(url_prefix)값을 전달

# @bp.route('/')
# def hello_pybo():
#     return 'Hello, Pybo!'

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))


