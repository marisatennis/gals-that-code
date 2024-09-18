# Animal Class

class Animal:
    def __init__ (self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

# Zoo Class

class Zoo:
    
    def __init__(self, opening_times):
        self.opening_times = opening_times
        self.animals = []
        
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise TypeError("Only objects of type 'Animal' can be added to the zoo")

    def get_all_animals(self):
        return self.animals

    def get_zoo_hours(self):
        print(self.opening_times)

    def get_species_count(self):
        species_count = {}
        for animal in self.animals:
            if animal.species in species_count:
                species_count[animal.species] += 1
            else:
                species_count[animal.species] = 1
        return species_count


my_zoo = Zoo("09:00 - 17:00")


# Read CSV

import csv

def load_animals_from_csv(file_path, my_zoo):
    with open(file_path, mode = 'r') as file:
        csvFile = csv.reader(file)
        
        next(csvFile)

        for line in csvFile:
            species, name, age = line
            animal = Animal(species, name, age)
            my_zoo.add_animal(animal)

file_path = "animals.csv"
load_animals_from_csv(file_path, my_zoo)

for animal in my_zoo.get_all_animals():
    print(f"{animal.name} the {animal.species}, Age: {animal.age}")


print("Species count:", my_zoo.get_species_count())



# Visitor Information Functions



def get_animal_count(my_zoo):
    return len(my_zoo.animals)

def get_oldest_animal(my_zoo):
    oldest_animal = max(my_zoo.animals, key=lambda animal: animal.age)
    return(oldest_animal.name, oldest_animal.species, oldest_animal.age)

def combined_animal_ages(my_zoo):
    combined_age = sum(my_zoo.animals, key=lambda animal:animal.age)
    return combined_age



# Bonus
import random

def random_selection(my_zoo):
    random_animals = random.choice(my_zoo.animals)
    return random_animals

def input_animal(my_zoo):
    species = input("Enter animal species: ")
    name = input("Enter animal name: ")
    age = ("Enter animal age: ")

    try:
        age = int(age)
    except ValueError:
        print("Age must be a valid number.")
        return
    
    new_animal = Animal(species, name, age)

    my_zoo.add_animal(new_animal)
    print(f"{name} the {species} has been added to the zoo!")
