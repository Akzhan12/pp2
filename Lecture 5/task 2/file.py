import os, os.path

print('-----------------------------')
print("Hi!")
print('-----------------------------\n')

def Main_Menu():
    print("\n---------------------\n")
    print("'1' -- Work with directory")
    print("'2' -- Work with file")
    print("'0 or stop' -- Exit\n")
    print('Current directory:  ', curDir, end = '\n')
    print("\n---------------------\n")

def Dir_Menu():
    print("\nYou're working with directory\n")
    print("'a' -- Rename directory")
    print("'b' -- Number of files")
    print("'c' -- Number of directories")
    print("'d' -- Content of the directory")
    print("'e' -- Add file")
    print("'f' -- New directory\n")

def File_Menu():
    print("\nYou're working with file\n")
    print("'a' -- Delete file")
    print("'b' -- Rename file")
    print("'c' -- Add content to file")
    print("'d' -- Rewrite content of file")
    print("'e' -- Return to the parent directory\n")

def Dir_Rename():
    Dir_Name = input('\nThe directory name: ')
    if os.path.isdir(Dir_Name):
        Dir_New_Name = input('The new name of directory:  ')
        os.rename(Dir_Name, Dir_New_Name)
        print('\nThe directory has renamed!\n')
    else:
        print('\nThe direction does not exist!\n')

def Dir_File_Count():
    Dir_Name = input('\nEnter direction:  ')
    if os.path.isdir(Dir_Name):
        files = next(os.walk(Dir_Name))[2]
        print("\nNumber of files: ", len(files), end = '\nDone!')
    else:
        print('\nThe direction does not exist!\n')

def Dir_Count():
    Dir_Name = input('\nEnter direction:  ')
    if os.path.isdir(Dir_Name):
        files = os.listdir(Dir_Name)
        print("\nNumber of directories: ", len(files), end = '\nDone!')
    else:
        print('\nThe direction does not exist!\n')

def Dir_Content():
    Dir_Name = input('\nEnter direction:  ')
    if os.path.isdir(Dir_Name):
        print('Content of directory:\n')
        files = os.listdir(Dir_Name)
        for i in files:
            print(i)
    else:
        print('\nThe direction does not exist!\n')

def Cur_Dir_Add_File():
    file_name = input('\nFilename:  ')
    try:
        open(file_name, 'x')
        print('\nFile added.\n')
    except FileExistsError:
        print('\nFile already exists!\n')

def New_Dir_Add():
    Dir = input("\nNew directory's directory:  ")
    if os.path.isdir(Dir):
        Dir_Name = input("New directory's name:  ")
        print(Dir_Name)
        if os.path.isdir(Dir + Dir_Name):
            print('\nDirection already exists!\n')
        else:
            os.mkdir(Dir + Dir_Name)
            print('\nDirection Added.\n')
    else:
        print('\nGiven direction does not exist!\n')

def File_Delete():
    filename = input('\nFilename:  ')
    if os.path.exists(filename):
        os.remove(filename)
        print('\nThe file removed.\n')
    else:
        print('\nThe file does not exist!\n')

def File_Rename():
    filename = input('\nFilename:  ')
    if os.path.exists(filename):
        new_file_name = input('New filename:  ')
        os.rename(filename, new_file_name)
        print('\nThe file renamed.\n')
    else:
        print('\nThe file does not exist!\n')

def Content_Add_File():
    filename = input('\nFilename:  ')
    if os.path.exists(filename):
        print("\nNote: If you're done with adding content - enter 'Done'\n")
        f = open(filename, 'a')
        while True:
            content = input()
            if content != 'Done':
                f.write(content + '\n')
            else:
                f.close()
                print('\nAdded content to the file.\n')
                break
    else:
        print('\nFile does not exist!\n')

def Rewrite_Content_File():
    filename = input('\nFilename:  ')
    if os.path.exists(filename):
        f = open(filename, 'w')
        print("\nNote: If you're done with rewriting content - enter 'Done'\n")
        while True:
            content = input()
            if content != 'Done':
                f.write(content + '\n')
            else:
                f.close()
                print('\nAdded content to the file.\n')
                break
    else:
        print('\nFile does not exist!\n')

def Par_Dir_Return():
    filename = input('\nFilename:  ')
    if os.path.exists(filename):
        path = os.path.abspath(os.path.join(os.path.dirname(filename),".."))
        print('\nThe parent directory is: ', path)
    else:
        print('\nFile does not exist!\n')

while True:
    curDir = os.getcwd()
    Main_Menu()
    users_choice = input('Select a type of work:  ')

    if users_choice == '1':
        Dir_Menu()
        users_choice_dir = input('Select an action with directory:  ')
        if users_choice_dir == 'a':
            Dir_Rename()
        elif users_choice_dir == 'b':
            Dir_File_Count()
        elif users_choice_dir == 'c':
            Dir_Count()
        elif users_choice_dir == 'd':
            Dir_Content()
        elif users_choice_dir == 'e':
            Cur_Dir_Add_File()
        elif users_choice_dir == 'f':
            New_Dir_Add()
        else:
            print('Input error!\nPlease, enter the given characters')

    elif users_choice == '2':
        File_Menu()
        users_choice_file = input('Select an action with file:  ')
        if users_choice_file == 'a':
            File_Delete()
        elif users_choice_file == 'b':
            File_Rename()
        elif users_choice_file == 'c':
            Content_Add_File()
        elif users_choice_file == 'd':
            Rewrite_Content_File()
        elif users_choice_file == 'e':
            Par_Dir_Return()
        else:
            print('Input error!\nPlease, enter the given characters')

    elif users_choice == '0' or users_choice == 'stop':
        print('\nThe work with the file manager is over\nGood luck!')
        exit()
    
    else:
        print('\nError! Please, choose the given actions.\n')