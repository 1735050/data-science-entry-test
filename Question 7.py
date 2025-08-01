class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def __init__(self, make, model, year):
        # Initialize the car's make, model, and year attributes
        self.make = make          # Assign the input 'make' to the instance's 'make' attribute
        self.model = model        # Assign the input 'model' to the instance's 'model' attribute
        self.year = year          # Assign the input 'year' to the instance's 'year' attribute


    def describe_car(self):
        # This method prints the car’s information in a formatted string: "Year Make Model"
        print(f"{self.year} {self.make} {self.model}")





# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020


# Create an instance of the Car class with specific attributes
my_car = Car("Toyota", "Corolla", 2020)

# Call the describe_car method to print car details
my_car.describe_car()  # Expected output: 2020 Toyota Corolla
