import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def executeScript(filename):
	# open and read the file
	con = sqlite3.connect("library.db")
	cur = con.cursor()
	fd = open(filename)
	sql_file = fd.read()
	fd.close()

	cur.executescript(sql_file)

def insertLibrarian(username, phone, email, password):
	hashed_password = generate_password_hash(password, method = 'sha256')
	con = sqlite3.connect("library.db")
	cur = con.cursor()
	cur.execute("INSERT INTO librarian (username, phone, email, password) VALUES (?,?,?,?)", (username, phone, email, hashed_password))
	con.commit()
	con.close()