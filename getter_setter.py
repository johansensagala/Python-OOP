class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter untuk nama
    @property
    def name(self):
        return self._name

    # Setter untuk nama
    @name.setter
    def name(self, value):
        self._name = value

    # Getter untuk umur
    @property
    def age(self):
        return self._age

    # Setter untuk umur
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Umur tidak boleh negatif")
        self._age = value

# Contoh penggunaan getter dan setter
person = Person("John Doe", 25)
print(person.name)  # Output: John Doe
print(person.age)  # Output: 25

person.name = "Jane Doe"
person.age = 30
print(person.name)  # Output: Jane Doe
print(person.age)  # Output: 30

# person.age = -10  # Raises ValueError: Umur tidak boleh negatif