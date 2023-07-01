# This program defines a simple car class that displays car information and control car speed with accelerate and brake buttons.

#Import tkinter for designs
import tkinter as tk

# Create a class for Car
class Car:
    def __init__(self, year_model, make):
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
        return f"Brand: {self.__make}\nYear Model: {self.__year_model}"
    
# Create a class for gui, set labels and designs
class CarGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Car Acceleration")
        self.window.geometry("600x400")

        self.car = Car(2022, "Toyota")

        self.info_frame = tk.LabelFrame(self.window, text="Car Information", padx=60, pady=30, fg="black", bg="lightpink")
        self.info_frame.pack(pady=10)

        self.info_label = tk.Label(self.info_frame, text=self.car.get_info(), fg="black", bg="lightblue")
        self.info_label.pack(pady=5)

        self.speed_frame = tk.LabelFrame(self.window, text="Speed", padx=40, pady=20, fg="black", bg="lightyellow")
        self.speed_frame.pack(pady=10)

        self.speed_label = tk.Label(self.speed_frame, text=f"{self.car.get_speed()}", fg="black", bg="white")
        self.speed_label.pack(pady=5)

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=10)

        self.accelerate_button = tk.Button(self.button_frame, text="Accelerate", command=self.accelerate_car, bg="orange", fg="black", width=10)
        self.accelerate_button.grid(row=0, column=0, padx=5)

        self.brake_button = tk.Button(self.button_frame, text="Brake", command=self.brake_car, bg="violet", fg="black", width=10)
        self.brake_button.grid(row=0, column=1, padx=5)

    def accelerate_car(self):
        self.car.accelerate()
        speed = self.car.get_speed()
        self.update_speed(speed)

    def brake_car(self):
        self.car.brake()
        speed = self.car.get_speed()
        self.update_speed(speed)

    def update_speed(self, speed):
        self.speed_label.config(text=speed)
    
# Run the main program
    def run(self):
        self.window.mainloop()

# Create an instance of the CarGUI class
gui = CarGUI()
gui.run()