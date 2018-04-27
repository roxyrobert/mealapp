from flask import Flask, jsonify, request
from functools import wraps


app = Flask(__name__)


users = []
meals = []

@app.route('/auth/signup', methods=['POST'])
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
@app.route('/get_meals', methods =['GET'])
def get_meals():
    for user in users:
        if user['role'] == 'admin':
            return jsonify({'message':'These are the available meals'})
    return jsonify({'message':'You are not authorised'})

#check if user is admin
#def is_user_admin(f):
#   @wraps(f)
#    def decorated(*args, **kwargs):
#     auth = request.authorization
#     if auth == is_ad


# Add meals; for only Admin
@app.route('/add_meal', methods =['POST'])
#@is_user_admin
def add_meal():
    for user in users:
        if user['role'] == 'admin':
            add_meal = request.get_json()
            new_meal = {'id':add_meal['id'], 'meal_name':add_meal['meal_name'], 'price':add_meal['price']}
            meals.append(new_meal)
            return jsonify({'Meals': meals})
        return jsonify({'message':'You are not authorised'})
    

@app.route('/edit_meal/<int:meal_id>', methods =['PUT'])
def edit_meal(meal_id):
    for user in users:
        if user['role'] == 'admin':
            new_meal = request.get_json(id)
            edited_meal = {'meal_name':new_meal['meal_name'], 'price':new_meal['price']}
            return jsonify({'Meals': meals})
        return jsonify({'message':'You are not authorised'})

    



@app.route('/delete_meal/<int:meal_id>', methods =['GET'])
def delete_meal(meal_id):
    return 'This deletes one meal by ID'


@app.route('/set_menu', methods=['POST'])
def set_menu():
    return 'This sets up the menu'

@app.route('/get_menu', methods=['GET'])
def get_menu():
    return 'This is the menu'

@app.route('/order_meal', methods=['POST'])
def order_meal():
    return 'Make an order'

@app.route('/edit_order', methods=['PUT'])
def edit_order():
    return 'Modify your order'

@app.route('/get_orders', methods=['GET'])
def get_orders():
    return 'Here you can view all orders'
    

'''
@app.route('/meal/<int:meal_id>', methods =['DELETE'])
def delete_meal(meal_id):
    return 'This deletes a meal by ID.'
'''
if __name__ == '__main__':
    app.run(debug=True)