# This program defines a Fan class to represent a fan with methods to access and modify its speed, on/off state, radius, and color.

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

# Run the program
