# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickle and Exceptions
# ChangeLog (Who,When,What):
# GYJ, 22.5.21, Creation of Assignment 07 file
# GYJ, 24.5.21 ,Addition of code to complete Assignment 07
# ---------------------------------------------------------------------------- #

import pickle

#--Data--#
strTask = ""                         # string task to include in table
strPriority = ""                     # priority of task
lstTable = []                        # table list
file_name = "picklelist.dat"         # .dat file to save into
choice = ""                          #menu selection

#-- Processing --#

def write_to_file(data, file_name):
    """ Creates binary file and writes to file"""
    objfile = open(file_name, 'ab')     #opens a binary file
    pickle.dump(data, objfile)          #writes pickle data to file
    objfile.close

def add_data_to_list(task, priority, list_of_rows):    #adds data to the file
    dicRow = {"Task": task, "Priority": priority}      #creates a dictionary
    list_of_rows.append(dicRow)
    return list_of_rows, 'Success'

def remove_data_from_list(task, list_of_rows):         #removes data from the file
    for row in list_of_rows:
        if row["Task"].lower() == task.lower():
                list_of_rows.remove(row)
                print("Task Removed")
                break
        else:
                print("Task not found")                #prompt to user if they made an invalid entry
    return list_of_rows, 'Success'

def read_from_file(file_name):                         #unpickle a file
    """read pickle data from file"""
    objfile = open(file_name, 'rb')
    data = pickle.load(objfile)
    return data

def print_menu():
    print('''
    Menu of Options
    1) Add a new Task
    2) Remove an existing Task
    3) Save Data to File        
    4) Read Data from File
    5) Exit Program
    ''')
    print()  # Add an extra line for looks

def menu_choice():
    try:                                                       #this part will run if the user puts a correct  entry
        choice = int(input("Please Enter Your Option:  "))
        print()
        return choice
    except ValueError:                                         #if a wrong entry is made, a prompt is given
        print("Please choose an option from 1 to 5")


#-- Main script --#

while(True):
    print_menu()
    choice = menu_choice()

    if choice == 1:
        strTask = input(str("Please Enter New Task:  "))                #task to input
        strPriority = input(str("Please Enter Priority of Task:  "))    #priority to input
        data = add_data_to_list(strTask, strPriority, lstTable)
        print(data)
        input('Press the [Enter] key to continue.')
        continue
    elif choice == 2:
        strTask = input(str("Please Enter Task to Remove:  "))          #task to remove
        data = remove_data_from_list(strTask, lstTable)
        print(data)
        input('Press the [Enter] key to continue.')
        continue
    elif choice == 3:
        write_to_file(data, file_name)                                  #write to a binary file
        print("Data saved")
        input('Press the [Enter] key to continue.')
        continue
    elif choice == 4:                                                   #read from the binary file
        data = read_from_file(file_name)
        print(data)
        input('Press the [Enter] key to continue.')
        continue
    elif choice == 5:
        print("Goodbye!")
        break