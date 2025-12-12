import random

print(random.randrange(1,11))
print(random.randint(1,10))

# Sortear um valor aleatório de uma lista
lista = ['maçã', 'banana', 'laranja', 'uva', 'pera']
print(random.choice(lista))

lista1 = [10, 20, 30, 40, 50]
print(random.choice(lista1))
print(random.choices(lista1, k=3))  # Seleciona 3 elementos com reposição

# Embaralhar uma lista
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(cartas)
random.shuffle(cartas)
print(cartas)
print(random.sample(cartas, 5))  # Seleciona 5 cartas aleatórias da lista embaralhada

print(random.random())  # Gera um número float aleatório entre 0.0 e 1.0

print(random.uniform(1.5, 10.5))  # Gera um número float aleatório entre 1.5 e 10.5

"""
seed()	Initialize the random number generator
getstate()	Returns the current internal state of the random number generator
setstate()	Restores the internal state of the random number generator
getrandbits()	Returns a number representing the random bits
randrange()	Returns a random number between the given range
randint()	Returns a random number between the given range
choice()	Returns a random element from the given sequence
choices()	Returns a list with a random selection from the given sequence
shuffle()	Takes a sequence and returns the sequence in a random order
sample()	Returns a given sample of a sequence
random()	Returns a random float number between 0 and 1
uniform()	Returns a random float number between two given parameters
triangular()	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
betavariate()	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate()	Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate()	Returns a random float number based on the Gamma distribution (used in statistics)
gauss()	Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate()	Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate()	Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate()	Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate()	Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate()	Returns a random float number based on the Weibull distribution (used in statistics)
"""