from flask import Flask, request, jsonify
#from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
#CORS(app)  # Allow Cross-Origin Resource Sharing

# Database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Replace with your MySQL password
    database="kimani_drilling"
)
cursor = db.cursor()

# Root route
@app.route('/')
def home():
    return "Welcome to the Kimani Drilling API!"

# Endpoint to fetch user details
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        sql = "SELECT * FROM authenticationdrilling WHERE id = %s"
        cursor.execute(sql, (user_id,))
        user = cursor.fetchone()

        if user:
            user_details = {
                'user_id': user[0],
                'username': user[1],
                'email': user[2],
                'phone': user[3],
                'bio': user[4]  # Adjust based on actual column index
            }
            return jsonify(user_details)
        else:
            return jsonify({'error': 'User not found'}), 404

    except mysql.connector.Error as err:
        return jsonify({'error': f"Database error: {err}"}), 500

# Endpoint to update user details
@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        phone = data.get('phone')

        sql = "UPDATE authenticationdrilling SET username = %s, email = %s, phone = %s WHERE id = %s"
        cursor.execute(sql, (username, email, phone, user_id))
        db.commit()

        return jsonify({'message': 'User details updated successfully'})

    except mysql.connector.Error as err:
        return jsonify({'error': f"Database error: {err}"}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False
