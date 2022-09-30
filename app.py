import os
import requests
from flask import Flask, jsonify, request
from flask_caching import Cache 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# app = Flask(__name__)
# app.config.from_object('config.Config')  # Set the configuration variables to the flask application
# cache = Cache(app) 
db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

def create_app():
    app = Flask(__name__)
    
    # app.config.from_pyfile('config.py')
    
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
     
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app

app = create_app()

@app.route("/users", methods=["GET"])
@cache.cached(timeout=30, query_string=True)
def get_users():
    API_URL = "http://anapi"
    r = requests.get(f"{API_URL}")
    return jsonify(r.json())


@app.route("/users/<string:id>")
@cache.cached(timeout=30, query_string=True)
def get_user(id):
    API_URL = "http://anapi/search?eg="
    user_id = request.args.get('id')
    r = requests.get(f"{API_URL}{user_id}")
    return jsonify(r.json())
  
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


# finish endpoints
# test databases, migrations and addition of users
# false data to test with
# test cache too
# write tests
