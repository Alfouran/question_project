import os

current_directory = os.getcwd()
target_directory = 'text_depo'
directory = os.path.join(current_directory, target_directory)

def search_text_in_files(directory, search_text):
    found_files = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename.endswith('.txt'):
            with open(filepath, 'r') as file:
                for line in file:
                    found = False
                    if search_text in line and not found:
                        if filename not in found_files:
                            found_files.append(filename)
                            found = True
                          
    if found_files:
        print(f"Search text '{search_text}' found in the following files:")
        for file in found_files:
            print(file)
    else:
        print(f"Search text '{search_text}' not found in any files.")

search_text = input("enter value to search : ")
search_text_in_files(directory, search_text)