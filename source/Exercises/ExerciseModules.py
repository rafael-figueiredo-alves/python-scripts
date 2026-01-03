import Exercise_Module # importando módulo completo

print(Exercise_Module.greets("Alice")) # Should print "Hello, Alice!"
print(Exercise_Module.sum_numbers(3, 7)) # Should print 10
print(Exercise_Module.numbers) # Should print [4, 5]
print(Exercise_Module.sum_numbers(*Exercise_Module.numbers)) # Should print 9

import Exercise_Module as em # importando módulo com alias

print(em.greets("Bob")) # Should print "Hello, Bob!"
print(em.sum_numbers(10, 15)) # Should print 25

from Exercise_Module import greets, sum_numbers # importando funções específicas

print(greets("Charlie")) # Should print "Hello, Charlie!"
print(sum_numbers(20, 30)) # Should print 50

from Exercise_Module import * # importando tudo do módulo

print(greets("Diana")) # Should print "Hello, Diana!"
print(sum_numbers(5, 10)) # Should print 15

import Exercise_Module

print(dir(Exercise_Module)) # Should list all attributes and methods in Exercise_Module

import platform

print(platform.system()) # Should print the system/OS name
print(platform.version()) # Should print the system's release version
print(platform.machine()) # Should print the machine type
print(platform.processor()) # Should print the (real) processor name
print(platform.python_version()) # Should print the Python version
print(platform.python_build()) # Should print the Python build number and date
print(platform.python_compiler()) # Should print the Python compiler information
print(platform.python_implementation()) # Should print the Python implementation (e.g., CPython)
print(platform.uname()) # Should print a named tuple with system information
print(platform.node()) # Should print the computer's network name
print(platform.architecture()) # Should print the bit architecture (e.g., '64bit')
print(dir(platform)) # Should list all attributes and methods in platform module