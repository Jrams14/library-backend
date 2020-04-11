from app import app, get_db
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()

	cur = get_db().cursor()
	cur.execute('SELECT * FROM librarian WHERE username = ?', [data['username']])
	librarian = cur.fetchone()
	print(librarian)

	if librarian and check_password_hash(librarian['password'], data['password']):
		response_object = {
			'status' : 'success',
			'librarianId' : librarian['ID']
		}

	return jsonify(response_object)