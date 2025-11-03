class myclass: #a simple example class
    i = 12345

    def f(self):
        return 'hello world'

x = myclass()
x.f()
xf = x.f()
print(myclass.f(x))
print(xf)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


class complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = complex(3.0, -4.5)

print(x.r, x.i)