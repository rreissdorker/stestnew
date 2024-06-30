import sqlite3
from flask import Flask, request

app = Flask(__name__)
conn = sqlite3.connect('testdb.db', check_same_thread=False)

@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    
    return {'users': rows}

if __name__ == '__main__':
    app.run(port=3000)
