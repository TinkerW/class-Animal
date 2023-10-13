class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Person1", 34)
person2 = Person("Person2", 12)
person3 = Person("Person3", 87)

print(f"Имя: {person1.name}, Возраст: {person1.age}")
print(f"Имя: {person2.name}, Возраст: {person2.age}")
print(f"Имя: {person3.name}, Возраст: {person3.age}")
