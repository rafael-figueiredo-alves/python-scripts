class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer.")
        self._age = value
    
# Example usage:
p = person("Alice", 30)
print(p.name)  # Output: Alice
print(p.age)   # Output: 30
p.age = 31
print(p.age)   # Output: 31
p.name = "Bob"
print(p.name)  # Output: Bob

p.city = "New York"  # Dynamically adding a new property
print(p.city)  # Output: New York
print(hasattr(p, 'city'))  # Output: True
del p.city  # Deleting the dynamically added property
print(hasattr(p, 'city'))  # Output: True