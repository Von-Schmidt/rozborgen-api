from flask import Flask, request, jsonify
from flask_cors import CORS
import main

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api', methods=['POST'])
def process():
    data = request.json
    # Assuming your string is in a field called 'string_input' in the JSON data
    string_input = data['string_input']
    # Use your Python function to process the string input and obtain a result
    result = main.callfunc(string_input)
    #result = string_input
    # Return the result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')