class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = person("John", 36)
person1.display()

class car:
    def __init__(self, make, model, year = 2025):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

car1 = car("Toyota", "Corolla")
car1.display_info()
car2 = car("Honda", "Civic", 2020)
car2.display_info()
