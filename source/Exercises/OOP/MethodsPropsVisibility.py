class person:
    """
    Público: sem underscore → uso livre.

Privado (convencional): _metodo → não recomendado fora da classe.

Privado com name mangling: __metodo → mais protegido, mas ainda acessível com truques.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name # Getter for name

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
    
    def _greetPrivado(self):
        return f"Hello, my name is {self.name}."
    
    def __greetNameMangling(self):
        return f"I am {self.age} years old."
    
    def greet(self):
        private_greet = self._greetPrivado()
        name_mangling_greet = self.__greetNameMangling()
        return f"{private_greet} {name_mangling_greet}"
    
# Exemplo de uso
p = person("Rafaela", 17)
print(p.greet())  # Acesso ao método público que usa os métodos privados internamente
# Acesso direto ao método privado convencional (não recomendado)
print(p._greetPrivado())
# Acesso ao método com name mangling (não recomendado, mas possível)
print(p._person__greetNameMangling())