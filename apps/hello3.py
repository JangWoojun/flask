from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕"

@app.route("/hello/<name>")
def hello(name):
    return f"안녕하세요 {name}님"

@app.route("/intTest/<int:n>")
def intTest(n):
    return f"숫자 출력 {n}"

@app.route("/user/<name>/<int:age>/<id>")
def user(name, age, id):
    return f"""<h1>반갑습니다. {name}<h1>
<h2>당신의 나이는 {age}<h2>. <h2>id는 {id}<h2>입니다"""
if __name__ == "__main__":
    app.run(debug=True)