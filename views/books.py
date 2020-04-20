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
        cur.execute("SELECT * FROM loan where b_id=? AND status='active'", (data['b_id']))
        db.commit()

        loaned_book = cur.fetchone()
        if loaned_book:
            response_object = {
            'status': 'fail',
            'message': 'book already loaned'
            }
            return jsonify(response_object)

        cur.execute("INSERT INTO loan(b_id, m_id, checkout_date, due_date, l_id, status) VALUES (?,?,?,?,?,?)", (data['b_id'], data['m_id'], date.today(), data['return_date'], data['l_id'], 
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
def addBook():
    data = request.get_json()
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO book(ISBN, author, title, year, pages, numOfCopies) VALUES (?,?,?,?,?,?)" , (data['ISBN'], data['author'], data['title'], data['year'], data['pages'], data['numOfCopies']))
        db.commit()
        response_object = {
            'status': 'success'
        }
        return jsonify(response_object)

    except:
        response_object = {
            'status': 'fail',
        }
        return jsonify(response_object)


@app.route('/return', methods = ["POST"])
def returnBook():
    data = request.get_json()

    try:
        db = get_db()
        cur = db.cursor()

        cur.execute("UPDATE loan SET status = 'complete' WHERE b_id = ?", data["b_id"])
        cur.execute("SELECT * FROM loan where b_id = ?", data["b_id"])

        db.commit()
        loan = cur.fetchone()
        
        # Create fine if returned past due date
        return_date = dateutil.parser.parse(loan['due_date']).date()
        if return_date < date.today():
            amount = (date.today() - return_date).days * 0.5
            cur.execute('INSERT INTO fine (amount, status) VALUES(?, ?)', (amount, 'active'))
            db.commit()

        cur.close()
        
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
       
        
