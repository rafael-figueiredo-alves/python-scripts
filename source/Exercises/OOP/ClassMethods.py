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
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old."
    
    def is_adult(self):
        return self.age >= 18
    
    @staticmethod # diferente de classmethod nao recebe a classe como primeiro argumento
    def Inicializar(Nome, Idade):
        return person(Nome, Idade)

    @classmethod
    def New(cls):
        return cls("Default Name", 0)
    
    @classmethod # obriga a usar a classe como primeiro argumento e nao a instancia
    def FromString(cls, info_str):
        name, age = info_str.split(',')
        return cls(name.strip(), int(age.strip()))
    
# Example usage:
p = person("John", 30)
print(p)  # Output: Person(name=John, age=30)
print(p.birthday())  # Output: Happy birthday John! You are now 31 years old.
print(p.is_adult())   # Output: True
p.age = 17
print(p.is_adult())   # Output: False
p.city = "New York"  # Dynamically adding a new property
print(p.city)  # Output: New York

p2 = person.Inicializar("Jailza", 48)
print(p2)  # Output: Person(name=Jailza, age=48)
print(p2.is_adult())  # Output: True
print(p2.birthday())  # Output: Happy birthday Jailza! You are now 49 years old.
print(p2.name)  # Output: Jailza
print(p2.age)   # Output: 49
print(hasattr(p, 'city'))  # Output: True

p3 = person.New()
print(p3)  # Output: Person(name=Default Name, age=0)

p4 = person.FromString("Alice, 25")
print(p4)  # Output: Person(name=Alice, age=25)