from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/users")
def get_users():
    API_URL = "http://anapi"
    r = requests.get(f"{API_URL}")
    return jsonify(r.json())


@app.route("/users/{id}")
def get_user(id):
    API_URL = "http://anapi/search?eg="
    user_id = request.args.get('id')
    r = requests.get(f"{API_URL}{user_id}")
    return jsonify(r.json())
  
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
