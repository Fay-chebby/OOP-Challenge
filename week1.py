
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 6
        self.energy = 7
        self.happiness = 9
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played")
        else:
            print(f"{self.name} is too tired to play, let them rest")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} learned a new trick: {trick}")

    def show_trick(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet")

    def get_status(self):
        print(f"\n {self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10\n")


my_pet = Pet ("Puppy")
my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.train("Eat")
my_pet.sleep()
my_pet.show_trick()


             
                       
                
      

               