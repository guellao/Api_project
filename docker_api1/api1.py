# app1.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Addition API
@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

# Division API
@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = a / b
        return jsonify({"result": result})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

