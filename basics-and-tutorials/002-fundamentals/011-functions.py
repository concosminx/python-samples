def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

#greet()

#function used to calculate miles / gallon
def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    calculate_mpg(car)