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

class student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Student ID must be a string.")
        self._student_id = value

    def __str__(self):
        print(super())
        return f", student_id={self.student_id})"
    
# Example usage:
s = student("Charlie", 20, "S12345")
print(s.name)        # Output: Charlie
print(s.age)         # Output: 20
print(s.student_id)  # Output: S12345
print(s)