from flask import Flask, jsonify, request


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
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    position = int(position)
    if position >= len(todos):
        return jsonify({"msg":"Invalid index"}), 400
    if len(todos)==0:
        return jsonify({"msg":"There are no tasks in the list"}), 400
    if position < 0:
        return jsonify({"msg":"Invalid index"}), 400
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text




# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)