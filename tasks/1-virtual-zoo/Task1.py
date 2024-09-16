# #Part 1 - Create a class for each animal with attributes species, name, age
class Animal1:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

a1 = Animal1("Lion","Simba", 5)

class Animal2:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

a2 = Animal2("Elephant","Dumbo",10)

class Animal3:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

a3 = Animal3("Tiger","Shere Khan",8)

class Animal4:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

a4 = Animal4("Cat", "Tom",2)

class Animal5:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
a5 = Animal5("Mouse","Jerry",4)

# #Part 2 - Create a Zoo class that manages animals by passing the opening and closing hours of the zoo as turple:

class zoo:
    def __init__(self, operating_time): ## tuple
        self.opening = operating_time[0]
        self.closing = operating_time[1]
        self.animals = []


    def add_animal(self, species, name, age): ## object method
        animal = {
        'species': species,
        'name': name,
        'age': age
        }
        self.animals.append(animal)
        print(f"{name} the {species} has been added to the zoo")

    def get_all_animals(self):
        if not self.animals:
            print("There are no animals in the zoo.")
        else:
            for animal in self.animals:
                print(f"{animal['name']} the {animal['species']} (Age: {animal['age']})")

    def get_zoo_hours(self): 
        print(f"The zoo is open from {self.opening} to {self.closing}.")

    def get_species_count(self):
        species_count = {}
        for animal in self.animals:
            species = animal['species']
            if species in species_count:
                species_count[species] += 1
            else:
                species_count[species] = 1
        return species_count

zoo = zoo(("09:00 AM", "17:30 PM")) 
zoo.get_zoo_hours()
zoo.add_animal("Lion", "Simba", 5)
zoo.get_all_animals()
species_count = zoo.get_species_count()
print(species_count)

#3. Reading from a CSV - Create a function to read animals' data from a CSV file and add them to the zoo automatically
from datetime import datetime

class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = int(age)

class Zoo:
    def __init__(self, operating_time): ## tuple
        self.opening = operating_time[0]
        self.closing = operating_time[1]
        self.animals = [] #list to store the animals

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.name} is a {animal.species} and is {animal.age} years old.")

import csv

def read_csv__and_create_instance(zoo, filename):
    animals = [] #List to store instances
    with open(filename, mode ='r') as file: #Reading the file
        csv_reader = csv.reader(file)
        next(csv_reader) #Skip the header

        for row in csv_reader: #For each row, create an instance
            species, name, age = row
            animal_instance = Animal(species, name, age) #Create an instance
            zoo.add_animal(animal_instance) #Store the instance in a list

zoo = Zoo(("0900","1730"))  # Initialize the Zoo instance outside the function

read_csv__and_create_instance(zoo, "C:/Users/clare/Documents/GalsThatCode/gals-that-code/tasks/1-virtual-zoo/animals.csv") #Call the function

zoo.display_animals()

# 4. Visitor Info Functions - Create the following functions to give the visitor info:
# - Given a time of arrival, let them whether the zoo is closed or opened
def check_zoo_opening(zoo, arrival_time_str):
    opening_time = datetime.strptime(zoo.opening, '%H%M').time()
    closing_time = datetime.strptime(zoo.closing, '%H%M').time()
    arrival_time = datetime.strptime(arrival_time_str, '%H%M').time()

    if opening_time <= arrival_time <= closing_time:
        return "Welcome, the zoo is open!"
    else:
        return "Sorry, the zoo is closed."
    
print(check_zoo_opening(zoo, "1050"))
print(check_zoo_opening(zoo, "1800"))

# - Tell them how many animals are in the zoo
def animal_count(zoo):
    return len(zoo.animals)

print(f"Number of animals in the zoo: {animal_count(zoo)}")

# - Tell them how many animals are there per species
def species_count(zoo):
    species_count_dict = {}
    for animal in zoo.animals:
        if animal.species in species_count_dict:
            species_count_dict[animal.species] += 1
        else:
            species_count_dict[animal.species] = 1
    return species_count_dict

print(f"Species in the zoo: {species_count(zoo)}")

# - Tell the age of the oldest animal and which one that is
def oldest_animal(zoo):
    oldest = zoo.animals[0]  # Assume the first animal is the oldest initially
    for animal in zoo.animals:
        if animal.age > oldest.age:
            oldest = animal
    return oldest

oldest = oldest_animal(zoo)
print(f"The oldest animal in the zoo is {oldest.name}, aged {oldest.age}")

# - Tell the age of all animals combined
def adding_ages(zoo):
    total_age = 0
    for animal in zoo.animals:
        total_age += animal.age
    return total_age

total_age = adding_ages(zoo)
print(f"The total age of the animals is {total_age}")