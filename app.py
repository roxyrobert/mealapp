from flask import Flask, jsonify, request

app = Flask(__name__)


users = []
meals = []

@app.route('/auth/user', methods=['POST'])
def register_user():
    newuser_data = request.get_json()

    new_user = {'id': newuser_data['id'], 'name':newuser_data['name'], 'username':newuser_data['username'], 'password':newuser_data['password'], 'role':newuser_data['role']}
    users.append(new_user)
    return jsonify({'Users': users})


@app.route('/auth/login', methods=['POST'])
def login():
    login_data = request.get_json()
    for user in users:
        if user['username'] == login_data['username'] and user['password'] == login_data['password']:
            return jsonify({'message':'user loged in'})
        return jsonify({'message':'username not found'})
    return jsonify({'message':'user not found'})


            
# Meals route for Admin only
@app.route('/meals', methods =['GET'])
def get_meals():
    for user in users:
        if user['role'] == 'admin':
            return jsonify({'message':'These are the available meals'})
    return jsonify({'message':'You are not authorised'})


@app.route('/meal/<int:meal_id>', methods =['GET'])
def get_meal(meal_id):
    return 'This returns one meal by ID'

# Add meals; for only Admin
@app.route('/meal', methods =['POST'])
def add_meal():
    for user in users:
        if user['role'] == 'admin':
            add_meal = request.get_json()
            new_meal = {'id':add_meal['id'], 'meal_name':add_meal['meal_name'], 'price':add_meal['price']}
            meals.append(new_meal)
        return jsonify({'message':'You are not authorised'})

    #return 'This adds a new meal'

@app.route('/meal/<int:meal_id>', methods =['PUT'])
def edit_meal(meal_id):
    return 'This updates a meal by ID.'

@app.route('/meal/<int:meal_id>', methods =['DELETE'])
def delete_meal(meal_id):
    return 'This deletes a meal by ID.'

if __name__ == '__main__':
    app.run(debug=True)