import pandas as pd

# Create animal class to use as a template "base class"
class animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
# this is needed so you can actually read the data
    def __repr__(self):
        return f"{self.species} - {self.name}, {self.age} years old"

# Create a function to create a class for each species
def createAnimalClass(species, name, age):
    class Animal(animal):
        def __init__ (self, name, age):
            super().__init__(species, name, age)
            
    return Animal

# create zoo
class zoo:
    def __init__(self, openingTime, closingTime):
        self.openingTime = openingTime
        self.closingTime = closingTime
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_all_animals(self):
        return (self.animals)
    
    def get_zoo_hours(self):
        return (self.openingTime, self.closingTime)
    
    def get_species_count(self):
        species_counter = {}
        for animal in self.animals:
            if animal.species in species_counter:
                species_counter[animal.species] += 1 
            else:
                species_counter[animal.species] = 1     
        return species_counter
    
my_zoo = zoo(openingTime = '08:00', closingTime = '18:00')

# add animal to the zoo funcation
def addAnimalToZoo(zoo, csv):
    animal_df = pd.read_csv(csv)
# iterate through csv and create an animal class 
    for index,row in animal_df.iterrows():
        species = row["species"]
        newAnimal = createAnimalClass(species, row["name"], row["age"])
        animal_instance = newAnimal(row["name"], row["age"])
        zoo.add_animal(animal_instance)

addAnimalToZoo(my_zoo, "zoo_env/animals.csv")

# Get and print all animals
print("All animals in the zoo:")
print(my_zoo.get_all_animals())

# Get and print the zoo hours
print("\nZoo hours:")
print(my_zoo.get_zoo_hours())

# Get and print the species count
print("\nSpecies count:")
print(my_zoo.get_species_count())


def VisitorInfo(arrival):

    def IsItOpen(arrival):
        opening = my_zoo.openingTime
        closing = my_zoo.closingTime

        if opening <= arrival <= closing:
            return("Come on in, that'll be £25")
        
        else:
            return("C L O S E D")
    
  #  def NumberOfAnimals():
       


