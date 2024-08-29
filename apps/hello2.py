from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕"

@app.route("/hi")
def hi():
    return "<h1>h1<h1>"

@app.route("/hello")
def hello():
    return "<h3>hello<h3>"

@app.route("/school")
def school():
    return "세명컴퓨터고등학교"

@app.route("/dept")
def dept():
    return "인공지능소프트웨어과"

@app.route("/dept/name")
def name():
    return "장우준"

if __name__ == "__main__":
    app.run(debug=True)