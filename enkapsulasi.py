class Student:
    def __init__(self, name, age, ipk, major):
        self.name = name
        self.age = age
        self.__ipk = ipk
        self.__major = major

    def get_ipk(self):
        return self.__ipk
    
    def get_major(self):
        return self.__major

    def set_ipk(self, ipk):
        if ipk < 0:
            self.__ipk = 0
        elif ipk > 4.0:
            self.__ipk = 4.0
        else:
            self.__ipk = ipk

# getter
student1 = Student("Johansen", 20, 3.83, "Informatics Engineering")
print(student1.name) # output: Johansen
print(student1.age) # output: 20
print(student1.get_ipk()) # output: 3.83
print(student1.get_major()) # output: Informatics Enginnering
print("\n")

# setter
student1.set_ipk(5.2)
print(student1.get_ipk())