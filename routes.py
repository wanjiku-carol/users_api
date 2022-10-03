import os
import json
from faker import Faker

from flask import Blueprint, jsonify, request, render_template
# from flask_caching import Cache 
from .models import User

# cache = Cache()
fake = Faker()

main_bp = Blueprint('main_bp', __name__,
                        template_folder='templates')



@main_bp.route("/", methods=["GET"])
def home():
    print("Heeeyy Were here!")
    return jsonify({"message": "Ola"})

@main_bp.route("/populate", methods=["GET"])
def populate():
    for _ in range(101):
        new_user = User(
                id=fake.random_number(digits=5),
                name=fake.name(),
                email=fake.email(),
                address=str(fake.address()),
                phone_number=str(fake.phone_number())
                )
        new_user.save()
    
    print("DB fully populated")
    
    print("Heeeyy were here!")
    return jsonify({"message": "Database populated"})


@main_bp.route("/users", methods=['GET', 'POST'])
# @cache.cached(timeout=100, query_string=True)
def all_users():
    if request.method == 'POST':
        return jsonify({"message": "Successfully Added Users", "status": "200"})
    elif request.method == 'GET':
        users = User.get_all_users()
        return jsonify(json_list = users)
    else:
        return jsonify({"message": "Not Found", "status": "404"})

@main_bp.route("/users/<string:id>", methods=['GET'])
# @cache.cached(timeout=10, query_string=True)
def get_user(id):
    user_id = request.args.get('id')
    user = User.get_user(user_id)
    return jsonify(user)
