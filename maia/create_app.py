import os

from flask import Flask, session, redirect, url_for, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'maia.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Import db
    from . import db
    db.init_app(app)

    # Import auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    # Import blog blueprint
    from . import blog
    app.register_blueprint(blog.bp)

    from .modules import weather
    app.register_blueprint(weather.bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/michi')
    def michi():
        return "Ciao michi, ti voglio bene!!"

    @app.endpoint("index")
    def home():
        user_id = session.get('user_id')
        if user_id is None:
            print("not logged in")
            return redirect(url_for("auth.login"))
        else:
            print("logged in")
            return render_template('index.html')
    app.add_url_rule("/",endpoint="index" )

    return app