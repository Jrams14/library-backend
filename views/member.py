from app import app, get_db
from flask import Flask, request, jsonify, make_response

@app.route('/addMember', methods=['POST'])
def addMember():
    data = request.get_json()
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO member(name, phone, email, balance) VALUES (?,?,?,?)", [data['name'], data['phone'], data['email'], '0'])
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

@app.route('/status/<m_id>', methods = ['GET'])
def getStatus(m_id):
    db = get_db()
    cur = db.cursor()

    try:
        # Retrieve member info
        cur.execute('SELECT * FROM member where m_id = ?', (m_id))
        member = cur.fetchone()

        member_data = {}
        member_data['name'] = member['name']
        member_data['balance'] = member['balance']

        # Retrieve members current loans
        cur.execute("SELECT * FROM loan INNER JOIN bookItem on loan.bi_id = bookItem.bi_id NATURAL JOIN book WHERE loan.m_id = ? AND loan.status = 'active'", (m_id))
        loans = cur.fetchall()

        # Retrieve the members fines
        cur.execute("SELECT * FROM fine INNER JOIN loan on fine.l_id = loan.l_id WHERE loan.m_id = ? AND fine.status = 'active'", (m_id))
        fines = cur.fetchall()

        loans_output = []
        for loan in loans:
            data = {}
            data['bi_id'] = loan['bi_id']
            data['ISBN'] = loan['ISBN']
            data['title'] = loan['title']
            data['author'] = loan['author']
            data['year'] = loan['year']
            loans_output.append(data)

        fines_output = []
        for fine in fines:
            data = {}
            data['loan'] = fine['l_id']
            data['amount'] = fine['amount']
            data['status'] = fine['status']
            fines_output.append(data)
        
        response_object = {
            'status': 'success',
            'member': member_data,
            'loans': loans_output,
            'fines': fines_output
        }

        return jsonify(response_object)
    
    except Exception as ex:
        print(ex)
        response_object = {
            'status': 'fail'
        }
        return jsonify(response_object)
