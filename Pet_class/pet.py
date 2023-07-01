# This program allows the user to input and store pet information (name, animal type, and age) and displays the saved data on the screen.

# Import tkinter for designs
import tkinter as tk
from tkinter import messagebox
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

# Create another class for gui
class PetGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pet Information")
        self.window.geometry("400x200")
        self.window.configure(bg="#F0EAD6")

        self.pet = Pet()

        self.name_label = tk.Label(self.window, text="Name:", bg="#FFDAB9")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.window, bg="#FFEFD5")
        self.name_entry.pack()

        self.type_label = tk.Label(self.window, text="Animal Type:", bg="#98FB98")
        self.type_label.pack()

        self.type_entry = tk.Entry(self.window, bg="#E0FFFF")
        self.type_entry.pack()

        self.age_label = tk.Label(self.window, text="Age:", bg="#B0C4DE")
        self.age_label.pack()

        self.age_entry = tk.Entry(self.window, bg="#FFC0CB")
        self.age_entry.pack()

        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_pet_info, bg="#87CEFA")
        self.submit_button.pack(pady=10)
            
    # Submit and display the info given by the user
    def submit_pet_info(self):
        name = self.name_entry.get()
        animal_type = self.type_entry.get()
        age = self.age_entry.get()

        self.pet.set_name(name)
        self.pet.set_animal_type(animal_type)
        self.pet.set_age(age)

        self.display_pet_info()

        messagebox.showinfo("Success!", "Pet information saved! Thank you!")

    def display_pet_info(self):
        info = f"Name: {self.pet.get_name()}\nAnimal Type: {self.pet.get_animal_type()}\nAge: {self.pet.get_age()}"
        messagebox.showinfo("Pet Information", info)
        
# Run the main program