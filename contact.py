from flask import Blueprint

bp_contact = Blueprint('bp_contact', __name__)


@bp_contact.route('/')
def index():
  return 'Hello World'
