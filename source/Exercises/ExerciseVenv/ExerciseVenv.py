# python -m venv ExerciseVenv
# source ExerciseVenv/bin/activate  (Linux/macOS)
# ExerciseVenv\Scripts\activate     (Windows)
# To deactivate the virtual environment, use the command:
# deactivate
# pip install --upgrade pip 
# pip install -r requirements.txt (to install dependencies if any) 
# rmdir /s /q myfirstproject (to remove a directory on Windows)
# rm -rf myfirstproject (to remove a directory on Linux/macOS)
# python -m pip freeze > requirements.txt (to create a requirements file)
# python -m pip install package_name (to install a package)

print("This is the ExerciseVenv module.")

import cowsay
cowsay.cow("Hello from the virtual environment!")
cowsay.tux("Virtual environment is active!")
cowsay.dragon("Python virtual environments are great!")