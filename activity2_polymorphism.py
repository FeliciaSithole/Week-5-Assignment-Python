class Car:
    def move(self):
        print("Driving on the road")

class Plane:
    def move(self):
        print("Flying in the sky")

class Boat:
    def move(self):
        print("Sailing on the water")

# Function demonstrating polymorphism
def start_moving(vehicle):
    vehicle.move()

# Objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# All vehicles use the same interface, move(), but act differently
for vehicle in [my_car, my_plane, my_boat]:
    start_moving(vehicle)
