from flask import Blueprint

bp = Blueprint('views', __name__)

from views import test
from views import mail_list