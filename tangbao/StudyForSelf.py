# coding=utf-8
def bar(self, y):
    return self.x + y
class Foo():
    x = 9
    b = bar
    def __init__(self, x):
        self.x = x

foo = Foo(5)
print(bar(foo, 1))
print(bar(Foo, 1))
print(Foo.b(foo, 4) == 9)
print(Foo.b(Foo, 4) == 9)
print(foo.b(1))
print(type(foo.b))
print(type(bar))
print(type(Foo.b))
print(bar(self=foo, y=1))