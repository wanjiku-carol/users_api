import requests
from flask import Flask, jsonify, request
from flask_caching import Cache 

app = Flask(__name__)
app.config.from_object('config.Config')  # Set the configuration variables to the flask application
cache = Cache(app) 

@app.route("/users")
@cache.cached(timeout=30, query_string=True)
def get_users():
    API_URL = "http://anapi"
    r = requests.get(f"{API_URL}")
    return jsonify(r.json())


@app.route("/users/{id}")
@cache.cached(timeout=30, query_string=True)
def get_user(id):
    API_URL = "http://anapi/search?eg="
    user_id = request.args.get('id')
    r = requests.get(f"{API_URL}{user_id}")
    return jsonify(r.json())
  
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
