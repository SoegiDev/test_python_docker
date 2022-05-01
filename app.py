from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/number/<int:number>')
def hello_number(number):
    return f'Hello,Your NUmber is {number} '

@app.route('/say/<name>')
def hello_say(name):
    return f'Hello, {name}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)