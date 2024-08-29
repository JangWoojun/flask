def test2(func):
    def inside(a, b):
        r = func(a, b)
        print(f"{func.__name__}(a={a}, b={b}) -> {r}")
        return r
    return inside

@test2
def add(a, b):
    return a + b

print(add(10, 20))