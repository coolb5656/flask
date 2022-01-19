import os
from flask import Flask
from flask_assets import Environment, Bundle


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    assets = Environment(app)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    )


    js = Bundle('js/lib/jquery.js', output='gen/packed.js')
    css = Bundle('css/lib/bootstrap.css', 'css/style.css', output='gen/style.css')

    assets.register('js_all', js)
    assets.register('css_all', css)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from .models import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app

