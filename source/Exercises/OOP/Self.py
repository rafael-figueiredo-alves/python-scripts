class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def display_self(self):
        self.display()

person1 = person("Alice", 30)
person1.display_self()

class car:
    def __init__(car_instance, make, model, year = 2025): # usando 'car_instance' em vez de 'self'
        car_instance.make = make
        car_instance.model = model
        car_instance.year = year

    def display_info(self): 
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

    def display_self_info(car_instance): # usando 'car_instance' em vez de 'self'
        car_instance.display_info()

car1 = car("Toyota", "Corolla")
car1.display_self_info()