# This program defines a Fan class to represent a fan with methods to access and modify its speed, on/off state, radius, and color.

# Import tkinter for designs
import tkinter as tk
from tkinter import messagebox

# Create a class for fan
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=1, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Get and set the speed
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    # Set the fan on
    def is_on(self):
        return self.__on

    def set_on(self, on):
        self.__on = on

    # Get and set the radius
    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    # Get and set the color
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
# Create a class for gui
class FanPropertiesGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Fan Properties")
        self.window.configure(bg='lightyellow')
        self.window.geometry("400x300")  
        
        # Create labels to display fan properties
        fan1_button = tk.Button(self.window, text="Fan 1", command=lambda: self.display_fan_properties(
            Fan(speed=Fan.FAST, radius=10, color='yellow', on=True), "Fan 1"), bg='lightblue')
        fan1_button.pack(pady=30)

        fan2_button = tk.Button(self.window, text="Fan 2", command=lambda: self.display_fan_properties(
            Fan(speed=Fan.MEDIUM, radius=5, color='blue', on=False), "Fan 2"), bg='lightpink')
        fan2_button.pack(pady=30)

    def display_fan_properties(self, fan, fan_number):
        messagebox.showinfo(f"Fan {fan_number} Properties", f"Speed: {fan.get_speed()}\n"
                                                           f"Radius: {fan.get_radius()}\n"
                                                           f"Color: {fan.get_color()}\n"
                                                           f"On: {fan.is_on()}")
        
# Run the program
