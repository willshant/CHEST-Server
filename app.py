from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.json:
        child_list = request.get_json()
        for child in child_list:
            print(child)
        return 'get data'
    else:
        return 'nothing'


app.run(port=8080)

