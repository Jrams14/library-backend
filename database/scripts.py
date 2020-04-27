import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def insertLibrarian(username, phone, email, password):
	hashed_password = generate_password_hash(password, method = 'sha256')
	con = sqlite3.connect("library.db")
	cur = con.cursor()
	cur.execute("INSERT INTO librarian (username, phone, email, password) VALUES (?,?,?,?)", (username, phone, email, hashed_password))
	con.commit()
	con.close()