from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, DevOps!k xa?"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

