import os

from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
# from flask_caching import Cache 

from .models import db



dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

migrate = Migrate()
# cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py') 

    app.config.from_mapping(
        # db mapping
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    cache_config = app.config.from_mapping(
        # cache mapping
        CACHE_TYPE = os.environ.get('CACHE_TYPE'),
        CACHE_REDIS_HOST = os.environ.get('CACHE_REDIS_HOST'),
        CACHE_REDIS_PORT = os.environ.get('CACHE_REDIS_PORT'),
        CACHE_REDIS_DB = os.environ.get('CACHE_REDIS_DB'),
        CACHE_REDIS_URL = os.environ.get('CACHE_REDIS_URL'),
        CACHE_DEFAULT_TIMEOUT = os.environ.get('CACHE_DEFAULT_TIMEOUT'),
    )
    
    db.init_app(app)
    migrate.init_app(app, db)
    # cache.init_app(app, config=cache_config)
    
    with app.app_context():
        from .routes import main_bp
        
        app.register_blueprint(main_bp)
        db.create_all()
        
        return app

  
if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0", port=5000)


# finish endpoints
# test databases, migrations and addition of users (Done)
# false data to test with
# test cache too
# write tests

# import issues*+ Kinda sorted
