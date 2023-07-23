class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Panggil static method tanpa menginstansiasi objek kelas
result1 = MathUtils.add(5, 3)
print(result1)  # Output: 8

result2 = MathUtils.multiply(2, 4)
print(result2)  # Output: 8
