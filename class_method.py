class MyClass:
    count = 0

    def __init__(self):
        print("woi")

    @classmethod
    def get_count(cls):
        return cls.count

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.get_count())