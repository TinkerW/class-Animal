
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

dog = Dog()
cat = Cat()
cow = Cow()


print("Dog's sound: " + dog.make_sound())
print("Cat's sound: " + cat.make_sound())
print("Cow's sound: " + cow.make_sound())
