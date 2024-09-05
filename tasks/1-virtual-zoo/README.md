# Virtual Zoo
## Goal
Build a virtual zoo by using Python’s core concepts like classes, loops, lists, tuples, and dictionaries.


## Pre Work

- Create a csv called `animals.csv` and add the something like this to it? you can add more of each species, etc.

```
species,name,age
Lion,Simba,5
Elephant,Dumbo,10
Tiger,Shere Khan,8
```

## Tasks

1. Animal Class
- Create a class for each animal with attributes species, name, age


2. Zoo Class with Methods
Create a Zoo class that manages animals by passing the opening and closing hours of the zoo as turple, with the following methods:

- add_animal(): Adds a new animal to the zoo.
- get_all_animals(): Returns all the animals in the zoo.
- get_zoo_hours(): Returns the zoo’s opening and closing hours (stored as a tuple).
- get_species_count(): Returns the number of animals of each species (stored in a dictionary).


3. Reading from a CSV

Create a function to read animals' data from a CSV file and add them to the zoo automatically. Clues:
 - initialise a zoo class instance like outside the function: 
 ```
 zoo = Zoo(opening_times)
 ```
 - inputs: zoo class instance, csv path
 - outputs: none
 - Read the CSV file 
 - for each row of the csv create an `Animal()` instance
 - Add each animal to your `zoo` instance


4. Visitor Info Functions
   
Create the following functions to give the visitor info
- Given a time of arrival, let them whether the zoo is closed or opened
- Tell them how many animals are in the zoo
- Tell them how many animals are there per species
- Tell the age of the oldest animal and which one that is
- Tell the age of all animals combined


5. Bonus

- Use random.choice to randomly display a selection of animals when a visitor “visits” the zoo.
- Add functionality to allow users to add new animals via input.
