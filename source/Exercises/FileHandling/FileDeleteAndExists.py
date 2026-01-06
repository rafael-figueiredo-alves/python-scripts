import os

def delete_file_if_exists(file_path):
    """Deletes the file at file_path if it exists.

    Args:
        file_path (str): The path to the file to be deleted.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"File '{file_path}' does not exist.")

# Example usage:
file_to_delete = 'example.txt'
delete_file_if_exists(file_to_delete)
# Check if the file still exists
if os.path.exists(file_to_delete):
    print(f"File '{file_to_delete}' still exists.")

delete_file_if_exists("arquivo.txt")
delete_file_if_exists("demofile.txt")
delete_file_if_exists("demofile1.txt")
delete_file_if_exists("demofile2.txt")