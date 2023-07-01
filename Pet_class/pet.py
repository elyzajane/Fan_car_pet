# This program allows the user to input and store pet information (name, animal type, and age) and displays the saved data on the screen.

# Create a class for pet
class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # Get and set the name, type and age of the animal
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self__age
    
    # Submit and display the info given by the user
    def submit_pet_info(self):
        name = self.name_entry.get()
        animal_type = self.type_entry.get()
        age = self.age_entry.get()

        self.pet.set_name(name)
        self.pet.set_animal_type(animal_type)
        self.pet.set_age(age)

        self.display_pet_info()


# Run the main program