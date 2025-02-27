class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (brand: {self.make}, top speed: {self.top_speed})"

def top_speed(cars):
    return max(cars, key=lambda car: car.top_speed).make # max for finding the car with highest speed

if __name__ == "__main__":
    car1 = Car("Porche", 250)
    car2 = Car("Toyota", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("GTR ", 295)

    cars = [car1, car2, car3, car4]
    print(top_speed(cars))  
