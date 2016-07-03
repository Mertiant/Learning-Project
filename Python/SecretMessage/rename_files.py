import os
def rename_files():
    
    #damn zamboni
    file_list = os.listdir(r"files")
    #cheese
    some_directory = os.getcwd();
    print("Directory is " + some_directory)
    os.chdir("files")
    print(file_list)
    print("Directory is " + os.getcwd())
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(some_directory)
    print("Directory is " + some_directory)
rename_files()