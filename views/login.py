from app import app, get_db
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()

	cur = get_db().cursor()
	cur.execute('SELECT * FROM librarian WHERE username = ?', [data['username']])
	librarian = cur.fetchone()

	if librarian and check_password_hash(librarian['password'], data['password']):
		response_object = {
			'status' : 'success',
			'id' : librarian['librarian_id']
		}
	else:
		response_object = {
			'status' : 'fail',
			'message' : 'Incorrect credentials'
		}
	return jsonify(response_object)