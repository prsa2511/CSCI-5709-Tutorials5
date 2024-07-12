from flask import Flask, request, jsonify
import json

app = Flask(__name__)

class User:
    def __init__(self, firstName, email):
        self.id = str(len(listOfUsers) + 1)
        self.firstName = firstName
        self.email = email

listOfUsers = []

user1 = User("ABC", "abc@abc.ca")
listOfUsers.append(user1)

user2 = User("XYZ", "xyz@xyz.ca")
listOfUsers.append(user2)

@app.route('/users', methods=['GET'])
def get_users():
    jsonList = json.dumps([ob.__dict__ for ob in listOfUsers])
    return jsonify({
        "message": "Users retrieved",
        "success": True,
        "users": json.loads(jsonList)
    }), 200

@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(data['firstName'], data['email'])
    listOfUsers.append(new_user)
    return jsonify({
        "message": "User added",
        "success": True
    }), 201

@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    for user in listOfUsers:
        if user.id == id:
            user.firstName = data.get('firstName', user.firstName)
            user.email = data.get('email', user.email)
            return jsonify({
                "message": "User updated",
                "success": True
            }), 200
    return jsonify({
        "message": "User not found",
        "success": False
    }), 404

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    for user in listOfUsers:
        if user.id == id:
            return jsonify({
                "success": True,
                "user": user.__dict__
            }), 200
    return jsonify({
        "message": "User not found",
        "success": False
    }), 404

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "message": "Resource not found",
        "success": False
    }), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "message": "Internal server error",
        "success": False
    }), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
