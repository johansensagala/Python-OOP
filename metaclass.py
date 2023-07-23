class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['bar'] = lambda self: 'bar'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    def foo(self):
        return 'foo'

obj = MyClass()
print(obj.foo())  # output: 'foo'
print(obj.bar())  # output: 'bar'