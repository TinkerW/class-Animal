class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Привет, меня зовут {self.name}!")

    def say_goodbye(self):
        print(f"До свидания, {self.name}!")

    def say_age(self, age):
        print(f"Мне {age} лет.")


my_object = MyClass("Misha")

# Вызов методов объекта
my_object.say_hello()
my_object.say_goodbye()
my_object.say_age(25)
