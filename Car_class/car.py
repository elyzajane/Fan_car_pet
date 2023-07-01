# This program defines a simple car class that displays car information and control car speed with accelerate and brake buttons.

# Create a class for Car
class Car:
    def __init_(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Use def functions to accelerate and brake to set the car's speed
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed
    
    # Get the info of the car
    def get_info(self):
        return f"Brand: {self.__make}\Year Model: {self.__year_model}"
    
# Run the main program