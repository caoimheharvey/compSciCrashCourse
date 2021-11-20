# create a class using the keyword 'class'
# This is the parent class for this program. It will be inherited by child classes.
class Animal:
    # The __init__ is always executed once the class is called
    # if there are parameters in the init function, then they must be passed
    # when the class is called
    def __init__(self, name, legs):
        # then you assign the values to the object using the key word self
        self._name = name
        # the self keyword refers to the object
        self._legs = legs

    # This is a method of an object
    # called by invoking it on an object
    def introduce(self):
        print(f"Hello, my name is {self._name} and I have {self._legs} legs")


# Cat inherits the Animal Class
class Cat(Animal):
    # Cat is overwriting the init function in Animal to add the noise parameter
    def __init__(self, name, legs, noise):
        # this new parameter must be added to the object
        self._noise = noise
        # the other two parameters will be added when calling super().__init__(params)
        # super().__init__() calls the parent class's __init__ function which will initialise the parameters passed
        super().__init__(name, legs)

    # overwrites the introduce functionality defined in the parent class
    def introduce(self):
        print(f"My name is {self._name} and I say {self._noise}")


# inherits from Animal but doesn't define any new properties or redefine the introduce method
class Dog(Animal):
    # adds new method for extended functionality
    def bark(self):
        print(f"Woof, Woof, Woof, my name is {self._name}")

    # using a setter, to set a new property specific to the dog object
    def set_age(self, age):
        self._age = age

    def set_legs(self, legs):
        self._legs = legs

    # using a getter to get a property of the dog object
    def get_legs(self):
        return self._legs

    def get_age(self):
        return self._age

    def get_human_age(self):
        return self._age % 7


# Inherits from Cat which is a child of Animal
class Lion(Cat):
    # re-define the init to use a keyword argument for noise with "rawr" as the default
    def __init__(self, name, legs, noise="rawr"):
        # super() will call Cat and Cat will then call super which is Animal
        super().__init__(name, legs, noise)

    def rawr(self):
        print(self._noise)


def main():
    # Creating an object (generic_animal) from a class (Animal)
    generic_animal = Animal("Sally", 2)
    # note that the param self is not passed. This is because generic_animal is the object which is self
    generic_animal.introduce()

    cat = Cat("Mr. Whiskers", 4, "Meow")
    cat.introduce()
    # directly calling the property from the initialized cat object
    print(f"I have {cat._legs} legs")

    dog = Dog("Good Boy", 4)
    dog.introduce()
    dog.bark()
    # can be used to set a new property or update an existing one - good practice is to set new properties in __init__
    dog.set_age(12)
    dog.set_legs(6)
    # alternative approach to obtaining a property or value from an object
    print(f"Dog age: {dog.get_age()}")
    print(f"New number of legs: {dog.get_legs()}")
    # can also perform actions and return the result
    print(f"Dog human age: {dog.get_human_age()}")

    # omitting the noise parameter and using default
    lion = Lion("Simba", 3)
    lion.introduce()
    lion.rawr()


if __name__ == "__main__":
    main()
