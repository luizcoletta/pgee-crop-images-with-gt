def existing_directory(name_folder):
    import os
    if not os.path.exists(name_folder):
        print(name_folder + " directory does not exist, created")
        os.makedirs(name_folder)
    else:
        print(name_folder + " directory exists, no action performed")