from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from maia.auth import login_required
from maia.db import get_db

bp = Blueprint('weather', __name__)


@bp.route('/weather')
@login_required
def index():
    return render_template('weather/index.html')