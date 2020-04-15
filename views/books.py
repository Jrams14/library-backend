from app import app, get_db
from flask import Flask, request, jsonify, make_response
from datetime import timedelta, date

@app.route('/checkout', methods=['POST'])
def checkout_book():
    data = request.get_json()
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO loan(b_id, m_id, checkout_date, due_date, l_id) VALUES (?,?,?,?,?)", (data['b_id'], data['m_id'], date.today(), date.today() + timedelta(days=30), data['l_id']))
        db.commit()
        response_object = {
            'status': 'success'
        }

        return jsonify(response_object)
    except:
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
