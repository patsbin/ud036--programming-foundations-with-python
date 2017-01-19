import os

def rename_files():
    file_directory  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prank/')
    file_list       = os.listdir(file_directory)
    
    saved_path= os.getcwd()
    os.chdir(file_directory)
    
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789")) 

    os.chdir(saved_path)


rename_files()
