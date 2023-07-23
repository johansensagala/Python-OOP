# __init__(self[, ...])

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

print(person.__dict__)

# # __str__(self)

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"

person = Person2("John", 30)
print(person) # Output: John (30)

# __len__(self)

class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list)) # Output: 5

# __add__(self, other)

class MyList2:
    def __init__(self, items):
        self.items = items
    
    def __add__(self, other):
        return MyList2(self.items + other.items)

list1 = MyList2([1, 2, 3])
list2 = MyList2([4, 5, 6])
list3 = list1 + list2
print(list3.items) # Output: [1, 2, 3, 4, 5, 6]

# __getitem__(self, index)

class MyList3:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]

my_list = MyList3([1, 2, 3, 4, 5])
print(my_list[2]) # Output: 3

# __setitem__(self, index, value)

class MyList4:
    def __init__(self, items):
        self.items = items
    
    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList4([1, 2, 3, 4, 5])
my_list[2] = 6
print(my_list.items) # Output: [1, 2, 6, 4, 5]

# __eq__(self, other)

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

person1 = Person3("John", 30)
person2 = Person3("Jane", 25)
person3 = Person3("John", 30)

print(person1 == person2) # Output: False
print(person1 == person3) # Output: True
