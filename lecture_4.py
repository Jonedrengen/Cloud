


class animal:
    def __init__(self, sound): #constructor
        self.sound = sound #adding variables (arguments when calling the class)
    
    def make_sound(self):
        return self.sound
    
    def print_all(self):
        pass

class Dog(animal):
    def __init__(self, sound):
        animal.__init__(self, sound)
        self.list_of_tricks = []

    def add_trick(self, trick):
        return self.list_of_tricks.append(trick)
    
    def print_me(self):
        return

class home(animal):
    def __init__(self):
        self.list_of_animals = []
    
    def add_animal(self, animal: animal):
        return self.list_of_animals.append(animal)
        



if __name__ == '__main__':
    d1 = Dog("vov")
    d1.add_trick("jump")
    d1.add_trick("fly")

    my_home = home()
    my_home.add_animal(d1)

    print(d1.make_sound())
    print(d1.list_of_tricks)
    print(my_home.list_of_animals)
