with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

try:
    with open("demofile1.txt", "a") as f:
        f.write("Hello world!")
except FileExistsError:
   with open("demofile1.txt", "w") as f:
      f.write("File created because it did not exist.")

"""
open("demofile1.txt", "w") => replaces the content of the file if it already exists
open("demofile1.txt", "x") => creates the file, returns an error if the file exists
open("demofile1.txt", "a") => appends to the end of the file if it exists
"""

try:
    with open("demofile2.txt", "x") as f:
        f.write("Hello world 2!")
except FileExistsError:
   with open("demofile2.txt", "w") as f:
      f.write("File created because it exists 2.")