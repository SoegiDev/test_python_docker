from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
@app.route('/test')
def hello_test():
    return 'Hello, Fajar Soegi!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)