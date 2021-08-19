"""Initialize Flask app."""
# from flask_assets import Environment
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, event
from flask_wtf.csrf import CSRFProtect

# import os

db = SQLAlchemy()
csrf = CSRFProtect()



def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    # assets = Environment()
    # assets.init_app(app)
    db.init_app(app)
    csrf.init_app(app)

    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    with app.app_context():
        # Import parts of our application
        # from .assets import compile_static_assets
        from .home import home
        from .script_generator import script_generator
        from .navigation_links import navigation_links
        # from .profile import profile

        # Register Blueprints
        app.register_blueprint(script_generator.script_generator_bp,
                               url_prefix="/script_generator/")
        app.register_blueprint(navigation_links.navigation_links_bp,
                               url_prefix="/navigation_links/")
        app.register_blueprint(home.home_bp)
        # app.register_blueprint(products.product_bp)

        # Compile static assets
        # compile_static_assets(assets)

        db.create_all(app=app)

        return app
