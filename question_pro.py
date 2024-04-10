import os

current_directory = os.getcwd()
target_directory = 'text_depo'
directory = os.path.join(current_directory, target_directory)

def search_text_in_files(directory, search_text):
    found_files = []  # List to store filenames where search text is found
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename.endswith('.txt'):
            with open(filepath, 'r') as file:
                for line in file:
                    if search_text in line:
                        found_files.append(filename)
                          # No need to continue searching in the same file once text is found change
    if found_files:
        print(f"Search text '{search_text}' found in the following files:")
        for file in found_files:
            print(file)
    else:
        print(f"Search text '{search_text}' not found in any files.")

search_text = input("enter value to search : ")
search_text_in_files(directory, search_text)