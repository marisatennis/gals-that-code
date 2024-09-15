from collections import Counter
import pandas as pd
import random

# create animals class
class Animals:
    def __init__(self, species: str, name: str, age: int):
        self.species=species
        self.name=name
        self.age=age

# to read animals in string form
    def __repr__(self):
        return f"{self.species}({self.name},{self.age} years old)"

# create zoo class
class Zoo:
    # pass opening and closing hours as tuple
    def __init__(self, openingtimes: tuple[str,str]):
        self.animals=[]
        self.openingtimes=openingtimes
    
    # add new animals
    def add_animal(self, animal: Animals):
        self.animals.append(animal)
    
    # return all animals as list
    def get_all_animals(self) -> list[Animals]:
        return self.animals

    # return zoo opening and closing hours as tuple
    def get_zoo_hours(self) -> tuple[str,str]:
        return self.openingtimes

    # return number of animals of each species as dict
    def get_species_count(self) -> dict[str,int]:
        species = [each.species for each in self.animals]
        return dict(Counter(species))

# read data from csv
def read_animals_data(zoo:Zoo):
    animal_df=pd.read_csv("zoo_env/Scripts/animals.csv")
    for index, row in animal_df.iterrows():
        species=row['species']
        name=row['name']
        age=row['age']
        animal = Animals(species,name,age)
        zoo.add_animal(animal)

# is the zoo open or closed
def zoo_open(zoo: Zoo, current_time) -> str:
    opening, closing=zoo.get_zoo_hours()
    if opening <= current_time <= closing:
        return("The zoo's open baby come in")
    else:
        return("The zoo's closed go home")

# number of animals in the zoo
def count_animals(zoo: Zoo) -> int:
    return len(zoo.get_all_animals())

# how many species
def no_of_species(zoo: Zoo) -> dict[str,int]:
    return zoo.get_species_count()

# age of oldest animal
def oldest_animal(zoo: Zoo) -> tuple[str,int]:
    animals=zoo.get_all_animals()
    oldest = max(animals, key=lambda a: a.age)
    return oldest.name, oldest.age

# combined age of all animals
def combined_age(zoo: Zoo):
  return sum(each.age for each in zoo.get_all_animals())

# random animals
def random_animals(zoo: Zoo) -> list[Animals]:
    return random.choice(zoo.get_all_animals())

# add animals using input
def input_animals(zoo: Zoo):
    species=input("Input the species of the animal: ")
    name=input("Input the name of the animal: ")
    age=input("Input the age of the animal: ")
    animal=Animals(species,name,age)
    zoo.add_animal(animal)
    print(f"Added {animal}")

# test outputs
openingtimes=("09:00","17:00")
zoo=Zoo(openingtimes)
read_animals_data(zoo)
current_time="12:00"
print("Current time: ", current_time, " -> " , zoo_open(zoo,current_time))
print("Number of animals: ", count_animals(zoo))
print("Species count: ",zoo.get_species_count())
print("Oldest animal:", oldest_animal(zoo))
print("Combined age of all animals:", combined_age(zoo))
print("Random animal: ", random_animals(zoo))

# choice to add animal
add_animal_question=input("Do you want to add an animal to the zoo? (Y/N): ")
if add_animal_question=="Y":
    input_animals(zoo)