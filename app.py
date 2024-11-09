from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! !"


@app.route('/get', methods=['GET'])
def get():
    dictionary = {
        'name': 'John',
        'age': 25
    }
    return jsonify(dictionary)


@app.route('/template', methods=['GET'])
def template():
    return render_template('index.html')