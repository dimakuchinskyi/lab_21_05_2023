import random
class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
        self.health = 100
        self.hunger = 0
        self.happiness = 100
    def grow(self):
        self.age += 1
        self.health -= random.randint(1, 10)
        self.hunger += random.randint(1, 10)
        self.happiness -= random.randint(1, 10)
    def eat(self):
        if self.hunger > 0:
            self.hunger -= random.randint(1, 10)
            self.happiness += random.randint(1, 10)
    def play(self):
        if self.happiness > 0:
            self.happiness -= random.randint(1, 10)
            self.hunger += random.randint(1, 10)
    def __str__(self):
        return f"{self.name} ({self.species}) - Age: {self.age}, Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}"
class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def remove_animal(self, animal):
        self.animals.remove(animal)
    def feed_all(self):
        for animal in self.animals:
            animal.eat()
    def play_with(self):
        for animal in self.animals:
            animal.play()
    def grow_all(self):
        for animal in self.animals:
            animal.grow()
    def save_zoo_state(self, day):
        filename = f"Day_{day}.txt"
        with open(filename, "w") as file:
            file.write(f"Zoo state - Day {day}\n\n")
            for animal in self.animals:
                file.write(str(animal) + "\n")
zoo = Zoo()
lion = Animal("Lion", "Максік", 3)
elephant = Animal("Elephant", "Хлеб", 5)
zebra = Animal("Zebra", "Сімба", 2)
zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(zebra)
for day in range(1, 11):
    zoo.feed_all()
    zoo.play_with()
    zoo.grow_all()
    zoo.save_zoo_state(day)
