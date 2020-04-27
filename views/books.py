from app import app, get_db
from flask import Flask, request, jsonify, make_response
from datetime import date, datetime
import dateutil.parser

@app.route('/checkout', methods=['POST'])
def checkout_book():
    data = request.get_json()
    try:
        db = get_db()
        cur = db.cursor()

        # Check if book is already checked out by a member
        cur.execute("SELECT * FROM loan where bi_id = ? AND status = 'active'", [data['b_id']])
        db.commit()

        loaned_book = cur.fetchone()
        if loaned_book:
            response_object = {
            'status': 'fail',
            'message': 'book already loaned'
            }
            return jsonify(response_object)

        cur.execute("INSERT INTO loan(bi_id, m_id, checkout_date, due_date, librarian_id, status) VALUES (?,?,?,?,?,?)", (data['b_id'], data['m_id'], date.today(), data['return_date'], data['l_id'], 
        'active'))
        db.commit()
        response_object = {
            'status': 'success'
        }

        return jsonify(response_object)
    except Exception as ex:
        print(ex)
        response_object = {
            'status': 'fail'
        }
        
        return jsonify(response_object)

@app.route('/addBook', methods=['POST'])
def add_book():
    data = request.get_json()
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute("BEGIN")
        cur.execute("INSERT INTO book(ISBN, author, title, year, pages, numOfCopies) VALUES (?,?,?,?,?,?)" , (data['ISBN'], data['author'], data['title'], data['year'], data['pages'], data['numOfCopies']))
        
        for i in range(int(data['numOfCopies'])):
            cur.execute("INSERT INTO bookItem(ISBN) VALUES (?)", [data['ISBN']])

        cur.execute("COMMIT")
        response_object = {
            'status': 'success'
        }
        return jsonify(response_object)

    except Exception as ex:
        print(ex)
        cur.execute("ROLLBACK")
        response_object = {
            'status': 'fail',
        }
        return jsonify(response_object)


@app.route('/return', methods = ["POST"])
def return_book():
    data = request.get_json()

    try:
        db = get_db()
        cur = db.cursor()
        # Start Transaction
        cur.execute("BEGIN")

        cur.execute("SELECT * FROM loan where bi_id = ? AND status = 'active'", [data["bi_id"]])

        loan = cur.fetchone()
        
        # Create fine if returned past due date
        return_date = dateutil.parser.parse(loan['due_date']).date()
        if return_date < date.today():
            amount = (date.today() - return_date).days * 0.5
            cur.execute('INSERT INTO fine (l_id, amount, status) VALUES(?, ?, ?)', [loan['l_id'], amount, 'active'])

        # Transaction successful, set loan status to complete
        cur.execute("UPDATE loan SET status = 'complete' WHERE bi_id = ?", [data["bi_id"]])
        cur.execute("COMMIT")
        cur.close()
        
        response_object = {
            'status': 'success'
        }
        return jsonify(response_object)

    except Exception as ex:
        print(ex)
        # There was an error, rollback transaction
        cur.execute("ROLLBACK")
        response_object = {
            'status': 'fail'
        }
        return jsonify(response_object)

@app.route('/search', methods = ["POST"])
def search_book():
    data = request.get_json()

    db = get_db()
    cur = db.cursor()

    print(data['title'])

    cur.execute("SELECT * FROM book where title LIKE ? ", ['%' + data['title'] + '%'])

    books = cur.fetchall()

    books_output = []
    for book in books:
        book_data = {}
        book_data['ISBN'] = book['ISBN']
        book_data['title'] = book['title']
        book_data['author'] = book['author']
        book_data['year'] = book['year']
        books_output.append(book_data)
    
    response_object = {
        'status': 'success',
        'books': books_output
    }

    return jsonify(response_object)

@app.route('/frequent', methods = ["GET"])
def get_frequent_books():
    db = get_db()
    cur = db.cursor()

    try:
        cur.execute('SELECT * FROM frequent_books')

        books = cur.fetchall()

        books_output = []
        for book in books:
            book_data = {}
            book_data['title'] = book['title']
            book_data['author'] = book['author']
            book_data['year'] = book['year']
            books_output.append(book_data)
        
        response_object = {
            'status': 'success',
            'books': books_output
        }
        return jsonify(response_object)
    except Exception as ex:
        print(ex)
        response_object = {
            'status': 'fail'
        }
        return jsonify(response_object)

@app.route('/payFine', methods = ["POST"])
def pay_fine():
    data = request.get_json()

    db = get_db()
    cur = db.cursor()

    try:
        cur.execute("UPDATE fine SET status = 'complete' WHERE l_id = ?", [data['l_id']])
        db.commit()
        response_object = {
            'status': 'success'
        }
        return jsonify(response_object)
    except Exception as ex:
        print(ex)
        response_object = {
            'status': 'fail'
        }
        return jsonify(response_object)
    
   