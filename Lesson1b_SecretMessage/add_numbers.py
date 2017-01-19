from random import randint
import os

file_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prank')

def add_numbers():
    
    file_list = os.listdir(file_directory)
    #print(files_list)

    for file_name in file_list:
        new_name = os.path.join(str(randint(0,9)) + str(randint(0,9)) + file_name)
        os.rename(os.path.join(file_directory, file_name), os.path.join(file_directory, new_name))


add_numbers()
