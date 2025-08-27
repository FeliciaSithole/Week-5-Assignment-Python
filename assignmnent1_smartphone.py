# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # private attribute (encapsulation)

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Invalid storage size!")

# Inherited class
class GamingPhone(Smartphone):
    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.get_storage()}GB storage!")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 128)
phone2 = GamingPhone("Asus", "ROG Phone 6", 256)

phone1.make_call("0818934752")
phone2.play_game("Genshin Impact")
