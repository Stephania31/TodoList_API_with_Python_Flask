from flask import Flask, jsonify,request

app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }, { "label": "My first task", "done": False }]


@app.route('/todos', methods=['GET'])
def todo_get():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos.append(request_body)
    json_text = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_text







# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)