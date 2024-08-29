def test(func):
    def inside():
        print(func.__name__, "함수 시작")
        func()
        print(func.__name__, "함수 종료")
    return inside

def hello():
    print("hello test")

def world():
    print("world test")

inside_hello = test(hello)
inside_hello()
inside_world = test(world)
inside_world()