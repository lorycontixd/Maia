from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from maia.auth import login_required
from maia.db import get_db

bp = Blueprint('blog', __name__)
