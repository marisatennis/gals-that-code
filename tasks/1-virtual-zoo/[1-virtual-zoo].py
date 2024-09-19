#0. Necessary imports
import csv
import datetime, time
import random

#1. Create an Animal class with attributes Species, Name and Age
class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

#2. Create a Zoo class with attribute opening_times
class Zoo:
    def __init__ (self,opening_times):
        self.opening_times = opening_times
        self.zoo_animals = []
#2.1. Method 1: add_animal(): Adds a new animal to the zoo.
    def add_animal(self, species, name, age):
        new_animal = Animal(species, name, age)
        self.zoo_animals.append(new_animal)
#2.2. Method 2: get_all_animals(): Returns all the animals in the zoo.
    def get_all_animals(self):
        return self.zoo_animals
#2.3. Method 3: get_zoo_hours(): Returns the zoo’s opening and closing hours (stored as a tuple).
    def get_zoo_hours(self):
        return self.opening_times
#2.4. Method 4: get_species_count(): Returns the number of animals of each species (stored in a dictionary).
    def get_species_count(self):
        species_count = {}
        for zoo_animal in self.zoo_animals:
            species_count[zoo_animal.species] = species_count.get(zoo_animal.species, 0) + 1
        return species_count
    
#3. Create a function to read animals' data from a CSV file and add them to the zoo automatically.
    def add_animals_from_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                species = row['species']
                name = row['name']
                age = row['age'] 
                animal = Animal(species, name, age)
                self.add_animal(animal)  

#4. Visitor Info Functions
#4.1 Given a time of arrival, let them know whether the zoo is closed or opened
class Zoo:
    def is_zoo_open(self, arrival_time):
        arrival_time = datetime.strptime(arrival_time, '%H:%M').time()
        if self.opening_times[0] <= arrival_time <= self.opening_times[1]:
            print("The zoo is open at that time.")
        else: 
            print("The zoo is closed at that time.")
#4.2 Tell them how many animals are in the zoo
    def get_animal_count(self):
        return len(self.zoo_animals)
#4.3. Tell them how many animals are there per species
    #See 2.4.
#4.4. Tell the age of the oldest animal and which one that is
    def get_age(self, animal):
        return animal.age
    def find_oldest_animal(self):
        oldest_animal = max(self.zoo_animals, key=self.get_age)
        return oldest_animal
#4.5. Tell the age of all animals combined
    def sum_ages(self):
        total_age = sum(animal.age for animal in self.zoo_animals)
        return total_age
#Full 4
class Zoo:
    def Visitor_Info(self):
            arrival_time = input("Enter your arrival time (HH:MM) to check if the zoo is open: ") #Ask for arrival time
            self.is_zoo_open(arrival_time) #Is it open at that time?
            print(f"Number of animals in the zoo: {self.get_animal_count()}") #Animals in the zoo
            print(f"These are the animals per species in the zoo: {self.get_species_count()}") #Animals per species
            print(f"This is the oldest animal in the zoo: {self.find_oldest_animal()}") #Oldest animal
            print(f"This is sum of all animals in the zoo combined: {self.sum_ages()}")
            print("Enjoy the zoo!")


#5. Bonus
#5.1. Use random.choice to randomly display a selection of animals when a visitor “visits” the zoo.
            print((f"This our animal of the day: {random.choice(self.animals)}"))

#5.2. Add functionality to allow users to add new animals via input.
class Zoo:
   def user_add_animal(self):
    species = input("Enter the species of the animal: ")
    name = input("Enter the name of the animal: ")
    age = int(input("Enter the age of the animal: "))
    print("Thank you!")
    self.add_animal(species, name, age)



#Example: 
Nemo=Animal('Fish', 'Nemo', 1)
Elenari=Zoo(time(10,0), time(18,0))
Elenari.add_animals_from_csv('Animals.csv')
Elenari.add_animal(Nemo)
Elenari.get_all_animals
Elenari.get_zoo_hours
Elenari.get_species_count
