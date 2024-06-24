from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('orders.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_order', methods=['POST'])
def add_order():
    data = request.json
    item = data.get('item')
    quantity = data.get('quantity')
    price = data.get('price')
    current_date = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    conn = get_db_connection()
    conn.execute('INSERT INTO orders (item_name, quantity, price, order_date, order_time) VALUES (?, ?, ?, ?, ?)',
                 (item, quantity, price, current_date, current_time))
    conn.commit()
    conn.close()
    return jsonify(success=True)

@app.route('/get_orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    orders = conn.execute('SELECT * FROM orders').fetchall()
    conn.close()
    return jsonify([dict(order) for order in orders])

@app.route('/delete_order', methods=['POST'])
def delete_order():
    data = request.json
    item_name = data.get('item_name')
    conn = get_db_connection()
    conn.execute('DELETE FROM orders WHERE item_name = ?', (item_name,))
    conn.commit()
    conn.close()
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
