"""
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

file = open("arquivo.txt", "rt")  # Open a file for reading in text mode (standard)
content = file.read()
print(content)
file.close()  # Close the file when done

# using 'with' statement to handle file closing automatically
with open("arquivo.txt", "rt") as file:
    print(file.read())
# Then you do not have to worry about closing your files, the with statement takes care of that.

with open("arquivo.txt", "rt") as file:
    print(file.read(10)) # read the first 10 characters

with open("arquivo.txt") as f:
  print(f.readline()) # Read one line

try:
   with open("demofile.txt") as f:
    print(f.readline())
except FileNotFoundError:
   print("The file demofile.txt does not exist")

with open("arquivo.txt") as f:
  for x in f:
    print(f"=> {x}")