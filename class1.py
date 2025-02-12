class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def makeNoise(self):
        print("bonk")

class Cat(Pet):
    def __init__(self, age, name, color):
        super().__init__(name, age)
        self.color = color
    def makeNoise(self):
        print("Meow");
    def eatKibble(self):
        print("This kibble is not delicious human give me your left overs and the majority of your income")


class Dog(Pet):
    def __init__(self, age, name, breed):
        super().__init__(name, age)
        self.breed = breed
    def makeNoise(self):
        if(self.breed == "Chihuahua"):
            print("Yapyapyap")
        if(self.breed == "Shitzu"):
            print("Bork Bark")
        if(self.breed == "Havenese"):
            print("Bark Bark Bark Bark Bark Bark Bark")
        else:
            print("Bark Bark")

    def eatOwnersFood(self):
        print("You shouldn't do that")
