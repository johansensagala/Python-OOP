class Student:

    def __init__(self, name, age, major, gpu):
        self.name = name
        self.age = age
        self._major = major #protected
        self.__gpu = gpu #private

    def get_gpu(self):
        return self.__gpu

student1 = Student("Johansen Sagala", 21, "Informatics Engineering", 3.83)

print(student1.__dict__)
print(student1._major) #tidak ada efek teknis namun tidak disarankan untuk dilakukan\
# print(student1.__gpu) #tidak bisa dilakukan
print(student1.get_gpu())