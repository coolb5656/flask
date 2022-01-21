from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    assets = Environment(app)

    bundles = {
        'js': Bundle(
            'js/lib/jquery-3.6.0.min.js',
            output='gen/app.js'),
        'css': Bundle(
            'css/style.css',
            'css/lib/bootstrap.css',
            output='gen/style.css'),
    }

    assets.register(bundles)

    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # blueprint for checkout routes in our app
    from .checkout import checkout as checkout_blueprint
    app.register_blueprint(checkout_blueprint, url_prefix='/checkout')

    # # blueprint for reserve routes in our app
    # from .reserve import reserve as reserve_blueprint
    # app.register_blueprint(reserve_blueprint)


    # # blueprint for views routes in our app
    # from .views import views as views_blueprint
    # app.register_blueprint(views_blueprint)

    return app