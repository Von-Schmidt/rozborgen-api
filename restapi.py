from flask import Flask, request, jsonify
from flask_cors import CORS
import main

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api', methods=['POST'])
def process():
    data = request.json
    string_input = data['string_input']
    result = main.callfunc(string_input)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')