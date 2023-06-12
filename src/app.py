from flask import Flask, jsonify,request


app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }, { "label": "My first task", "done": False }]


@app.route('/blabla', methods=['GET'])
def hello_world():
    message = 'Hello, World!'
    return jsonify(message=message)

@app.route('/todos', methods=['GET'])
def todo_get():
    message = 'Hello!'
    return jsonify(message=message)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'






# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)