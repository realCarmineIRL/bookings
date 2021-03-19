from flask import Blueprint
bookings_blueprint = Blueprint('bookings', __name__)

from . import routes
