# ============================================
# Assignment 1: Design Your Own Class! 
# ============================================

# Base Class
class Device:
    def __init__(self, brand, model):  # Constructor to initialize attributes
        self.brand = brand  # Set the brand of the device
        self.model = model  # Set the model of the device
    
    def power_on(self):  # Method to simulate powering on the device
        print(f"{self.brand} {self.model} is powering on...")

# Derived Class with Encapsulation
class Smartphone(Device):  # Smartphone inherits from Device
    def __init__(self, brand, model, storage):  # Constructor with extra attribute
        super().__init__(brand, model)  # Call parent constructor
        self.__storage = storage  # Private attribute (encapsulation)
    
    def install_app(self, app_name):  # Method to install an app
        print(f"Installing {app_name} on {self.brand} {self.model}.")

    def get_storage(self):  # Public method to access private storage
        return f"Storage capacity: {self.__storage}GB"

# Create a Smartphone object with unique values
phone1 = Smartphone("Samsung", "Galaxy S25", 256)  # Instantiate Smartphone
phone1.power_on()  # Call inherited method
phone1.install_app("WhatsApp")  # Call Smartphone-specific method
print(phone1.get_storage())  # Access encapsulated attribute via method

# ============================================
# Assignment 2: Polymorphism Challenge! 🎭
# ============================================

# Define a Car class with move() method
class Car:
    def move(self):  # Method defined differently for each class
        print("Driving")

# Define a Plane class with move() method
class Plane:
    def move(self):
        print("Flying")

# Define a Boat class with move() method
class Boat:
    def move(self):
        print("Sailing")

# List of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Loop through each object and call the same method name 'move()'
for v in vehicles:
    v.move()  # Polymorphism: behavior changes based on object type
