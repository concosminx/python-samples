#return values for functions
def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    return f"{car['make']} {car['model']}"

def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon.")

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    print_car_info(car)

def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y


print(divide(10, 2))
print(divide(6, 0))