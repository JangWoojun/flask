from flask import Flask
# flask: 모듈(module)
# Flask: 클래스(class)
#       -Flask는 애플리케이션을 생성하는데 사용함.
app = Flask(__name__)
# Flask 애플리케이션 객체를 생성
# __name__은 현재 모듈의 이름이고,
# 이 이름을 애플리케이션의 이름으로 사용함.

@app.route('/')
# Flask 애플리케이션의 데코레이터
# 이 데코레이터는 특정 URL(여기서는 /)에 대해
# 해당 URL이 호출될 때 실행될 함수를 지정함.
# '/'는 root(처음) URL을 의미하고
# http://localhost:500/' 에 접속할 때 호출됨.

def index():
# root URL로 접근할 때 실행될 함수.
# Flask가 이 함수를 실행하여 응답을 생성함.
    return '안녕'
# hello() 함수의 반환 값.
# 문자열 '안녕'을 웹 브라우저에 표시함.
# root URL에 접속